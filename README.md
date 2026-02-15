# 🏥 Custom FHIR Terminology API  
### Node.js (Express) | MVC Architecture | Healthcare Interoperability

A scalable and modular **FHIR-based Terminology Service** built using **Node.js (Express)** following clean **MVC Architecture** principles.

This system bridges **NAMASTE (National AYUSH Morbidity Codes)** with **ICD-11 TM2** to enable healthcare interoperability between traditional medicine systems and global clinical standards.

---

# 🚀 Key Features

- 🔍 NAMC ↔ ICD-11 Search  
- 🔁 ICD → NAMC Translation  
- 📝 Smart Autocomplete  
- 📦 FHIR-like `$expand` (ValueSet expansion)  
- 🧠 Hybrid Deterministic + AI Mapping Pipeline  
- ✅ Clean MVC architecture  
- ✅ FHIR-style JSON responses  
- ✅ Pagination support  
- ✅ CORS enabled (Frontend ready)  
- ✅ Modular & production-ready structure  

---

# 🏗️ Backend Architecture (MVC)

```
fhir-terminology-api/
│
├── server.js
├── app.js
│
├── config/
│   └── loadData.js
│
├── controllers/
│   └── terminologyController.js
│
├── models/
│   └── terminologyModel.js
│
├── routes/
│   └── terminologyRoutes.js
│
└── static/
    └── files/
        ├── atharva_codesystem.json
        └── atharva_conceptmap.json
```

## Layer Responsibilities

| Layer | Responsibility |
|--------|---------------|
| **Model** | Terminology logic, filtering, mapping, pagination |
| **Controller** | Handles HTTP requests & FHIR-like responses |
| **Routes** | API endpoint definitions |
| **Config** | Loads terminology JSON files |
| **Server/App** | Express bootstrap & middleware setup |

---

# 🧠 Terminology Engineering Pipeline (Data_PreProcessing)

This project includes a structured terminology mapping pipeline that converts raw NAMASTE Excel data into FHIR-compliant artifacts.

```
Data_PreProcessing/
│
├── Data/
│   ├── NATIONAL SIDDHA MORBIDITY CODES.xls
│   └── namaste_with_icd.xlsx
│
├── ICD11TM2_Search.py
├── translator4_batchwise.py
├── ConceptMap_CodeSystem_Generator.py
```

---

# 📊 Source Dataset

The raw NAMASTE dataset includes:

- NAMC_ID  
- NAMC_CODE  
- NAMC_TERM  
- Tamil Term  
- Short Definition  
- Long Definition  
- English Translation  
- Clinical References  

This multilingual + descriptive dataset enables semantic-level mapping.

---

# ⚙️ Hybrid Terminology Matching Strategy

Healthcare terminology mapping is complex because:

- Traditional medicine terms may not have exact ICD equivalents  
- Regional language terms differ from standardized medical vocabulary  
- Some mappings are conceptual rather than literal  

To solve this, we implemented a **3-layer hybrid matching pipeline**:

---

## 1️⃣ Deterministic ICD-11 TM2 Lookup

Script: `ICD11TM2_Search.py`

- Automates ICD-11 TM2 browser search (via Selenium)  
- Searches NAMC terms directly on official WHO ICD-11 platform  
- Extracts:
  - ICD Code  
  - ICD Title  
- Updates Excel sheet batch-wise  
- Ensures high-confidence, authoritative mappings  

✔ Used when exact ICD match exists  
✔ Highest confidence level  

---

## 2️⃣ AI-Assisted Semantic Matching (Fallback Layer)

Script: `translator4_batchwise.py`

When no exact match is found:

- Uses:
  - Long definitions  
  - Short definitions  
  - English translations  
  - Tamil terms  
  - Transliteration  
- Applies LLM-based semantic similarity matching  
- Finds closest ICD concept  
- Flags uncertain matches for review  

✔ Improves coverage  
✔ Handles conceptual and linguistic variations  
✔ Reduces manual effort  

---

## 3️⃣ FHIR Resource Generation

Script: `ConceptMap_CodeSystem_Generator.py`

After validation:

- Generates **FHIR CodeSystem** (NAMASTE codes)  
- Generates **FHIR ConceptMap** (NAMC ↔ ICD-11 mapping)  

These artifacts power the Node.js terminology API.

---

# 🏗️ End-to-End Architecture Flow

```
Excel Source (NAMASTE Terms)
        ↓
Data Cleaning & Transliteration
        ↓
Deterministic ICD Lookup (Selenium)
        ↓
AI Semantic Matching (LLM Fallback)
        ↓
Validation & Confidence Check
        ↓
FHIR CodeSystem + ConceptMap JSON
        ↓
Node.js Terminology API (MVC)
```

---

# 📡 API Endpoints

## 🔍 Search

Search by NAMC term, NAMC code, or ICD code.

```
GET /search
```

Examples:

```
/search?namc_term=liver
/search?namc_code=N123
/search?icd_code=K70
```

---

## 🔁 Translate

Translate ICD → NAMC

```
GET /translate?icd_code=K70
```

---

## 📝 Autocomplete

```
GET /autocomplete?query=liv&limit=5
```

---

## 📦 Expand (FHIR-like `$expand`)

```
GET /expand?filter=liver&count=10&offset=0
```

### Sample Response

```json
{
  "resourceType": "ValueSet",
  "expansion": {
    "total": 120,
    "offset": 0,
    "count": 10,
    "contains": []
  }
}
```

---

# 🏥 FHIR Alignment

This API mimics key FHIR terminology operations:

- `$expand`  
- `$translate`  
- ConceptMap-based mapping  
- Terminology search & filtering  

Designed to be extendable to **HL7 FHIR R4 compliance**.

---

# 🛠️ Installation

```bash
git clone https://github.com/atharv290/FHIR_Backend.git
cd FHIR_Backend
npm install
node server.js
```

Server runs at:

```
http://localhost:8000
```

---

# 🧩 Tech Stack

- Node.js  
- Express.js  
- MVC Architecture  
- Selenium (ICD lookup automation)  
- LLM-assisted semantic matching  
- JSON-based terminology store  

---

# 🎯 Why This Project Matters

- Bridges Traditional Medicine and Modern Clinical Coding  
- Enables Healthcare Interoperability  
- Automates complex terminology engineering  
- Produces FHIR-compliant terminology artifacts  
- Demonstrates scalable backend architecture  

---

## 👨‍💻 Author

**Atharva Joshi**  
Full Stack Developer | Healthcare Interoperability Enthusiast  

---
