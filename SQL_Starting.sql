/*Drop functions*/
drop database if exists IsTech;
drop table if exists Major;
drop table if exists Student;

/*Remove fk commands*/
alter table Student
drop fk_Student;

SET DATEFORMAT DMY;

/*Create functions*/
create database IsTech;

create table Major(
	Class_ID varchar(6) not null,
	Class_Name varchar(50),
	No_of_Students int,
	constraint pk_Major primary key (Class_ID),
);

create table Student(
	Student_ID int identity(001,1),
	Student_Name varchar(50),
	Date_of_Birth date,
	Class_ID varchar(6),
	constraint pk_Student primary key (Student_ID)
);

/*Setting relationships*/
alter table Student
add constraint fk_Student foreign key (Class_ID) references Major (Class_ID)

/*Inserting data*/
insert into Major (Class_ID,Class_Name,No_of_Students)
values	
	('ISM','Math',45),
	('ISP','Programming',40),
	('ISPAS','Probability and Statistic',50),
	('ISH','History',45),
	('ISE','English',43);

insert into Student (Student_Name,Date_of_Birth,Class_ID)
values
	('James Walker','05/06/2016','ISM'),
	('Velma Clemons','05/06/2016','ISPAS'),
	('Kibo Underwood','05/06/2016','ISM'),
	('Louis Mcgee','05/06/2016','ISE'),
	('Phyllis Paul','05/06/2016','ISP'),
	('Zenaida Decker','05/06/2016','ISM'),
	('Gillian Tillman','05/06/2016','ISPAS'),
	('Constance Boone','05/06/2016','ISPAS'),
	('Giselle Lancaster','05/06/2016','ISE'),
	('Kirsten Mcdowell','05/06/2016','ISE'),
	('Solomon Ray','05/06/2016','ISP'),
	('John Marshall','05/06/2016','ISE'),
	('Merrill Carney','05/06/2016','ISP'),
	('Hakeem Gillespie','05/06/2016','ISE'),
	('Hayden Boyer','05/06/2016','ISP'),
	('Griffin Mcleod','05/06/2016','ISE'),
	('Allistair Patton','05/06/2016','ISM'),
	('Rina Slater','05/06/2016','ISPAS'),
	('Caldwell Skinner','05/06/2016','ISE'),
	('Portia Galloway','05/06/2016','ISPAS'),
	('Noelle Valentine','05/06/2016','ISP');

/*test*/
select * from Student
having COUNT(*) > 20;

/*Stored eliminated table*/
select * into Eliminated from Student
where Student_ID > 20;

select * from Eliminated

/*Delete information*/
delete from Student 
where Student_ID > 20;

/*update infor*/
update Student
set Date_of_Birth = '12-2-2005'
where Student_ID = 18;
		
/*rename column*/
EXEC sp_rename 'Student.Date_of_Birth', 'Rolling_Day', 'COLUMN';