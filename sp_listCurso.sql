CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_listCurso`(
in pcodigo int)
BEGIN
select * from curso where codigo_professor = pcodigo;
END