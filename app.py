from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='achu@2005',
        database='projectdb'
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        donor_name = request.form['donor_name']
        donor_phone = request.form['donor_phone']
        pet_species = request.form['pet_species']
        pet_breed = request.form['pet_breed']

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Donor (donor_name, donor_phone) VALUES (%s, %s)", (donor_name, donor_phone))
        donor_id = cursor.lastrowid
        cursor.execute("INSERT INTO Pet (pet_species, pet_breed, donor_id) VALUES (%s, %s, %s)", (pet_species, pet_breed, donor_id))

        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('home'))
    return render_template('donate.html')

@app.route('/adopt', methods=['GET', 'POST'])
def adopt():
    message = ''
    if request.method == 'POST':
        adopter_name = request.form['adopter_name']
        adopter_phone = request.form['adopter_phone']
        pet_id = request.form['pet_id']

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT available FROM Pet WHERE pet_id = %s", (pet_id,))
        pet = cursor.fetchone()

        if pet and pet['available'] == 1:
            cursor.execute("INSERT INTO Adopter (adopter_name, adopter_phone, pet_id) VALUES (%s, %s, %s)",
                           (adopter_name, adopter_phone, pet_id))
            cursor.execute("UPDATE Pet SET available = 0 WHERE pet_id = %s", (pet_id,))
            connection.commit()
            message = 'Adoption successful!'
        else:
            message = 'Pet not available.'

        cursor.close()
        connection.close()

    return render_template('adopt.html', message=message)

@app.route('/view')
def view():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.pet_id, p.pet_species, p.pet_breed, d.donor_name, d.donor_phone
        FROM Pet p
        JOIN Donor d ON p.donor_id = d.donor_id
        WHERE p.available = 1
    """)
    pets = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('view.html', pets=pets)

if __name__ == '__main__':
    app.run(debug=True)
