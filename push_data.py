import pandas as pd
import numpy as np
import os
import sys
from networksecurity.logging.logger import logging
from networksecurity.exceptions.exception import NetworkSecurityException
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL=os.getenv('MONGO_DB_URL')
