# importing Flask and other modules
import psycopg2
from psycopg2 import Error
from flask import Flask, render_template, redirect, request, session
from flask_session import Session


def select():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                    password="Sudheer@123",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="NBA")

        # Create a cursor to perform database operations
        cursor = connection.cursor()


        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return cursor, connection

# Flask constructor
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/base', methods =["GET", "POST"])
def base():
    # data = select()

    cursor,connection = select()

    if request.method == "POST":

        
        query = request.form.get("query")
        session['data'] = query


    query = session.get('data', None)
    
    postgreSQL_select_Query = query
    

    if 'select'.casefold() in query.casefold():

        if 'league_seasons'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('league_seasons.html', employee_=data)

        if 'teams'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('teams.html', employee_=data)

        if 'team_seasons'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('team_seasons.html', employee_=data)

        if 'leagues'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('leagues.html', employee_=data)

        if 'players'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('players.html', employee_=data)

        if 'season_types'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('season_types.html', employee_=data)

        if 'player_season_stat_totals'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('player_season_stat_totals.html', employee_=data)
    


# INSERT INTO teams (team_id, league_id, full_name) VALUES (0, 98, 'B. Braun Sheffield Sharks')

    if 'insert'.casefold() in query.casefold():
        cursor.execute(postgreSQL_select_Query)
        connection.commit()
        count = cursor.rowcount
        res = str(count)
        return res+"records deleted successfully"

# UPDATE Teams SET full_name='Juan' WHERE team_id = 0 and league_id = 98;

    if 'update'.casefold() in query.casefold():
        cursor.execute(postgreSQL_select_Query)
        connection.commit()
        count = cursor.rowcount
        return "records updated successfully"

# Delete from Teams where team_id = 0 and league_id = 98
    if 'delete'.casefold() in query.casefold():
        cursor.execute(postgreSQL_select_Query)
        connection.commit()
        count = cursor.rowcount
        res = str(count)
        return res+"records deleted successfully"


if __name__ == "__main__":
    app.run(debug=True)
