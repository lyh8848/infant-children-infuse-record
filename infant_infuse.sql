use infuse_record;
create table nurse(
id integer,
cur_mission1_id integer,
cur_mission2_id integer,
cur_mission3_id integer,
cur_mission4_id integer,
cur_mission5_id integer);
create table patient(
id integer,
sex enum('M','F'),
room integer,
bed integer);
create table mission(
id integer,
patient_id integer,
nurse_id integer,
kind enum('INJECT','INSPECT','UPDATE','FINISH'),
priority enum('PRIVATE','PUBLIC'),
todo_time timestamp,
detail json,
state enum('TODO','ABNORM','INTERRAPT','COMPLETE'),
abnorm varchar(100));


