# Component Diagram for OMR 5 Star Checklist Components
from diagrams import Diagram, Cluster
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.ml import AIPlatform
from diagrams.gcp.storage import GCS
from diagrams.gcp.database import Firestore

with Diagram("Component Diagram: OMR 5 Star Checklist Components", show=False):
    pubsub = PubSub("Pub/Sub")
    
    with Cluster("OMR Service Components"):
        message_reader = ComputeEngine("Message Reader")
        parser = ComputeEngine("Parser")
        pdf_downloader = ComputeEngine("PDF Downloader")
        version_finder = ComputeEngine("Version Finder")
        icd_code_extractor = ComputeEngine("ICD Code Extractor")
        model_runner = ComputeEngine("Model Runner")
        results_filter = ComputeEngine("Results Filter")
        api_interactor = ComputeEngine("API Interactor")
    
    lm_model = AIPlatform("LM Model (Donut-based)")
    storage = GCS("Cloud Storage")
    firestore = Firestore("Firestore")
    five_star_api = ComputeEngine("5 Star Service API")
    
    pubsub >> message_reader >> parser
    parser >> pdf_downloader >> storage
    parser >> version_finder >> five_star_api
    version_finder >> icd_code_extractor >> five_star_api
    icd_code_extractor >> model_runner >> lm_model
    model_runner >> results_filter >> api_interactor >> five_star_api
    results_filter >> firestore