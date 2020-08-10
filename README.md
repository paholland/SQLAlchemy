SQLAlchemy Project 

    To do some climate analysis and data exploration of the database. The deployed assignment utilizes the SQLAlchemy library to retrieve data 
    from a database which is used to generate charts and an API.


Precipitation Analysis (Gets the correct results for the last year of data (note that the last day in the dataset is 8/23/2017), creates a pandas dataframe
using the date and precipitation columns, sorts the dataframe by date, makes a plot using pandas with date as the x and precipitation as the y variables).

Station Analysis (correctly outputs the number of stations in the dataset (9), correctly finds the most active station by using count (USC00519281), gets the min, max, and average temperatures for the most active station (USC00519281), correctly plots a histogram for the last year of data using tobs as the column to count).

API SQLite Connection & Landing Page (The Flask Application does all of the following: correctly generates the engine to the correct sqlite file, uses automap_base() and reflects the database schema, correctly saves references to the tables in the sqlite file(measurement and station), correctly creates and binds the session between the python app and database).

API Static Routes (the static routes do all of the following: Precipitation route returns the jsonified precipitation data for the last year in the database, returns json with the date as the key and the value as the precipitation. Stations route returns jsonified data of all of the stations in the database. Tobs route returns jsonified data for the most active station(USC00519281) for the last year of data).

API Dynamic Route (the dynamic route does all of
the following: Start route accepts the start date as a parameter from the URL, returns the min, max, and average temperatures calculated from the given start
date to the end of the dataset. Start/end route accepts the start and end dates as parameters from the URL, returns the min, max, and average temperatures calculated from the given start date to the given end date).

Additional Analyses (Trip Temperature Analysis uses the calc_temps function to get the min, max, and average temperatures for a date range of their choosing, uses the calculated temperatures to generate a bar chart with an error bar. Daily Rainfall Average calculates the min, max, and average temperatures for each day of their trip and appends them to a list, creates a dataframe from the list and generates a stacked line chart plotting the min, max, and average temps for each day of their trip).

SQLAlchemy ORM queries, Pandas, and Matplotlib.

### SQLAlchemy ORM queries, Pandas, and Matplotlib






