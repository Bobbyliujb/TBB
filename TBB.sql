use tbb;

set foreign_key_checks = 0;
drop table if exists users;
drop table if exists user_to_user;
drop table if exists items;
drop table if exists type;
drop table if exists item_to_type;
drop table if exists item_from_user;
drop table if exists item_for_user;
drop table if exists user_to_type;

-- table for user message
create table users(
	username varchar(20) not null, 
	nickname varchar(20) not null,
	password varchar(20) not null, 
	headurl varchar(50) not null, 
	college varchar(50) default "", 
	qq varchar(20) default "",
	grade varchar(10) default "", 
	-- class varchar(10) default null, 
	phone varchar(20) default "",
	constraint username primary key (username) 
)character set = utf8;

-- table for user relationship (many to many)
create table user_to_user(
	user1 varchar(20) not null,
	user2 varchar(20) not null,
	constraint user1 foreign key (user1) references users(username), 
	constraint user2 foreign key (user2) references users(username), 
	constraint user_pair primary key (user1, user2)
)character set = utf8;

-- table for item message
create table items(
	item_id int not null auto_increment,
	item_name varchar(20) not null,
	item_text varchar(100) not null,
	item_time varchar(20) not null, 
	item_price varchar(20) not null,
	imageurl varchar(50) default "", 
	buy_flag boolean default false,
	constraint item_id primary key (item_id)
)auto_increment = 1, character set = utf8;

-- table for item type 
create table type(
	typename varchar(20) not null,
	typetext varchar(100) default "", 
	constraint typename primary key (typename)
)character set = utf8;

-- table for relationship between items and types (many to one)
create table item_to_type(
	item_id int(10) not null,
	typename varchar(20) not null,
	constraint item_in_item_to_type foreign key (item_id) references items(item_id),
	constraint typename_in_item_to_type foreign key (typename) references type(typename),
	constraint item_and_type primary key (item_id)
)character set = utf8;

-- table for relationship between items and sellers (many to one)
create table item_from_user(
	item_id int(10) not null,
	username varchar(20) not null,	
	constraint item_in_item_from_user foreign key (item_id) references items(item_id),
	constraint username_in_item_from_user foreign key (username) references users(username),
	constraint item_and_user primary key (item_id)
)character set = utf8;

-- table for relationship between items and buyers (many to one)
create table item_for_user(
	item_id int(10) not null,
	username varchar(20) not null,	
	constraint item_in_item_for_user foreign key (item_id) references items(item_id),
	constraint username_in_item_for_user foreign key (username) references users(username),
	constraint item_and_user primary key (item_id)
)character set = utf8;

-- table for relationship between item and type (many to one)
create table user_to_type(
	username varchar(20) not null, 
	typename varchar(20) not null, 
	constraint username_in_user_to_type foreign key (username) references users(username), 
	constraint typename_in_user_to_type foreign key (typename) references type(typename),
	constraint user_and_type primary key (username, typename)
)character set = utf8;