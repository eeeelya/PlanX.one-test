SELECT notebooks_brand.title, COUNT(notebooks_brand.title) AS "notebook_count"
FROM notebooks_notebook
	 INNER JOIN notebooks_brand ON notebooks_brand.id = notebooks_notebook.brand_id
GROUP BY notebooks_brand.title
ORDER BY COUNT(notebooks_brand.title) DESC