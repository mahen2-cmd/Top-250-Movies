from flask import Flask, render_template
import sqlite3

app = Flask(__name__)




@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('Top250Movies.db')
    cursor = conn.cursor()

    # Retrieve the data from the database
    cursor.execute('SELECT * FROM top250movies')
    rows = cursor.fetchall()

    # Close the connection``
    conn.close()

    # Render the template with the data
    return render_template('index.html', rows=rows)




if __name__ == '__main__':
    app.run()
