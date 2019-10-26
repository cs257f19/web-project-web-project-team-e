'''
psycopg2-test.py

Sample code demonstrating how to use the psycopg2 Python library to connect
to a database and execute a query.

author: Amy Csizmar Dalal
date: 22 October 2019
Adapted from code originally written by Jeff Ondich
'''
import getpass
import psycopg2


def connect(user, password):
	'''
	Establishes a connection to the database with the following credentials:
		user - username, which is also the name of the database
		password - the password for this database on perlman

	Returns: a database connection.

	Note: exits if a connection cannot be established.
	'''
	try:
		connection = psycopg2.connect(database=user, user=user, password=password)
	except Exception as e:
		print("Connection error: ", e)
		exit()
	return connection

def getNumberOfProjects(connection):
	'''
	Gives the total number of projects(entries) in the datatable. This is done to avoid having a 'magic number'

	PARAMETERS:
		connection - the connection to the database

	RETURNS:
		an int that is the total number of entries
	'''
	try:
		cursor = connection.cursor()
		query = "SELECT COUNT(ID) FROM ksdata"
		cursor.execute(query)
		return int(cursor.fetchall()[0][0])

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return connection.cursor()

def getMinimumValueOfVariable(connection, nameOfVariable):
	'''
	Returns the smallest value (a float) in the dataset for a given variable (filter)

	PARAMETERS:
		nameOfVariable - the major variable from which the minimum value is being taken

	RETURN:
		a float that is the smallest value in the dataset for the variable provided

	'''

	try:
		cursor = connection.cursor()
		query = "SELECT MIN(" + str(nameOfVariable) + ") FROM ksdata"
		cursor.execute(query)
		smallestValue = float(cursor.fetchall()[0][0])
		return smallestValue

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None

def main():

	# Replace these credentials with your own
	user = 'santosb'
	password = 'books347winter'

	# Connect to the database
	connection = connect(user, password)


	results = getNumberOfProjects(connection)
	minVariable = getMinimumValueOfVariable(connection, 'backers')

	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	if minVariable is not None:
		print("The smallest number of backers was ")
		print(minVariable)

	# Disconnect from database
	connection.close()

main()
