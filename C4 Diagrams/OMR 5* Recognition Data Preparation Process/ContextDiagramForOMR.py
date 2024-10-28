# Context Diagram for OMR 5 Star Checklist System
from diagrams import Diagram, Cluster
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.ml import AIPlatform
from diagrams.gcp.storage import GCS
from diagrams.gcp.database import Firestore

with Diagram("Context Diagram: OMR 5 Star Checklist System", show=False):
    external_pubsub = PubSub("Pub/Sub")
    
    with Cluster("OMR 5 Star Checklist System"):
        omr_service = ComputeEngine("OMR Service")
        lm_model = AIPlatform("LM Model (Donut-based)")
        storage = GCS("Cloud Storage")
        firestore = Firestore("Firestore")
        five_star_service = ComputeEngine("5 Star Service")
    
    external_pubsub >> omr_service
    omr_service >> five_star_service
    omr_service >> lm_model
    omr_service >> storage
    omr_service >> firestore