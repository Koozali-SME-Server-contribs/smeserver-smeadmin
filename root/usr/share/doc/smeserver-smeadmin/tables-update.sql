USE `smeadmin`;


-- Modify one error in table construction
ALTER TABLE `pppoe` CHANGE `ip` `ip` INT( 10 ) UNSIGNED NOT NULL DEFAULT '0'
;
-- Update size of some fields
ALTER TABLE `pppoe` CHANGE `volume_in` `volume_in` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ,
CHANGE `volume_out` `volume_out` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ;

ALTER TABLE `vpn` CHANGE `volume_in` `volume_in` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ,
CHANGE `volume_out` `volume_out` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ;

ALTER TABLE `ftp` CHANGE `volume_in` `volume_in` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ,
CHANGE `volume_out` `volume_out` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ;

ALTER TABLE `afp` CHANGE `volume_write` `volume_write` INT( 20 ) UNSIGNED NULL DEFAULT NULL ,
CHANGE `volume_read` `volume_read` BIGINT( 20 ) UNSIGNED NULL DEFAULT NULL ;

