import psycopg2

conn = psycopg2.connect(host="localhost", dbname="example", user="soda", password="soda")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

for _ in range(1000):
    cursor = conn.cursor()
    cursor.execute(f"INSERT into realtime_table (key, type, value_float) values (%s, %s, %s)", ("PR_VAL1", "float",  11.2))
    cursor.execute(f"INSERT into realtime_table (key, type, value_str) values (%s, %s, %s)", ("HB_VAL1", "str",  "message"))
    conn.commit()
    import time
    time.sleep(0.1)