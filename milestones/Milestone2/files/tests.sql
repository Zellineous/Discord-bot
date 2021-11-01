-- This file will test the integrity of the DB

USE RailwayManagementDB;

-- Testing Passenger
DELETE FROM Passenger WHERE name = 'tommy';
UPDATE Passenger SET passenger_id = 4 WHERE name = 'jeff';

-- Testing AccountType
DELETE FROM AccountType WHERE version = 'basic';
UPDATE AccountType SET account_typeid = 3 WHERE version = 'premium';

-- Testing Region
DELETE FROM Region WHERE name = 'south region';
-- UPDATE Region SET region_id = 1 WHERE name = 'east region';

-- Testing Station
DELETE FROM Station WHERE name = 'north station';
-- UPDATE Station SET station_id = 4 WHERE name = 'east region';

-- Testing User
DELETE FROM User WHERE name = 'Jim';
UPDATE User SET user_id = 3 WHERE name = 'bob';

-- Testing Account
-- DELETE FROM Account WHERE email = 'yes@456.com';
-- UPDATE Account SET account_id = 5 WHERE email = 'yes@456.com';

-- Testing Train
DELETE FROM Train WHERE model = '2';
UPDATE Train SET train_id = 6 WHERE model = '1';

-- Testing Employee
-- DELETE FROM Employee WHERE name = 'Joe';
UPDATE Employee SET employee_id = 6 WHERE name = 'Ted';

-- Testing PoliceDepartment
DELETE FROM PoliceDepartment WHERE police_name = 'north dept';
UPDATE PoliceDepartment SET p_station_id = 6 WHERE police_name = 'south dept';

-- Testing FireDepartment
DELETE FROM FireDepartment WHERE firefighter_name = 'north dept';
UPDATE FireDepartment SET f_station_id = 6 WHERE firefighter_name = 'south dept';

-- Testing TrainYard
DELETE FROM TrainYard WHERE name = 'north yard';
UPDATE TrainYard SET t_yard_id = 8 WHERE name = 'east yard';

-- Testing RepairYard
DELETE FROM RepairYard WHERE name = 'north yard';
UPDATE RepairYard SET r_yard_id = 8 WHERE name = 'east yard';

-- Testing Trip
DELETE FROM Trip WHERE name = 'south trip';
-- UPDATE Trip SET trip_id = 3 WHERE name = 'north trip';

-- Testing Routes
DELETE FROM Routes WHERE name = 'north route';
UPDATE Routes SET route_id = 8 WHERE name = 'south route';

-- Testing Ticket
DELETE FROM Ticket WHERE exp_id = '1 day';
UPDATE Ticket SET ticket_id = 8 WHERE exp_id = 'all week pass';

-- Testing Driver
DELETE FROM Driver WHERE name = 'mike';
-- UPDATE Driver SET driver_id = 3 WHERE name = 'ben';

-- Testing Manager
DELETE FROM Manager WHERE name = 'steph';
UPDATE Manager SET manager_id = 2 WHERE name = 'celine';

-- Testing PaymentType
DELETE FROM PaymentType WHERE billing_adress = 'somewhere east';
UPDATE PaymentType SET type_id = 4 WHERE billing_adress = 'somewhere south';

-- Testing Supplier
DELETE FROM Supplier WHERE name = 'south supplier';
UPDATE Supplier SET supplier_id = 5 WHERE name = 'east supplier';

-- Testing MobileDevice
DELETE FROM MobileDevice WHERE brand_name = 'apple';
UPDATE MobileDevice SET device_id = 5 WHERE brand_name = 'nokia';


