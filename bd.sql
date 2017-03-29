create database proyectoClase;

use proyectoClase;

create table catedratico(
	codigo int not null auto_increment,
    usuario varchar(50) unique not null,
    nombre varchar(100) not null,
    contrasenia varchar(50),
    constraint codigo primary key (codigo)
);
