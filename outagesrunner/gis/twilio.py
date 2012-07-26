from outagesrunner.gis import BaseGISProvider

#### ! Ripped from TG2 quickstart cause it works ####

from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

# Global session manager: DBSession() returns the Thread-local
# session object appropriate for the current web request.
maker = sessionmaker(autoflush=True, autocommit=False,
                             extension=ZopeTransactionExtension())
DBSession = scoped_session(maker)

# Base class for all of our model classes: By default, the data model is
# defined with SQLAlchemy's declarative extension, but if you need more
# control, you can switch to the traditional method.
DeclarativeBase = declarative_base()

# There are two convenient ways for you to spare some typing.
# You can have a query property on all your model classes by doing this:
DeclarativeBase.query = DBSession.query_property()
# Or you can use a session-aware mapper as it was used in TurboGears 1:
# DeclarativeBase = declarative_base(mapper=DBSession.mapper)

# Global metadata.
# The default metadata is the one from the declarative base.
metadata = DeclarativeBase.metadata

def init_model():
    """Call me before using any of the tables or classes in the model."""


from sqlalchemy import *
from sqlalchemy.types import String, Integer, Float

#### ! Address object for database ####

class Address(DeclarativeBase):
    __tablename__ = 'address'

    id = Column(String(10), primary_key=True)
    seq = Column(String(3), primary_key=True)
    name = Column(String(30))
    prefix = Column(String(2))
    type = Column(String(4))
    type_dtmf = Column(String(4))
    startlat = Column(Float(precision=8))
    endlat = Column(Float(precision=8))
    startlong = Column(Float(precision=8))
    endlong = Column(Float(precision=8))
    leftzip = Column(Integer(5))
    rightzip = Column(Integer(5))
    leftaddr1 = Column(String(11))
    leftaddr2 = Column(String(11))
    rightaddr1 = Column(String(11))
    rightaddr2 = Column(String(11))
    name_dtmf = Column(String(30))
    prefix_dtmf = Column(String(2))


class TwilioDBProvider(BaseGISProvider):
    """
    Provides lookup access to the Twilio GIS database snapshot on AWS.
    """
    def __init__(self):
        # Start the DB Connection
        engine = create_engine('mysql://localhost/addresses')
        DBSession.configure(bind=engine)

    def get_latlong(testables):
        pass
