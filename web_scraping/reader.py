import pandas as pd
import logging
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)

def read_to_postgres(db_name, table_name, connection_string):
    engine = create_engine(connection_string)
    logging.info(f"Reading from database: '{db_name}', table '{table_name}'")
    return pd.read_sql_table(table_name, con=engine)
