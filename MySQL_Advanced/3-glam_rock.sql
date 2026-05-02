-- sql for calcualting bands with glam rock
SELECT band_name, IF(split IS NOT NULL, split - formed, YEAR(2024) - formed) AS life_span
FROM metal_bands
WHERE genre = 'glam rock'
GROUP BY band_name
ORDER BY life_span DESC;