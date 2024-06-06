import pandas as pd
import logging
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)

def write_to_postgres(df, db_name, table_name, connection_string):
    engine = create_engine(connection_string)
    logging.info(f"Writing to database: '{db_name}', table '{table_name}'")
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
