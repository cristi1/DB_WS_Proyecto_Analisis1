create database proyectoClase;
use proyectoClase;

create table catedratico(
	codigo int not null auto_increment,
    usuario varchar(50) unique not null,
    nombre varchar(100) not null,
    contrasenia varchar(50),
    constraint codigo primary key (codigo)
);

create table curso(
	codigo int not null auto_increment,
    nombre varchar(100) not null,
    codigo_professor int not null, 
    constraint codigo primary key (codigo)
);

create table asistencia (
	numero int not null auto_increment,
	nombre_curso varchar(100) not null,
	id_alumno varchar(10) not null,
    fecha date not null,
    codigo_asistencia varchar(5) not null,
    constraint numero primary key (numero)
);

--alter table catedratico_curso add fecha date not null;
alter table curso add codigo_asistencia varchar(5) not null;