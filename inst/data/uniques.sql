
DROP TABLE IF EXISTS chemicals;

CREATE TABLE chemicals
(
  chemsub text,
  code text,
  -- blank text,
  id serial PRIMARY KEY NOT NULL
)
WITH (
  OIDS=FALSE
);

CREATE or REPLACE FUNCTION importData() RETURNS trigger AS $$
DECLARE result INTEGER;
BEGIN
result = (select count(*) from chemicals 
	where chemsub=new.chemsub and code=new.code);
if result = 1 THEN
 RETURN null;
 END IF;
 
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER btestinsert
BEFORE INSERT
ON chemicals
FOR EACH ROW
EXECUTE PROCEDURE importdata();

-- Use:
-- COPY chemicals (chemsub, code, blank) from '/home/rowlings/Downloads/Data/T201301CHEM SUBS.CSV' WITH delimiter ',' CSV HEADER;
 