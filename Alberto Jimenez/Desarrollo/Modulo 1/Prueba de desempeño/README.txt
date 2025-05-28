(El archivo con el nombre completo viene con 5 productos añadidos por mi predeterminadamente y el archivo con el titulo en siglas, cuenta con la logica de añadir los 5 primeros articulos por parte del usuario al momento de ejecutarlo)
Sistema de gestion de inventario

El programa se ejecuta en consola y despliega un mensaje de bienvenida junto a un menú con 6 opciones al que el usuario puede acceder digitando su numero correspondiente, el programa solo acepta numeros del 1 al 6 y muestra error si el usuario no digita una de las opciones validas

Ejemplo:

    1. Añadir productos al inventario.
    2. Consultar productos del inventario.
    3. Actualizar productos del inventario.
    4. Eliminar productos del inventario.
    5. Calcular valor total de los productos del inventario.
    6. Salir.

    Entrada: (Numero de cualquiera de las seis opciones) Se ejecuta el bloque de codigo correspondiente.
    Entrada: (Cualquier numero que no sea una de las opciones) Mensaje de error y se vuelve a pedir un valor valido.
    Entrada: (Cualquier caracter que no sea un numero) Mensaje de error y se vuelve a pedir un valor valido.

1. Añadir productos al inventario
En el primer apartado se registran los productos que se guardaran en el inventario, se le pide al usuario el nombre y se valida si el producto no fue registrado anteriormente, posteriormente el precio y la cantidad de productos y todo eso se guarda en un diccionario llamado "inventory". En el precio y la cantidad de productos no se aceptaran valores negativos o iguales a 0 en caso de la cantidad, y se pueden registrar productos indefinidamente hasta que el usuario salga del apartado digitando "0" como nombre del producto, y esta logica se repite en cada uno de los puntos que requieren un input del usuario.

Ejemplo:

    Ingrese nombre del producto (0 para volver al menú)

    Entrada: (Producto sin registrar) El nombre se almacena en una variable y se sigue con el siguiente paso.
    Entrada: (Producto ya registrado) Se le notifica al usuario que el producto que intenta registrar ya ha sido registrado anteriormente y se le pide nuevamente la informacion.
    Entrada: "0" Se vuelve a desplegar el menú y da la posibilidad de realizar cualquier otra accion.


    Ingrese precio del producto

    Entrada: (Cualquier numero positivo) Se almacena en una variable y se sigue con el siguiente paso.
    Entrada: (Cualquier numero negativo) Se valida, se le notifica al usuario que no puede haber un numero negativo como precio y se le pide la informacion nuevamente.
    Entrada: (Cualquier caracter que no sea un numero) Se le notifica al usuario que no se puede registrar algo que no es un numero como un precio y se le pide nuevamente la informacion.


    Ingrese cantidad del producto

    Entrada: (Cualquier numero positivo) Se almacena en una variable y se sigue con el siguiente paso.
    Entrada: (Cualquier numero negativo o igual a 0) Se valida, se le notifica al usuario que la cantidad no puede ser igual o menor a 0 y se le pide la informacion nuevamente.
    Entrada: (Cualquier caracter que no sea un numero) Se le notifica al usuario que no se puede registrar un caracter que no es un numero como un cantidad y se le pide nuevamente la informacion.

2. Consultar productos del inventario
En el apartado de consultar productos se valida que el inventario no esté vacio y le despliega al usuario una lista con los nombres de los productos ya registrados, posteriormente, se le pide al usuario que digite el nombre de uno de los productos para que asi se le muestren los detalles del susodicho.

Ejemplo:

    Ingrese el nombre del producto a consultar (0 para volver al menú)

    Entrada: (Producto ya registrado) Se le despliega al usuario los detalles del producto, estos siendo el precio y la cantidad.
    Entrada: (Producto sin registrar) Se le notifica al usuario que el producto que intenta consultar no existe en el inventario y se le pide nuevamente un nombre para consultar.
    Entrada: "0" Se vuelve a desplegar el menú y da la posibilidad de realizar cualquier otra accion.

3. Actualizar productos del inventario
En el tercer apartado, primero se valida que el inventario no se encuentre vacio, posteriormente, se le despliega al usuario una lista con los productos que ya han sido registrados para que el usuario seleccione que producto desea actalizar digitando su nombre, entonces se le pide un nuevo precio y una nueva cantidad que asignar al producto seleccionado para asi actualizarlo en el inventario.

Ejemplo:

    Ingrese el nombre del producto a actualizar (0 para volver al menú)

    Entrada: (Producto de de la lista) Se almacena en una variable para la actualizacion y se sigue con el siguiente paso.
    Entrada: (Producto sin registrar) Se le notifica al usuario que el producto que intenta actualizar no existe en el inventario y se le pide nuevamente un nombre para actualizar.
    Entrada: "0" Se vuelve a desplegar el menú y da la posibilidad de realizar cualquier otra accion.


    Ingrese el nuevo precio del producto
    
    Entrada: (Cualquier numero positivo) Se almacena en una variable y se sigue con el siguiente paso.
    Entrada: (Cualquier numero negativo) Se valida, se le notifica al usuario que no puede haber un numero negativo como precio y se le pide la informacion nuevamente.
    Entrada: (Cualquier caracter que no sea un numero) Se le notifica al usuario que no se puede registrar un caracter que no es un numero como un precio y se le pide nuevamente la informacion.


    Ingrese la nueva cantidad del producto
    
    Entrada: (Cualquier numero positivo) Se almacena en una variable y se sigue con el siguiente paso.
    Entrada: (Cualquier numero negativo o igual a 0) Se valida, se le notifica al usuario que la cantidad no puede ser igual o menor a 0 y se le pide la informacion nuevamente.
    Entrada: (Cualquier caracter que no sea un numero) Se le notifica al usuario que no se puede registrar un caracter que no es un numero como un cantidad y se le pide nuevamente la informacion.

4. Eliminar productos del inventario
En este apartado se despliega una lista con los productos que ya han sido registrados y se le pide al usuario el nombre de un producto existente para poder eliminarlo del inventario siempre y cuando el inventario no esté vacio, en este caso, se le notificara de ello al usuario y el bloque no se ejecutará.

Ejemplo:

    Ingrese el producto que desea eliminar (0 para volver al menú)

    Entrada: (Producto de la lista) Se le notifica al usuario que el producto que seleccionó se eliminó y ya no se encuentra en el inventario.
    Entrada: (Producto sin registrar) Se le notifica al usuario que el producto que intenta eliminar no existe en el inventario y se le pide nuevamente un nombre para eliminar.
    Entrada: "0" Se vuelve a desplegar el menú y da la posibilidad de realizar cualquier otra accion.

5. Calcular valor total de los productos del inventario
El ultimo apartado del programa se ejecuta automaticamente cuando el usuario selecciona la opcion correspondiente. Se hace un calculo de todos los productos registrados en el inventario y se le imprime el total de manera sencilla.

6. Salir
El usuario cierra el programa al seleccionar la opcion correspondiente.