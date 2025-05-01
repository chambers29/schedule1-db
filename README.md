# schedule1-db

A homemade relational database project built for learning, practice, and fun. It contains data related to NPCs and related entities from the game *Schedule 1*.

This database is designed using relational tables to represent key aspects of the game. It can be useful during gameplay, for example to check:
- the area of a specific NPC,
- their favorite effect,
- and which ingredient gives that effect.

## Repository structure

- `schedule1.sql` – SQL file that creates all database tables and relationships based on the ER diagram.
- `schedule1_database_diagram.png` – Visual entity-relationship diagram used as a base for the database structure.
- `insert/` – SQL scripts with `INSERT INTO` statements that populate the database with values.
- `scripts/` – Python scripts that automate table population.
- `data/` – Text files with raw data (copied from the game wiki: [Schedule-1 Wiki](https://schedule-1.fandom.com/)), used by the scripts.

## Query and table examples

```sql
SELECT
	n.name npc_name
	, eff.name effect_name
	, i.name ingredient_name
FROM effects_npc e
JOIN npcs n ON e.npc_id = n.npc_id
JOIN effects eff ON e.effect_id = eff.effect_id
JOIN ingredients i ON i.effect_id = e.effect_id
ORDER BY n.npc_id
LIMIT 10 OFFSET 10;

![example](examples/example_npc_effect_ingredient.png)
This sample output demonstrates how the database can save time during gameplay by helping the player quickly identify which ingredients produce the effects preferred by specific NPCs.

In the game, you only see which effects an NPC likes — but you still have to remember or manually check which ingredients provide those effects.
This query makes that process much faster and more convenient.
