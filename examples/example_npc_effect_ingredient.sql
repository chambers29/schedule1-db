SELECT
	n.name npc_name
	, eff.name effect_name
	, i.name ingredient_name
FROM effects_npc e
JOIN npcs n ON e.npc_id = n.npc_id
JOIN effects eff ON e.effect_id = eff.effect_id
JOIN ingredients i ON i.effect_id = e.effect_id
ORDER BY n.npc_id
LIMIT 10 OFFSET 10