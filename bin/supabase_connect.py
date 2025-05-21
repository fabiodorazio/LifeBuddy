import os
from supabase import create_client, Client
from dotenv import load_dotenv
from pathlib import Path

# Step 1: Construct the absolute path to env.local
try:
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Navigate up to project root, then to the env file location
    env_path = script_dir.parent / "LifeBuddy" / "assets" / "env.local"
    
    # Verify the path exists
    if not env_path.exists():
        raise FileNotFoundError(f"Could not find .env.local file at: {env_path}")
    
    print(f"Loading environment variables from: {env_path}")
    
    # Step 2: Load environment variables
    load_dotenv(env_path)
    
    # Step 3: Initialize Supabase client with verification
    url = os.environ.get("NEXT_PUBLIC_SUPABASE_URL")
    key = os.environ.get("NEXT_PUBLIC_SUPABASE_ANON_KEY")
    
    if not url or not key:
        raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in environment variables")
    
    supabase: Client = create_client(url, key)
    print("Supabase client initialized successfully!")
    
except Exception as e:
    print(f"Error during initialization: {str(e)}")
    # Optionally re-raise if you want the error to propagate
    # raise