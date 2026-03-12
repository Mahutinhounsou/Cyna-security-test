# Test technique Data Engineering - Cyna

## Objectif

Ce projet implémente un pipeline de traitement de **logs de sécurité** permettant d'analyser des événements réseau et de détecter des activités potentiellement malveillantes.

L'objectif est de construire une pipeline simple mais complète permettant :

- d’ingérer des logs de sécurité générés artificiellement
- d’intégrer un flux de **Threat Intelligence** contenant des IP malveillantes
- d’enrichir les logs avec ces informations
- d’identifier les logs associés à des IP suspectes
- de visualiser les résultats dans un **dashboard interactif**

Ce type de pipeline est typiquement utilisé dans des environnements **SOC (Security Operations Center)** afin d'analyser de grands volumes de logs de sécurité.

---

# Architecture du pipeline

Le pipeline suit les étapes suivantes :

1. **Ingestion du Threat Intelligence Feed**

   Chargement d’une liste d’IP malveillantes provenant du projet open-source *IPsum*.

2. **Génération et ingestion des logs de sécurité**

   Utilisation d’un **Security Log Generator** pour produire des logs réalistes :
   - logs IDS (Intrusion Detection System)
   - logs d’accès web

3. **Enrichissement des logs**

   Extraction des adresses IP présentes dans les logs puis comparaison avec la liste d’IP malveillantes.

4. **Création d’un dataset enrichi**

   Les logs sont enrichis avec :

   - type de log
   - IP source
   - IP destination
   - IP malveillante détectée
   - nombre de signalements de cette IP
   - indicateur booléen `is_malicious`

5. **Visualisation**

   Un dashboard qui permet d’explorer les résultats et d’identifier les comportements suspects.

---

# Structure du projet
```text
cyna-security-test/
├── ingestion/
│   ├── generate_logs.py        # génération des logs de sécurité
│   └── load_threat_feed.py     # ingestion du flux de Threat Intelligence
├── processing/
│   └── enrich_logs.py          # enrichissement des logs avec les IP malveillantes
├── dashboards/
│   └── dashboard.py            # dashboard Streamlit pour visualiser les résultats
├── data/
│   ├── logs/                   # logs générés (IDS et access)
│   ├── threat_feed/            # flux d’IP malveillantes
│   └── enriched/               # dataset enrichi final
├── requirements.txt            # dépendances du projet
└── README.md                   # documentation du projet
 ```

---

# Description des composants

## 1. Génération des logs

Les logs sont générés à partir du projet open source :

**Security Log Generator**

Ce générateur produit différents types de logs réalistes :

- IDS logs
- Access logs

Ces logs simulent des événements réseau tels que :

- scans de ports
- trafic suspect
- requêtes web

---

## 2. Threat Intelligence Feed

Le projet utilise la base :

**IPsum**

Cette base contient des IP identifiées comme malveillantes.

Chaque IP possède un **nombre de signalements** correspondant au nombre de listes noires sur lesquelles elle apparaît.

Exemple : 2.57.121.25 10

Cela signifie que cette IP apparaît dans **10 blacklists différentes**.

---

## 3. Enrichissement des logs

Les logs sont analysés afin d'extraire les adresses IP :

### Logs IDS

Format simplifié : timestamp - severity - protocol - src_ip:port --> dest_ip:port - flags - alert

Les champs extraits :

- `src_ip`
- `dest_ip`

### Logs Access

Format simplifié : client_ip - user "GET resource HTTP/1.1"

Le champ extrait :

- `client_ip`

Ces IP sont ensuite comparées à la base **IPsum** afin de déterminer si elles sont malveillantes.

---

# Dataset enrichi

Le fichier final `enriched_logs.csv` contient :

| colonne | description |
|------|------|
| log_type | type de log (ids / access) |
| timestamp | date du log |
| source_ip | IP source |
| destination_ip | IP destination |
| matched_ip | IP identifiée comme malveillante |
| reports | nombre de signalements de l’IP |
| is_malicious | indicateur booléen |

---

# Dashboard

Le dashboard Streamlit permet de visualiser :

- le nombre total de logs analysés
- le nombre de logs malveillants détectés
- la répartition des logs par type
- les IP malveillantes les plus fréquentes
- un échantillon des logs suspects

Cela permet d'identifier rapidement les événements de sécurité importants.

---

# Choix techniques

### Python

Python a été choisi pour sa simplicité et sa popularité dans le domaine du **Data Engineering et de la cybersécurité**.

---

### Pandas

Pandas permet de :

- manipuler facilement les datasets
- filtrer et enrichir les logs
- effectuer des analyses rapides

---

### Streamlit

Streamlit permet de créer rapidement un **dashboard interactif** pour explorer les données sans développer une interface web complexe.

---

### Architecture du pipeline

Le projet suit une séparation claire :
ingestion
processing
visualisation

Cette organisation est classique dans les pipelines data et permet de :

- séparer les responsabilités
- faciliter la maintenance
- rendre le pipeline extensible

---

# Installation

Installer les dépendances :
pip install -r requirements.txt


---

# Exécution

### 1. Générer les logs
python ingestion/generate_logs.py


---

### 2. Charger le flux de Threat Intelligence


python ingestion/load_threat_feed.py


---

### 3. Enrichir les logs


python processing/enrich_logs.py


---

### 4. Lancer le dashboard


python -m streamlit run dashboards/dashboard.py


---

# Résultat

Le pipeline permet d'analyser plus de **100 000 logs** et d'identifier les événements associés à des IP malveillantes.

Le dashboard permet ensuite d'explorer ces événements et d’identifier les comportements suspects.

---

# Améliorations possibles

- ajout de nouvelles sources de Threat Intelligence
- stockage dans une base de données
- automatisation du pipeline
- ajout d'analyses temporelles des attaques


