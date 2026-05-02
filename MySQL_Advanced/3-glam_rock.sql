-- lists Glam rock bands 
SELECT band_name,
       IFNULL(2024 - split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;