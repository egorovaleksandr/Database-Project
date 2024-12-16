-- create database mipt_project;

drop table if exists customer;
drop table if exists seller;
drop table if exists payment;
drop table if exists maker;
drop table if exists model;
drop table if exists price;
drop table if exists automobile;
drop table if exists service_info;
drop table if exists service;

create schema if not exists dealership;
set search_path to dealership, public;



create table if not exists customer
(
	customer_id integer not null primary key,
	full_name varchar(100) not null,
	phone_number varchar(12) not null
);

create table if not exists seller
(
	seller_id integer not null primary key,
	full_name varchar(100) not null,
	phone_number varchar(12) not null
);

create table if not exists payment
(
	pay_id smallint not null primary key,
	pay_method varchar(30) not null,
	pay_date date not null,
	account_number varchar(35) not null,
	receipt_size float check(receipt_size >= 0)
);

create table if not exists maker
(
	maker_id smallint not null primary key,
	company varchar(100) not null unique,
	country varchar(100) not null
);

create table if not exists model
(
	model_id integer not null primary key,
	model_name varchar(50) not null,
	color varchar(50) not null,
	number_of_seats smallint check(number_of_seats > 0 and number_of_seats < 10),
	engine varchar(50) not null
);

create table if not exists price
(
	model_id integer not null,
	price float not null check(price > 0),
	date_from date not null,
	date_to date,
	foreign key (model_id) references model(model_id),
	primary key (model_id, date_from)
);

create table if not exists automobile
(
	automobile_id integer not null primary key,
	car_brand varchar(20) not null,
	maker_id smallint not null,
	foreign key (maker_id) references maker(maker_id),
	model_id integer not null,
	foreign key (model_id) references model(model_id)
);

create table if not exists service_info
(
	service_id smallint primary key not null,
	seller_id integer not null,
	foreign key (seller_id) references seller(seller_id),
	automobile_id smallint not null,
	foreign key (automobile_id) references automobile(automobile_id),
	service_date date not null,
	pay_id smallint not null,
	foreign key (pay_id) references payment(pay_id)
);

create table if not exists service
(
	customer_id integer not null,
	foreign key (customer_id) references customer(customer_id),
	service_id smallint not null,
	foreign key (service_id) references service_info(service_id),
	automobile_id smallint not null,
	foreign key (automobile_id) references automobile(automobile_id)
);
