import os
from sample_config import Config as config
from database.database import Database

db = Database(config.MONGODB_URI, config.BOT_USERNAME)
