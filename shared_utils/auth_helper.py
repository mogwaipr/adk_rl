import os
from google.cloud import aiplatform
from dotenv import load_dotenv

"""
USE THE CODE BLOCK BELOW TO AUTHENTICATE WITH VERTEX AI 
import sys
import os

# Optional: Auto-reload modules to pick up changes without restarting kernel
# %load_ext autoreload
# %autoreload 2

# Add the project root to the path so we can import shared_utils
sys.path.append(os.path.abspath("../../")) 

from shared_utils.auth_helper import initialize_vertex_ai

# Authenticate using environment variables
initialize_vertex_ai()
"""

def initialize_vertex_ai(project_id=None, location=None):
    """
    Sets up the Google Cloud environment using the local keys.json file.
    """
    # Explicitly load .env from the project root to ensure it is found regardless of where the script is run
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if not load_dotenv(env_path, override=True):
        print(f"Warning: .env file not found at {env_path}")
    else:
        print(f"Loaded .env from: {env_path}")

    # Use a relative path to ensure it works from any subdirectory
    key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "keys.json")
    
    if os.path.exists(key_path):
        if not project_id:
            project_id = os.getenv("PROJECT_ID")
        
        if not project_id:
            raise ValueError(f"PROJECT_ID not found. Please check your .env file at {env_path}")

        if not location:
            location = os.getenv("LOCATION", "us-central1")

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
        aiplatform.init(project=project_id, location=location)
        print(f"Successfully authenticated project {project_id} using {key_path}")
    else:
        print(f"Error: Could not find keys.json at {key_path}")
        raise FileNotFoundError(f"Could not find keys.json at {key_path}")