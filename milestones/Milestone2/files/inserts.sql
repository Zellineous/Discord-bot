-- This file will populate the tables with data

USE RailwayManagementDB;

-- Passenger table inserts
INSERT INTO Passenger (passenger_id, name, description) VALUES (1,'steve','morning time'),(2,'tommy','evening time'),(3,'jeff','night time');

-- AccountType table inserts
INSERT INTO AccountType (account_typeid, version, description) VALUES (1,'basic', 'few features'),(2,'premium','all features');

-- Region table inserts
INSERT INTO Region (region_id, name, description) VALUES (1,'north region','located in the north'),(2,'south region','located in the south'),(3,'east region','located in the east');

-- Station table inserts
INSERT INTO Station (station_id, name, description, region) VALUES (1,'north station', 'clean', 1),(2,'south station', 'dirty', 2),(3,'east station', 'quiet', 3);

-- User table inserts
INSERT INTO User (user_id, name, last_name) VALUES (1,'Bob', 'something'),(2,'John', 'anotherthing'),(3,'Jim','random lastname');

-- Account table inserts
INSERT INTO Account (account_id, email, password, a_type, user) VALUES (1,'hello@123.com', 'yes486651', 1, 2),(2,'no@123.com', 'no94161486',1,3),(3,'yes@456.com', 'newpass',2,1);

-- Train table inserts
INSERT INTO Train (train_id, model, description) VALUES (1,1,'new'),(2,3,'old'),(3,2,'used');

-- Employee table inserts
INSERT INTO Employee (employee_id, name, description, station) VALUES (1,'Joe', 'management',1),(2,'Albert','low pay',2),(3,'Ted','high pay',3);

-- Police dept table inserts
INSERT INTO PoliceDepartment (p_station_id, police_name, description) VALUES (1,'north dept','old'),(2,'south dept','new'),(3,'east dept','used');

-- Fire dept table inserts
INSERT INTO FireDepartment (f_station_id, firefighter_name, description) VALUES (1,'north dept','old'),(2,'south dept','new'),(3,'east dept','used');

-- Train yard table inserts
INSERT INTO TrainYard (t_yard_id, name, description) VALUES (1,'north yard','old'),(2,'south yard','new'),(3,'east yard','used');

-- Repair yard table inserts
INSERT INTO RepairYard (r_yard_id, name, description) VALUES (1,'north yard','old'),(2,'south yard','new'),(3,'east yard','used');

-- Trip table inserts
INSERT INTO Trip (trip_id, name, description) VALUES (1,'north trip','to north station'),(2,'south trip','to south station'),(3,'east trip','to east station');

-- Routes table inserts
INSERT INTO Routes (route_id, name, description) VALUES (1,'north route','to north station'),(2,'south route','to south station'),(3,'east route','to east station');

-- Ticket table inserts
INSERT INTO Ticket (ticket_id, exp_id, description) VALUES (1,'1 day','all day pass'),(2,'7 day','all week pass'),(3,'1 trip','standard ticket');

-- Driver table inserts
INSERT INTO Driver (driver_id, name, description) VALUES (1,'mike','old'),(2,'ben','young'),(3,'jose','old');
 
-- Manager table inserts
INSERT INTO Manager (manager_id, name, description) VALUES (1,'steph','north station manager'),(2,'celine','south station manager'),(3,'william','east station manager');

-- PaymentType table inserts
INSERT INTO PaymentType (type_id, billing_adress, description) VALUES (1,'somewhere north','creditcard'),(2,'somewhere south','debitcard'),(3,'somewhere east','bank wire');

-- Supplier table inserts
INSERT INTO Supplier (supplier_id, name, description) VALUES (1,'north supplier','N-supply'),(2,'south supplier','S-supply'),(3,'east supplier','E-supply');

-- MobileDevice table inserts
INSERT INTO MobileDevice (device_id, brand_name, description) VALUES (1,'apple','a iphone'),(2,'samsung','a samsung galaxy'),(3,'nokia','nokia smartphone');

