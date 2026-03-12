# Test technique Data Engineering - Cyna

## Objectif

Ce projet implémente un pipeline de traitement de logs de sécurité permettant :

- d’ingérer des logs générés par un Security Log Generator
- d’intégrer un flux de Threat Intelligence contenant des IP malveillantes
- d’enrichir les logs avec ces informations
- de visualiser les résultats dans un dashboard interactif
## Architecture du pipeline

Le pipeline de données suit les étapes suivantes :

1. Ingestion du flux de Threat Intelligence (blacklist d’IP malveillantes)
2. Génération et ingestion des logs de sécurité
3. Enrichissement des logs avec les IP malveillantes
4. Stockage du dataset enrichi
5. Visualisation des résultats via un dashboard
## Structure du projet
SCHEMA EXPLICATIF 

cyna-security-test/

ingestion/ : scripts d’ingestion des données  
processing/ : enrichissement et transformation des logs  
dashboards/ : visualisation des données  
data/ : stockage des datasets (logs, threat feed, données enrichies)  
scripts/ : orchestration du pipeline

## Choix techniques

Python : utilisé pour sa simplicité et son écosystème de traitement de données.

Pandas : utilisé pour manipuler efficacement les datasets de logs.

Streamlit : utilisé pour créer rapidement un dashboard interactif.

Structure du pipeline : séparation ingestion / processing / visualisation afin de respecter une architecture de pipeline de données classique.

## Installation

Installer les dépendances :

pip install -r requirements.txt

## Exécution

1. Générer les logs
python ingestion/generate_logs.py

2. Charger le flux de Threat Intelligence
python ingestion/load_threat_feed.py

3. Enrichir les logs
python processing/enrich_logs.py

4. Lancer le dashboard
streamlit run dashboards/dashboard.py