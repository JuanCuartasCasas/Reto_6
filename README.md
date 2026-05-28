# Reto 6: Uso de Excepciones 
> El presente repositorio lleva a cabo una aplicación de las excepciones en python a partir de los ejericios anteriormente designados

Se busca solucionar: 

- Add the required exceptions in the Reto 1 code assigments.
- In the package Shape identify at least three cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

-----
A partir de lo requerido, nos basamos en el [Reto 1](https://github.com/JuanCuartasCasas/Reto_1.git) y el [Reto 5](https://github.com/JuanCuartasCasas/Reto_5.git) para analizar el uso de excepciones en cada caso

## Excepciones Reto 1:

En la situación del reto 1 las excepciones más usadas son la validación de valores: además se creó una Excepción especial en el caso de calculadora,
pues escreo una clase  ```OperaciónNovalida(Exception):``` que almacena el error de seleccionar una operación en la calculadora inesperada.

## Excepciones Reto 2:

Al analizar el paquete *Shape* observamos Errores inseperados en el calculo de los componentes de cada forma, por lo que se genero una 
nueva clase llamada ```InvalidShapeError(Exception)``` que ofrece una señal semántica de que los problemas surgen de los compoenentes de la clase,
en lugar de propagar excepciones genéricas

# Referencias 
- [clase 12: Excepciones](https://github.com/fegonzalez7/poo_unal_clase12.git)
