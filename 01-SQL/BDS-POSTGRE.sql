/* show datastyle; - ve o padrao da DATA no SGBD */
/* Para mudar em caso de erro, ir ao arquivo de conf do postgre para alterar o padrao */
/* Apos reinicar em SERVICES, sempre que modificar algum arquivo interno do SGBD */

/* dataset - numero de linhas mostradas no resultado */
/* limitando o dataset */

select * from funcionarios
limit 10;

/* funçoes (sum, avg) com group by */

select
	departamento,
	sum(salario) as "Salario_total",
	avg(salario) as "Media_salarial"
from funcionarios
group by departamento;

select
	departamento,
	sum(salario)
from funcionarios
group by departamento;

/* MIN/MAX funciona com o group by, mostra o minimo e maximo de cada categoria */

select
	sexo,
	max(salario) as "maior salario",
	min(salario) as "menor salario"
from funcionarios
group by sexo;

/* DATA SCIENCE - moda, mediana, desv padrao, variancia */
/* modelagem para data science - colunar, nao se importa com crescimento vertical
 nao separa por conta de redundancia de dados - facilita consulta sem joins */
 
/* moda - maior repetiçao dos dados */
/* SELECT com group by com qtd e maquina */

SELECT maquina, qtd, count(*) as MODA
from maquinas
group by maquina, qtd
order by 3 DESC

SELECT MODE() WITHIN GROUP(ORDER BY('COLUNA')) AS 'MODA'
FROM 'TABELA'
ORDER BY MAQUINAS

/* mediana - valor do meio */

/* desv padrao - media de variaçao em relaçao a media geral (raiz da variancia) */
/* possui funçao no postgre */

STDDEV('COLUNA') as desv padrao

/* variancia - "distancia" da media, se eleva ao quadrado para evitar negativo
	se subtrai o valor da ocorrencia X da media geral, eleva ao quadrado, e divide
	no fim pelo numero de ocorrencias */

VAR_POP ('COLUNA') variancia

/*  coef variante - valor do desv padrao em PORCENTAGEM - desvpadrao/media *100 */

/* AMPLITUDE - distancia entre o maior e menor valor */

SELECT maquina, min(), max(), max()-min() as AMP
from maquinas
group by maquina
order by 4 desc;

/* MIN e MAX - servem para identificar outlier (valor descrepante) e melhorar o desvio padrao */

/* IMPORTANTO CSV PARA UMA TABELA */

COPY 'NOME TABELA'
FROM 'CAMINHO DO ARQUIVO'
DELIMITER 'O QUE SEPARA AS COLUNAS'
CSV HEADER 'POSSUI CABEÇALHO - CORTA A LINHA 1'

ROUND('COLUNA','Nº APOS VIRGURA')

/* CRIANDO UM RELATORIO COLUNAR DE UM BANCO RELACIONAL */
/* DEVE ALEM DE PONTEIRAR COLUNA IGUAL, USAR ALIAS */

CREATE TABLE RELATORIO AS
	SELECT L.IDLOCACAO, F.NOME AS FILME, G.NOME AS GENERO, L.DIAS AS DIAS, L.MIDIA AS MIDIA
	FROM GENERO G
	INNER JOIN FILME F
	ON G.IDGENERO = F.ID_GENERO
	INNER JOIN LOCACAO
	ON L.ID_FILME = F.IDFILME
;

/* PARA SABER SE AS TABELAS ESTAO SINCRONIZADAS ATRAVES DE !!QUANTOS!! */

SELECT MAX(IDLOCACAO) AS LOCACAO, (SELECT MAX(IDLOCACAO) FROM LOCACAO) AS LOCACAO
FROM REL_LOC;

/* SELECT PARA SABER !!QUAIS!! ESTAO FALTANDO DA TABELA ORIGINAL */

	SELECT L.IDLOCACAO, F.NOME AS FILME, G.NOME AS GENERO, L.DIAS AS DIAS, L.MIDIA AS MIDIA
	FROM GENERO G
	INNER JOIN FILME F
	ON G.IDGENERO = F.ID_GENERO
	INNER JOIN LOCACAO
	ON L.ID_FILME = F.IDFILME
	WHERE L.IDLOCACAO NOT IN(SELECT IDLOCACAO FROM REL_LOC);

/* AGORA PARA INSERIR NA TABELA DE RELATORIO OS VALORES FALTANTES */

INSERT INTO REL_LOC
	SELECT L.IDLOCACAO, F.NOME AS FILME, G.NOME AS GENERO, L.DIAS AS DIAS, L.MIDIA AS MIDIA
	FROM GENERO G
	INNER JOIN FILME F
	ON G.IDGENERO = F.ID_GENERO
	INNER JOIN LOCACAO
	ON L.ID_FILME = F.IDFILME
	WHERE L.IDLOCACAO NOT IN(SELECT IDLOCACAO FROM REL_LOC)
;

/* TRIGGER PARA AUTOMATIZAR - NO POSTGRE SE CRIA A FUNÇAO E APOS A TRIGGER */

CREATE OR REPLACE FUNCION ATT_REL()
RETURNS TRIGGER AS $$ /* ESPECIFICANDO QUE ESSA FX SERA EXECUTADA POR TRIGGER */
BEGIN
	
	INSERT INTO REL_LOC
		(SELECT L.IDLOCACAO, F.NOME AS FILME, G.NOME AS GENERO, L.DIAS AS DIAS, L.MIDIA AS MIDIA
		FROM GENERO G
		INNER JOIN FILME F
		ON G.IDGENERO = F.ID_GENERO
		INNER JOIN LOCACAO
		ON L.ID_FILME = F.IDFILME
		WHERE L.IDLOCACAO NOT IN(SELECT IDLOCACAO FROM REL_LOC));
	
	
	COPY REL_LOC TO
	'C:\Users\kedso\Downloads\RELATORIO.CSV'
	DELIMITER ','
	CSV HEADER

RETURN NEW;
END;
$$
LANGUAGE PLPGSQL;

CREATE TRIGGER ATT_REL
AFTER INSERT ON LOCACAO
FOR EACH ROW
	EXECUTE PROCEDURE ATT_REL();

/* TRIGGER PARA DELETAR AGORA O REGISTRO */

CREATE OR REPLACE FUNCTION DEL_LOC
RETURNS TRIGGER AS $$
BEGIN
	DELETE FROM REL_LOC
	WHERE IDLOCACAO = old.IDLOCACAO
	
	COPY REL_LOC TO
	'C:\Users\kedso\Downloads\RELATORIO.CSV'
	DELIMITER ','
	CSV HEADER

RETURN OLD;
END;
$$
LANGUAGE PLPSQL;

CREATE TRIGGER ATT_REL
AFTER DELETE ON LOCACAO
FOR EACH ROW
	EXECUTE PROCEDURE DEL_ATT_REL();

/* DELETANDO UMA TRIGGER */

DROP TRIGGER 'NOME' ON 'TABELA';

/* PARA EXPORTAR EM .CSV AGORA */

COPY 'TABELA' TO
'CAMINHO ONDE QUER SALVAR/NOME DO ARQUIVO.CSV'
DELIMITER 'OQ SEPARA AS COLUNAS'
CSV HEADER 'TEM CABEÇALHO'

/* SEQUENCY - VETOR que armazena os numeros de 1 ao infinito para ID */

CREATE SEQUENCY SEQ_LOCACAO;

/* PARA USAR A SEQUENCY SE COLOCA NEXTVAL NO LUGAR DA ID NO CONJ DE INSERTS */

INSERT INTO 'TABELA' VALUES (NEXTVAL('NOME DA SEQUENCY'), 'VALOR1', 'VALOR2')

/* USO DO CASE NO POSTGRE */

select 	nome,
		case
			when sexo = 'Masculino'
			then 'M'
			else 'F'
		end as sexo
from funcionarios;

/* colunas DUMMY - COLUNAS TRANFORMADAS EM BINARIOS PARA MACHINE LEARNING */
/* no DUMMY deve ser por cada VARIVEL, a coluna DUMMY */
/* em valores muito HETEROGENEOS, se utiliza CLASSES */

/* UTILIZANDO SELECT PARA RETORNAR VALOR BOOLEANO */

SELECT NOME, DEPARTAMENTO, (SEXO = 'Masculino') as Masculino
FROM FUNCIONARIOS;

/* AGORA O CASE PARA TRANSFORMAR EM 0 ou 1 */


SELECT 	NOME, DEPARTAMENTO, 
		CASE 
			WHEN (SEXO = 'Masculino') = true THEN 1
			ELSE 0
		END AS MASCULINO,
		CASE 
			WHEN (SEXO = 'Feminino') = true THEN 1
			ELSE 0
		END AS FEMININO
FROM FUNCIONARIOS;

/* HAVING - CLAUSULA DE FILTRO PARA UTILIZAR VALORES DE FUNÇOES AGREGADAS */
/* APOS O GROUP BY PARA NAO DAR ERRO */

SELECT DEPARTAMENTO, sum(salario) as "Total"
FROM FUNCIONARIOS
WHERE DEPARTAMENTO LIKE 'B%'
GROUP BY DEPARTAMENTO
HAVING SUM(SALARIO) > 40000;

/* FILTRANDO O COUNT */
/* 2 COLUNAS COM COUNT E FILTROS DIFERENTES */

SELECT 	COUNT(*) AS "FUNCIONARIOS",
		COUNT(*) FILTER(WHERE SEXO = 'Masculino')
FROM funcionarios;

/* DISCTINCT 'COLUNA'- traz todos os possiveis diferentes sem repetir */

select distinct departamento from funcionarios;

/* UPPER CASE - printa com todas as letras maiusculas*/

select upper('coluna string')

/* LOWER - printa com todas as letras minusculas */

select lower('coluna string')

/* CONCATENANDO - JUNTANDO 2 COLUNAS COM STRING */

select cargo || ' - ' || departamento
from funcionarios;

/* LENGTH (MOSTRA QUANTOS CARACTERES TEM) e TRIM (RETIRA ESPAÇOS) */

SELECT LENGTH('COLUNA')
SELECT TRIM('STRING')

SELECT 	NOME,
		CARGO,
		CASE WHEN (CARGO = '%Assistant%') = TRUE THEN 1
		ELSE 0
		END AS 'ASSITENTE?'
FROM funcionarios;


SELECT 	NOME,
		CARGO,
		(CARGO like '%Assistente%')
FROM funcionarios;