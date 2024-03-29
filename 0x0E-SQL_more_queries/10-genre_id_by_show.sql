-- The script will list all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.

-- join is used to dsplay data and order based on title and genre id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
