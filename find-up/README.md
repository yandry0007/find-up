
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://find-up-yampier.c9users.io/' and the admin page from 
'https://find-up-yampier.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide

MIGRACION INICIAL
python manage.py migrate            //SE CREAN LAS TABLAS POR DEFECTO
python manage.py createsuperuser    //SE CREA EL SUPER USUARIO
python manage.py makemigrations     //SE CREAN LAS PRIMERAS MIGRACIONES DEL MODELO YA PERSONALIZADO
python manage.py migrate            //SE APLICAN LAS MIGRACIONES EN LA DB

ERRORES AL DEPLOYAR EN HEROKU
error: 
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
solucion:
yampier:~/workspace (master) $ export DJANGO_SETTINGS_MODULE=find_up.settings
yampier:~/workspace (master) $ heroku config:set DJANGO_SETTINGS_MODULE=find_up.settings

COMANDOS POSTGRES HEROKU PEPA

1)Nuestro segundo comando nos ayudara a saber la lista de nuestras bases de datos, el comando es:
\l
3)Seleccionar una base de datos o cambiar de base:
\c basename
4)Listar las tablas de una base de datos:
\d 
Si la lista es muy larga veremos que podemos movernos hacia abajo y luego para salir solo digitamos la letra “q”
5)Para ver la información de la estructura de una tabla en especifico:
\d nombre_table
6)Vaciar una tabla en especifico o el famoso TRUNCATE que conocemos:
TRUNCATE TABLE table RESTART IDENTITY
Con este comando borramos el contenido de una tabla y reiniciamos su indice sino agregamos RESTART IDENTITY nuestros indices no seran reiniciados y seguiran según el ultimo registro.
7)Crear una base de datos:
CREATE DATABASE basename;
8)Borrar o eliminar una base de datos:
DROP DATABASE basename;
9)Borrar o eliminar una tabla en especifico:
DROP TABLE tablename;
10)Enviar resultados de una consulta a un archivo delimitado por |
COPY (SELECT * FROM tablename) TO '/home/tablename.csv' WITH DELIMITER '|';
Cabe mencionar que el archivo necesito permisos de escritura.
11)Uso de LIMIT y OFFSET
SELECT * FROM table LIMIT limit OFFSET offset;
Donde:
limit: es nuestro limite de registros a mostrar
offset: indica desde donde comenzaran a mostrarce los registros
12)Uso de comillas:
SELECT “column” FROM “table” WHERE “column” = 'value';
Generalmente podemos utilizar comillas dobles para nuestras columnas y comillas simples para nuestros valores, esto no es una regla pero a veces es necesario en casos especiales, tales como cuando ocupamos nombres reservados, por ejemplo:
SELECT to FROM table;
En este caso tenemos un campo llamado “to”, esto nos dará un error de sintaxis, por lo tanto tendremos que usar comillas dobles:
SELECT “to” FROM table;
13)Salir del cliente psql:
\q 


CREATE TABLE PROVEEDORES(
PROVEEDORID int NOT NULL,
NOMBREPROV char(50) NOT NULL,
CONTACTO char(50) NOT NULL,
CELUPROV char(12) NULL,
FIJOPROV char(12) NULL,
CONSTRAINT PK_PROVEEDORES PRIMARY KEY
(PROVEEDORID ) );

CREATE TABLE CATEGORIAS(
CATEGORIAID int NOT NULL,
NOMBRECAT char(50) NOT NULL,
CONSTRAINT PK_CATEGORIAS PRIMARY KEY
(CATEGORIAID) ) ;

CREATE TABLE CLIENTES(
CLIENTEID int NOT NULL,
CEDULA_RUC char(10) NOT NULL,
NOMBRECIA char(30) NOT NULL,
NOMBRECONTACTO char(50) NOT NULL,
DIRECCIONCLI char(50) NOT NULL,
FAX char(12) NULL,
EMAIL char(50) NULL,
CELULAR char(12) NULL,
FIJO char(12) NULL,
CONSTRAINT PK_CLIENTES PRIMARY KEY
(CLIENTEID) );

COMANDOS HEROKU:
//Ingresar a la base de datos postgres de heroku
dir/del/proyrcto->heroku pg:psql

//Agregar contenido a heroku
dir/del/proyrcto->git add . 
//Agregar comentarios 
dir/del/proyrcto->git commit -m "Primer cambio de modulos"
//Subir todos los cambios a heroku
dir/del/proyrcto->git push heroku master
//Deployment en la web
dir/del/proyrcto->heroku open
//Deployment localmente
dir/del/proyrcto->heroku local
