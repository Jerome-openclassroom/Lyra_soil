
import json
import pandas as pd
import sys
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def parse_jsonl_to_dataframe(data):
    records = []
    for i, item in enumerate(data):
        try:
            params = {k: v for k, v in [line.split(": ", 1) for line in item["messages"][0]["content"].split("\n")]}
            params["synthese"] = item["messages"][1]["content"]
            params["line_index"] = i
            records.append(params)
        except Exception as e:
            print(f"Erreur de parsing à la ligne {i}: {e}")
    return pd.DataFrame(records)

def check_duplicates(df):
    duplicates = df[df.duplicated(keep=False)][["line_index"]].to_dict('records')
    param_columns = [col for col in df.columns if col not in ["synthese", "line_index"]]
    param_duplicates = df[df.duplicated(subset=param_columns, keep=False)][["line_index"]].to_dict('records')
    return duplicates, param_duplicates

def check_outliers(df, valid_ranges):
    outliers = []
    for param, (min_val, max_val) in valid_ranges.items():
        df[param] = pd.to_numeric(df[param], errors='coerce')
        invalid = df[(df[param] < min_val) | (df[param] > max_val) | df[param].isna()][["line_index", param]]
        for _, row in invalid.iterrows():
            outliers.append({"line_index": int(row["line_index"]), "param": param, "value": row[param]})
    return outliers

def check_inconsistencies(df):
    inconsistencies = []
    for i, row in df.iterrows():
        if row["matière organique"] == "élevée" and row["activité biologique"] != "élevée":
            inconsistencies.append({"line_index": int(row["line_index"]), "issue": "MO élevée mais activité biologique non élevée"})
        if row["aluminium"] == "élevé" and float(row["pH eau"]) > 5.5:
            inconsistencies.append({"line_index": int(row["line_index"]), "issue": "Aluminium élevé mais pH eau > 5.5"})
        if row["texture"] == "sablo-limoneuse" and row["stabilité structurale"] == "bonne":
            inconsistencies.append({"line_index": int(row["line_index"]), "issue": "Texture sablo-limoneuse mais stabilité bonne"})
        if row["calcaire actif"] in ["moyen", "élevé"] and float(row["pH eau"]) < 7:
            inconsistencies.append({"line_index": int(row["line_index"]), "issue": f"Calcaire actif {row['calcaire actif']} mais pH eau < 7"})
        delta_ph = float(row["pH eau"]) - float(row["pH KCl"])
        if delta_ph > 1.5 and row["texture"] not in ["argilo-calcaire", "limono-argileuse"]:
            inconsistencies.append({"line_index": int(row["line_index"]), "issue": "Delta pH > 1.5 mais texture non argileuse/calcaire"})
        synthese = row["synthese"].lower()
        if "cec estimée très bonne" in synthese and float(row["surface interne argiles"]) < 50 and row["matière organique"] != "élevée":
            inconsistencies.append({"line_index": int(row["line_index"]), "issue": "CEC très bonne mais SIA < 50 m²/g et MO non élevée"})
    return inconsistencies

def check_repetitive_syntheses(df, threshold=0.9):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["synthese"])
    similarity = cosine_similarity(X)
    repetitive_syntheses = []
    for i in range(len(similarity)):
        for j in range(i + 1, len(similarity)):
            if similarity[i, j] > threshold:
                repetitive_syntheses.append({
                    "line_index_1": int(df.iloc[i]["line_index"]),
                    "line_index_2": int(df.iloc[j]["line_index"]),
                    "similarity": similarity[i, j]
                })
    return repetitive_syntheses

def analyze_jsonl(file_path):
    data = load_jsonl(file_path)
    df = parse_jsonl_to_dataframe(data)

    valid_ranges = {
        "pH eau": (4, 8),
        "pH KCl": (3.5, 7.5),
        "azote NO3": (0, 100),
        "phosphore P": (10, 50),
        "potassium K": (50, 200),
        "surface interne argiles": (10, 100)
    }

    duplicates, param_duplicates = check_duplicates(df)
    outliers = check_outliers(df, valid_ranges)
    inconsistencies = check_inconsistencies(df)
    repetitive_syntheses = check_repetitive_syntheses(df)

    report = {
        "Doublons de lignes": [{"line_index": d["line_index"]} for d in duplicates],
        "Doublons de paramètres (sans synthèse)": [{"line_index": d["line_index"]} for d in param_duplicates],
        "Valeurs aberrantes": outliers,
        "Incohérences": inconsistencies,
        "Synthèses similaires (cosine > 0.9)": repetitive_syntheses
    }

    return report

def print_report(report):
    for key, value in report.items():
        print(f"\n{key}:")
        if not value:
            print("  Aucun problème détecté.")
        else:
            for item in value:
                print(f"  {item}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERREUR] Usage : python verif_grok.py <chemin_du_fichier.jsonl>")
    else:
        file_path = sys.argv[1]
        print(f"[INFO] Fichier analysé : {file_path}")
        report = analyze_jsonl(file_path)
        print_report(report)
