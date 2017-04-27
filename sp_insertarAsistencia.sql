CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertarAsistencia`(
in pIdAlumno varchar(10),
in pCodigoAsistencia varchar(5))
BEGIN
declare vFechaActual date;
select @vFechaActual := curdate();
insert into asistencia (id_alumno,fecha,codigo_asistencia) values (pIdAlumno,@vFechaActual,pCodigoAsistencia);
END