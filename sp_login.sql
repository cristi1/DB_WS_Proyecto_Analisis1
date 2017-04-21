CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_login`(
in pUsuario varchar(50),
in pContrasenia varchar(50))
BEGIN
select nombre,usuario from catedratico where usuario = pUsuario and contrasenia = pContrasenia;
END