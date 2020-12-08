"""Constants used throughout the repo."""
from pathlib import Path

# Define some Path objects to folders within the repo
# Path to the repo as a whole
DIR_REPO = Path(__file__).resolve().parent.parent

# Path to the log file directory
DIR_LOGS = DIR_REPO / 'logs'

# Path to various locations within the documentation
DIR_DOCS = DIR_REPO / 'docs'
DIR_DOCS_SRC = DIR_DOCS / 'source'
DIR_DOCS_SRC_DN = DIR_DOCS_SRC / 'developer_notes'
