insert into customer (customer_id, full_name, phone_number)
values (1, 'Петров Алексей Вячеславович', '+79194234312');
insert into customer (customer_id, full_name, phone_number)
values (2, 'Столяров Висилий Иванович', '+79855534392');
insert into customer (customer_id, full_name, phone_number)
values (3, 'Баранова Анна Анатольевна', '+79152560823');
insert into customer (customer_id, full_name, phone_number)
values (4, 'Долгов Владимир Алексеевич', '+79167895643');
insert into customer (customer_id, full_name, phone_number)
values (5, 'Титов Александр Викторович', '+79153467890');
insert into customer (customer_id, full_name, phone_number)
values (6, 'Скалов Дуэйн Джонсонович', '+79857777777');
insert into customer (customer_id, full_name, phone_number)
values (7, 'Иванова Валерия Антоновна', '+79167239302');
insert into customer (customer_id, full_name, phone_number)
values (8, 'Алиев Анатолий Владимирович', '+79853476509');
insert into customer (customer_id, full_name, phone_number)
values (9, 'Кожухов Тимур Юрьевич', '+79194234313');
insert into customer (customer_id, full_name, phone_number)
values (10, 'Форсажев Доминик Тореттович', '+88003141592');

insert into seller (seller_id, full_name, phone_number)
values (1, 'Продавцов Иван Петрович', '+79252309878');
insert into seller (seller_id, full_name, phone_number)
values (2, 'Продавашкина Наталья Юрьевна', '+79544274311');
insert into seller (seller_id, full_name, phone_number)
values (3, 'Торговцев Вячеслав Артёмович', '+79199345647');
insert into seller (seller_id, full_name, phone_number)
values (4, 'Базаров Юрий Витальевич', '+79194235511');
insert into seller (seller_id, full_name, phone_number)
values (5, 'Продажев Денис Васильевич', '+79194230902');
insert into seller (seller_id, full_name, phone_number)
values (6, 'Втирашкин Кирилл Сергеевич', '+79194234234');
insert into seller (seller_id, full_name, phone_number)
values (7, 'Скидкин Алексей Александрович', '+79117434319');
insert into seller (seller_id, full_name, phone_number)
values (8, 'Наваров Вадим Алексеевич', '+79111234314');
insert into seller (seller_id, full_name, phone_number)
values (9, 'Щедрый Илья Степанович', '+79854200312');
insert into seller (seller_id, full_name, phone_number)
values (10, 'Хитрова Евгения Игоревна', '+89872478574');

insert into maker (maker_id, country, company)
values (1, 'Япония', 'Mitsubishy Motors');
insert into maker (maker_id, country, company)
values (2, 'Германия', 'German Super Auto');
insert into maker (maker_id, country, company)
values (3, 'США', 'BMW Group');
insert into maker (maker_id, country, company)
values (4, 'Россия', 'ВАЗ');
insert into maker (maker_id, country, company)
values (5, 'Китай', 'KIA Engine');

insert into model (model_id, model_name, color, number_of_seats, engine)
values (1, 'BMW 320d xDrive', 'black', 5, 'disel');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (2, 'BMW i4 xDrive', 'white', 5, 'electric');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (3, 'BMW XM', 'blue', 5, 'hybrid');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (4, 'KIA K5', 'gray', 5, 'petrol');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (5, 'KIA sorenta', 'dark green', 7, 'petrol');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (6, 'AUDI A6', 'silver gray', 5, 'disel');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (7, 'LADA Priora', 'black', 5, 'petrol');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (8, 'LADA Vesta', 'green', 5, 'petrol');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (9, 'Mitsubishy Lancer 9', 'dark blue', 5, 'petrol');
insert into model (model_id, model_name, color, number_of_seats, engine)
values (10, 'Toyota Camry 3.5', 'black', 5, 'petrol');

insert into price (model_id, price, date_from, date_to)
values (1, 3500000.0, '2019-12-04', '2020-05-11');
insert into price (model_id, price, date_from, date_to)
values (1, 5450000.0, '2020-05-12', null);
insert into price (model_id, price, date_from, date_to)
values (2, 5000000.0, '2021-06-03', '2022-12-10');
insert into price (model_id, price, date_from, date_to)
values (2, 7500000.0, '2022-12-11', null);
insert into price (model_id, price, date_from, date_to)
values (3, 16000000.0, '2022-12-16', null);
insert into price (model_id, price, date_from, date_to)
values (4, 2250000.0, '2020-02-13', '2022-03-15');
insert into price (model_id, price, date_from, date_to)
values (4, 3500000.0, '2022-03-16', null);
insert into price (model_id, price, date_from, date_to)
values (5, 3000000.0, '2020-02-14', '2022-03-16');
insert into price (model_id, price, date_from, date_to)
values (5, 5400000.0, '2022-03-17', null);
insert into price (model_id, price, date_from, date_to)
values (6, 5500000.0, '2021-05-24', null);
insert into price (model_id, price, date_from, date_to)
values (7, 230000.0, '2007-09-27', '2014-03-29');
insert into price (model_id, price, date_from, date_to)
values (7, 350000.0, '2014-03-30', '2019-11-15');
insert into price (model_id, price, date_from, date_to)
values (7, 590000.0, '2019-11-16', null);
insert into price (model_id, price, date_from, date_to)
values (8, 500000.0, '2015-06-17', '2019-04-21');
insert into price (model_id, price, date_from, date_to)
values (8, 900000.0, '2019-04-22', '2022-11-02');
insert into price (model_id, price, date_from, date_to)
values (8, 1400000.0, '2022-11-03', null);
insert into price (model_id, price, date_from, date_to)
values (9, 450000.0, '2010-01-23', '2018-08-24');
insert into price (model_id, price, date_from, date_to)
values (9, 600000.0, '2018-08-25', null);
insert into price (model_id, price, date_from, date_to)
values (10, 4500000.0, '2019-07-12', null);

insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (1, 'BMW', 3, 1);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (2, 'BMW', 3, 2);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (3, 'BMW', 3, 3);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (4, 'KIA', 5, 4);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (5, 'KIA', 5, 5);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (6, 'KIA', 5, 4);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (7, 'AUDI', 2, 6);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (8, 'LADA', 4, 7);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (9, 'LADA', 4, 7);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (10, 'MITSUBISHY', 1, 9);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (11, 'BMW', 3, 1);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (12, 'LADA', 4, 7);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (13, 'LADA', 4, 8);
insert into automobile (automobile_id, car_brand, maker_id, model_id)
values (14, 'TOYOTA', 1, 10);

insert into payment (pay_id, pay_method, pay_date, account_number, receipt_size)
values (1, 'перевод', '2019-04-21', '4290 9320 3248 8420', 600000.0);
insert into payment (pay_id, pay_method, pay_date, account_number, receipt_size)
values (2, 'перевод', '2020-04-02', '2345 5948 3829 3849', 900000.0);
insert into payment (pay_id, pay_method, pay_date, account_number, receipt_size)
values (3, 'перевод', '2022-05-12', '4234 9425 3268 7414', 5400000.0);
insert into payment (pay_id, pay_method, pay_date, account_number, receipt_size)
values (4, 'перевод', '2021-03-12', '4299 3938 3748 4738', 4500000.0);
insert into payment (pay_id, pay_method, pay_date, account_number, receipt_size)
values (5, 'наличные', '2008-11-20', '-', 230000.0);
insert into payment (pay_id, pay_method, pay_date, account_number, receipt_size)
values (6, 'перевод', '2023-01-29', '4328 2983 3285 5833', 5450000.0);

insert into service_info (service_id, seller_id, automobile_id, service_date, pay_id)
values (1, 7, 10, '2019-04-21', 1);
insert into service_info (service_id, seller_id, automobile_id, service_date, pay_id)
values (2, 5, 1, '2023-01-28', 6);
insert into service_info (service_id, seller_id, automobile_id, service_date, pay_id)
values (3, 4, 9, '2008-11-21', 5);
insert into service_info (service_id, seller_id, automobile_id, service_date, pay_id)
values (4, 7, 13, '2020-04-05', 2);
insert into service_info (service_id, seller_id, automobile_id, service_date, pay_id)
values (5, 3, 5, '2022-05-12', 3);
insert into service_info (service_id, seller_id, automobile_id, service_date, pay_id)
values (6, 2, 14, '2021-03-12', 4);

insert into service (customer_id, service_id, automobile_id)
values (10, 3, 9);
insert into service (customer_id, service_id, automobile_id)
values (4, 1, 10);
insert into service (customer_id, service_id, automobile_id)
values (3, 2, 1);
insert into service (customer_id, service_id, automobile_id)
values (10, 4, 13);
insert into service (customer_id, service_id, automobile_id)
values (7, 5, 5);
insert into service (customer_id, service_id, automobile_id)
values (8, 6, 14);
