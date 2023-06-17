import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

import datetime as dt
from dateutil.relativedelta import relativedelta

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/tobs_mostActiveStation<br/>"
        f"/api/v1.0/tobs_DateRange"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""

    response = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    rainfall_list = []

    for date, prcp in response:
        rainfall_dict = {}
        rainfall_dict["date"] = date
        rainfall_dict["rainfall"] = prcp
        rainfall_list.append(rainfall_dict)

    return jsonify(rainfall_list)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""

    response = session.query(Station.station, Station.name,
                             Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    station_list = []

    for station, name, latitude, longitude, elevation in response:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        station_list.append(station_dict)

    return (station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    response = session.query(
        Measurement.station, Measurement.date, Measurement.tobs).all()

    session.close()

    temperature_list = []

    for station, date, tobs in response:
        temperature_dict = {}
        temperature_dict["temp"] = tobs
        temperature_dict["station"] = station
        temperature_dict["date"] = date
        temperature_list.append(temperature_dict)

    return jsonify(temperature_list)


@app.route("/api/v1.0/tobs_mostActiveStation")
def mostActiveStation():
    # Create our session (link) from Python to the DB

    session = Session(engine)

    response = session.query(Measurement.station, func.count(Measurement.station).label("station_count")).\
        group_by(Measurement.station).\
        order_by(desc("station_count")).\
        all()

    session.close()

    activeStations_list = []

    # get list of station activity, in descending order

    for station, station_count in response:
        activeStations_dict = {}
        activeStations_dict["station"] = station
        activeStations_dict["station_count"] = station_count
        activeStations_list.append(activeStations_dict)

    # use the most active station

    mostActiveStation = activeStations_list[0]['station']

    print(mostActiveStation)

    # query dates and temps for most active station
    session = Session(engine)

    response = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == mostActiveStation).\
        all()

    # query dates and temps for most active station - only previous year data

    session.close()

    most_active_station_temps_list = []

    for station, date, tobs in response:
        most_active_station_temps_dict = {}
        most_active_station_temps_dict["station"] = station
        most_active_station_temps_dict["date"] = date
        most_active_station_temps_dict["tobs"] = tobs
        most_active_station_temps_list.append(most_active_station_temps_dict)

        # use the most active station

    return jsonify(most_active_station_temps_list)


@app.route("/api/v1.0/tobs_DateRange/<start_date>/<end_date>")
def DateRange(start_date, end_date):
    print(start_date)
    print(end_date)

    return '{} {}'.format(start_date, end_date)

    r  # eturn (start_date, end_date)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
