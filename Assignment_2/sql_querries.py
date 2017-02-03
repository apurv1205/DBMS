#!/usr/bin/python
# The package installed by the pip install command
import MySQLdb
from prettytable import PrettyTable

# connecting to the mySQL database
db = MySQLdb.connect(host="10.5.18.102", 	    # your host, usually localhost
                     user="14CS10006",          # your username
                     passwd="btech14",  		# your password
                     db="14CS10006")        	# name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
print "\n*******Connection to the required table in the specified database is successful\n*******Executing SQL querries\n"

# Executing the sql querries of assignment 1
# enclosing in try except block for error handling
###############First###########################
try:
	#first querry : List all the Courses taught by the teacher - "PPC" 
	cur.execute("SELECT Cname FROM Courses WHERE CID IN (SELECT CID FROM Teacher,Teaches WHERE Teacher.TID=Teaches.TID AND Teacher.name='PPC')")
	rows=cur.fetchall()

	# print the result set of above the sql querries
	print "\n1.All the Courses taught by the teacher - 'PPC' :"

	#using pretty table for sql formatted output
	x = PrettyTable([cur.description[0][0]])
	for row in rows:
	    x.add_row(row)
	print x

except MySQLdb.Error,e:
	print "MySQL Error: %s" % str(e)


###############Second########################
try:
	#second querry : List all students registered in the courses taught by "PPC"
	cur.execute("SELECT name FROM Student WHERE roll IN (SELECT roll FROM Takes WHERE CID IN (SELECT CID FROM Teacher,Teaches WHERE Teacher.TID=Teaches.TID AND Teacher.name='PPC'))")
	rows=cur.fetchall()

	# print the result set of the above sql querries
	print "\n2.All students registered in the courses taught by 'PPC' :"

	#using pretty table for sql formatted output
	x = PrettyTable([cur.description[0][0]])
	for row in rows:
	    x.add_row(row)
	print x


except MySQLdb.Error,e:
	print "MySQL Error: %s" % str(e)


##################Third#########################
try:
	#third querry : List the timings of all courses in Class-Room 'NC142'
	cur.execute("SELECT time_schedule FROM Timings WHERE slot IN (SELECT slot FROM Teaches WHERE CLID='NC142')")
	rows=cur.fetchall()

	# print the result set of the above sql querries
	print "\n3.The timings of all courses in Class-Room 'NC142' :"

	#using pretty table for sql formatted output
	x = PrettyTable([cur.description[0][0]])
	for row in rows:
	    x.add_row(row)
	print x

except MySQLdb.Error,e:
	print "MySQL Error: %s" % str(e)


##################Fourth############################
try:
	#fourth querry : List the name of the students who received the highest marks in the courses taught by 'PPC'
	cur.execute("SELECT name FROM Student WHERE roll in (SELECT roll FROM (SELECT CID,MAX(marks) AS max_marks FROM Takes GROUP BY CID HAVING CID IN (SELECT CID FROM Teacher,Teaches WHERE Teacher.TID=Teaches.TID AND Teacher.name='PPC')) AS T,Takes  WHERE T.max_marks=Takes.marks)")
	rows=cur.fetchall()

	# print the result set of the above sql querries
	print "\n4.The name of the students who received the highest marks in the courses taught by 'PPC' :"

	#using pretty table for sql formatted output
	x = PrettyTable([cur.description[0][0]])
	for row in rows:
		x.add_row(row)
	print x

except MySQLdb.Error,e:
	print "MySQL Error: %s" % str(e)


#################Fifth############################
try:
	#fifth querry :  List the students who have received a grade of 'EX' in the largest number of courses
	cur.execute("SELECT name FROM Student,(SELECT roll,grades,CID,COUNT(grades) AS EX_count FROM Grade_card WHERE grades='EX' GROUP BY roll) AS T WHERE T.roll=Student.roll AND EX_count = (SELECT MAX(EX_count) FROM (SELECT roll,grades,CID,COUNT(grades) AS EX_count FROM Grade_card WHERE grades='EX' GROUP BY roll) AS T )")
	rows=cur.fetchall()

	# print the result set of the above sql querries
	print "\n5.The students who have received a grade of 'EX' in the largest number of courses :"

	#using pretty table for sql formatted output
	x = PrettyTable([cur.description[0][0]])
	for row in rows:
		x.add_row(row)
	print x

except MySQLdb.Error,e:
	print "MySQL Error: %s" % str(e)


#closing the cursor and the database
cur.close()
db.close()

print "\n*******All querries executed successfully\n*******The database and cursor object is now closed\n"