from datetime import datetime
import requests
import random
import json
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for,session, make_response
import smtplib
from email.mime.multipart import MIMEMultipart
import sqlite3
import numpy as np

# Connect to a database (will be created if it doesn't exist)

# Create a cursor object
from email.mime.text import MIMEText


from flask_session import Session
 
import uuid


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "filesystem"
Session(app)
articles = [];
topic = ["news","india"]
for i in range(0,len(topic)):
    url = f"https://newsapi.org/v2/everything?q={topic[i]}&apiKey=a26e90658ca8499ca068782aa2179116"
    response = requests.get(url)
    data = response.json()
    articles.extend(data["articles"])
    

id_array = []
main = ["hay","hello"]
views_array = []

@app.route('/')
def index_1():
	 username = session.get("username")
	 if username:
	   	 	return redirect(f"/home/profile/{username}")

	 time_2 = []
	 for id in articles:
	 	if isinstance(id, dict):  # Check if id is a dictionary
	 		id["views"] = sum([i[2] if i[2] is not None else 0 for i in read_record("user.db", "views") if id["publishedAt"] == i[1]])
	 		time_2.append(int(''.join(id["publishedAt"].split('T')[0].split('-'))))
	 	else:
	 		print(f"Unexpected data format:")
	 time_4 = []

	 for i in range(0,len(time_2)):
	 	time_4.append(str(np.argmax(time_2)))
	 	time_2[np.argmax(time_2)] = 0
	 articles.append(time_4)
	 	 					 			
	 time = datetime.now().year
	 return render_template('index.html',data=articles,time = time,time_4=time_4)



@app.route('/sport')
def index_1_4():
	 username = session.get("username")
	 quary = 'sport'
	 url = f"https://newsapi.org/v2/everything?q={quary}&apiKey=a26e90658ca8499ca068782aa2179116"
	 response = requests.get(url)
	 data_2 = response.json()
	 for id in data_2["articles"]:
	 		id["views"] = sum([ i[2] for i in read_record("user.db","views") if id["publishedAt"] == i[1]])		 
	 return render_template('index.html',data=data_2["articles"])
	 	 
@app.route('/india')
def index_11():
	 username = session.get("username")
	 quary = 'sport'
	 url = f"https://newsapi.org/v2/everything?q={quary}&apiKey=a26e90658ca8499ca068782aa2179116"
	 response = requests.get(url)
	 data_2 = response.json()
	 for id in data_2["articles"]:
	 		id["views"] = sum([ i[2] for i in read_record("user.db","views") if id["publishedAt"] == i[1]])		 
	 return render_template('index.html',data=data_2["articles"])	 

@app.route('/news')
def index_12():
	 username = session.get("username")
	 quary = 'news'
	 url = f"https://newsapi.org/v2/everything?q={quary}&apiKey=a26e90658ca8499ca068782aa2179116"
	 response = requests.get(url)
	 data_2 = response.json()
	 for id in data_2["articles"]:
	 		id["views"] = sum([ i[2] for i in read_record("user.db","views") if id["publishedAt"] == i[1]])		 
	 return render_template('index.html',data=data_2["articles"])	 
	 	 	 		 		 	 		 	
@app.route('/search')
def index_2():
    sug_data = []
    for i in range(0,10):
    	data_1 = articles[i]
    	sug_data.append(data_1["title"])
   # for id in data_2["articles"]:
    	#id["views"] = sum([ i[2] for i in read_record("user.db","views") if id["publishedAt"] == i[1]])		 
    return render_template('search.html',data=sug_data)
    
@app.route('/view',methods=['POST'])
def index_2_2_4():
      data = (request.get_json()[0],request.get_json()[1])
      table = "views"
      create_table_1("user.db",table)
      insert_view_record("user.db",table,data)
      return "hay"
             
@app.route('/search/quary', methods=['GET'])
def index_3():
    username = session.get("username")
    quary = request.args.get("quary")
    url = f"https://newsapi.org/v2/everything?q={quary}&apiKey=a26e90658ca8499ca068782aa2179116"
    response = requests.get(url)
    data_2 = response.json()

    time_2 = []
    for id in data_2["articles"]:
        if isinstance(id, dict):  # Check if id is a dictionary
            id["views"] = sum([i[2] if i[2] is not None else 0 for i in read_record("user.db", "views") if id["publishedAt"] == i[1]])
            time_2.append(int(''.join(id["publishedAt"].split('T')[0].split('-'))))
        else:
            print(f"Unexpected data format: {id}")

    time_4 = []
    for i in range(0, len(time_2)):
        time_4.append(str(np.argmax(time_2)))
        time_2[np.argmax(time_2)] = 0

    data_2["articles"].append(time_4)

    return render_template('index.html', data=data_2["articles"])

     
@app.route('/signup')
def index_5():
	return render_template('signup.html')
	
@app.route('/login')
def index_6():
	return render_template('login.html')
	
@app.route('/login/auth/co',methods=['POST'])
def index_6_2():
	return render_template('login.html')

	
auth_link = []
auth_id = []
@app.route('/signup/auth', methods=['POST'])
def index_5_2():
	 email = request.form['email']
	 username = request.form['username']
	 password = request.form['password']
	 create_table("login.db","user",1)
	 data_2 = read_record("login.db","user")
	 data = []
	 for data_4 in data_2:
	 	data.append({
	 	"username":data_4[1],
	 "email":data_4[2],
	 "password":data_4[3]
	 	})
	 if any(user_info.get("email") == email  for user_info in data):
            return render_template('login.html')
	 id_au = {
	 "username":username,
	 "email":email,
	 "password":password
	 }
	 auth_id.append(id_au)
	 un_link_id = uuid.uuid4()
	 auth_link.append(un_link_id)
	 smtp_server = 'smtp.gmail.com'
	 smtp_port = 587
	 sender_email = 'khelendra1112@gmail.com'
	 password = 'pwys ohtn murd xngy'
	 message = MIMEMultipart()
	 message['From'] = sender_email
	 message['To'] = email
	 message['Subject'] = 'Subject of the Email'
	 body = f'your vrification link is https://newsflow-jmsx.onrender.com//signup/auth/{un_link_id} '
	 message.attach(MIMEText(body, 'plain'))
	 server = smtplib.SMTP(smtp_server, smtp_port)
	 server.starttls() 
	 server.login(sender_email, password)
	 server.send_message(message)
	 server.quit()
	 return render_template('signup_auth.html')

	
@app.route('/signup/auth/<auth_link_1>', methods=['GET'])
def index_7(auth_link_1):
    data_2 = read_record("login.db","login")
    data = []
    for data_4 in data_2:
    	data.append({
	 	"username":data_4[1],
	 "email":data_4[2],
	 "password":data_4[3]
	 	})
    auth_link_1 = auth_link[len(auth_link)-1]
    email = auth_id[len(auth_id)-1]["email"]
    username = auth_id[len(auth_id)-1]["username"]
    password = auth_id[len(auth_id)-1]["password"]
    login = {
                "username": username,
                "email": email,
                "password": password
            }
    login_2 = (username,email,password)        
    session['username'] = username
    session['email'] = email
    insert_record("login.db","user",login_2)
    return redirect(f'/home/profile/{username}')
    
	   	   	   	    	
@app.route('/login/auth', methods=['POST'])
def index_8():
    username = session.get("username")
    email = request.form['email']
    password = request.form['password']
    data_2 = read_record("login.db","user")
    for data_4 in data_2:
    		if data_4[2] == email and data_4[3] == password:
    			return redirect(f'/home/profile/{username}')
    data = "your email and password is wrong"			
    return render_template('login.html',data=data)	
    		 	
@app.route('/home/profile/<username>')
def index_2_2(username):
	username = session.get("username")
	return render_template('index.html',data=articles,link=f'/profile/{username}')

@app.route('/profile/<username>')
def upload_file(username):
    # Get the username cookie
    id_1 = username
    formatted_date = datetime.now().strftime("%B %d, %Y")
    # Check if the cookie is None
    if id_1 is None:
        # Handle the case where the username cookie is not set
        return redirect("/login")
    
    # Convert username to a list
    id_2 = list(id_1)
    
    # Create the id_4 variable
    id_4 = "@" + ''.join(id_2)
        
    # Assuming file.filename is defined elsewhere in your code
    image_url = url_for('static',filename="360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.webp")
    data={"name": username,
    "image": image_url,
    "id": id_4,
    "profile_text": "hsys  uzhdhe ydbsh","time": formatted_date,
    "profile":f"/home/profile/{username}"
    }
    # Render template with data
    return render_template('profile.html', data=data)

def read_record(db_name, table_name):
    """
    Read records from an SQLite database.

    :param db_name: Name of the SQLite database file.
    :param table_name: Name of the table from which records will be read.
    :return: List of tuples representing the records.
    """
    records = []
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Prepare and execute the SQL query
        sql = f'SELECT * FROM {table_name}'
        cursor.execute(sql)
        
        # Fetch all records
        records = cursor.fetchall()
        
        #print("Records read successfully.")
    except sqlite3.Error as e:
        print(f"Error reading records: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
    
    return records

def insert_record(database_name, table_name, user_data):
    # कनेक्शन बनाएं
    conn = sqlite3.connect(database_name)
    
    # कर्सर ऑब्जेक्ट बनाएं
    cursor = conn.cursor()
    
    # डेटा डालने का SQL स्टेटमेंट
    insert_query = f'''
    INSERT INTO {table_name} (username, email, password)
    VALUES (?, ?, ?)
    '''
    
    # डेटा डालें
    cursor.execute(insert_query, user_data)
    
    # चेंज को सेव करें
    conn.commit()
    
    # कनेक्शन बंद करें
    conn.close()

           
def update_column_by_id(db_name, table_name, record_id, column_name, new_value):
    """
    Update the value of a specific column for a given ID in an SQLite database.

    :param db_name: Name of the SQLite database file.
    :param table_name: Name of the table where the record will be updated.
    :param record_id: The ID of the record to be updated.
    :param column_name: The name of the column to be updated.
    :param new_value: The new value to be set for the specified column.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Prepare the SQL query
        sql = f'UPDATE {table_name} SET {column_name} = ? WHERE id = ?'
        
        # Execute the SQL query
        cursor.execute(sql, (new_value, record_id))
        
        # Commit the transaction
        conn.commit()
        
        print("Column value updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating column value: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
            
def create_table_1(database_name, table_name):
    # कनेक्शन बनाएं (अगर फाइल नहीं है, तो यह एक नई फाइल बनाएगा)
    conn = sqlite3.connect(database_name)
    
    # कर्सर ऑब्जेक्ट बनाएं
    cursor = conn.cursor()
    
    # टेबल बनाने का SQL स्टेटमेंट
    create_table_query = f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY,
    mainid TEXT,
    view INT
)
'''
                
    # क्वेरी को निष्पादित करें
    cursor.execute(create_table_query)
    
    # चेंज को सेव करें
    conn.commit()
    
    # कनेक्शन बंद करें
    conn.close()

def create_table(database_name, table_name,conf):
    # कनेक्शन बनाएं (अगर फाइल नहीं है, तो यह एक नई फाइल बनाएगा)
    conn = sqlite3.connect(database_name)
    
    # कर्सर ऑब्जेक्ट बनाएं
    cursor = conn.cursor()
    
    # टेबल बनाने का SQL स्टेटमेंट
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS
    {table_name}(
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT
        )'''    	
                
    # क्वेरी को निष्पादित करें
    cursor.execute(create_table_query)
    
    # चेंज को सेव करें
    conn.commit()
    
    # कनेक्शन बंद करें
    conn.close()

def insert_view_record(database_name, table_name,data):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    insert_query = f'''
    INSERT INTO {table_name} (mainid,view)
    VALUES (?, ?)
    '''  
    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()

    
def table_exists(database_name, table_name):
    # कनेक्शन बनाएं (अगर फाइल नहीं है, तो यह एक नई फाइल बनाएगा)
    conn = sqlite3.connect(database_name)
    
    # कर्सर ऑब्जेक्ट बनाएं
    cursor = conn.cursor()
    
    # तालिका के अस्तित्व की जांच के लिए SQL क्वेरी
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table' AND name=?
    ''', (table_name,))
    
    # परिणाम प्राप्त करें
    result = cursor.fetchone()
    
    # कनेक्शन बंद करें
    conn.close()
    
    # परिणाम के आधार पर 'YES' या 'NO' लौटाएं
    if result:
        return 'YES'
    else:
        return 'NO'
									
