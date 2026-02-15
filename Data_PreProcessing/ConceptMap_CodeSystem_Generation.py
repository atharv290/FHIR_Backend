import pandas as pd
import json
from datetime import datetime

# ---- Load CSV ----
df = pd.read_excel(r"C:\Users\ATHARVA M JOSHI\Desktop\IMP files\icd_results.xlsx")

# ---- CodeSystem ----
codesystem = {
    "resourceType": "CodeSystem",
    "id": "atharva-namaste-codes",
    "url": "http://atharvajoshi.in/fhir/CodeSystem/namaste",  # 👈 custom namespace
    "version": "1.0.0",
    "name": "AtharvaNAMASTECodeSystem",
    "title": "Atharva NAMASTE Code System",
    "status": "active",
    "publisher": "Atharva Joshi",
    "content": "complete",
    "date": datetime.utcnow().isoformat() + "Z",
    "concept": []
}

for _, row in df.iterrows():
    concept = {
        "code": str(row["NAMC_CODE"]),
        "display": str(row["NAMC_TERM"] if pd.notna(row["English Term"]) else row["NAMC_TERM"])
    }
    if pd.notna(row.get("Short_definition")):
        concept["definition"] = row["Short_definition"]
    elif pd.notna(row.get("Long_definition")):
        concept["definition"] = row["Long_definition"]
    codesystem["concept"].append(concept)

with open("atharva_codesystem.json", "w", encoding="utf-8") as f:
    json.dump(codesystem, f, indent=2, ensure_ascii=False)

# ---- ConceptMap ----
conceptmap = {
    "resourceType": "ConceptMap",
    "id": "atharva-namaste-to-icd11",
    "url": "http://atharvajoshi.in/fhir/ConceptMap/namaste-to-icd11",  # 👈 custom namespace
    "version": "1.0.0",
    "name": "AtharvaNAMASTEtoICD11",
    "status": "draft",
    "sourceUri": "http://atharvajoshi.in/fhir/CodeSystem/namaste",
    "targetUri": "http://atharvajoshi.in/fhir/CodeSystem/icd11",
    "group": [{
        "source": "http://atharvajoshi.in/fhir/CodeSystem/namaste",
        "target": "http://atharvajoshi.in/fhir/CodeSystem/icd11",
        "element": []
    }]
}

for _, row in df.iterrows():
    if pd.notna(row.get("ICD_Code")):
        element = {
            "code": str(row["NAMC_CODE"]),
            "display": str(row["NAMC_TERM"] if pd.notna(row["English Term"]) else row["NAMC_TERM"]),
            "target": [{
                "code": str(row["ICD_Code"]),
                "display": str(row["ICD_Title"]),
                "equivalence": "equivalent"
            }]
        }
        conceptmap["group"][0]["element"].append(element)

with open("atharva_conceptmap.json", "w", encoding="utf-8") as f:
    json.dump(conceptmap, f, indent=2, ensure_ascii=False)

print("✅ Generated atharva_codesystem.json and atharva_conceptmap.json")
