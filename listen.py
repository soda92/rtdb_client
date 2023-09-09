import asyncio
import psycopg2

# dbname should be the same for the notifying process
conn = psycopg2.connect(host="localhost", dbname="example", user="soda", password="soda")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute(f"LISTEN watch_realtime_table;")

def handle_notify():
    conn.poll()
    for notify in conn.notifies:
        print(notify.payload)
    conn.notifies.clear()

# It works with uvloop too:
# import uvloop
# loop = uvloop.new_event_loop()
# asyncio.set_event_loop(loop)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.get_event_loop()
loop.add_reader(conn, handle_notify)
try:
    loop.run_forever()
finally:
    loop.close()