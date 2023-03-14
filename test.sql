
SET SQL_MODE ="NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `sikapay_user`(
    `id` int(200) NOT NULL,
    `Firstname` varchar(200) NOT NULL,
    `Lastname` varchar(200) NOT NULL,
    `surname` varchar(200) NOT NULL,
    `Email` varchar(200) NOT NULL,
    `Phonenumber` int(20) NOT NULL,
    `Age` int(20) NOT NULL,
    `Gender` varchar(10) NOT NULL,
    `nationality` varchar(200) NOT NULL,
    `City` varchar(200) NOT NULL,
    `Country` varchar(200) NOT NULL,
    `address1` int(20) NOT NULL,
    `Address2` int(20) NOT NULL,
    `PostalCode` int(20) NOT NULL,
    `Password` varchar(200) NOT NULL,
    )ENGINE=InnoDB DEFAULT CHARSET=latin1_swedish_ci;

    INSERT INTO `sikapay_user` (`id`,`Firstname`,`Lastname`,`surname`,`Email`,`Phonenumber`,`Age`,`Gender`,`nationality`,`City`,`Country`,address1,`Address2`,`PostalCode`,`Password`)VALUES
    (1,'Paul','Gitonga','Mwangi,'mwangigitonga21@gmail.com','0797873427','34','male','kenya','mombasa','kenya','00100','55055','0000','sudo12345');

    INSERT INTO `sikapay_user`(`id`, `Firstname`, `Lastname`, `surname`, `Email`, `Gender`, `nationality`, `City`, `Country`, `address1`, `Address2`, `PostalCode`, `Password`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]