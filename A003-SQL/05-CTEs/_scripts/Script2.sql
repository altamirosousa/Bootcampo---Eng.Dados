SELECT  t1."date",
		t1."rank",
		t1.song,
		t1.artist,
		t1."last-week",
		t1."peak-rank",
		t1."weeks-on-board"
FROM PUBLIC."Billboard" AS t1 limit 100
-----------------------------------------------------------------------------------
select distinct 
		t1.artist,
		t1.song		
from PUBLIC."Billboard" as t1
order by t1.artist, 
		 t1.song;

select 	t1.artist,
		count(*) as qtd_art 		
from PUBLIC."Billboard" as t1
group by t1.artist
order by t1.artist desc;

select 	t1.song,
		count(*) as qtd_art 		
from PUBLIC."Billboard" as t1
group by t1.song 
order by t1.song;
-----------------------------------------------------------------------------------
--NORMAL
SELECT DISTINCT t1.artist
	,t2.qtd_artist
	,t1.song
	,t3.qtd_song
FROM PUBLIC."Billboard" AS t1
LEFT JOIN (
	SELECT t1.artist
		,count(*) AS qtd_artist
	FROM PUBLIC."Billboard" AS t1
	GROUP BY t1.artist
	ORDER BY t1.artist
	) AS t2 ON (t1.artist = t2.artist)
LEFT JOIN (
	SELECT t1.song
		,count(*) AS qtd_song
	FROM PUBLIC."Billboard" AS t1
	GROUP BY t1.song
	ORDER BY t1.song
	) AS t3 ON (t1.song = t3.song)
ORDER BY t1.artist
	,t1.song;

-- COM CTEs
WITH cte_artist
AS (
	SELECT t1.artist
		,count(*) AS qtd_artist
	FROM PUBLIC."Billboard" AS t1
	GROUP BY t1.artist
	ORDER BY t1.artist
	)
	,cte_song
AS (
	SELECT t1.song
		,count(*) AS qtd_song
	FROM PUBLIC."Billboard" AS t1
	GROUP BY t1.song
	ORDER BY t1.song
	)
SELECT DISTINCT t1.artist
	,t2.qtd_artist
	,t1.song
	,t3.qtd_song
FROM PUBLIC."Billboard" AS t1
LEFT JOIN cte_artist AS t2 ON (t1.artist = t2.artist)
LEFT JOIN cte_song AS t3 ON (t1.song = t3.song)
ORDER BY t1.artist
	,t1.song;

