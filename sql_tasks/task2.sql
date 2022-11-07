SELECT (ROUND(width), ROUND(height), ROUND(depth)) AS "dimensions",
       COUNT(width) AS "notebook_counts"
FROM notebooks_notebook
GROUP BY width, height, depth
ORDER BY COUNT(width) DESC