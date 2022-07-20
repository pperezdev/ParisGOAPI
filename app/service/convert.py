import psycopg2
import csv
import pandas as pd

def connect_sql():
    return psycopg2.connect(
        host="db01pa4dd01.cy9dbtaa6m9y.eu-west-3.rds.amazonaws.com",
        database="db01pa4dd01",
        user="admindb01pa4dd01",
        password="pasSwordA16dmin")

def csv_to_sql(output_file, header_took, database_table, header_sql, mapped_column=None):
    conn = connect_sql()
    cursor = conn.cursor()
    filtered_df = pd.read_csv(f"D:\projetAnnuel\ParisGOAPI\data\{output_file}", encoding='utf8', usecols=header_took, sep = ';')
    filtered_df = filtered_df.fillna("")
    if mapped_column != None:
        for col in mapped_column:
            filtered_df[col] = filtered_df[col].astype("string")

    filtered_df['Filename'] = output_file

    values = filtered_df.to_records(index=False)
    sql_header_val = ""
    for i in range(0, len(header_took)+1):
        sql_header_val += "%s,"

    sql_header_val = sql_header_val[:-1]
    args = ','.join(cursor.mogrify(f"({sql_header_val})", i).decode('utf-8')
                    for i in values)

    cursor.execute(f"INSERT INTO {database_table} {header_sql} VALUES {args}")
    conn.commit()
    cursor.close()
    conn.close()

def get_table(columns_header, database_table):
    conn = connect_sql()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {database_table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns_header, row)))
    conn.commit()
    cursor.close()
    conn.close()
    return result

def get_table_id(columns_header, database_table, id_name, id):
    conn = connect_sql()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {database_table} WHERE {id_name} = {id}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns_header, row)))
    conn.commit()
    cursor.close()
    conn.close()
    return result