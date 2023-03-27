create database prueba;

use prueba;

create table Usuario(id int, email varchar(255), username varchar(50))

DROP TABLE usuario;

SELECT * FROM prueba.usuario;

ALTER TABLE usuario ADD edad INT;
ALTER TABLE usuario modify column email varchar(50);

INSERT INTO usuario (email,username,edad) VALUES ('prueba@hotmail.com', 'prueba de user', 21 );
INSERT INTO usuario (email,username,edad) VALUES ('prueba2@hotmail.com', 'prueba de user2', 22 );
INSERT INTO usuario (email,username,edad) VALUES ('prueba3@hotmail.com', 'prueba de user3', 30 );

DELETE FROM usuario WHERE email = 'prueba@hotmail.com' limit 1;

ALTER table usuario add primary key (id);
ALTER table usuario modify column id INT AUTO_INCREMENT;

SELECT * FROM usuario WHERE email = 'prueba2@hotmail.com';
SELECT * FROM usuario WHERE edad > 22;

UPDATE usuario SET edad = 32 WHERE id = 3;

DELETE FROM usuario WHERE id = 1;