# 🏥 Custom FHIR Terminology API  
### Node.js (Express) | MVC Architecture | Healthcare Interoperability

A scalable and modular **FHIR-based Terminology Service** built using **Node.js (Express)** following clean **MVC Architecture** principles.

This API provides terminology operations such as:

- 🔍 Search (NAMC ↔ ICD)
- 🔁 Translate (ICD → NAMC)
- 📝 Autocomplete
- 📦 ValueSet Expansion ($expand)

Designed for healthcare interoperability systems and FHIR-compliant environments.

---

## 🚀 Features

- ✅ Clean MVC Architecture
- ✅ FHIR-like API responses
- ✅ In-memory JSON terminology engine
- ✅ Pagination support
- ✅ CORS enabled (Frontend ready)
- ✅ Modular and scalable structure
- ✅ Production-ready code organization

---

## 🏗️ Project Structure

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

---

## 🧠 Architecture (MVC Pattern)

| Layer        | Responsibility |
|-------------|---------------|
| **Model**        | Handles terminology logic & data processing |
| **Controller**   | Manages request & response flow |
| **Routes**       | Defines API endpoints |
| **Config**       | Loads JSON data |
| **Server/App**   | Bootstraps Express application |

---

## 🛠️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/fhir-terminology-api.git
cd fhir-terminology-api
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Run Server

```bash
node server.js
```

Server will start at:

```
http://localhost:8000
```

---

## 📡 API Endpoints

---

### 🔍 Search

Search by NAMC term, NAMC code, or ICD code.

```
GET /search
```

#### Examples:

```
/search?namc_term=liver
/search?namc_code=N123
/search?icd_code=K70
```

---

### 🔁 Translate

Translate ICD → NAMC

```
GET /translate?icd_code=K70
```

---

### 📝 Autocomplete

Autocomplete NAMC terms.

```
GET /autocomplete?query=liv&limit=5
```

---

### 📦 Expand (FHIR-like $expand)

Mimics FHIR ValueSet expansion.

```
GET /expand?filter=liver&count=10&offset=0
```

#### Sample Response:

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

## 🏥 FHIR Alignment

This API mimics key FHIR terminology operations:

- `$expand`
- `$translate`
- ConceptMap-based mapping
- Terminology search & filtering

It can be extended to full **HL7 FHIR R4 compliance**.

---

## ⚙️ Tech Stack

- Node.js
- Express.js
- MVC Architecture
- CORS
- JSON-based terminology store

---

## 🔮 Future Enhancements

- MongoDB integration
- ElasticSearch for fast indexing
- Redis caching
- Swagger documentation
- Docker deployment
- Full FHIR R4 compliance

---

## 👨‍💻 Author

**Atharva Joshi**  
Full Stack Developer | Healthcare Interoperability Enthusiast  

---
