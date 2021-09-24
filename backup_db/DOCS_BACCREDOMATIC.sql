-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: tococo_db
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Dumping data for table `toc_categoria`
--

LOCK TABLES `toc_categoria` WRITE;
/*!40000 ALTER TABLE `toc_categoria` DISABLE KEYS */;
INSERT INTO `toc_categoria` VALUES (1,'Arroz'),(2,'Papas'),(3,'Tacos'),(4,'Pollo'),(5,'Hamburguesas'),(6,'Nachos'),(7,'Carnes'),(8,'Combos');
/*!40000 ALTER TABLE `toc_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `toc_producto`
--

LOCK TABLES `toc_producto` WRITE;
/*!40000 ALTER TABLE `toc_producto` DISABLE KEYS */;
INSERT INTO `toc_producto` VALUES (1,'Cantonés Grande',2800,1),(2,'Cantonés Pequeño',2000,1),(3,'Camarón Grande',3800,1),(4,'Camarón Pequeño',3000,1),(5,'Papas supremas',3000,2),(6,'Salchipapas',2300,2),(7,'Patatas',2200,2),(8,'Papas Grandes',2000,2),(9,'Papas pequeñas',1400,2),(10,'1 Taco',1000,3),(11,'2 Tacos',1500,3),(12,'Supertaco',2000,3),(13,'Porción Sencilla',1500,4),(14,'Porción + Papas',2000,4),(15,'Pieza de pollo + Papas',1000,4),(16,'8 Piezas + Refresco',2000,4),(17,'Hamburguesa con Papas',1900,5),(18,'Hamburguesa Sencilla',1400,5),(19,'Tacoburger',3000,5),(20,'Nachos con Carne',3000,6),(21,'Nachos con Pollo',3000,6),(22,'Chalupa',3000,6),(23,'Carne mechada normal',2500,7),(24,'Carne mechada mexicana',2500,7),(25,'Quesadilla + Papas',2500,8),(26,'Burritos + Papas',2500,8),(27,'Nuggets de pollo',2500,8),(28,'Nuggets de pescado',2500,8),(29,'Filet de pollo',2500,8),(30,'Filet de pescado',2500,8);
/*!40000 ALTER TABLE `toc_producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-23 19:12:55
