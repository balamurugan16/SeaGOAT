from seagoat.server import start_server
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
  repo_path = os.getenv("REPO_PATH")
  port = int(os.getenv("PORT"))
  start_server(repo_path=repo_path, custom_port=port)