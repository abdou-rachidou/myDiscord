--
-- Table structure for table `utilisateurs`
--
USE `abdou-rachidou-arouna_mydiscord`;



CREATE TABLE `utilisateurs` (
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mot_de_passe` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=InnoDB;

--
-- Dumping data for table `utilisateurs`
--


--
-- Table structure for table `messages`
--


CREATE TABLE `messages` (
  `id_message` int NOT NULL AUTO_INCREMENT,
  `contenu_message` text,
  `heure_publication` datetime DEFAULT NULL,
  `id_utilisateur` int DEFAULT NULL,
  PRIMARY KEY (`id_message`),
  KEY `id_utilisateur` (`id_utilisateur`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB;

--
-- Dumping data for table `messages`
--





--
-- Table structure for table `reactions`
--

CREATE TABLE `reactions` (
  `id_reaction` int NOT NULL AUTO_INCREMENT,
  `id_message` int DEFAULT NULL,
  `id_utilisateur` int DEFAULT NULL,
  `emoji` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_reaction`),
  KEY `id_message` (`id_message`),
  KEY `id_utilisateur` (`id_utilisateur`),
  CONSTRAINT `reactions_ibfk_1` FOREIGN KEY (`id_message`) REFERENCES `messages` (`id_message`),
  CONSTRAINT `reactions_ibfk_2` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB;
--
-- Dumping data for table `reactions`
--

-- Dump completed on 2024-02-12 13:37:39