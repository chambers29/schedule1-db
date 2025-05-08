UPDATE npcs n
SET standards = CASE
	WHEN name IN ('Geraldine Poon','Jessi Waters','Keith Wagner','Greg Figgle','Genghis Barn') THEN 'Very Low'
	ELSE standards
END