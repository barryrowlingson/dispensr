
create table prescriptions (
   id    serial primary key,
       sha  text,
       pct  text,
       practice  text,
bnfcode  text,
bnfname  text,
chemical_code  text,
chemical_name  text,
product  text,
generic  text,
equivalent  text,
items  integer,
nic  numeric(10,2),
act_cost  numeric(10,2),
quantity  integer,
period  integer,
year  integer,
month  integer,
xgrid  integer,
ygrid  integer,
postcode text
)
