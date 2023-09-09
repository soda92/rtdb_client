DROP TRIGGER IF EXISTS watch_realtime_table_trigger ON realtime_table;
DROP TABLE IF EXISTS realtime_table;
DROP FUNCTION IF EXISTS notify_trigger;

/* Replace with your SQL commands */
CREATE TABLE realtime_table (id serial primary key, key varchar, type varchar,
    value_int NUMERIC, value_float double precision, value_str text);
CREATE FUNCTION notify_trigger() RETURNS trigger AS $$
DECLARE
BEGIN
    PERFORM pg_notify('watch_realtime_table', row_to_json(NEW)::text);
    RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER watch_realtime_table_trigger AFTER INSERT ON realtime_table
FOR EACH ROW EXECUTE PROCEDURE notify_trigger();
