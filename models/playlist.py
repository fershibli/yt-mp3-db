from pony import orm
from .base import db


class PlaylistEntity(db.Entity):
    name = orm.Required(str)
    url = orm.Required(str)
    content = orm.Optional(list)
