CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertarCurso`(
in pNombre varchar(100))
BEGIN
insert into curso (nombre) values (pNombre);
END