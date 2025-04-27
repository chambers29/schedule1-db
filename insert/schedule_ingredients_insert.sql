INSERT INTO ingredients
VALUES 
	(1, 'Cuke', 2, (SELECT effect_id FROM effects WHERE name='Energizing')),
	(2, 'Banana', 2, (SELECT effect_id FROM effects WHERE name='Gingeritis')),
	(3, 'Paracetamol', 3, (SELECT effect_id FROM effects WHERE name='Sneaky')),
	(4, 'Donut', 3, (SELECT effect_id FROM effects WHERE name='Calorie-Dense')),
	(5, 'Viagra', 4, (SELECT effect_id FROM effects WHERE name='Tropic Thunder')),
	(6, 'Mouth Wash', 4, (SELECT effect_id FROM effects WHERE name='Balding')),
	(7, 'Flu Medicine', 5, (SELECT effect_id FROM effects WHERE name='Sedating')),
	(8, 'Gasoline', 5, (SELECT effect_id FROM effects WHERE name='Toxic')),
 	(9, 'Energy Drink', 6, (SELECT effect_id FROM effects WHERE name='Athletic')),
 	(10, 'Motor Oil', 6, (SELECT effect_id FROM effects WHERE name='Slippery')),
 	(11, 'Mega Bean', 7, (SELECT effect_id FROM effects WHERE name='Foggy')),
 	(12, 'Chili', 7, (SELECT effect_id FROM effects WHERE name='Spicy')),
	(13, 'Battery', 8, (SELECT effect_id FROM effects WHERE name='Bright-Eyed')),
 	(14, 'Iodine', 8, (SELECT effect_id FROM effects WHERE name='Jennerising')),
 	(15, 'Addy', 9, (SELECT effect_id FROM effects WHERE name='Thought-Provoking')),
 	(16, 'Horse Semen', 9, (SELECT effect_id FROM effects WHERE name='Long Faced'));