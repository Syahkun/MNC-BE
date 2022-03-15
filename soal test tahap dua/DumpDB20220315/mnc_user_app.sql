-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mnc
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `user_app`
--

DROP TABLE IF EXISTS `user_app`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_app` (
  `user_id` varchar(255) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `pin` varchar(255) NOT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `saldo` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_app`
--

LOCK TABLES `user_app` WRITE;
/*!40000 ALTER TABLE `user_app` DISABLE KEYS */;
INSERT INTO `user_app` VALUES ('3ace97c4-a409-11ec-a99c-a0510bfeea51','Asa','Sarini','0811255506','Jl. Kebon Sirih No. 1','64fe2e47d7d5a7b3c15a0967126751013d634516d0334031381427bf0afe82a61f10f412a5f160998a8e196dc5b197ec7bba9f6b953e4ed3d0924e9c82f10df9','5ad017cfa0ac41d19db284c4e3c945f6',0,'2022-03-15 09:40:08',NULL),('834a4a3f-a404-11ec-9458-a0510bfeea51','Yaqqaa','Saqqaa','0811255504','Jl. Keboan Aqsam No. 1','531fd10662b362c89517284bd91819411a937e879b12776c902b386a831a7d14c6c9e0141e38670bbbce6d5cbe90e38b91dc1d05db00cec69c374b949ec383b8','b0566c7cf00a459da8669e7827a87023',6500000,'2022-03-15 09:06:23','2022-03-15 09:49:43'),('98df5443-a404-11ec-8788-a0510bfeea51','Asa','Sarin','0811255505','Jl. Kebon Sirih No. 1','c2c181403d7c69fe00a6719727924fc4d46847385b22c2b2894dd24deaa3918bec37a6f5349426031e0c225378f79fc165a75ad74fc0cf13c9d747c2d99ebf11','67928648c3ce434982f48b0eb11df91c',4000000,'2022-03-15 09:06:59','2022-03-15 09:37:17'),('a2c89880-a409-11ec-9420-a0510bfeea51','Asssa','Sariaani','0811255507','Jl. Kebon Sirih No. 1','c7379f3f27eb72ef00443cec9f2df9a8b30a62acd979957433b55bb7e668e58732756df58dc213f832e28c072b4506e0a4d3df4c2f34437adba495e43dc767e9','edb8af3ff222442fafc06a4ab8a9c0a0',0,'2022-03-15 09:43:03',NULL);
/*!40000 ALTER TABLE `user_app` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-15 11:01:52