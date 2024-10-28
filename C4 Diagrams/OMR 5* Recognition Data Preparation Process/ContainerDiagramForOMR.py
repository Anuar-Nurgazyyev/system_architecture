# Container Diagram for OMR 5 Star Checklist System
from diagrams import Diagram, Cluster
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.ml import AIPlatform
from diagrams.gcp.storage import GCS
from diagrams.gcp.database import Firestore

with Diagram("Container Diagram: OMR 5 Star Checklist System", show=False):
    pubsub = PubSub("Pub/Sub")
    
    with Cluster("OMR 5 Star Checklist Service"):
        omr_service = ComputeEngine("OMR Service")
    
    with Cluster("5 Star Service"):
        five_star_service = ComputeEngine("5 Star Service")
    
    lm_model = AIPlatform("LM Model (Donut-based)")
    storage = GCS("Cloud Storage")
    firestore = Firestore("Firestore")
    
    pubsub >> omr_service
    omr_service >> storage
    omr_service >> five_star_service
    omr_service >> lm_model
    omr_service >> firestore