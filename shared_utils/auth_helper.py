import os
from google.cloud import aiplatform
"""
USE THE CODE BLOCK BELOW TO AUTHENTICATE WITH VERTEX AI 
import sys
import os

# Add the project root to the path so we can import shared_utils
sys.path.append(os.path.abspath("../../../")) 

from shared_utils.auth_helper import initialize_vertex_ai

# Replace with your actual project ID from the gcloud setup
initialize_vertex_ai(project_id="metal-being-479116-m4")
"""
def initialize_vertex_ai(project_id, location="us-central1"):
    """
    Sets up the Google Cloud environment using the local keys.json file.
    """
    # Use the absolute path to ensure it works from any subdirectory
    key_path = "/Users/robert/Projects/adk_rl/keys.json"
    
    if os.path.exists(key_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
        aiplatform.init(project=project_id, location=location)
        print(f"Successfully authenticated using {key_path}")
    else:
        print(f"Error: Could not find keys.json at {key_path}")