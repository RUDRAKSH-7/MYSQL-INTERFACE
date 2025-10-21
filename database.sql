create database SHOWROOM;
use SHOWROOM;

create table CARS (Car_No int primary key NOT NULL,
 CarName varchar(60) NOT NULL, 
 LaunchDate DATE NOT NULL,
 Model varchar(10) NOT NULL);
 
create table SALES (Car_No int primary key NOT NULL, 
 Price_Lakhs float DEFAULT 0.00,
 Available_Units int DEFAULT 0,
 Total_Sold int DEFAULT 0);

create table Buyers (Cust_No int, Cust_Name varchar(20),
 Purchase_Date date NOT NULL,
 Mobile_No varchar(10),
 Car_No int primary key NOT NULL,
 Model varchar(10) NOT NULL);