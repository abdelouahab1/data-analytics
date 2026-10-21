/* a) The actor table contains information about actors, including their actor ID, first name, last name, and last update timestamp. 

b) The film table contains information about films, including their film ID, title, description, release year, language, rental rate, length, and rating. 

c) The film_actor table contains both actor_id and film_id columns and connects actors to the films they appear in. 

d) The rental table includes rental IDs, rental dates, inventory IDs, customer IDs, return dates, staff IDs, and last update timestamps. This information can be hard to read because it uses numeric IDs instead of names, so we need to connect it to other tables to understand the records. 

e) The inventory table includes inventory IDs, film IDs, store IDs, and last update timestamps. It identifies which film copies are available at each store. 

f) The rental, inventory, and film tables are needed to find the names of all films rented on a specific date. The rental table contains the rental date and inventory ID. The inventory table connects the inventory ID to a film ID, and the film table uses the film ID to provide the film title. These tables can be joined using their related ID columns. */ 

SELECT rental_date, inventory_id FROM rental; 

SELECT inventory_id, film_id FROM inventory; 

SELECT film_id, title FROM film; 