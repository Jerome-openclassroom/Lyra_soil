
# 🌱 Lyra Soil v3 – IA pédologique écologique pour la science participative

![Bannière](assets/lyra_soil_banner.png)

> **Lyra Soil** est un modèle IA fine-tuné conçu pour produire des diagnostics pédologiques structurés et pertinents à partir de paramètres mesurés sur le terrain. La version 3 intègre une précision agronomique et une sensibilité écologique, optimisée pour un usage réel dans des contextes de science participative et de suivi agro-environnemental.

---

## 🔍 Objectif et approche scientifique

Lyra Soil s’inscrit dans un cadre plus large, développé par **Jerome-X1**, visant à préparer l’émergence d’une AGI appliquée à l’écologie. Ce modèle a été conçu pour :

- Fournir un diagnostic pédologique rapide et exploitable en conditions de terrain
- Soutenir la surveillance environnementale dans des contextes associatifs ou ONG
- Servir de base à des systèmes d’intelligence écologique distribuée

> ⚠️ **Avertissement** : Ce modèle est fourni à des fins **pédagogiques et de démonstration**. Le concepteur ne peut être tenu responsable d’un usage en contexte opérationnel, réglementaire ou agricole.

---

## 🔧 Processus de fine-tuning

Le modèle a été entraîné sur GPT-3.5-turbo via trois itérations successives :

- **v1** – Diagnostic de base (600 lignes d'entraînement / 200 de validation)
- **v2** – Réactivité accrue en cas de sols dégradés (50 lignes d'entraînement / 20 de validation)
- **v3** – Sensibilité écologique (150 lignes d'entraînement / 50 de validation)

Chaque jeu de données a été vérifié avec des scripts **Jupyter Notebook** :
- Plages de valeurs valides
- Logique interne
- Évitement des doublons
- Analyse de similarité (cosine distance)

---

## 🔬 Science participative et instruments low-tech

Lyra Soil est pensé pour fonctionner avec des outils de terrain simples et accessibles. Les 14 paramètres peuvent être mesurés avec des méthodes **low-tech / low-cost** telles que :

- ✅ **Kits d’analyse LaMotte** (pH, NPK, etc.)
- ✅ **Calcimètre de Bernard** (calcaire actif)
- ✅ **pH-mètres numériques portables**
- ✅ **Test de stabilité structurale (test de floculation, test au doigt)**
- ✅ **Bandes colorimétriques (nitrates, phosphates)**

Publics visés :
- Réseaux citoyens de surveillance des sols
- Classes ou écoles agricoles
- Projets ONG / collectifs écologiques
- Zones isolées, sans accès à des laboratoires

---

## 🧪 Exemples de prompts et réponses

### Prompt : sol forestier pauvre en azote
```
activité biologique: bonne
pH eau: 7.0
pH KCl: 5.0
azote NO3: 4 mg/kg
phosphore P: 11 mg/kg
potassium K: 57 mg/kg
calcaire actif: faible
surface interne argiles: 55 m²/g
texture: limono-argileuse
stabilité structurale: bonne
compactage: globalement faible
matière organique: élevée
aluminium: non détecté
type de milieu: forêt
```

**Réponse IA (v3) :**
```
Type de sol : limono-argileuse. Comportement hydrique : bon. Statut nutritionnel : modéré. Activité biologique : bonne.
L’azote est bas (4 mg/kg), mais cohérent avec le milieu forestier. Le pH KCl (5.0) doit être suivi. Aucun amendement nécessaire.
```

---

## 🛠️ Intégration sur le terrain

Le modèle a été connecté dans un workflow de terrain comprenant :

- **Replit** : formulaire HTML (mobile), Flask backend, PostgreSQL
- **Make.com** : webhook vers OpenAI + génération automatique de compte rendu dans Google Docs

Cette chaîne simule l’envoi d’un message automatisé ou retour SMS/email pour le technicien.

---

## 🖥️ Déploiement local : mini-datacenter

Pour les structures souhaitant une autonomie complète (ONG, associations, laboratoires citoyens), Lyra Soil peut être adapté en local :

- Modèle : `Mixtral 8x7B` (Mixture of Experts)
- Déploiement : `vLLM`, `Ollama`, ou `Transformers` HF
- Matériel recommandé :
  - 2 × RTX 4090 ou 1 × A100
  - 128 Go de RAM
  - SSD NVMe 2 To
- Stack : Linux, modèle open-weight

💰 **Budget estimé** : entre 5500 et 7000 €  
→ Permet une IA écologique complète, sans dépendance cloud.

---

## 📁 Contenu du dépôt

```
/data/
  lyra_soil_v3_train.jsonl
  lyra_soil_v3_val.jsonl

/screenshots/
  lyra_interface_replit.png
  lyra_output_docs.png

/app/
  form.html
  main.py
  .env.example

notebooks/
  verification_script.ipynb

README.md
README_FR.md
LICENSE
```

---

## 👤 Auteur

Développé par **Jerome-X1**  
Expertise : agronomie, IA appliquée, écologie participative

---

## 📄 Licence

Licence MIT  
Copyright (c) 2025

Permission est accordée, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le « Logiciel »), de traiter le Logiciel sans restriction...

(texte complet de la licence à suivre)
