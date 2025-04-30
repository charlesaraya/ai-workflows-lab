import yaml
import os
from dotenv import load_dotenv

def load_config(filepath):
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, filepath)
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def set_env(var: str):
    if not os.environ.get(var):
        load_dotenv()   # Load environment variables from a .env file
        os.environ[var] = os.getenv(var)