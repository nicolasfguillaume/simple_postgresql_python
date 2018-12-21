# coding: utf-8
import pandas as pd

def replace_table(df, table_name, db):
	df.to_sql(table_name, db, if_exists='replace')


def query_table(table_name, db):
	return pd.read_sql_query('select * from {}'.format(table_name), db)