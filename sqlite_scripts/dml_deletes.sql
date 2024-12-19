CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS SELECT name FROM sqlite_master WHERE type='table' AND name IN ('customer', 'seller', 'service', 'service_info', 'payment', 'automobile', 'model', 'maker', 'price');

DELETE FROM customer WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'customer');
DELETE FROM seller WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'seller');
DELETE FROM service WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'service');
DELETE FROM service_info WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'service_info');
DELETE FROM payment WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'payment');
DELETE FROM automobile WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'automobile');
DELETE FROM model WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'model');
DELETE FROM maker WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'maker');
DELETE FROM price WHERE EXISTS (SELECT 1 FROM temp_table WHERE name = 'price');

DROP TABLE temp_table;
