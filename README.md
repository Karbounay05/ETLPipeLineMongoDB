# 📊 ETL Pipeline MongoDB – Entrepôt de Données à partir de Sources Multiples

## 📖 Présentation

Ce projet a été réalisé dans le cadre du module **Data Engineering**.

L'objectif est de concevoir et d'implémenter un pipeline **ETL (Extract – Transform – Load)** permettant d'extraire des données provenant de plusieurs sources hétérogènes, de les nettoyer et les transformer, puis de les charger dans un entrepôt de données MongoDB afin de faciliter les analyses décisionnelles.

Le pipeline est entièrement développé en **Python** et utilise **MongoDB Community Server** comme base NoSQL cible.

---

# 🎯 Objectifs du projet

Le projet répond aux objectifs suivants :

- Extraire des données depuis plusieurs sources.
- Nettoyer et transformer les données.
- Uniformiser les formats.
- Supprimer les doublons.
- Charger les données dans MongoDB.
- Automatiser le pipeline ETL.
- Journaliser chaque exécution.
- Réaliser des analyses grâce au Framework d'agrégation MongoDB.

---

# 🏗 Architecture du projet

```
                +----------------+
                |   Sales CSV    |
                +----------------+
                       |
                       |
                +----------------+
                |  REST API      |
                +----------------+
                       |
                       |
                +----------------+
                | SQLite Database|
                +----------------+
                       |
                       |
                 EXTRACTION
                       |
                       ▼
              TRANSFORMATION
          (Pandas Cleaning)
                       |
                       ▼
                MongoDB Warehouse
                       |
        +--------------+-------------+
        |                            |
 Pipeline Logs              Aggregation Queries
```

---

# 📂 Structure du projet

```
ETL_Pipeline_MongoDB/

│
├── src/
│   │
│   ├── analytics/
│   │      aggregation_queries.py
│   │
│   ├── data/
│   │      sales.csv
│   │      company.db
│   │
│   ├── extract/
│   │      api_extract.py
│   │      csv_extract.py
│   │      sqlite_extract.py
│   │
│   ├── load/
│   │      mongo_loader.py
│   │
│   ├── scheduler/
│   │      scheduler.py
│   │
│   ├── transform/
│   │      transform.py
│   │
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

---

# 🛠 Technologies utilisées

| Technologie | Utilisation |
|-------------|-------------|
| Python 3.11 | Développement |
| MongoDB Community Server | Entrepôt de données |
| MongoDB Compass | Interface graphique |
| Pandas | Nettoyage des données |
| Requests | Consommation API REST |
| SQLite | Base de données relationnelle |
| PyMongo | Communication avec MongoDB |
| Schedule | Automatisation du pipeline |

---

# 📚 Sources de données

Le projet utilise trois types de sources.

## 1️⃣ CSV

Fichier :

```
sales.csv
```

Contient les ventes de produits.

Exemple :

| id | produit | prix | quantité |
|----|----------|------|----------|

---

## 2️⃣ API REST

Exemple :

```
https://jsonplaceholder.typicode.com/users
```

Les données sont récupérées automatiquement via la bibliothèque Requests.

---

## 3️⃣ Base SQLite

```
company.db
```

Contient les informations des employés.

Exemple :

- employés
- départements

---

# ⚙ Fonctionnement du Pipeline

## Étape 1 : Extraction

Les données sont récupérées depuis :

- CSV
- API REST
- SQLite

Chaque source est indépendante.

---

## Étape 2 : Transformation

Les données sont nettoyées avec Pandas.

Les principales transformations sont :

- suppression des doublons
- gestion des valeurs manquantes
- uniformisation des colonnes
- conversion des types
- standardisation des formats de dates
- suppression des espaces inutiles
- fusion des données

---

## Étape 3 : Chargement

Les données transformées sont chargées dans MongoDB.

Collection :

```
warehouse
```

Chaque ligne est enregistrée sous forme de document BSON.

---

# 📝 Journalisation

Chaque exécution du pipeline est enregistrée dans :

```
pipeline_logs
```

Exemple :

```json
{
    "date":"2026-07-19",
    "status":"SUCCESS",
    "records_processed":520,
    "duration":"2.5 sec"
}
```

En cas d'erreur :

```json
{
    "status":"FAILED",
    "error":"Connection refused"
}
```

---

# 🔄 Automatisation

Le pipeline est exécuté automatiquement grâce à la bibliothèque :

```
schedule
```

Exemple :

Toutes les heures :

```pytho schedule.every().hour.do(run_pipeline)
```

---

# 📊 Analyses MongoDB

Le projet contient plusieurs requêtes d'agrégation.

Exemples :

- Nombre total d'enregistrements
- Nombre d'employés par département
- Produits les plus vendus
- Revenu total
- Revenu moyen
- Nombre de ventes par catégorie
- Top clients
- Répartition géographique
- Statistiques générales

Toutes les analyses utilisent :

```
MongoDB Aggregation Framework
```

---

# ▶ Exécution

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer MongoDB.

Puis exécuter :

```bash
python src/main.py
```

Pour lancer le scheduler :

```bash
python src/scheduler/scheduler.py
```

---

# 📦 Dépendances

```
pandas
pymongo
requests
schedule
sqlite3
```

---

# 🎓 Compétences mises en œuvre

Ce projet permet de mettre en pratique :

- Data Engineering
- ETL Pipeline
- Data Cleaning
- Data Transformation
- MongoDB
- NoSQL
- Python
- Pandas
- REST API
- SQLite
- Data Warehouse
- Scheduling
- Logging
- MongoDB Aggregation Framework

---

# 🚀 Améliorations possibles

- Tableau de bord Power BI
- Tableau de bord Grafana
- Dockerisation
- Apache Airflow
- Apache Kafka
- PostgreSQL comme source
- API météo réelle
- Authentification MongoDB
- Déploiement Cloud MongoDB Atlas

---

# 👨‍💻 Auteur

Projet réalisé dans le cadre du module **Data Engineering**.

**Sujet :**

> Utilisation de MongoDB dans le Data Engineering : Conception d'un pipeline ETL à partir de plusieurs sources de données vers un entrepôt de données MongoDB.

Université : **(Votre université)**

Année universitaire : **2025–2026**