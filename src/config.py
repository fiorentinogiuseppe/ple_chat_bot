import sys
from dotenv import load_dotenv, find_dotenv

sys.path.insert(0, '..')
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
