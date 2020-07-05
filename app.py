# Climate App
# Now that initial analysis are completed, design a Flask API based on the queries that you have just developed.
# Use Flask to create your routes.
# Need to join the station and measurement tables for some of the queries.
# Flask jsonify used to convert API data into a valid JSON response object.

# Dependencies
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
# from matplotlib import style
# style.use('fivethirtyeight') 
import matplotlib.pyplot as plt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# db reflection 
Base = automap_base()
Base.prepare(engine, reflect = True)

Station = Base.classes.station
Meas = Base.classes.measurement

# session from Python to db
session = Session(engine)

#################################################
# Flask Setup
#################################################

# Create an app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


# Home page
# List all routes that are available.
@app.route("/")
def Welcome():

    """List all available api routes."""
    return (
        f"Welcome to my App using Flask!<br>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/date/<start><br/>"
        f"/api/v1.0/<start_date>/<end_date>"
        
    )

# /api/v1.0/precipitation

@app.route("/api/v1.0/precipitation")
def precipitation():

    past_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query data
    prcp_result = session.query(Meas.date, Meas.prcp).filter(Meas.date >= past_date).all()


    return jsonify(prcp_result )
    

# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():

    # Query data
    station_data = session.query(Station.name, Meas.station).filter(Station.station == Meas.station).group_by(Station.name).all()

    return jsonify(station_data) 
  
#print("-------------------------")

# /api/v1.0/tobs
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year. 

@app.route("/api/v1.0/tobs")
def tobs():
    # session = Session(engine)
    most_active_result = 'USC00519281'
    last_data_point = session.query(Meas.date).order_by(Meas.date.desc()).first().date
    past_date = dt.datetime.strptime(last_data_point, '%Y-%m-%d') - dt.timedelta(days=365)
    num_temp_observ= session.query(Meas.date, Meas.tobs).filter(Meas.station == most_active_result).filter(Meas.date >= past_date).all()
    session.close()

    
    return jsonify(num_temp_observ)

#print("-------------------------")


# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive. 

@app.route("/api/v1.0/date/<start>")

def start(start_date):
    last_data_point = session.query(Meas.date).order_by(Meas.date.desc()).first().date  
    temp_results = session.query(func.min(Meas.tobs),
                            func.avg(Meas.tobs),
                            func.max(Meas.tobs)).\
            filter(Meas.date >= start_date).\
            filter(Meas.date <= last_data_point).all() 
 
 
    return jsonify(temp_results)

#print("-------------------------")

    
@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date,end_date):

    temp_results = session.query(func.min(Meas.tobs),
                            func.avg(Meas.tobs),
                            func.max(Meas.tobs)).\
            filter(Meas.date >= start_date).\
            filter(Meas.date <= end_date).all() 
    # return jsonify(temp_results)
    return jsonify(temp_results)


if __name__ == '__main__':
    app.run(debug=True)