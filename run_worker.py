# coding: utf-8

# https://www.tutorialspoint.com/postgresql/postgresql_python.htm

import pandas as pd
from sqlalchemy import create_engine
from postgres_utils import replace_table, query_table

db = create_engine('postgresql://postgres:example@localhost:5400/postgres')

if __name__ == '__main__':

	df = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
	df.columns = df.iloc[0, :]

	replace_table(df, 'df', db)

	df = query_table('df', db)

	print df.head()
