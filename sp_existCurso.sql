CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_existCurso`(
in pCurso varchar(100))
BEGIN
select codigo from curso where nombre = pCurso;
END