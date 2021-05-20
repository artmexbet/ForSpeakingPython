import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Link(SqlAlchemyBase):
    __tablename__ = 'links'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def __str__(self):
        return f"Link {self.link} : {self.id}"
