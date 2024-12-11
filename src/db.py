from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here
<<<<<<< HEAD
=======

class HealthData(db.Model):
  """
  HealthData Model 
  """
  __tablename__ = "health_data"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  heart_rate = db.Column(db.Integer, nullable=False)  # Heart rate in beats per minute
  blood_oxygen = db.Column(db.Float, nullable=False)  # Blood oxygen level as a percentage
  hrv = db.Column(db.Float, nullable=True)  # Heart rate variability in milliseconds
  glucose_level = db.Column(db.Float, nullable = True) # Glucose level in mg/dL 
  latitude = db.Column(db.Float, nullable=False)  # Latitude of the location
  longitude = db.Column(db.Float, nullable=False)  # Longitude of the location
  timestamp = db.Column(db.DateTime, nullable=False)  # Timestamp of data collection

  def __init__(self, **kwargs):
    """
    Initializes a healthdata object
    """
    self.heart_rate = kwargs.get("heart_rate", 0)
    self.blood_oxygen = kwargs.get("blood_oxygen", 0)
    self.hrv = kwargs.get("hrv", 0)
    self.glucose_level = kwargs.get("glucose_level", 0)
    self.longitude = kwargs.get("longitude", 0)
    self.latitude = kwargs.get("latitude", 0)
    self.timestamp = kwargs.get("timestamp", "")

  def serialize(self):
    """ 
    Serialize a healthdata object 
    """
    return {
      "id": self.id,
      "heart_rate": self.heart_rate,
      "blood_oxygen": self.blood_oxygen,
      "hrv": self.hrv,
      "glucose_level": self.glucose_level,
      "latitude": self.latitude, 
      "longitude": self.longitude,
      "timestamp": self.timestamp.isoformat()
    }
>>>>>>> 72756d5bb76813f5cdef8d269ef7284e42c7f675
