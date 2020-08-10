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
CREATE DATABASE /*!32312 IF NOT EXISTS*/`spkkaryawanterbaik` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `spkkaryawanterbaik`;

/*Table structure for table `karyawan` */

DROP TABLE IF EXISTS `karyawan`;

CREATE TABLE `karyawan` (
  `IDKaryawan` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `Nama` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Divisi` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Jns_Kelamin` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Tgl_Lahir` date DEFAULT NULL,
  `Alamat` text COLLATE utf8_unicode_ci,
  `No_Telpon` varchar(13) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`IDKaryawan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `karyawan` */

insert  into `karyawan`(`IDKaryawan`,`Nama`,`Divisi`,`Jns_Kelamin`,`Tgl_Lahir`,`Alamat`,`No_Telpon`) values 
('0000000001','Rendy','hr','L','0000-00-00','Tangerang','085681209312\r'),
('0000000002','Abdullah','hr','L','0000-00-00','Jakarta','089613643661\r'),
('0000000003','Rizal','it','L','0000-00-00','','\r'),
('0000000004','Lia','it','P','0000-00-00','','\r'),
('0000000005','Rizqa','it','L','0000-00-00','','\r'),
('0000000006','Daniel','it','L','0000-00-00','','\r'),
('0000000007','Angga','','L','0000-00-00','','\r'),
('0000000008','Pras','','L','0000-00-00','','\r'),
('0000000009','Bisma','','L','0000-00-00','','\r'),
('0000000010','Rizki','','L','0000-00-00','','\r'),
('0000000011','Reza','','L','0000-00-00','','\r'),
('0000000012','Gilang','','L','0000-00-00','','\r'),
('0000000013','Mahsa','','P','0000-00-00','','\r'),
('0000000014','Ita','','P','0000-00-00','','\r'),
('0000000015','Fajar','','L','0000-00-00','','\r'),
('0000000016','Rezza','','L','0000-00-00','','\r'),
('0000000017','Intan','','P','0000-00-00','','\r'),
('0000000018','Eve','','P','0000-00-00','','\r'),
('0000000019','Andri','','L','0000-00-00','','\r'),
('0000000020','Daus','','L','0000-00-00','','\r');

/*Table structure for table `kriteria` */

DROP TABLE IF EXISTS `kriteria`;

CREATE TABLE `kriteria` (
  `kode_krit` char(5) COLLATE utf8_unicode_ci NOT NULL,
  `nama_krit` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bobot_krit` double(5,2) DEFAULT NULL,
  `keterangan_krit` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`kode_krit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `kriteria` */

insert  into `kriteria`(`kode_krit`,`nama_krit`,`bobot_krit`,`keterangan_krit`) values 
('A0001','Disiplin',0.30,'kedisiplinan karyawan'),
('A0002','Profession',0.30,'Profesionalitas karyawan'),
('A0003','Personalit',0.20,'Sikap Karyawan'),
('A0004','Psikotes',0.10,'Nilai Psikotes Karyawan'),
('A0005','Lama',0.10,'aasdasd');

/*Table structure for table `penilaiankaryawan` */

DROP TABLE IF EXISTS `penilaiankaryawan`;

CREATE TABLE `penilaiankaryawan` (
  `IDKaryawan_nilai` char(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Tanggal` date DEFAULT NULL,
  `kode_sub_nilai` char(6) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nilai` double(5,2) DEFAULT NULL,
  KEY `IDKaryawan_nilai` (`IDKaryawan_nilai`),
  KEY `kode_sub_nilai` (`kode_sub_nilai`),
  CONSTRAINT `penilaiankaryawan_ibfk_1` FOREIGN KEY (`IDKaryawan_nilai`) REFERENCES `karyawan` (`IDKaryawan`),
  CONSTRAINT `penilaiankaryawan_ibfk_2` FOREIGN KEY (`kode_sub_nilai`) REFERENCES `subkriteria` (`kode_sub`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `penilaiankaryawan` */

insert  into `penilaiankaryawan`(`IDKaryawan_nilai`,`Tanggal`,`kode_sub_nilai`,`nilai`) values 
('0000000001','2020-07-29','AA0001',90.00),
('0000000002','2020-07-29','AA0001',62.00),
('0000000003','2020-07-29','AA0001',96.00),
('0000000004','2020-07-29','AA0001',71.00),
('0000000005','2020-07-29','AA0001',97.00),
('0000000001','2020-07-29','AA0002',97.00),
('0000000002','2020-07-29','AA0002',73.00),
('0000000003','2020-07-29','AA0002',75.00),
('0000000004','2020-07-29','AA0002',64.00),
('0000000005','2020-07-29','AA0002',64.00),
('0000000001','2020-07-29','AA0003',76.00),
('0000000002','2020-07-29','AA0003',87.00),
('0000000003','2020-07-29','AA0003',98.00),
('0000000004','2020-07-29','AA0003',75.00),
('0000000005','2020-07-29','AA0003',90.00),
('0000000001','2020-07-29','BA0001',62.00),
('0000000002','2020-07-29','BA0001',62.00),
('0000000003','2020-07-29','BA0001',66.00),
('0000000004','2020-07-29','BA0001',71.00),
('0000000005','2020-07-29','BA0001',90.00),
('0000000001','2020-07-29','BA0002',79.00),
('0000000002','2020-07-29','BA0002',66.00),
('0000000003','2020-07-29','BA0002',99.00),
('0000000004','2020-07-29','BA0002',65.00),
('0000000005','2020-07-29','BA0002',72.00),
('0000000001','2020-07-29','BA0003',91.00),
('0000000002','2020-07-29','BA0003',73.00),
('0000000003','2020-07-29','BA0003',96.00),
('0000000004','2020-07-29','BA0003',76.00),
('0000000005','2020-07-29','BA0003',78.00),
('0000000001','2020-07-29','CA0001',77.00),
('0000000002','2020-07-29','CA0001',85.00),
('0000000003','2020-07-29','CA0001',78.00),
('0000000004','2020-07-29','CA0001',62.00),
('0000000005','2020-07-29','CA0001',63.00),
('0000000001','2020-07-29','CA0002',88.00),
('0000000002','2020-07-29','CA0002',62.00),
('0000000003','2020-07-29','CA0002',66.00),
('0000000004','2020-07-29','CA0002',97.00),
('0000000005','2020-07-29','CA0002',99.00),
('0000000001','2020-07-29','CA0003',84.00),
('0000000002','2020-07-29','CA0003',64.00),
('0000000003','2020-07-29','CA0003',77.00),
('0000000004','2020-07-29','CA0003',84.00),
('0000000005','2020-07-29','CA0003',97.00),
('0000000001','2020-07-29','CA0004',85.00),
('0000000002','2020-07-29','CA0004',70.00),
('0000000003','2020-07-29','CA0004',72.00),
('0000000004','2020-07-29','CA0004',86.00),
('0000000005','2020-07-29','CA0004',62.00),
('0000000001','2020-07-29','DA0001',88.00),
('0000000002','2020-07-29','DA0001',83.00),
('0000000003','2020-07-29','DA0001',96.00),
('0000000004','2020-07-29','DA0001',94.00),
('0000000005','2020-07-29','DA0001',97.00),
('0000000001','2020-07-29','DA0002',62.00),
('0000000002','2020-07-29','DA0002',88.00),
('0000000003','2020-07-29','DA0002',100.00),
('0000000004','2020-07-29','DA0002',65.00),
('0000000005','2020-07-29','DA0002',66.00),
('0000000001','2020-07-29','DA0003',90.00),
('0000000002','2020-07-29','DA0003',61.00),
('0000000003','2020-07-29','DA0003',66.00),
('0000000004','2020-07-29','DA0003',85.00),
('0000000005','2020-07-29','DA0003',60.00),
('0000000001','2020-07-29','EA0001',64.00),
('0000000002','2020-07-29','EA0001',91.00),
('0000000003','2020-07-29','EA0001',82.00),
('0000000004','2020-07-29','EA0001',63.00),
('0000000005','2020-07-29','EA0001',100.00);

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

/*Data for the table `subkriteria` */

insert  into `subkriteria`(`kode_sub`,`kode_krit_fk`,`nama_sub`,`bobot_sub`,`keterangan_sub`) values 
('AA0001','A0001','Absen',0.50,NULL),
('AA0002','A0001','Telat',0.30,NULL),
('AA0003','A0001','WaktuTelat',0.20,NULL),
('BA0001','A0002','Tingkat Pendidikan',0.50,NULL),
('BA0002','A0002','Komitmen',0.30,NULL),
('BA0003','A0002','Kesesuaian',0.20,NULL),
('CA0001','A0003','Teamwork',0.30,NULL),
('CA0002','A0003','Relation',0.30,NULL),
('CA0003','A0003','Look',0.30,NULL),
('CA0004','A0003','Hutang',0.10,NULL),
('DA0001','A0004','Psikotes1',0.35,NULL),
('DA0002','A0004','Psikotes2',0.35,NULL),
('DA0003','A0004','Psikotes3',0.30,NULL),
('EA0001','A0005','Lama Kerja',1.00,'asdasd');

/*Table structure for table `shownilai` */

DROP TABLE IF EXISTS `shownilai`;

/*!50001 DROP VIEW IF EXISTS `shownilai` */;
/*!50001 DROP TABLE IF EXISTS `shownilai` */;

/*!50001 CREATE TABLE  `shownilai`(
 `IDKaryawan_nilai` char(10) ,
 `Nama` varchar(50) ,
 `Tanggal` date ,
 `nama_sub` varchar(20) ,
 `nilai` double(5,2) 
)*/;

/*Table structure for table `showsaw` */

DROP TABLE IF EXISTS `showsaw`;

/*!50001 DROP VIEW IF EXISTS `showsaw` */;
/*!50001 DROP TABLE IF EXISTS `showsaw` */;

/*!50001 CREATE TABLE  `showsaw`(
 `IDKaryawan_nilai` char(10) ,
 `kode_krit_fk` char(5) ,
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

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `shownilai` AS (select `a`.`IDKaryawan_nilai` AS `IDKaryawan_nilai`,`z`.`Nama` AS `Nama`,`a`.`Tanggal` AS `Tanggal`,`c`.`nama_sub` AS `nama_sub`,`a`.`nilai` AS `nilai` from ((`penilaiankaryawan` `a` left join `karyawan` `z` on((`a`.`IDKaryawan_nilai` = `z`.`IDKaryawan`))) left join `subkriteria` `c` on((`a`.`kode_sub_nilai` = `c`.`kode_sub`)))) */;

/*View structure for view showsaw */

/*!50001 DROP TABLE IF EXISTS `showsaw` */;
/*!50001 DROP VIEW IF EXISTS `showsaw` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `showsaw` AS (select `penilaiankaryawan`.`IDKaryawan_nilai` AS `IDKaryawan_nilai`,`subkriteria`.`kode_krit_fk` AS `kode_krit_fk`,`penilaiankaryawan`.`kode_sub_nilai` AS `kode_sub_nilai`,`subkriteria`.`bobot_sub` AS `bobot_sub`,`penilaiankaryawan`.`nilai` AS `nilai`,`penilaiankaryawan`.`Tanggal` AS `tanggal` from (`penilaiankaryawan` left join `subkriteria` on((`penilaiankaryawan`.`kode_sub_nilai` = `subkriteria`.`kode_sub`))) order by `penilaiankaryawan`.`IDKaryawan_nilai`,`subkriteria`.`kode_krit_fk`,`penilaiankaryawan`.`kode_sub_nilai`) */;

/*View structure for view subkriteriaview */

/*!50001 DROP TABLE IF EXISTS `subkriteriaview` */;
/*!50001 DROP VIEW IF EXISTS `subkriteriaview` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `subkriteriaview` AS (select `subkriteria`.`kode_sub` AS `kode_sub`,`subkriteria`.`nama_sub` AS `nama_sub`,`kriteria`.`nama_krit` AS `nama_krit`,`subkriteria`.`bobot_sub` AS `bobot_sub`,`subkriteria`.`keterangan_sub` AS `keterangan_sub` from (`subkriteria` left join `kriteria` on((`subkriteria`.`kode_krit_fk` = `kriteria`.`kode_krit`)))) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
