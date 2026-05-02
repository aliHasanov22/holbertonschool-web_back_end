-- sql for calcualting bands with glam rock
SELECT band_name, 
       IFNULL(2024 - split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%glam rock%'
ORDER BY lifespan DESC;