UPDATE npcs n
SET standards = CASE
	WHEN n.is_customer = FALSE THEN '-'
	WHEN a.name IN ('Northtown','Westville') THEN 'Low'
	WHEN a.name IN ('Docks','Downtown') THEN 'Moderate'
	WHEN a.name IN ('Suburbia','Town') THEN 'High'
	ELSE standards
END
FROM areas a
WHERE a.area_id = n.area_id




