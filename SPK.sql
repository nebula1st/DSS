/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 10.1.32-MariaDB : Database - spkkaryawanterbaik
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`karyawanterbaik` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `spkkaryawanterbaik`;

/*Table structure for table `karyawan` */

DROP TABLE IF EXISTS `karyawan`;

CREATE TABLE `karyawan` (
  `IDKaryawan` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `Nama` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Divisi` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Jns_Kelamin` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Tgl_Lahir` date DEFAULT NULL,
  `Alamat` text COLLATE utf8_unicode_ci,
  `No_Telpon` varchar(13) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`IDKaryawan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Table structure for table `kriteria` */

DROP TABLE IF EXISTS `kriteria`;

CREATE TABLE `kriteria` (
  `kode_krit` char(5) COLLATE utf8_unicode_ci NOT NULL,
  `nama_krit` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bobot_krit` double(5,2) DEFAULT NULL,
  `keterangan_krit` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`kode_krit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Table structure for table `penilaiankaryawan` */

DROP TABLE IF EXISTS `penilaiankaryawan`;

CREATE TABLE `penilaiankaryawan` (
  `IDKaryawan_nilai` char(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Tanggal` date DEFAULT NULL,
  `kode_sub_nilai` char(6) COLLATE utf8_unicode_ci DEFAULT NULL,
  `kode_krit_nilai` char(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nilai` double(5,2) DEFAULT NULL,
  KEY `IDKaryawan_nilai` (`IDKaryawan_nilai`),
  KEY `kode_sub_nilai` (`kode_sub_nilai`),
  KEY `kode_krit_nilai` (`kode_krit_nilai`),
  CONSTRAINT `penilaiankaryawan_ibfk_1` FOREIGN KEY (`IDKaryawan_nilai`) REFERENCES `karyawan` (`IDKaryawan`),
  CONSTRAINT `penilaiankaryawan_ibfk_2` FOREIGN KEY (`kode_sub_nilai`) REFERENCES `subkriteria` (`kode_sub`),
  CONSTRAINT `penilaiankaryawan_ibfk_3` FOREIGN KEY (`kode_krit_nilai`) REFERENCES `kriteria` (`kode_krit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Table structure for table `subkriteria` */

DROP TABLE IF EXISTS `subkriteria`;

CREATE TABLE `subkriteria` (
  `kode_sub` char(6) COLLATE utf8_unicode_ci NOT NULL,
  `kode_krit_fk` char(5) COLLATE utf8_unicode_ci NOT NULL,
  `nama_sub` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bobot_sub` double(5,2) DEFAULT NULL,
  `keterangan_sub` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`kode_sub`),
  KEY `kode_krit_fk` (`kode_krit_fk`),
  CONSTRAINT `subkriteria_ibfk_1` FOREIGN KEY (`kode_krit_fk`) REFERENCES `kriteria` (`kode_krit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Table structure for table `shownilai` */

DROP TABLE IF EXISTS `shownilai`;

/*!50001 DROP VIEW IF EXISTS `shownilai` */;
/*!50001 DROP TABLE IF EXISTS `shownilai` */;

/*!50001 CREATE TABLE  `shownilai`(
 `IDKaryawan_nilai` char(10) ,
 `Nama` varchar(50) ,
 `Tanggal` date ,
 `nama_krit` varchar(10) ,
 `nama_sub` varchar(20) ,
 `nilai` double(5,2) 
)*/;

/*Table structure for table `showsaw` */

DROP TABLE IF EXISTS `showsaw`;

/*!50001 DROP VIEW IF EXISTS `showsaw` */;
/*!50001 DROP TABLE IF EXISTS `showsaw` */;

/*!50001 CREATE TABLE  `showsaw`(
 `IDKaryawan_nilai` char(10) ,
 `kode_krit_nilai` char(5) ,
 `kode_sub_nilai` char(6) ,
 `bobot_sub` double(5,2) ,
 `nilai` double(5,2) ,
 `tanggal` date 
)*/;

/*Table structure for table `subkriteriaview` */

DROP TABLE IF EXISTS `subkriteriaview`;

/*!50001 DROP VIEW IF EXISTS `subkriteriaview` */;
/*!50001 DROP TABLE IF EXISTS `subkriteriaview` */;

/*!50001 CREATE TABLE  `subkriteriaview`(
 `kode_sub` char(6) ,
 `nama_sub` varchar(20) ,
 `nama_krit` varchar(10) ,
 `bobot_sub` double(5,2) ,
 `keterangan_sub` text 
)*/;

/*View structure for view shownilai */

/*!50001 DROP TABLE IF EXISTS `shownilai` */;
/*!50001 DROP VIEW IF EXISTS `shownilai` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `shownilai` AS (select `a`.`IDKaryawan_nilai` AS `IDKaryawan_nilai`,`z`.`Nama` AS `Nama`,`a`.`Tanggal` AS `Tanggal`,`x`.`nama_krit` AS `nama_krit`,`c`.`nama_sub` AS `nama_sub`,`a`.`nilai` AS `nilai` from (((`penilaiankaryawan` `a` left join `karyawan` `z` on((`a`.`IDKaryawan_nilai` = `z`.`IDKaryawan`))) left join `kriteria` `x` on((`a`.`kode_krit_nilai` = `x`.`kode_krit`))) left join `subkriteria` `c` on((`a`.`kode_sub_nilai` = `c`.`kode_sub`)))) */;

/*View structure for view showsaw */

/*!50001 DROP TABLE IF EXISTS `showsaw` */;
/*!50001 DROP VIEW IF EXISTS `showsaw` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `showsaw` AS (select `penilaiankaryawan`.`IDKaryawan_nilai` AS `IDKaryawan_nilai`,`penilaiankaryawan`.`kode_krit_nilai` AS `kode_krit_nilai`,`penilaiankaryawan`.`kode_sub_nilai` AS `kode_sub_nilai`,`subkriteria`.`bobot_sub` AS `bobot_sub`,`penilaiankaryawan`.`nilai` AS `nilai`,`penilaiankaryawan`.`Tanggal` AS `tanggal` from (`penilaiankaryawan` left join `subkriteria` on((`penilaiankaryawan`.`kode_sub_nilai` = `subkriteria`.`kode_sub`))) order by `penilaiankaryawan`.`IDKaryawan_nilai`,`penilaiankaryawan`.`kode_krit_nilai`,`penilaiankaryawan`.`kode_sub_nilai`) */;

/*View structure for view subkriteriaview */

/*!50001 DROP TABLE IF EXISTS `subkriteriaview` */;
/*!50001 DROP VIEW IF EXISTS `subkriteriaview` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `subkriteriaview` AS (select `subkriteria`.`kode_sub` AS `kode_sub`,`subkriteria`.`nama_sub` AS `nama_sub`,`kriteria`.`nama_krit` AS `nama_krit`,`subkriteria`.`bobot_sub` AS `bobot_sub`,`subkriteria`.`keterangan_sub` AS `keterangan_sub` from (`subkriteria` left join `kriteria` on((`subkriteria`.`kode_krit_fk` = `kriteria`.`kode_krit`)))) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
