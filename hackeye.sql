-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: hackeye
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admininfo`
--

DROP TABLE IF EXISTS `admininfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admininfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admininfo`
--

LOCK TABLES `admininfo` WRITE;
/*!40000 ALTER TABLE `admininfo` DISABLE KEYS */;
INSERT INTO `admininfo` VALUES (1,'hackeye','$2y$10$Qp3FPSRC6mJcXTYAelrkQ.n52L1w9xUQVn06GgVJFBMkaORi.uFSO');
/*!40000 ALTER TABLE `admininfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alert`
--

DROP TABLE IF EXISTS `alert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alert` (
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `msg` varchar(20) DEFAULT NULL,
  `receiver` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alert`
--

LOCK TABLES `alert` WRITE;
/*!40000 ALTER TABLE `alert` DISABLE KEYS */;
INSERT INTO `alert` VALUES ('2023-09-13','12:30:23','Security Alert','Manoj'),('2023-04-28','13:45:01','Fire Alarm','Shri Hari'),('2024-01-12','09:15:59','Intruder Detected','Vignesh'),('2023-10-12','10:31:33','Unauthorized Access','Manoj'),('2023-11-08','14:23:03','Emergency Evacuation','Shri Hari'),('2023-12-03','19:20:44','Security Breach','Vignesh'),('2024-01-02','09:35:53','Fire Drill Reminder','Manoj'),('2024-02-15','13:34:09','Suspicious Activity','Shri Hari'),('2024-03-21','16:00:00','Security Update','Vignesh'),('2024-04-17','20:15:43','Emergency Drill','Manoj'),('2024-05-10','11:32:56','Fire Alarm Test','Shri Hari'),('2024-06-25','18:41:30','Access Point Failure','Vignesh'),('2024-07-18','07:34:08','Security Alert','Manoj'),('2024-08-12','14:47:56','Unauthorized Entry','Shri Hari'),('2024-09-05','09:31:55','System Update','Vignesh'),('2024-10-20','16:23:44','Intrusion Detected','Manoj'),('2024-11-14','12:22:12','Fire Drill','Shri Hari'),('2024-12-09','18:34:02','Emergency Test','Vignesh'),('2024-12-25','10:15:01','Security Advisory','Manoj'),('2023-07-01','14:43:40','Access Alert','Shri Hari'),('2023-08-10','11:22:55','Fire System Test','Vignesh'),('2023-09-20','17:11:33','Security Breach','Manoj'),('2023-10-05','09:32:00','Emergency Test','Shri Hari'),('2023-11-15','13:20:45','Unauthorized Attempt','Vignesh'),('2023-12-30','20:00:33','Security Update','Manoj'),('2024-01-15','08:41:30','Fire Alarm Test','Shri Hari'),('2024-02-28','16:32:40','Intruder Alert','Vignesh'),('2024-03-10','12:11:40','Security Advisory','Manoj'),('2024-04-22','18:00:34','Unauthorized Entry','Shri Hari');
/*!40000 ALTER TABLE `alert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crime`
--

DROP TABLE IF EXISTS `crime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crime` (
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `camera_no` int DEFAULT NULL,
  `camera_name` varchar(20) DEFAULT NULL,
  `camera_loc` varchar(20) DEFAULT NULL,
  `type_of_crime` varchar(20) DEFAULT NULL,
  `detection_count` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crime`
--

LOCK TABLES `crime` WRITE;
/*!40000 ALTER TABLE `crime` DISABLE KEYS */;
INSERT INTO `crime` VALUES ('2023-09-13','12:30:23',1,'Camera1','Hallway','Blood',2),('2023-04-28','13:45:01',2,'Camera2','Cafeteria','Violence',1),('2024-01-12','09:15:59',3,'Camera3','Prison Junction','Fire/Smoke',3),('2023-11-14','14:00:37',1,'Camera1','Hallway','Blood',1),('2023-08-12','16:30:12',2,'Camera2','Cafeteria','Violence',2),('2024-09-19','20:45:05',3,'Camera3','Prison Junction','Blood',1),('2024-01-16','11:00:19',1,'Camera1','Hallway','Violence',2),('2023-09-29','18:15:00',2,'Camera2','Cafeteria','Fire/Smoke',1),('2023-08-16','07:45:33',3,'Camera3','Prison Junction','Blood',3),('2024-01-17','14:32:01',1,'Camera1','Hallway','Violence',1),('2024-01-21','09:23:04',1,'Camera2','Cafeteria','Blood',2),('2024-01-03','16:47:56',3,'Camera3','Prison Junction','Violence',1),('2024-01-17','12:03:30',1,'Camera1','Hallway','Fire/Smoke',3),('2023-01-19','17:36:12',2,'Camera2','Cafeteria','Blood',1),('2023-01-29','14:41:20',3,'Camera3','Prison Junction','Violence',2),('2023-03-20','19:34:58',1,'Camera1','Hallway','Blood',1),('2024-10-25','10:38:43',2,'Camera2','Cafeteria','Violence',2),('2023-05-21','21:13:51',3,'Camera3','Prison Junction','Fire/Smoke',1),('2024-08-15','08:46:23',1,'Camera1','Hallway','Blood',3),('2023-12-22','15:12:09',2,'Camera2','Cafeteria','Violence',1),('2024-03-23','11:22:22',3,'Camera3','Prison Junction','Blood',2),('2024-12-05','17:25:44',1,'Camera1','Hallway','Fire/Smoke',1),('2024-05-19','09:27:08',2,'Camera2','Cafeteria','Violence',2),('2024-09-27','14:15:34',3,'Camera3','Prison Junction','Armoury',1),('2024-12-03','18:45:56',1,'Camera1','Hallway','Blood',3),('2024-10-06','22:09:34',2,'Camera2','Cafeteria','Fire/Smoke',2),('2024-06-21','03:30:00',3,'Camera3','Prison Junction','Violence',1),('2024-03-18','13:19:56',1,'Camera1','Hallway','Armoury',2),('2023-02-23','07:42:03',2,'Camera2','Cafeteria','Blood',1),('2023-04-04','16:05:23',3,'Camera3','Prison Junction','Fire/Smoke',3);
/*!40000 ALTER TABLE `crime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `face`
--

DROP TABLE IF EXISTS `face`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `face` (
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `cam_no` int DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `loc` varchar(30) DEFAULT NULL,
  `face` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `face`
--

LOCK TABLES `face` WRITE;
/*!40000 ALTER TABLE `face` DISABLE KEYS */;
INSERT INTO `face` VALUES ('2023-07-15','08:30:45',1,NULL,'Entrance','Person1'),('2023-08-20','12:15:20',2,NULL,'Lobby','Person2'),('2023-09-05','17:45:35',3,NULL,'Hallway','Person3'),('2023-10-12','10:30:10',1,NULL,'Staircase','Person4'),('2024-11-08','14:20:50',2,NULL,'Cafeteria','Person5'),('2023-12-03','19:00:15',3,NULL,'Office','Person3'),('2024-01-02','09:45:30',1,NULL,'Meeting Room','Person4'),('2024-02-15','13:30:40',2,NULL,'Corridor','Person3'),('2024-03-21','16:00:25',3,NULL,'Reception','Person1'),('2024-04-17','20:15:55',1,NULL,'Break Room','Person2'),('2024-05-10','11:30:05',2,NULL,'Restroom','Person1'),('2024-06-25','18:45:50',3,NULL,'Outdoor','Person2'),('2024-07-18','07:00:30',1,NULL,'Elevator','Person3'),('2024-08-12','14:40:18',2,NULL,'Hallway','Person4'),('2024-09-05','09:30:22',3,NULL,'Lobby','Person5'),('2024-10-20','16:20:38',1,NULL,'Office','Person1'),('2024-11-14','12:00:12',2,NULL,'Cafeteria','Person3'),('2024-12-09','18:30:48',3,NULL,'Meeting Room','Person5'),('2024-12-25','10:15:10',1,NULL,'Staircase','Person4'),('2023-07-01','14:45:28',2,NULL,'Break Room','Person2'),('2023-08-10','11:00:42',3,NULL,'Reception','Person1'),('2023-09-20','17:15:07',1,NULL,'Lobby','Person2'),('2023-10-05','09:30:55',2,NULL,'Outdoor','Person3'),('2023-11-15','13:20:33',3,NULL,'Elevator','Person2'),('2023-12-30','20:00:20',1,NULL,'Restroom','Person5'),('2024-01-15','08:45:14',2,NULL,'Corridor','Person1'),('2024-02-28','16:30:22',3,NULL,'Hallway','Person3'),('2024-03-10','12:10:48',1,NULL,'Office','Person2'),('2024-04-22','18:00:30',2,NULL,'Meeting Room','Person2'),('2024-05-01','09:30:10',3,NULL,'Break Room','Person3');
/*!40000 ALTER TABLE `face` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `officerinfo`
--

DROP TABLE IF EXISTS `officerinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `officerinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `officerinfo`
--

LOCK TABLES `officerinfo` WRITE;
/*!40000 ALTER TABLE `officerinfo` DISABLE KEYS */;
INSERT INTO `officerinfo` VALUES (1,'ram','$2y$10$HJDP9mvMuR6oqOVvkYYCJOsIPdL5pO7/8Mo16UkfbjjKOLTEbdoAG'),(2,'hari','$2y$10$sgZB8Kxn0AGdSchIa7qqWu4SjCGUMyOPfBQgcYaf1jP88.JtKdB9W'),(3,'manoj','$2y$10$.ACq9vQ3oB2BhiOgaNL.8u6fwYHm4VFrEw.bRNvJL5J5VYNicge/2');
/*!40000 ALTER TABLE `officerinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-14 17:00:41
