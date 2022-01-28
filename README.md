# Chocobo's Sanctuary

## Parte 1

Bienvenido al santuario de Chocobo, donde las majestuosas aves pasean libres!

Actualmente tenemos una aplicación llamada Safari, que se encarga del agendamiento de vehículos blindados y equipados con protección anti-ave. El desarrollador encargado de mantenerla se ha "enfermado" indefinidamente luego de un encuentro con una de las aves, por lo que te pedimos que si el proyecto no funciona o contiene malas prácticas intentes arreglarlo por tu cuenta, al menos los endpoints que vas a utilizar. Nos gusta seguir la regla del Boy Scout: "dejo el campamento más limpio que como lo encontré".

### Tu tarea en este proyecto es:

- Clonar el proyecto
- Eliminar los decoradores `@pytest.mark.skip` de los tests
- Desarrollar las funcionalidades para que pase las pruebas ejecutando `docker-compose run --rm test`

### Requirements

- docker
- docker-compose

### Start the project

`docker-compose up`

#### Swagger

http://localhost:8000/api/schema/swagger-ui/


#### Mailhog

http://localhost:1025


## Parte 2

Hemos tenido problemas con nuestros vehículos, ha habido un aumento de casos en los que nuestros usuarios se quedan sin combustible en medio de su recorrido por nuestro parque. La distribución del parque y sus caminos fue hecha por una persona a quien le encantan los árboles de búsqueda binaria, por lo que un mapa se vería de la siguiente forma.
  
![mapa safari](https://i.imgur.com/noULk0A.png)
  
  
Notar que cada nodo puede tener 2 nodos "hijos": el de la izquierda con un valor inferior y el de la derecha con valor superior. Todos los puntos conectados a la izquierda de un nodo son inferiores a éste, y todos los conectados a la derecha son superiores. Básicamente comportándonse como un árbol binario de búsqueda.  
  
Cada punto marcado por una sombrilla y un símbolo de gasolinera es una zona de descanso.  
- Todas las zonas de descanso se identifican por el kilómetro en cual se encuentra.
- Las zonas de descanso tienen estaciones para cargar combustible con precios distintos.
- Los caminos se pueden considerar como líneas rectas para efectos de consumo de combustible.
- Todos los vehículos tienen rendimiento de combustible y tamaño de estanque distintos.
- Hay vehículos que no van a poder completar recorridos sin parar a cargar combustible.
- La implementación de esto se encuentra en el proyecto Safari, app 'adventure'.
  
## Tu tarea:
  
Necesitamos que desarrolles un script o una API separada del proyecto safari, en el lenguaje o framework que prefieras, que cumpla con las siguientes funciones:  
- Obtener la ruta de un punto A a un punto B cualquiera, listando las áreas de servicio por las cual se debería pasar.
- Calcular en qué puntos y cuánto combustible debe uno cargar para que una ruta completa (desde un punto A a un punto B cualquiera) sea lo más barata posible. Considerar lo siguiente
    - La función recibe: punto de inicio, punto de término y patente del vehículo.
    - Debe retornar una lista con los puntos donde parar y cuántos litros cargar.
    - Un viaje puede comenzar y terminar en cualquier punto de descanso, sin devolverse.
    - Todos los vehículos comienzan con el estanque lleno, no es necesario devolverlos llenos.
    - No todos los vehículos tienen el mismo rendimiento ni tamaño de estanque.
    - No todos los vehículos van a tener rendimiento y estanque suficiente como para realizar un recorrido completo sin cargar combustible.
    - No es necesario realizar carga completa del estanque cuando uno pasa por un punto de descanso, se puede cargar lo suficiente como para sólo llegar hasta el siguiente.
    - Todas las áreas de servicio tienen precios de combustible distintos.

# Para conocerte mejor

1. Cuáles crees que son los aspectos más importantes al momento de hacer Code Review
    Mejorar la calidad del código y la comunicación del equipo.
2. Has trabajado con control de versiones? Cuál ha sido el flujo que has utilizado? Por favor explicar.
    Si, mediante el flujo de trabajo de ramas, se crean ramas para cada función o incidencia a partir de la rama principal con el último estado del proyecto, cuando se tiene el código listo se envía a la rama remota (de la función) para realizar el code review y una vez listo, se añade a la rama principal.
3. Cuál ha sido tu experiencia utilizando herramientas fuera de desarrollo del código mismo? (AWS, GCP, VPS, Docker, etc.)
    He utilizado Docker desde hace 6 meses aproximadamente, entiendo el uso de Dockerfile y docker compose.
4. Tienes algún servicio en la nube favorito? Cuál y por qué? No.
5. Has tenido experiencia con microservicios? En caso de que la tengas, podrías explicar por qué en ese caso fue mejor un microservicio que otro tipo de arquitectura? Sí, es mejor por el código reutilizable y la integración continua
