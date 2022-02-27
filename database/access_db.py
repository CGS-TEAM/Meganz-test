import os
from sample_config import MONGODB_URI, BOT_USERNAME
from database.database import Database

db = Database(MONGODB_URI, BOT_USERNAME)
