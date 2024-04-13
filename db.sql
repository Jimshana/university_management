/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - unique_id
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`unique_id` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `unique_id`;

/*Table structure for table `batch` */

DROP TABLE IF EXISTS `batch`;

CREATE TABLE `batch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `batch` varchar(20) DEFAULT NULL,
  `crsid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `batch` */

insert  into `batch`(`id`,`batch`,`crsid`) values 
(1,'2020-2023',1),
(2,'2020-2023',2);

/*Table structure for table `callinternal` */

DROP TABLE IF EXISTS `callinternal`;

CREATE TABLE `callinternal` (
  `callid` int(11) NOT NULL AUTO_INCREMENT,
  `clg` varchar(20) DEFAULT NULL,
  `crsid` varchar(20) DEFAULT NULL,
  `batch` int(11) DEFAULT NULL,
  `sem` varchar(20) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`callid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `callinternal` */

/*Table structure for table `college` */

DROP TABLE IF EXISTS `college`;

CREATE TABLE `college` (
  `clgid` int(11) NOT NULL AUTO_INCREMENT,
  `clgname` varchar(30) DEFAULT NULL,
  `phno` bigint(20) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`clgid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `college` */

insert  into `college`(`clgid`,`clgname`,`phno`,`email`,`place`,`street`,`pin`,`login_id`) values 
(1,'stas pullarikkunnu',1234567890,'stas@gmail.com','kottayam','pullarikkunnu',123456,2),
(2,'cms ktm',987654321,'cms@gmail.com','kottayam','chungam',20021,3);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `from` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`complaint`,`date`,`reply`,`status`,`uid`,`from`) values 
(1,'ttdghbn ','2024-03-11','pending','pending',9,'student');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `crsid` int(11) NOT NULL AUTO_INCREMENT,
  `crs` varchar(50) DEFAULT NULL,
  `crscode` varchar(20) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`crsid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`crsid`,`crs`,`crscode`,`department_id`) values 
(1,'bsc cyberforensic','cyberforensic123',2),
(2,'bsc computerscience','computerscience123',3);

/*Table structure for table `coursealloc` */

DROP TABLE IF EXISTS `coursealloc`;

CREATE TABLE `coursealloc` (
  `crsallocid` int(11) NOT NULL AUTO_INCREMENT,
  `clgname` int(30) DEFAULT NULL,
  `crs` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`crsallocid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `coursealloc` */

insert  into `coursealloc`(`crsallocid`,`clgname`,`crs`) values 
(1,2,'1'),
(2,2,'2'),
(3,1,'1'),
(4,1,'2');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`department_id`,`department`) values 
(2,'cyberforensic'),
(3,'computer science');

/*Table structure for table `externalmk` */

DROP TABLE IF EXISTS `externalmk`;

CREATE TABLE `externalmk` (
  `ex-mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(20) DEFAULT NULL,
  `inter_id` int(11) DEFAULT NULL,
  `mark` int(11) DEFAULT NULL,
  PRIMARY KEY (`ex-mark_id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=latin1;

/*Data for the table `externalmk` */

insert  into `externalmk`(`ex-mark_id`,`regno`,`inter_id`,`mark`) values 
(1,'100000',2,26),
(2,'100001',2,34),
(3,'100005',2,54),
(4,'100000',30,45),
(5,'100001',30,45),
(6,'100005',30,56),
(7,'100002',14,45),
(8,'100003',14,34),
(9,'100004',14,45),
(10,'100002',15,45),
(11,'100003',15,34),
(12,'100004',15,34),
(13,'100000',3,45),
(14,'100001',3,34),
(15,'100005',3,26),
(16,'100000',4,34),
(17,'100001',4,23),
(18,'100005',4,35),
(19,'100002',16,34),
(20,'100003',16,22),
(21,'100004',16,32),
(22,'100002',17,33),
(23,'100003',17,33),
(24,'100004',17,24),
(25,'100000',5,33),
(26,'100001',5,33),
(27,'100005',5,24),
(28,'100000',6,33),
(29,'100001',6,23),
(30,'100005',6,33),
(31,'100002',18,33),
(32,'100003',18,23),
(33,'100004',18,14),
(34,'100002',20,34),
(35,'100003',20,45),
(36,'100004',20,23),
(37,'100000',7,33),
(38,'100001',7,33),
(39,'100005',7,33),
(40,'100000',8,34),
(41,'100001',8,33),
(42,'100005',8,23),
(43,'100002',21,34),
(44,'100003',21,33),
(45,'100004',21,23),
(46,'100002',29,34),
(47,'100003',29,55),
(48,'100004',29,34),
(49,'100000',9,34),
(50,'100001',9,35),
(51,'100005',9,57),
(52,'100000',10,56),
(53,'100001',10,56),
(54,'100005',10,56),
(55,'100002',22,56),
(56,'100003',22,56),
(57,'100004',22,56),
(58,'100002',23,34),
(59,'100003',23,45),
(60,'100004',23,56),
(61,'100000',11,34),
(62,'100001',11,45),
(63,'100000',12,45),
(64,'100001',12,46),
(65,'100005',12,56),
(66,'100002',24,34),
(67,'100003',24,54),
(68,'100004',24,56),
(69,'100002',25,56),
(70,'100003',25,45),
(71,'100004',25,34);

/*Table structure for table `internalmk` */

DROP TABLE IF EXISTS `internalmk`;

CREATE TABLE `internalmk` (
  `markid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(20) DEFAULT NULL,
  `subjectid` int(20) DEFAULT NULL,
  `internmrk` int(11) DEFAULT NULL,
  `attndnc` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`markid`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

/*Data for the table `internalmk` */

insert  into `internalmk`(`markid`,`regno`,`subjectid`,`internmrk`,`attndnc`) values 
(1,'100000',2,30,'75'),
(2,'100000',30,27,'75'),
(3,'100000',3,27,'75'),
(4,'100000',4,27,'75'),
(5,'100000',5,32,'75'),
(6,'100000',6,27,'75'),
(7,'100000',7,32,'75'),
(8,'100000',8,27,'75'),
(9,'100000',9,22,'75'),
(10,'100000',10,34,'75'),
(11,'100000',11,27,'75'),
(12,'100000',12,27,'75'),
(13,'100001',2,27,'75'),
(14,'100001',30,27,'75'),
(15,'100001',3,27,'75'),
(16,'100001',4,35,'75'),
(17,'100001',5,27,'75'),
(18,'100001',6,36,'75'),
(19,'100001',7,27,'75'),
(20,'100001',8,7,'75'),
(21,'100001',9,27,'75'),
(22,'100001',10,34,'75'),
(23,'100001',11,27,'99'),
(24,'100001',12,27,'89'),
(25,'100005',2,27,'75'),
(26,'100005',30,27,'75'),
(27,'100005',3,27,'99'),
(28,'100005',4,35,'75'),
(29,'100005',5,27,'99'),
(30,'100005',6,27,'75'),
(31,'100005',7,27,'75'),
(32,'100005',8,33,'75'),
(33,'100005',9,27,'75'),
(34,'100005',10,33,'75'),
(35,'100005',11,27,'75'),
(36,'100005',12,27,'75'),
(37,'100002',14,27,'75'),
(38,'100002',15,27,'75'),
(39,'100002',16,26,'75'),
(40,'100002',17,27,'75'),
(41,'100002',18,27,'75'),
(42,'100002',20,36,'75'),
(43,'100002',21,27,'75'),
(44,'100002',22,27,'75'),
(45,'100002',23,27,'100'),
(46,'100002',24,27,'75'),
(47,'100002',25,27,'75'),
(48,'100002',29,27,'35'),
(49,'100003',14,27,'48'),
(50,'100003',15,27,'75'),
(51,'100003',16,27,'75'),
(52,'100003',17,27,'75'),
(53,'100003',18,27,'75'),
(54,'100003',20,27,'75'),
(55,'100003',21,27,'75'),
(56,'100003',29,27,'75'),
(57,'100003',22,27,'75'),
(58,'100003',23,27,'75'),
(59,'100003',24,27,'75'),
(60,'100003',25,27,'75'),
(61,'100004',14,27,'75'),
(62,'100004',15,27,'75'),
(63,'100004',16,27,'75'),
(64,'100004',17,27,'75'),
(65,'100004',18,40,'75'),
(66,'100004',20,27,'75'),
(67,'100004',21,27,'75'),
(68,'100004',22,27,'75'),
(69,'100004',23,27,'75'),
(70,'100004',24,27,'75'),
(71,'100004',25,27,'75'),
(72,'100004',29,27,'75');

/*Table structure for table `key` */

DROP TABLE IF EXISTS `key`;

CREATE TABLE `key` (
  `key_id` int(11) NOT NULL AUTO_INCREMENT,
  `reg_no` varchar(50) DEFAULT NULL,
  `key` varchar(50000) DEFAULT NULL,
  PRIMARY KEY (`key_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `key` */

insert  into `key`(`key_id`,`reg_no`,`key`) values 
(1,'123456123','[-0.09442066  0.10487175 -0.03958959 -0.0467214  -0.13887785 -0.05060111\n  0.01586618 -0.11365444  0.14558962 -0.05117111  0.1649534  -0.01170003\n -0.22736874 -0.08612827 -0.01318003  0.12008015 -0.14403033 -0.06545118\n -0.15435477 -0.16509108  0.01227786  0.03309114 -0.00623021 -0.02529114\n -0.13487881 -0.21254425 -0.08789422 -0.07028944  0.0775577  -0.08567873\n  0.07069924 -0.00939503 -0.25857493 -0.08003914 -0.03156203  0.04740539\n -0.11733458 -0.0984429   0.17356002 -0.03761207 -0.12195817  0.11694153\n  0.09593479  0.18319131  0.21212484 -0.02524104  0.00542298 -0.10559032\n  0.12082711 -0.20059115 -0.00822453  0.18730669  0.08457928  0.10060387\n  0.06489863 -0.0736908   0.03227683  0.16133417 -0.15186432  0.04941982\n  0.10192189 -0.03509578 -0.05572195 -0.08406591  0.1337118   0.04314445\n -0.08251414 -0.12326265  0.15474212 -0.20145148 -0.05971032  0.07007498\n -0.06639679 -0.18583195 -0.28795019  0.12546633  0.38430911  0.22799113\n -0.11610553  0.02178224 -0.09764738 -0.04190879  0.00773893  0.02077547\n -0.07593981 -0.10604639 -0.10205828  0.06393087  0.21585512 -0.03193526\n  0.03627367  0.2497865   0.07408413 -0.01001823 -0.06201163  0.01647377\n -0.17355286 -0.04481032 -0.0290696  -0.03551385  0.10271305 -0.16782838\n  0.04689698  0.15768752 -0.13027455  0.20614858 -0.03366915 -0.00840632\n -0.00525265  0.04444858 -0.00083447 -0.00222257  0.13403761 -0.15684904\n  0.25485301  0.1547372  -0.04088277  0.09634256  0.07770343  0.15693538\n -0.08128846  0.02567462 -0.13310255 -0.13168065 -0.04671797 -0.01592504\n  0.06558213  0.06559446]'),
(2,'123456123','[-0.09442066  0.10487175 -0.03958959 -0.0467214  -0.13887785 -0.05060111\n  0.01586618 -0.11365444  0.14558962 -0.05117111  0.1649534  -0.01170003\n -0.22736874 -0.08612827 -0.01318003  0.12008015 -0.14403033 -0.06545118\n -0.15435477 -0.16509108  0.01227786  0.03309114 -0.00623021 -0.02529114\n -0.13487881 -0.21254425 -0.08789422 -0.07028944  0.0775577  -0.08567873\n  0.07069924 -0.00939503 -0.25857493 -0.08003914 -0.03156203  0.04740539\n -0.11733458 -0.0984429   0.17356002 -0.03761207 -0.12195817  0.11694153\n  0.09593479  0.18319131  0.21212484 -0.02524104  0.00542298 -0.10559032\n  0.12082711 -0.20059115 -0.00822453  0.18730669  0.08457928  0.10060387\n  0.06489863 -0.0736908   0.03227683  0.16133417 -0.15186432  0.04941982\n  0.10192189 -0.03509578 -0.05572195 -0.08406591  0.1337118   0.04314445\n -0.08251414 -0.12326265  0.15474212 -0.20145148 -0.05971032  0.07007498\n -0.06639679 -0.18583195 -0.28795019  0.12546633  0.38430911  0.22799113\n -0.11610553  0.02178224 -0.09764738 -0.04190879  0.00773893  0.02077547\n -0.07593981 -0.10604639 -0.10205828  0.06393087  0.21585512 -0.03193526\n  0.03627367  0.2497865   0.07408413 -0.01001823 -0.06201163  0.01647377\n -0.17355286 -0.04481032 -0.0290696  -0.03551385  0.10271305 -0.16782838\n  0.04689698  0.15768752 -0.13027455  0.20614858 -0.03366915 -0.00840632\n -0.00525265  0.04444858 -0.00083447 -0.00222257  0.13403761 -0.15684904\n  0.25485301  0.1547372  -0.04088277  0.09634256  0.07770343  0.15693538\n -0.08128846  0.02567462 -0.13310255 -0.13168065 -0.04671797 -0.01592504\n  0.06558213  0.06559446]'),
(3,'2100987','[-0.19113038  0.07567091  0.05952412 -0.04961952 -0.04525074 -0.07759775\n  0.0183036  -0.08202678  0.14642154 -0.0786428   0.19688305 -0.07420541\n -0.22430535 -0.10599352  0.00958272  0.06479571 -0.14409073 -0.20185871\n -0.08707543 -0.11905081  0.04834796  0.05196679 -0.01613084  0.064147\n -0.12774387 -0.3448953  -0.04214631 -0.16852643  0.02280005 -0.06937151\n  0.02674062  0.01484181 -0.25636509 -0.00845758 -0.08246096  0.00851154\n  0.07861527 -0.02570719  0.15813874 -0.01739935 -0.17853338 -0.08987243\n  0.04048543  0.20925404  0.19136314  0.01048502 -0.02141001 -0.04916666\n  0.04104818 -0.2151399   0.02069051  0.1510248   0.05088536 -0.00046988\n  0.04430971 -0.16320619 -0.00114772 -0.03146753 -0.17889805  0.0023605\n  0.00654385 -0.02732917 -0.0542242   0.00601569  0.28649101  0.04843152\n -0.06594548 -0.12255564  0.16008227 -0.21994993 -0.01974969  0.12323701\n -0.08090628 -0.11731926 -0.29257801  0.06583631  0.42700931  0.06531164\n -0.17797446  0.08913532 -0.20621833 -0.04393217  0.08105298 -0.01307348\n -0.1212281   0.04943307 -0.18886122  0.03532546  0.23045494  0.02433118\n -0.04223884  0.194023    0.01045593 -0.0215692   0.09313846  0.03223488\n -0.07708383 -0.0632352  -0.09356853 -0.04143924  0.08323521 -0.05276623\n -0.06151401  0.11666316 -0.18453848  0.06764136  0.01071408 -0.08643951\n -0.05746524  0.00866935 -0.08937678 -0.09908096  0.1228705  -0.20230637\n  0.11024632  0.09842937  0.03205169  0.18269587  0.03342564  0.06572822\n -0.09370929 -0.01405849 -0.11140597 -0.04556683  0.07541645  0.00309103\n  0.08877508  0.04961949]'),
(4,'2100987','[-0.07637871  0.17170765  0.05861941 -0.03099767 -0.02980099 -0.07493445\n  0.01610773 -0.01403978  0.1825441  -0.00404676  0.19725518 -0.010481\n -0.18686531 -0.0773321  -0.02403855  0.0910844  -0.07309637 -0.11989422\n -0.10962781 -0.04059412 -0.04580535  0.02552254  0.02898808  0.06098254\n  0.03043436 -0.35606897 -0.02900009 -0.17733367  0.062938   -0.17724803\n -0.04325043 -0.00454959 -0.18416902 -0.11379911 -0.02139173  0.00498736\n  0.02276303 -0.05699758  0.17666033  0.00242567 -0.1505947  -0.01011844\n  0.00489636  0.31027433  0.1917111   0.03642995  0.0284376  -0.04955383\n  0.12692314 -0.13430656  0.12099848  0.0453941   0.11458787  0.00815624\n  0.0576623  -0.19801572 -0.01801809  0.01860972 -0.18421848  0.03492313\n  0.07680842  0.02217621 -0.10496391 -0.02322344  0.25938764  0.06329976\n -0.10683719 -0.12070169  0.10255866 -0.14642008  0.03444306  0.03684752\n -0.10609844 -0.08926631 -0.22109593  0.13997845  0.38331968  0.11473239\n -0.16472907  0.03593661 -0.16484886 -0.00329186  0.01222987  0.0309754\n -0.13869888  0.06053416 -0.12149813  0.01583297  0.11249048  0.04137864\n -0.10384093  0.10683775 -0.08097313  0.00621488  0.00136105  0.00410505\n -0.13100058  0.01874434 -0.13475977 -0.04814471  0.0862684  -0.06946774\n -0.05021278  0.09822139 -0.20661122  0.06873544  0.01756095  0.01859832\n  0.0234076   0.06949473 -0.11590872 -0.06790194  0.1265517  -0.20165755\n  0.21205473  0.09403516  0.08021063  0.13776046  0.09858675  0.03863638\n  0.03914078 -0.00840326 -0.13477476 -0.05715727  0.09448155  0.05965147\n  0.12506202  0.04729629]'),
(5,'210089','[-0.12092926  0.16690977  0.09988804 -0.05971301 -0.09667578 -0.03862163\n -0.0075593  -0.06841411  0.21793886 -0.10127094  0.24891675 -0.02921471\n -0.15638223 -0.17582364 -0.00478367  0.1012559  -0.12550135 -0.16416654\n -0.04706033 -0.02401141  0.03403618 -0.08838936  0.03549147  0.06212945\n -0.06928648 -0.45806283 -0.06344358 -0.12538022  0.10881747 -0.16036941\n -0.08118406  0.00862428 -0.25526914 -0.14173244 -0.10810031  0.09466018\n -0.03688773 -0.04746639  0.1125671  -0.04563163 -0.14942333 -0.04647525\n -0.04144907  0.24896191  0.19466184  0.07743611  0.07403726 -0.0464568\n  0.07822351 -0.2254938   0.0979453   0.14870049  0.09172512  0.03303918\n  0.03772454 -0.12188777 -0.00812251  0.01019936 -0.22435568  0.07283711\n  0.09868834  0.01958148 -0.10099366 -0.04124115  0.26757595  0.16055159\n -0.09027468 -0.13022231  0.19540785 -0.18811998  0.02421031 -0.0109254\n -0.10209817 -0.16976906 -0.2454633   0.11555552  0.35292962  0.19155478\n -0.14276181 -0.00670795 -0.19100532  0.00920895 -0.00325083  0.02471785\n -0.10736776  0.05972727 -0.13265869  0.07536998  0.10220677  0.00605162\n -0.02070012  0.21258819 -0.01379137  0.01623972  0.01057414  0.04498654\n -0.12705804  0.07315401 -0.14085214  0.01556433  0.11305251 -0.07184029\n -0.00954778  0.11503032 -0.14778942  0.126526   -0.04126357  0.02903637\n  0.03228605  0.01697978 -0.15403076 -0.14424616  0.12811708 -0.17798115\n  0.20046547  0.19517419  0.06388114  0.15262263  0.1214105   0.09231856\n  0.0726833  -0.06914533 -0.13517809 -0.03605311  0.02778906 -0.03872199\n  0.00766001  0.05989857]'),
(6,'210056','[-0.20541354  0.04257658  0.07648615 -0.01846885 -0.01476378 -0.0221768\n  0.04633306 -0.07902881  0.1669912  -0.11809494  0.30529717  0.01443071\n -0.21733984 -0.17080179  0.09249647  0.05372491 -0.11454917 -0.14261326\n -0.0934017  -0.04852132  0.07806613  0.01664089 -0.01279377  0.07596153\n -0.15221424 -0.38136891 -0.10138581 -0.16159797  0.00893439 -0.13027711\n -0.06429105  0.0047097  -0.21240896 -0.05617213 -0.09821574  0.02219718\n  0.01946994 -0.04680492  0.11485274 -0.05280317 -0.14306936 -0.08287477\n -0.01811916  0.24939938  0.15134218 -0.05451052  0.05552297 -0.02248312\n  0.06948358 -0.24110466 -0.01015564  0.09480315  0.12500823  0.02534568\n  0.05356558 -0.09485894  0.00113777 -0.01802697 -0.19275133  0.03020863\n -0.0005398  -0.08853091 -0.08007608  0.00854854  0.21809064  0.08310989\n -0.069001   -0.12947442  0.12653187 -0.16984046  0.00997237  0.11723165\n -0.13882668 -0.19506471 -0.2857182   0.06561589  0.4080739   0.08063678\n -0.16003869  0.0777939  -0.23073494 -0.02456873  0.01806765 -0.02395578\n -0.08836585  0.10337353 -0.19012561  0.18123551  0.21293801 -0.02096449\n  0.02656662  0.21898584  0.03746826 -0.02363641  0.1009178   0.0717338\n -0.01804492 -0.04373701 -0.05404883  0.05067461  0.11134747 -0.09076113\n  0.00580885  0.06746078 -0.21203396  0.13379735  0.0124054  -0.04354916\n  0.00771595 -0.0601388  -0.10759154 -0.06134838  0.09089486 -0.25835347\n  0.0648396   0.13372135  0.03154391  0.16910435 -0.06944135  0.03310654\n -0.12008801 -0.05835336 -0.14478572 -0.01297812  0.08043289  0.02035606\n  0.02931769  0.00123652]'),
(7,'210094','[-0.1899136   0.07092836  0.05624477 -0.05072846 -0.04028952 -0.07503647\n  0.01711803 -0.08382227  0.14588356 -0.0779011   0.19177793 -0.07372721\n -0.22381902 -0.10882488  0.00817554  0.06481533 -0.14519191 -0.20058525\n -0.08738986 -0.11784597  0.04870783  0.05000803 -0.01595229  0.06227503\n -0.13009308 -0.34763095 -0.04375641 -0.16854887  0.02306505 -0.06599748\n  0.02577352  0.01540059 -0.25629497 -0.00967079 -0.07963981  0.01088065\n  0.08091385 -0.02286549  0.15960541 -0.01571491 -0.17541379 -0.08806103\n  0.04128447  0.21074906  0.19102566  0.01390233 -0.01783513 -0.04794689\n  0.04513326 -0.21538313  0.022961    0.14805709  0.04897464 -0.00144546\n  0.04608398 -0.16244128 -0.00197287 -0.0287756  -0.18099247  0.00722199\n  0.00544281 -0.02780329 -0.05545326  0.00925001  0.28349316  0.04673756\n -0.0664659  -0.12180293  0.1620746  -0.21788052 -0.01330137  0.11917298\n -0.0790375  -0.11764447 -0.29075357  0.06582653  0.43228203  0.06486857\n -0.17779517  0.09092847 -0.20611145 -0.04766677  0.08521108 -0.01575506\n -0.11873054  0.05087551 -0.18732351  0.03649285  0.23245634  0.02609039\n -0.04013608  0.19315     0.00951014 -0.02298067  0.09381464  0.03386438\n -0.08064022 -0.06195525 -0.09479683 -0.0430774   0.08491245 -0.05386112\n -0.05733802  0.11348139 -0.18415552  0.07082009  0.01159008 -0.08651056\n -0.05639703  0.00822006 -0.09202684 -0.09773708  0.12410287 -0.20276931\n  0.10848091  0.09828989  0.03168697  0.184173    0.0330079   0.06543419\n -0.09081921 -0.01194913 -0.11157327 -0.04797012  0.07415099  0.0061712\n  0.09127021  0.04958429]');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(20) DEFAULT NULL,
  `pswd` varchar(20) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`Username`,`pswd`,`type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'stas@gmail.com','9400','college'),
(3,'cms@gmail.com','4095','college'),
(4,'lijinraj@2002','rajlijin129','subadmin'),
(5,'vismaya@2001','vismaya2505','subadmin'),
(9,'abhi@gmail.com','1234','student'),
(10,'avinash@gmail.com','9874563245','student'),
(12,'lenin@gamil.com','7034232685','student'),
(13,'albinsannn@gmail.com','9076547634','student'),
(15,'surrr@gmail.com','7012515647','student'),
(18,'vishnu@gmail.com','9657435690','student'),
(20,'sincy@gmail.com','9874536709','teacher'),
(21,'mam@gmail.com','123','verifier');

/*Table structure for table `notifctn` */

DROP TABLE IF EXISTS `notifctn`;

CREATE TABLE `notifctn` (
  `notfid` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(100) DEFAULT NULL,
  `clg` varchar(50) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `callid` int(11) DEFAULT NULL,
  PRIMARY KEY (`notfid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notifctn` */

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(500) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `verifier_lid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`report_id`,`file`,`date`,`verifier_lid`,`status`) values 
(1,'/static/report/20240227134810.jpg','2024-02-27',21,'pending'),
(2,'/static/report/20240227134930.jpg','2024-02-27',21,'pending'),
(3,'/static/report/20240227135055.jpg','2024-02-27',21,'pending');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `stdntid` int(11) NOT NULL AUTO_INCREMENT,
  `clgid` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `hname` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `street` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `guardian` varchar(30) DEFAULT NULL,
  `lguardian` varchar(30) DEFAULT NULL,
  `crs` varchar(30) DEFAULT NULL,
  `batch` int(11) DEFAULT NULL,
  `sem` varchar(30) DEFAULT NULL,
  `phno` bigint(20) DEFAULT NULL,
  `regno` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`stdntid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`stdntid`,`clgid`,`name`,`gender`,`dob`,`hname`,`place`,`street`,`post`,`pin`,`state`,`guardian`,`lguardian`,`crs`,`batch`,`sem`,`phno`,`regno`,`email`,`photo`,`login_id`) values 
(2,1,'abhijith','Male','2003-04-02','alumkalhouse','kottayam','nattakam','nattakam po',342508,'kerala','shaji','shaji','1',1,'6th semester',9786543219,'100000','abhi@gmail.com','c.jpg',9),
(3,1,'avinash','Male','2003-06-05','puthanveedu','kottayam','kidangoor ','kidangoor po',567347,'kerala','johny','johny','1',1,'6th semester',9874563245,'100001','avinash@gmail.com','2100987.jpg',10),
(5,1,'LENIN RAJ','Male','2000-02-06','leninvilla','alappuzha','kayamkulam','keerikkad',690508,'kerala','rajan','rajan','2',2,'6th semester',7034232685,'100002','lenin@gamil.com','2100987.jpg',12),
(6,1,'albin','Male','2003-03-23','albinhouse','kottayam','ettumanoor','pattithanam',678954,'kerala','honey','honey','2',2,'6th semester',9076547634,'100003','albinsannn@gmail.com','210089.jpg',13),
(8,1,'suraj','Male','2003-08-08','pandarappatathil','kottayam','vadakkenirappu','vadakkenirappu',686612,'kerala','suresh','suresh','2',2,'6th semester',7012515647,'100004','surrr@gmail.com','210056.jpg',15),
(9,1,'vishnu','Male','2003-06-05','kottarathil','kottayam','kumarakom','kumarakom po',686563,'kerala','jayamon','jayamon','1',1,'6th semester',9657435690,'100005','vishnu@gmail.com','210094.jpg',18);

/*Table structure for table `subadmin` */

DROP TABLE IF EXISTS `subadmin`;

CREATE TABLE `subadmin` (
  `subadminid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(11) DEFAULT NULL,
  PRIMARY KEY (`subadminid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `subadmin` */

insert  into `subadmin`(`subadminid`,`loginid`,`name`,`gender`,`dob`,`photo`,`email`,`phone`) values 
(1,4,'lijin','Male','2002-08-06','/static/subadmin/240226-150540.jpg','rajlijin@gmail.com',987654321),
(2,5,'vismaya B','Female','2001-05-25','/static/subadmin/240226-150938.jpg','vismayabiju@gmail.com',9061504567);

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subjectid` int(11) NOT NULL AUTO_INCREMENT,
  `crs` varchar(20) DEFAULT NULL,
  `sem` varchar(20) DEFAULT NULL,
  `batch` varchar(20) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`subjectid`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subjectid`,`crs`,`sem`,`batch`,`subject`) values 
(2,'1','1st semester','1','c++'),
(3,'1','2nd semester','1','English'),
(4,'1','2nd semester','1','digital'),
(5,'1','3rd semester','1','English'),
(6,'1','3rd semester','1','datastructure'),
(7,'1','4th semester','1','java'),
(8,'1','4th semester','1','os'),
(9,'1','5th semester','1','OR'),
(10,'1','5th semester','1','maths'),
(11,'1','6th semester','1','stv'),
(12,'1','6th semester','1','Ethical hacking'),
(14,'2','1st semester','2','stv'),
(15,'2','1st semester','2','cs'),
(16,'2','2nd semester','2','cs-part2'),
(17,'2','2nd semester','2','digital'),
(18,'2','3rd semester','2','OR'),
(20,'2','3rd semester','2','CT'),
(21,'2','4th semester','2','C++'),
(22,'2','5th semester','2','DS'),
(23,'2','5th semester','2','ENGLISH'),
(24,'2','6th semester','2','MINIPROJECT'),
(25,'2','6th semester','2','EH'),
(29,'2','4th semester','2','MATHS'),
(30,'1','1st semester','1','maths');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  `clgid` int(11) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`login_id`,`first_name`,`last_name`,`gender`,`dob`,`house_name`,`place`,`pincode`,`district`,`phone`,`email`,`qualification`,`photo`,`clgid`) values 
(1,19,'suraj','NS','Male','1989-07-31','Valiyaveettil','alappuzha','690567','alappuzha','8976543456','surajns@gmail.com','msc computerscience','/static/teacher/a1316edd-32e2-49e7-acd4-e2d9b4132490.jpg',1),
(2,20,'sincy','mol','Female','1989-07-05','mangalath','kottayam','678590','kottayam','9874536709','sincy@gmail.com','BA&BED','/static/teacher/af34729f-3286-43f2-b886-b999c842ada8.jpg',1);

/*Table structure for table `verifier` */

DROP TABLE IF EXISTS `verifier`;

CREATE TABLE `verifier` (
  `verifier_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Purpose` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`verifier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `verifier` */

insert  into `verifier`(`verifier_id`,`login_id`,`Name`,`phone`,`Email`,`Purpose`) values 
(1,21,'Mamtha K','96455635284','venus.mamata@gmail.com','job hiring ');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
