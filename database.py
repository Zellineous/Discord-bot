# database.py
# Handles all the methods interacting with the database of the application.
# Students must implement their own methods here to meet the project requirements.

import os
import pymysql.cursors

db_host = os.environ['DB_HOST']
db_username = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']


conn = pymysql.connect(host=db_host,
                               port=3306,
                               user=db_username,
                               password=db_password,
                               db=db_name,
                               charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

def connect():
    try:
        print("Bot connected to database {}".format(db_name))
        return conn
    except:
        print("Bot failed to create a connection with your database because your secret environment variables " +
              "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
        print("\n")

# your code here


List1 = []
List2 = []
List3 = []
List4 = []

def q1(m):

  cur = conn.cursor()
  sql = ("SELECT Region.name, Station.name, Station.description, Station.t_yard, Station.r_yard FROM Region JOIN Station ON Region.region_id = Station.region WHERE Station.description >= (%s);")

  cur.execute(sql, (m))
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  List3.clear()
  List4.clear()
  for x in result:
    List1.append(x['description'])
    List2.append(x['Station.name'])
    List3.append(x['t_yard'])
    List4.append(x['r_yard'])
  response = ("The station ", List2, " is newer than ", m ," with a start date of ", List1 ," and their train status is ", List3," and the repair yard status is ", List4)
  return response
  
def q2(o,p):
  cur = conn.cursor()
  sql = ("SELECT Driver.name, Manager.name, Driver.description, Manager.description, Driver.salary, Manager.salary FROM Driver JOIN Manager ON Driver.yearsHere = Manager.yearsHere WHERE Manager.description BETWEEN %s AND %s")
  cur.execute(sql,(o,p))
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  List3.clear()
  List4.clear()
  for x in result:
    List1.append(x['Manager.name'])
    List2.append(x['Manager.salary'])
    List3.append(x['name'])
    List4.append(x['salary'])
  a = sum(List2)/len(List2)
  b = sum(List4)/len(List4)
  c = (a+b)/2
  response = ("The names of the managers are ",List1," the name of the drivers are ", List3, " with a sallary of ", List2," and ", List4, " respectivly. The average of managers is ", a," and for dirvers is ", b," The average of both is ",c)
  return response


def q3(y):
  cur = conn.cursor()
  sql = ("SELECT Trip.name, Routes.name, Trip.people, Routes.timestaken FROM Trip JOIN Routes ON Trip.trip_id = Routes.route_id WHERE Routes.timestaken >= %s ")
  cur.execute(sql, (y))
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  List3.clear()
  for x in result:
    List1.append(x['name'])
    List2.append(x['Routes.name'])
    List3.append(x['timestaken'])
  response = ("The trips ", List1, " that had routes taken more than ", List3," is called ",List2)
  return response

def q4 (r):
  cur = conn.cursor()
  sql = ("SELECT Passenger.name, Train.model, Passenger.description, Train.description FROM Passenger JOIN Train ON Passenger.passenger_id = Train.train_id WHERE Passenger.description > (%s) ")
  cur.execute(sql, (r))
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  List3.clear()
  for x in result:
    List1.append(x['name'])
    List2.append(x['Train.description'])
    List3.append(x['model'])
  response = ("Passengers", List1," borded the train model ", List3," about ", List2," times after ",r)
  return response

def q5(l,k):
  cur = conn.cursor()
  sql = ("SELECT Trip.name, Trip.description, Trip.people, Passenger.name FROM Trip JOIN Passenger ON Passenger.passenger_id = Trip.trip_id WHERE Trip.description BETWEEN (%s) AND (%s)")
  cur.execute(sql,(l,k))
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  List3.clear()
  for x in result:
    List1.append(x['people'])
    List2.append(x['name'])
    List3.append(x['Passenger.name'])
  o = sum(List1)/len(List1)
  response = ("The average ammount of people, inluding", List3, " taking the trip between ", l ," and", k," is ", o, " for trips ",List2)
  return response

def q6 (f,g):
  cur = conn.cursor()
  sql = ("SELECT name, miles FROM Routes WHERE miles >= (%s) AND miles <= (%s)")
  cur.execute(sql,(f,g))
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  for x in result:
    List1.append(x['name'])
    List2.append(x['miles'])
    a = sum(List2)/len(List2)
  response = (" All routes that are less than ",f,"miles and more than ",g,"miles are ", List1," and the average miles are ",a)
  return response 

def q7 (d):
  cur = conn.cursor()
  a = d
  sql = ("SELECT Station.name, Trip.name FROM Station JOIN Trip ON Station.station_id = Trip.trip_id WHERE Station.name LIKE '" + a + "%'")
  cur.execute(sql)
  result = cur.fetchall()
  List1.clear()
  List2.clear()
  for x in result:
    List1.append(x['name'])
    List2.append(x['Trip.name'])
  response = ("The trips ",List2, " with stations that start with", a," in their name are",List1)
  return response
