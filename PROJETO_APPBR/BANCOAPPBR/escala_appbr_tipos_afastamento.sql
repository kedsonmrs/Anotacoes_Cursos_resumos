-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: escala_appbr
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tipos_afastamento`
--

DROP TABLE IF EXISTS `tipos_afastamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_afastamento` (
  `IDTIPO_AFASTAMENTO` int NOT NULL AUTO_INCREMENT,
  `NOME_AFASTAMENTO` varchar(15) NOT NULL,
  `DESCRICAO` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`IDTIPO_AFASTAMENTO`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_afastamento`
--

LOCK TABLES `tipos_afastamento` WRITE;
/*!40000 ALTER TABLE `tipos_afastamento` DISABLE KEYS */;
INSERT INTO `tipos_afastamento` VALUES (1,'-','Solicitação de Folga'),(2,'ACC','Serviço no ACC'),(3,'CUR','Curso'),(4,'CVM','Serviço Vigilância Manhã'),(5,'CVP','Serviço Vigilância Pernoite'),(6,'CVT','Serviço Vigilância Tarde'),(7,'DME','Dispensa Médica'),(8,'FER','Férias'),(9,'INS','Inspeção de Saúde'),(10,'LIM','Licença Maternidade'),(11,'LIP','Licença Paternidade'),(12,'LUT','Luto'),(13,'MIS','Missão'),(14,'NUP','Núpcias');
/*!40000 ALTER TABLE `tipos_afastamento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-11 13:15:59
