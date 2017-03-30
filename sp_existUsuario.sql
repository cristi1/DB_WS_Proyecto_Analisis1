CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_existUsuario`(
in pUsuario varchar(50))
BEGIN
select usuario from catedratico where usuario = pUsuario;
END