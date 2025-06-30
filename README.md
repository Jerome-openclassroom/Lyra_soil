
# 🌱 Lyra Soil v3 – Ecological Pedological AI for Participatory Science

![Banner](assets/lyra_soil_banner.png)
[![OpenAI Model](https://img.shields.io/badge/Model-GPT--3.5--turbo-blue)](https://platform.openai.com/docs/guides/fine-tuning)
[![Fine-tuned](https://img.shields.io/badge/Fine--Tuned-Yes-brightgreen)](https://platform.openai.com/docs/guides/fine-tuning)
[![Agriculture IA](https://img.shields.io/badge/Domain-Agriculture-critical)]()
[![Status](https://img.shields.io/badge/Validated_by-Grok_Analysis-orange)]()
🛡️ Sous licence MIT – Voir section Licence en bas de page.

> **Lyra Soil** is a fine-tuned AI model designed to generate structured and insightful soil diagnostics from field-measured parameters. Version 3 integrates agronomic precision with ecological sensitivity, optimized for real-world use in participatory science and sustainable land monitoring.

---

## 🔍 Purpose & Scientific Approach

Lyra Soil is part of a broader framework designed by **Jerome-X1** to prepare for the upcoming transition to applied AGI in ecology. This model was developed with the intent to:

- Provide low-latency soil diagnostics in real conditions
- Empower environmental monitoring in rural or NGO-led contexts
- Serve as a building block for distributed ecological intelligence

> ⚠️ **Disclaimer**: This model is provided for **educational and demonstration** purposes. The designer cannot be held responsible for any consequences if used in operational, agricultural, or legal contexts.

---

## 🔧 Training Process & Iterations

The model was refined in three successive fine-tuning iterations using OpenAI’s GPT-3.5-turbo:

- **v1** – Core diagnostic logic (600 train / 200 validation)
- **v2** – Enhanced response to degraded or critical soils (50 train / 20 validation)
- **v3** – Ecological awareness (150 train / 50 validation)

Each dataset was checked using **Jupyter Notebook scripts** for:
- Value ranges
- Logical consistency
- Absence of exact duplicates
- Embedding similarity control (cosine distance)

---

## 🔬 Orientation: Participatory Science & Low-Tech Tools

Lyra Soil is intended to function with **simple field instrumentation** and is compatible with low-tech or low-cost approaches. The model was designed around 14 core parameters measurable via:

- ✅ **LaMotte soil test kits** (NPK, pH, etc.)
- ✅ **Bernard calcimeter** (active lime content)
- ✅ **Digital pH meters**
- ✅ **Slake test for soil structure**
- ✅ **Colorimetric test strips** (nitrate/phosphate)

This makes it ideal for:
- Educational ecosystems
- NGO monitoring programs
- Participatory citizen science
- Resilient ecological systems

---

## 🧪 Example Prompts and Outputs

### Prompt: Forest soil with low nitrogen
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

**AI Response (v3):**
```
Type of soil: Limono-argileuse. Hydric behavior: good. Nutritional status: moderate. Biological activity: good. 
Although nitrogen is low (4 mg/kg), the system is balanced and suitable for forest conditions.
pH KCl (5.0) should be monitored. No corrective actions required.
```

---

## 🛠️ Integration Example

The model is deployed in real time using:

- **Replit**: user-friendly mobile HTML form + Flask + PostgreSQL
- **Make.com**: webhook integration > OpenAI API > formatted Google Docs output

This makes Lyra Soil ideal for real-time use in the field, with confirmation messages that simulate SMS/email dispatch.

---

## 🖥️ Deployment in a Local Mini-Datacenter

For full technical autonomy (especially in NGOs or associations), Lyra Soil can be adapted to run locally via open-source frameworks:

- Model type: `Mixtral 8x7B` (Mixture of Experts)
- Deployment: `vLLM`, `Ollama`, or `Transformers`
- Hardware:
  - 2 × RTX 4090 or 1 × A100
  - 128 GB RAM
  - 2 TB NVMe SSD
- Environment: Linux + HuggingFace stack

💰 **Estimated budget**: ~5500 to 7000 EUR

This option provides robust, cloud-independent ecological intelligence.

---

## 📁 Repository Overview

```
/data/
lyra_soil_v3_train.jsonl → Fine-tuning training dataset
lyra_soil_v3_val.jsonl → Validation dataset

/notebooks/
dataset_check.py → Python script to check duplicates, ranges, and logic

/screenshots/
Animation.gif → Interface preview (Replit + workflow flow)
Metric.png → Final learning curve after training
Result.png → Output sample in formatted document
When_message_is_sent.png → Confirmation interface on dispatch
Workflow_Make.png → Diagram of the Make.com scenario

LISEZ_MOI_VERSION_FRANCAISE.MD → Full French-language README
README.md → English version (main documentation)

```

---

## 👤 Author

Developed by **Jerome-X1**  
Expertise: agronomy, AI integration, participatory environmental science

---

## 📄 License

MIT License  
Copyright (c) 2025 Jerome-X1

Permission is hereby granted, free of charge, to any person obtaining a copy...

(full MIT license text follows)
