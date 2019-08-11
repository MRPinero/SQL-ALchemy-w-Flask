# Import dependencies
#################################################
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

#################################################
# set engine
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

#List the routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"

    )

    #Convert the query results to a Dictionary using date as the key and prcp as the value. Return the JSON representation of your dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Query all date and prcp
    prcp_date=session.query(Measurement.date, Measurement.prcp)

    session = Session(engine)
    results_precipitation= session.query(Measurement.date, Measurement.prcp).filter

    all_precipitation = []
    for date, prcp in results_precipitation:
        all_precipitation = (results_precipitation.date, results_precipitation.prcp, results_precipitation.station)
        all_precipitation_data.append(all_precipitation)

    return jsonify(all_precipitation)

#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/station")
def station():
    
    # Query all stations
    session = Session(engine)
    results_station = session.query(Measurement.station).all()

    return jsonify(results_station)

@app.route("/api/v1.0/tobs")
def tobs():

    #query for the dates and temperature observations from a year from the last data point.
    results_tobs = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").filter(Measurement.date <= "2017-08-23").all()
    
    #Return a JSON list of Temperature Observations (tobs) for the previous year. 
    return jsonify(convert_to_dict(results_tobs, label="tobs")) 

 
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start():

    results_start=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date < end_date).all()

    list

    return jsonify(convert_to_dict(results_start, label="start")) 

#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    results_start_end_date=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date > start_date).filter(Measurement.date <= end_date).all()

    return jsonify(convert_to_dict(results_start_end_date, label="start/end_date")) 

if __name__ == '__main__':
    app.run(debug=True)
