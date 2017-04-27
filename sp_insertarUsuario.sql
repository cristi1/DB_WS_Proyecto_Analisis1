CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertarUsuario`(
in pNombre varchar(100),
in pUsuario varchar(50),
in pContrasenia varchar(50),
in pCorreo varchar(50)
)
BEGIN
insert into catedratico (nombre, usuario, contrasenia,correo) values (pNombre, pUsuario, pContrasenia,pCorreo);
END