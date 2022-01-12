
--CREATE TABLE BILLBOARD
create table public."Billboard" (
	"date" date null,
	"rank" int4 null,
	song varchar(300) null,
	artist varchar(300) null,
	"last-week" int4 null,
	"peak-rank" int4 null,
	"weeks-on-board" int4 null
);

select count(*) as quantidade
from public."Billboard"
limit 100


