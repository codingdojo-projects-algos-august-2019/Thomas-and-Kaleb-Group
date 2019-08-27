-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema assets
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `assets` ;

-- -----------------------------------------------------
-- Schema assets
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `assets` DEFAULT CHARACTER SET utf8 ;
USE `assets` ;

-- -----------------------------------------------------
-- Table `assets`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `assets`.`users` ;

CREATE TABLE IF NOT EXISTS `assets`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(255) NULL DEFAULT NULL,
  `lname` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `assets`.`assets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `assets`.`assets` ;

CREATE TABLE IF NOT EXISTS `assets`.`assets` (
  `idasset` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `description` VARCHAR(45) NULL DEFAULT NULL,
  `count` INT(11) NULL DEFAULT NULL,
  `brand` VARCHAR(45) NULL DEFAULT NULL,
  `make` VARCHAR(45) NULL DEFAULT NULL,
  `year` VARCHAR(45) NULL DEFAULT NULL,
  `value` FLOAT NULL DEFAULT NULL,
  `location` VARCHAR(45) NULL DEFAULT NULL,
  `comments` LONGTEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idasset`),
  INDEX `fk_farms_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_farms_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `assets`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `assets`.`messages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `assets`.`messages` ;

CREATE TABLE IF NOT EXISTS `assets`.`messages` (
  `idmessages` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `messages` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idmessages`),
  INDEX `fk_messages_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `assets`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `assets`.`users_likes_messages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `assets`.`users_likes_messages` ;

CREATE TABLE IF NOT EXISTS `assets`.`users_likes_messages` (
  `users_id` INT(11) NOT NULL,
  `messages_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`users_id`, `messages_id`),
  INDEX `fk_messages_has_users_users1_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_messages_has_users_messages1_idx` (`messages_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_has_users_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `assets`.`messages` (`idmessages`),
  CONSTRAINT `fk_messages_has_users_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `assets`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
