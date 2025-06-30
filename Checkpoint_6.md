# Conceptos teóricos

## ¿Para qué usamos Clases en Python?

Las clases son un concepto que se relaciona en Python con la programación orientada a objetos (PPO), es decir, que, de alguna forma, el cada elemento de este tipo de programación en un objeto.

Utilizamos las clases para englobar características y funciones para, con ellas, crear objetos. Las clases son objetos en sí mismos que funcionan como plantillas con las que crearemos otros objetos. Las clases, como su nombre indica, representan los atributos y métodos comunes de una clase o tipo de algo; por ejemplo, la clase Perros guardará las características y acciones de los perros en general, de donde crearemos objetos de perros específicos, por ejemplo. La mejor manera de comprender el uso de las clases es mediante ejemplos. En este caso, vamos a crear una clase que nos sirva para generar personajes de un juego. Cada personaje tendrá un nombre propio, un color de camiseta específico y un color de pantalón específico; estas características son únicas en cada personaje(objeto) para el que creemos una instancia. La instancia es la llamada con la cual creamos un objeto basado en la plantilla que hemos creado con una clase. La sintaxis para esta clase se vería así:

~~~
class Personaje:
	def __init__(self, nombre, color_camiseta, color_pantalón):
		self.nombre = nombre
		self.color_camiseta = camiseta
		self.color_pantalón = pantalón
	def  saludar(self, amigo):
		print(f"Hola, {amigo}")
personaje_uno = Personaje("Libe", "rojo", "verde")
personaje_dos = Personaje("Uxue", "azul", "blanco")
~~~

Si analizamos el ejemplo anterior, vemos que creamos una clase con la clave "class" seguida por el nombre que queramos darle a la clase. Aunque se puede escribir el nombre como queramos, se considera una buena práctica escribirlo en mayúsculas siguiendo el estilo"camel case", es decir, si son varias palabras, se escriben unidas con la primera letra en mayúsculas (ejemplo: OtroPersonaje).

Tras los dos puntos y sangrado escribimos el primer método obligatorio en una clase para su correcto funcionamiento, el `__init__`: este método se considera un método constructor que nos permite definir los atributos que definen la clase y a los que tendrán acceso el resto de métodos, así como las clases de herencia que explicaré más adelante. Al final del ejemplo vemos las instancias que he mencionado (personaje_uno y personaje_dos) las cuales llaman la clase e introducen los atributos específicos de esta instancia. Los atributos mapeados a los argumentos que hemos introducido representarían lo siguiente: nombre => Libe; color_camiseta => rojo; color_pantalón => verde. Para generar el método constructor, seguiremos el siguiente patrón:

~~~
def __init__(self, argumento_uno, argumento_dos):
	self.argumento_uno = argumento_uno
	self.argumento_dos = argumento_dos
~~~

Vemos que el primer argumento de este método es "self"; esto es necesario para que los valores que introduzcamos al crear una instancia se relacionen con los métodos y atributos de la clase así como que los métodos dentro de la clase se relacionen con los atributos del método constructor, es decir, self hace referencia a sí mismo. De este modo, self nos permite acceder a los atributos de la clase. Es importante recordar que "self" no es una palabra clave, podríamos utilizar cualquier otra, pero su uso se considera una buena práctica.

Ya he mencionado los métodos en las clases; estas son funciones como las que ya hemos visto previamente, que se llaman métodos cuando se relacionan con un objeto específico que se da dentro de una clase.

Hemos visto la sintaxis básica y el uso básico de las clases y ahora introduciré el concepto de herencia relacionada con las clases. Las clases base serían aquellas que creamos como base, cuyos atributos y métodos podrán ser heredados por las clases de herencia. A su vez, las clases de herencia podrán modificar los atributos y métodos que han heredado, así como añadir métodos y atributos nuevos y específicos para esa clase. La herencia no se limita a una sola clase, por lo que una clase podrá heredar de varias. La sintaxis es parecida al resto de clases:

~~~
class NuevaClase(Clase, OtraClase):
~~~

Un ejemplo de herencia sería una clase base llamada animales, que englobaría atributos generales compartidos entre los animales y métodos como, por ejemplo, comer o moverse, que se dan en la mayoría de animales. Por su parte, podríamos generar una clase llamada Perro que heredaría de la clase Animales y añadiría el método ladrar. Así aprovecharíamos la clase base y solo tendríamos que generar el código específico en vez de reescribirlo todo para cada clase:

~~~
class Animales:
	def __init__(self, nombre, color):
		self.nombre = nombre
		self.color = color
	def comer(self):
		pass
	def moverse(self):
		pass
class Perro(Animale):
	def ladrar()
~~~

---

## ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

El método que se genera automáticamente cuando creamos una instancia de una clase es el `__init__` que inicia las características de la instancia. Estas características son las que incluiremos como atributo específico del objeto de la instancia al crearla. En el ejemplo anterior, hemos visto cómo los atributos nombre, color_camiseta y color_pantalón se han definido al crear una instancia. Para ello solo hemos tenido que llamar a la clase y el método `__init__` se ha ejecutado automáticamente generando un objeto con las características que le hemos pasado. Ya he expuesto las características, sintaxis y ejemplo de estos métodos en el apartado anterior.

Voy a extender el conocimiento sobre los atributos que creamos con la función `__init__` hablando sobre el acceso a estos datos. En el apartado anterior hemos definido los atributos de la siguiente manera:

~~~
self.atributo = atributo
~~~

Esto significa que estos datos son accesibles desde cualquier parte del programa, pero puede que eso no sea lo que queramos. Para ello, podemos utilizar dos opciones. La primera es colocar una barra baja precediendo al atributo:

~~~
self._atributo = atributo
~~~

Esto indica que queremos que este dato no se exponga o se cambie desde el exterior, desde fuera de la clase, por ejemplo. Esta es una convención que comunica una intención a otros desarrolladores, pero en la práctica el acceso a estos datos sigue siendo público. Si, por el contrario, queremos que no se puedan modifica, python nos permite conseguirlo prefijando dos guiones bajos:

~~~
self.__atributo = atributo
~~~

Debemos tener en cuenta que tendremos que imitar esta sintaxis cada vez que utilicemos este atributo en la clase que estemos construyendo.

Recursos:

<https://codigofacilito.com/articulos/atributos-privados-python>

---

## ¿Cuáles son los tres verbos de API?

Cuando hablamos de verbos de API, nos referimos a los verbos de HTTP que utilizamos para comunicar la intención que tenemos en esa comunicación de la API. Estos verbos definen el tipo de interacción que tendrá un usuario con el servidor. Hay varios verbos, pero estos son los más relevantes:

- GET: Este verbo pide que se devuelva algún dato que se quiera ver; no genera ningún cambio en estos datos.
- POST: Este verbo se utiliza para mandar datos al servidor, crea contenido en el servidor.
- PUT: Este verbo nos sirve para modificar y actualizar datos del servidor.
- DELETE: Este verbo se utiliza para eliminar un documento del servidor.

Hay dos conceptos importantes en relación con estos verbos: la idempotencia y la seguridad. La primera hace referencia al hecho de que las peticiones API que hagamos devuelvan siempre el mismo resultado; por ejemplo, las peticiones tipo GET se consideran idempotentes porque la misma petición GET siempre nos devolverá el mismo resultado. Los verbos PUT y DELET pueden o no ser idempotentes, dependiendo de cómo los apliquemos, pero POST nunca podrá tener esta propiedad. Por otro lado, la seguridad se refiere al hecho de que la petición produzca cambios en el servidor o que no lo haga. Las peticiones GET son seguras porque no generan cambios en el servidor, pero PUT, POST y DELETE siempre generan cambios, por lo que no se consideran seguras, alteran el estado del servidor.

Recursos:

<https://medium.com/@alrazak/understanding-http-verbs-in-rest-api-f6080711d580>

---

## ¿Es MongoDB una base de datos SQL o NoSQL?

Mongo DB es una base de datos NoSQL. La diferencia entre las bases de datos SQL y las NoSQL es la estructura en la que se guardan los datos. Las bases de datos SQL (Structured Query Language) tienen estructuras relacionales, de formato tabular que, aunque tienen ventajas en cuanto a recuperación de información, es poco escalable y ocupa más espacio. Las bases de datos NoSQL pueden tener diferentes tipos de estructuras y permiten una mayor flexibilidad y menor espacio.

Recursos:

<https://www.ibm.com/es-es/think/topics/nosql-databases>

---

## ¿Qué es una API?

Application Programming Interface (API). Una API es una interfaz que permite la comunicación entre diferentes componentes  de software, así se integran. Por ejemplo, permite la comunicación entre una página web y una base de datos. Las API pueden ser públicas, privadas, de aliados comerciales y compuestas; y de ello depende que tengamos libre acceso a su contenido o no; parcial o completa. Hay varios formatos en los que podemos recibir la información por medio de una API, la más popular hoy en JSON (JavaScript Object Notation), este es un lenguaje en forma de objetos de datos clave-valor.

Las API hacen de puente que reciben las peticiones de una web fuente a un destino y recogen la respuesta para devolverla a la web fuente.

Para realizar las llamadas o solicitudes de API, creamos lo que se llaman endpoints con los que proporcionamos una dirección desde la cual se realiza la solicitud.

Recursos:

<https://www.sydle.com/es/blog/api-6214f68876950e47761c40e7>

---

## ¿Qué es Postman?

Postman es un programa que utilizamos para comunicarnos con una base de datos por medio de API. Esta aplicación nos permite crear y probar las API y cerciorarnos de que la comunicación se ha establecido correctamente. Para ello, necesitamos crear los script en los que definimos el comportamiento que queremos que tenga la API; estos son los Endpoint y nos sirven para revisar contenido, añadirlo, eliminarlo, entre otras funciones. Estos Endpoint se basan en los verbos API que ya he mencionado anteriormente.

Postman nos permite realizar y comprobar las peticiones HTTP y nos explicita los errores que se presentan en estas comunicaciones; así podemos crear las API y solucionar posibles errores.

Recursos:

<https://formadoresit.es/que-es-postman-cuales-son-sus-principales-ventajas/>

<https://qalified.com/es/blog/postman-para-api-testing/>

---

## ¿Qué es el polimorfismo?

Desde un punto de vista general, el polimorfismo es la cualidad de que un objeto tome diferentes formas. Un ejemplo general en Python puede ser el hecho de que una misma función funcione con diferentes tipos de datos (listas, tuplas, cadenas, etc.). Si aplicamos el concepto de polimorfismo a las clases, se centra especialmente en el hecho de que un mismo método se puede reutilizar en distintos contextos, compartir entre distintas clases e incluso llamar métodos de distintas clases desde una misma llamada.

El polimorfismo está directamente relacionado con la herencia de las clases y para comprender a qué se refiere voy a presentar un ejemplo:

~~~
class Animal:
	def adivinanza():
		return "Este animal hace así:"
class Perro(Animal):
	def hablar():
		return "uau, uau"
class Pato(Animal):
	def hablar():
		return "cua, cua"
class Gato(Animal):
	def hablar():
		return "miau, miau"
animales = [Perro, Pato, Gato]
for animal in animales:
	print(f"{animal.adivinanza()} {animal.hablar()}")
~~~

El resultado de este  bucle for in es el siguiente:

![Animales](/Animales.png)

Si observamos lo que hemos hecho, vemos que tenemos una superclase llamada animal que contiene el método adivinanza() y devuelve un mensaje. Después tenemos tres métodos que heredan de Animal y tienen cada uno un método llamado hablar; cada uno de estos métodos hablar() devuelve un resultado diferente. Lo interesante de esto es que podemos crear un bucle que itera sobre cada una de las clases Perro, Pato y Gato e imprime el mensaje de la adivinanza junto al método hablar() que corresponde a cada uno. El polimorfismo en este caso es el hecho de poder llamar el método hablar() y que cada vez tome una forma diferente. Esto permite la reutilización de código y la flexibilidad.

Para terminar de hablar del polimorfismo, hay que tener en cuenta que si en el ejemplo anterior hubiese un método hablar() en la clase Animal, se anularía y reemplazaría por el método hablar() de cada una de las clases que heredan de Animal, es decir, el resultado que hemos obtenido no cambiaría.

Recursos:

<https://www.w3schools.com/python/python_polymorphism.asp>

---

## ¿Qué es un método dunder?

Los métodos dunder, también llamados métodos mágicos, son métodos especiales que utilizamos en las clases que están integrados en Python, es decir, no tenemos que crearlos nosotros. La sintaxis de estos métodos se distingue porque su nombre va precedido y seguido por dos barras bajas: `__método__`.

Aunque hay varios métodos dunder, voy a presentar aquí los más relevantes para el nivel en el que nos estamos manejando. El primero que quiero comentar ya lo he explicado antes en esta documentación, y es el método constructor `__init__` que utilizamos para establecer los atributos de una clase y que se ejecuta automáticamente cuando instanciamos una clase.

Un método dunder común es `__str__`. Este método nos devuelve una representación comprensible de una instancia que, de otra forma, devolvería un objeto. Este método hace que podamos tener una idea más comprensible sobre lo que hace un método que hemos definido. Es la representación en forma de cadena del resultado de un método.

Muchos de estos métodos dunder son funciones que permiten convertir tipos de datos: `__int__` equivale a la función `int()`; `__float__` equivale a la función `float()`; etc.

Puedes revisar más métodos dunder en los siguientes enlaces:

<https://www.geeksforgeeks.org/python/dunder-magic-methods-python/>

<https://www.pythonmorsels.com/every-dunder-method/>

---

## ¿Qué es un decorador de Python?

Los decoradores en Python son funciones que añaden funcionalidad a otras funciones sin modificarlas. Esto quiere decir que nos permiten introducir funciones como argumento de otra función, pero con una sintaxis más sencilla. Voy a presentar un ejemplo para ver la sintaxis general de los decoradores y la comparación con la forma de conseguir lo mismo sin el uso de decoradores; esta comparación hace más sencilla la comprensión de este concepto:

~~~
def función_decoradora(función):
	def función_interna():
		acción del decorador
		función()
	return función_interna
@función_decoradora
def función():
	acción de la función
función()
~~~

Vamos a analizar la sintaxis básica de un decorador. Primero tenemos la función decoradora que tomará como argumento otra función (podremos reutilizar el decorador con todas las funciones que queramos). Debemos recordar que en Python todo es un objeto, incluidas las funciones, y esto nos permite tratarlas como argumentos de una función, guardarlas en variables, etc. El siguiente paso es crear la función o funciones internas que guardan las acciones que queremos que se ejecuten cuando utilicemos el decorador; aquí incluimos el argumento que se reemplazará con la función para la que utilizaremos el decorador; devolveremos la función interna. Cuando queramos utilizar el decorador, deberemos añadir el nombre de la función decoradora encabezando la función que quiere decorar antecedida por una arroba (`@función_decoradora`). Una vez hecho esto, llamaremos la función que creemos y el sistema interpretará que debe aplicar la función decoradora a esta nueva función.

Cabe mencionar que podemos aplicar varios decoradores a una función colocándolas unas encima de las otras:

~~~
@decorador_uno
@decorador_dos
def función():
	acción
~~~

Es importante saber que, si queremos introducir argumentos en la función que queremos decorar, debemos haber creado la función decoradora de manera distinta.

~~~
def función_decoradora(función):
	def función_interna(*args):
		acción del decorador
		función(*args)
	return función_interna
@función_decoradora
def función():
	acción de la función
función()
~~~

En este caso vemos que hemos añadido `*args` a la función interna y a la función que entra como argumento. Esto es necesario para que la función pueda tomar argumentos. Recordemos que *args es una convención para decir que podemos introducir una cantidad de argumentos indefinida; el asterisco es lo que realmente lleva a cabo esta acción, pero se considera buenas prácticas utilizar el nombre args.

A continuación voy a presentar un ejemplo de lo que acabo de explicar y su forma sin decorador para poder comprender lo que ocurre de forma más sencilla:

Con decorador:

![Con_decorador](\Con decorador.png)

Sin decorador:

![Sin_decorador](\Sin decorador.png)

En ambos casos, el resultado es el mismo en consola:

![Resultado](\Resultado.png)

Añado enlaces que explican este concepto con diferentes ejemplos:

<https://www.youtube.com/watch?v=U-G-mSd4KAE>

Dentro de los decoradores, hay algunos que utilizamos para manejar los atributos de una clase; estos son los decoradores @property. Estos tipos de decoradores forman parte de Python, es decir, no tenemos que crear el decorador, sino que lo podemos utilizar directamente. Nos permiten llevar a cabo varias acciones como, por ejemplo, actuar de getter (una forma de visualizar los datos en forma de "solo lectura"), también podemos utilizar estos decoradores para cambiar algún valor (actúa como setter) o para eliminar algún valor. Aunque hay otras maneras de conseguir los mismos resultados, hay que tener en cuenta que al programar intentamos comunicar lo que queremos conseguir con cada línea de código, por lo que es importante utilizar las herramientas que nos ayudan a conseguir comunicar nuestras intenciones. Cuando otra persona vea el decorador @property, sabrá que le seguirá una especie de getter, setter o deleter.

Además, he mencionado anteriormente que es posible ocultar o hacer privados ciertos atributos de una clase con la doble barra baja; al crear una función getter con el decorador @property conseguimos que haya un acceso controlado a estos atributos ocultos. Este concepto de acceso a atributos y métodos de una clase se relaciona con el concepto de encapsulamiento, esto es, el proceso de hacer que estos atributos y métodos no sean accesibles desde fuera de la clase. La sintaxis para llevar a cabo estas acciones es la siguiente:

~~~
class Clase:
	def __init__(self, atributo):
		self.atributo = atributo
	@property:
	def atributo(self):
		return self.atributo
~~~

Aquí vemos que hemos creado una clase con un método constructor y un atributo que hemos asignado. Después hemos añadido el decorador @property y una función que devuelve el atributo, es decir, funciona como un getter. El nombre de la función o método puede ser cualquiera, pero se considera una buena práctica llamarlo con el nombre del atributo que queremos ver. Tras crear el getter podemos crear dos funciones más que funcionen como setter y como deleter:

~~~
@property:
def atributo(self):
	return self.atributo

@atributo.setter
def atributo(self, atributo):
	self.atributo = atributo

@atributo.deleter
def atributo(self):
	del self.atributo
~~~

Como vemos he empezado por crear el getter con el decorador property; después, he creado el setter que se llamará con el nombre del atributo + .setter y el método de reasignación; por último, he creado el deleter con el nombre del atributo + .deleter y he definido el método que elimina el atributo asignado.

Recursos:

<https://www.freecodecamp.org/espanol/news/python-decorador-property/>

<https://ellibrodepython.com/decorador-property-python>

<https://ellibrodepython.com/encapsulamiento-poo>

<https://www.freecodecamp.org/news/python-property-decorator/>

<https://ellibrodepython.com/decoradores-python>