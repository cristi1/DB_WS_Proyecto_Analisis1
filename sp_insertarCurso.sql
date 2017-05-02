CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertarCurso`(
in pNombre varchar(100),
in pCodigoAsistencia varchar(5))
BEGIN
insert into curso (nombre) values (pNombre);
END