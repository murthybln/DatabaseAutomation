import pandas as pd
import pyodbc as db


def get_db_data(db_conn, query):
	"""
	Executes the given query and returns the number of rows
	:param db_conn:
	:param query:
	:return: number of rows
	"""
	with db.connect(db_conn, autocommit=True) as dbconn:
		df_result = pd.read_sql_query(query, dbconn)
	return len(df_result)

