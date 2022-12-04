We have connected UI of our web application with the postgres database using Flask.

in Flask:

we have imported psycopg2 library that helped to connect to the local host in which PGadmin is running, to access the databases.

connection = psycopg2.connect(user="postgres",
                                    password="XXXXXXXX@XXXXX",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="NBA")


In the UI we have provided a text box which will take the query input in the form of text and a button to submit the query to the server.
The code for above is in 'index.html'
query = request.form.get("query")

app.py has the backend code to execute the queries provided.

In the backend, to process the query provided we fetched it into 'query' variable in 'app.py' file, and passed it onto cursor.execute()

Once we fetch query from UI, we look for keywords, 'select', 'insert', 'update', 'delete' and perform the action accordingly.

Under 'select' we again have 7 cases since we have 7 tables.

To fetch data accordingly with correct attribute names we have created 7 .html files.

select has the following logic: 
if 'select'.casefold() in query.casefold():
    if 'league_seasons'.casefold() in query.casefold():
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            return render_template('league_seasons.html', employee_=data)
Here in the return we'll be passing our data to the corresponding table's html page to display.

league_seasons.html has the following code:

<div class="content">
    {% for data in employee_ %}
        <div class="League_seasons">
            <p>
                <b>LeagueID:</b>{{ data[0] }}
                <b>season_id:</b>{{ data[1] }}
            </p>
        </div>


Insert has the following logic:

if 'insert'.casefold() in query.casefold():
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

Update has the following code:

if 'update'.casefold() in query.casefold():
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

Delete has the following code:

if 'delete'.casefold() in query.casefold():
        cursor.execute(postgreSQL_select_Query)
        connection.commit()


This way CURD actions are handled. 

Demonstration was given on thursday and hence not attaching any screenshots of the results. 




