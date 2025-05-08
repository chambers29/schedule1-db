SELECT
	n.area_id
	,a.name
	,COUNT(a.name)
	,n.standards
FROM npcs n
JOIN areas a ON a.area_id = n.area_id
WHERE standards != '-'
GROUP BY n.area_id, a.name, n.standards
ORDER BY n.area_id