from pony import orm
import settings
from models import db

db.bind(**settings.db_params)
db.generate_mapping(create_tables=True)
