CREATE TABLE "npcs" (
  "npc_id" int PRIMARY KEY,
  "name" varchar(50),
  "area_id" int,
  "is_customer" bool,
  "role_id" int
);

CREATE TABLE "roles" (
  "role_id" int PRIMARY KEY,
  "name" varchar(25)
);

CREATE TABLE "areas" (
  "area_id" int PRIMARY KEY,
  "name" varchar(50),
  "level" int
);

CREATE TABLE "buildings" (
  "building_id" int PRIMARY KEY,
  "name" varchar(50),
  "type_id" int,
  "area_id" int
);

CREATE TABLE "building_types" (
  "type_id" int PRIMARY KEY,
  "name" varchar(50)
);

CREATE TABLE "effects" (
  "effect_id" int PRIMARY KEY,
  "name" varchar(50)
);

CREATE TABLE "effects_npc" (
  "effect_id" int,
  "npc_id" int
);

CREATE TABLE "ingredients" (
  "ingredient_id" int PRIMARY KEY,
  "name" varchar(50),
  "cost" decimal,
  "effect_id" int
);

ALTER TABLE "buildings" ADD FOREIGN KEY ("area_id") REFERENCES "areas" ("area_id");

ALTER TABLE "npcs" ADD FOREIGN KEY ("area_id") REFERENCES "areas" ("area_id");

ALTER TABLE "buildings" ADD FOREIGN KEY ("type_id") REFERENCES "building_types" ("type_id");

ALTER TABLE "effects_npc" ADD FOREIGN KEY ("npc_id") REFERENCES "npcs" ("npc_id");

ALTER TABLE "effects_npc" ADD FOREIGN KEY ("effect_id") REFERENCES "effects" ("effect_id");

ALTER TABLE "npcs" ADD FOREIGN KEY ("role_id") REFERENCES "roles" ("role_id");

ALTER TABLE "ingredients" ADD FOREIGN KEY ("effect_id") REFERENCES "effects" ("effect_id");
