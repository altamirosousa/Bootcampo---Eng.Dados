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

--IMPORTADOS DADOS VIA CSV

--SELECT DE DADOS
SELECT  t1."date",
		t1."rank",
		t1.song,
		t1.artist,
		t1."last-week",
		t1."peak-rank",
		t1."weeks-on-board"
FROM PUBLIC."Billboard" AS t1 limit 100
-------------------------------------------
SELECT  t1.song,
		t1.artist
FROM PUBLIC."Billboard" AS t1 
where t1.artist = 'Chuck Berry'
-------------------------------------------
SELECT  t1.song,
		t1.artist,
		count(*) as "#song"
FROM PUBLIC."Billboard" as t1 
--where t1.artist = 'Chuck Berry' or t1.artist = 'Frankie Vaughan'
where t1.artist in ('Chuck Berry', 'Frankie Vaughan')
group by t1.artist, t1.song
order by "#song"	desc;	


