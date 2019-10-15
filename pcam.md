# Modelo PCAM

## Por:

 * Sergio Andres Muñoz Rojas
 * Juan Felipe Rojas Martinez
 * Santiago Baena Rivera

# Problema

 * En el mercado de acciones se deben tener en cuenta muchos factores para dar con una
 buena inversión, así que decidimos que tomaríamos una base de datos con los indicadores
 mas relevantes para este mercado, así como lo son los precios de apertura y cierre,
 los valores mas altos y bajos que se registraron en ese día para una acción y el volumen
  de éstas mismas que es la cantidad de acciones que están siendo comercializadas, con todos
  estos indicadores, podemos sacar valores que pueden ser determinantes para realizar un
  movimiento o no tales como: el promedio en el crecimiento o el decrecimiento de una acción
  a lo largo de los años.


# Partición

 * Como de entrada teníamos muchos datos, necesitamos primero, disminuir esa cantidad,
 luego de elegir una lista de datos mas reducida pasamos al siguiente tema, descomponer
 el proceso en pedazos de interés de tal forma que solo queden la fecha y el indicador
 que se desea, para luego, procesar y posteriormente proceder con la computación que queremos realizar.

# Comunicación

* Todas las tareas vienen dadas por indicadores que se deben calcular, y por esto todas deben de tener la misma cantidad de operaciones, porque, los indicadores se dan para una cantidad de fechas y si no se tienen los mismos datos los estos no seran congruentes entre si, donde se utiliza un modelo de comunicación global donde estas llamadas se pueden realizar en concurencia porque se toman los datos, pero no se modifican, lo que hace que no existan las condiciones de carrera.

# Aglomeración

* En la aglomeración se pueden tomar varios datos que se pueden estar recalculando en la ejecución del algoritmo(tales como el promedio anual o total de cualquier columna) y llevarlo a otro indicador para ahorrar tiempo de procesamiento.

# Mapeo

* Para este proyecto se podría decir que estamos implementando una bisección recursiva, solo que en vez de separar tareas dentro de un mismo algoritmo, estamos dividiendo el proyecto en subtareas que son realizadas por programas independientes uno del otro con un costo computacional similar.
