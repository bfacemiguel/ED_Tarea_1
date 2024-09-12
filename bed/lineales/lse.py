#Adrian Alejandro Guzman Chicaiza
#Miguel Angel Rosero Enrriquez

# print("NAME:", __name__, "PAQUETE:", __package__)
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE
else:
    # from .nodos import Nodo_listaSE
    from bed.lineales.nodos import Nodo_listaSE

class Lista_SE:
    """Clase que implementa el funcionamiento de una lista simplemente enlazada
    """

    # (1) Método Constructor
    def __init__(self):
        """Método que realiza la creación e inicialización de la
        Lista Simplemente Enlazada.
        """
        self.__cab = None        

    # (2) Método es_vacia
    def es_vacia(self):
        """Método que verifica si la lista se encuentra vacía.

        Returns
        -------
        bool
            Retorna True si la lista es vacia. False en caso contrario.
        """
        return self.__cab is None

    # (3.1) Método adicionar al final de la lista
    def adicionar(self, nuevo_dato):
        """ Método que adiciona un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.

        Returns
        -------
        bool
            True cuando el dato es añadido en la lista. False en caso
            contrario.
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            actual  = self.__cab
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo_nodo
        
       
    # (3.2) CONSULTAR: Método posicionar
    def posicionar(self, nuevo_dato, pos=0):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será
        cero. Si la lista ya contiene datos, serán válidas posiciones
        intermedias o la posición inmediatemente superior a la del último dato.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos : int, optional
            Posición a insertar en la lista, por defecto 0.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        estado = False
        i = 0
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        contador = -1
        longitud_lista = len(self)
        if not self.es_vacia():
            actual = self.__cab
            anterior = None
            while actual:
                
                contador += 1
                if contador == pos:
                    if pos != 0 and pos <= (longitud_lista - 1):
                        aux = actual
                        anterior.sig = nuevo_nodo
                        nuevo_nodo.sig = aux
                    else:
                        aux = actual
                        self.__cab = nuevo_nodo 
                        nuevo_nodo.sig = aux 
                    
                    estado = True
                else:
                    anterior = actual
                    actual = actual.sig
        
        if pos == longitud_lista:
            actual = self.__cab
            
            while actual.sig is not None:
                actual = actual.sig
            
            actual.sig = nuevo_nodo
            estado = True
        if self.es_vacia():
            if pos != 0:
                return False
            else:
                self.__cab = nuevo_nodo
                estado = True
        
        return estado

    # (4) Método recorrer una lista
    def recorrer(self):
        """Método que recorre la lista, imprimiendo cada uno de los datos que
        contenga, siempre y cuando no sea una lista vacía.
        """
        nodo_actual = self.__cab
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.sig

    # (5.1) Método econtrar un dato en la lista por dato
    def encontrar(self, dato_buscar):
        """Método que realiza la búsqueda de un dato en la lista.

        Parameters
        ----------
        dato_buscar : object
            Corresponde al valor del dato a ser encontrado en la lista.

        Returns
        -------
        object|None
            object si se encuentra el dato en la lista, None en caso contrario.
        """
        if not self.es_vacia():
            nodo_actual = self.__cab
            while nodo_actual:
                if nodo_actual.dato == dato_buscar:
                    return dato_buscar
                    break
                else:
                    nodo_actual = nodo_actual.sig
                

        return None

    # (5.2) CONSULTA: Método ubicar un dato por posición en la lista
    def ubicar(self, pos):
        """Método que realiza la búsqueda de un dato en la lista dependiendo
        de la posición ingresada.

        Parameters
        ----------
        pos : int
            Corresponde a la posición en la lista a ubicar el dato.

        Returns
        -------
        object|None
            object si el dato es ubicado en la lista, None en caso contrario.
        """
        contador = -1
        if not self.es_vacia() and pos >= 0:
            nodo_actual = self.__cab
            while nodo_actual:
                contador += 1
                if contador == pos:
                    return nodo_actual.dato
                else:
                    nodo_actual = nodo_actual.sig



        return None

    # (6) Método remover por dato (* CONSULTA) o posición
    def remover(self, item, por_pos=True):
        """Método que permite remover un nodo de la lista ya sea por una
        posición o por el dato correspondiente. Si es por dato, deberá
        remover cada uno de los nodos que contenga dicho dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder al valor del dato a ser removido de la lista
            o a la posición en la lista a remover el dato.
            En el caso de remover por dato, se buscará todas las coincidencias
            del dato a eliminar en la lista y serán quitadas.
        por_pos : bool, optional
            Si es True, el método intentará remover un dato por su posición,
            de lo contrario se intentará hacerlo por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista. False en caso
            contrario.
        """
        if por_pos:
            return self.__remover_pos(item)
        else:
            # CONSULTA: remover por dato
            return self.__remover_dato(item)

    # (6.1) Método oculto remover por posición
    def __remover_pos(self, pos_elim):
        contador = -1   
        if not self.es_vacia() and pos_elim >=0:
            actual = self.__cab
            anterior = None
            while actual:
                contador += 1
                if contador == pos_elim:
                    if anterior is None:
                        self.__cab = actual.sig
                        
                    else:
                        anterior.sig = actual.sig
                    return True
                else:
                    
                    anterior = actual
                    actual = actual.sig
        
        return False

    # (6.2) CONSULTAR: Método oculto remover por dato
    def __remover_dato(self, dato_eliminar):
        datos_eliminados = 0
        if not self.es_vacia():
            actual = self.__cab
            anterior = None
            while actual:
                if actual.dato == dato_eliminar:
                    if anterior is None:
                        self.__cab = actual.sig 
                    else:
                        anterior.sig = actual.sig
                    datos_eliminados += 1
                
                
                anterior = actual
                actual = actual.sig
                #debug
            print(f"datos elimindos {datos_eliminados}")
        if datos_eliminados > 0:
            return True
        return False


    # (7) CONSULTA: Método __str__
    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, o una
        cadena vacía en el caso de que la lista sea vacía.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el foramato:
                "(dato_0) :>: (dato_1) :>: (dato_2) :>: ... :>: (dato_n)"
                "(7) :>: (8) :>: (5) :>: (5) :>: (9)"
            de lo contrario retornará una cadena vacía: ""
        """
        cadena = ""
        if not self.es_vacia():
            nodo_actual = self.__cab
            while nodo_actual:
                cadena_aux = f"({nodo_actual.dato}) :>: "
                cadena = cadena + cadena_aux
                nodo_actual = nodo_actual.sig
            cadena = cadena[:-5]
        return cadena

    # (8) CONSULTAR: Sobre-escritura del método __len__
    def __len__(self):
        """Método que calcula el tamaño de la lista.

        Returns
        -------
        int
            El número de nodos que tiene la lista.
        """    
        longitud_lista = 0
        i=0
        if not self.es_vacia():
            nodo_actual = self.__cab
            while nodo_actual:
                longitud_lista +=1
                nodo_actual = nodo_actual.sig
             
        return  longitud_lista
 
    # hacer la lista iterable con un ciclo for
    # en la parte inicial van los nombres de los autores en MAYUS
    #enviar la bilbioteca completa 
if __name__ == "__main__":
    #se crea la lista enlazada
    list_num = Lista_SE()
    #se añaden nodos a la lista 
    #puedes añadir los que quieras para testear las funcionalidades 
    print("---- Lista original ----")
    list_num.adicionar(1)
    list_num.adicionar(2)
    list_num.adicionar(3)
    list_num.adicionar(4)
    list_num.adicionar(9)
    #se recorre la lista enlazada
    list_num.recorrer()
    print("")
    #se verifica la funcionalidad encontrar
    #cambia esto para probarlo como quieras 
    print("1. Encontrar por dato ")
    print(list_num.encontrar(9))
    print("")
    #se verifica la funcionalidad ubicar por pos
    #cambia esto para probarlo como quieras 
    print("2. Ubicar por posición")
    print(list_num.ubicar(5))
    print("")
    #se verifica remover por pos
    #cambia esto para probarlo como quieras 
    print("3. lista con datos eliminados por posición")
    print(list_num.remover(0, True))
    list_num.recorrer()
    print("")
    # se verifica remover por dato (todas las conicidencias)
    #cambia esto para probarlo como quieras 
    print("4. Lista con datos eliminados según dato")
    print(list_num.remover(9, False))
    list_num.recorrer()
    print("")
    #se verifica la correcta sobreescritura de __str__
    print("5. Reescritura del método str")
    print(list_num)
    print("")
    #se verifica la función de posicionar
    #cambia esto para probarlo como quieras 
    print("6. Posicionar")
    list_num.posicionar(5,1)
    list_num.recorrer()
    print("")
    #verificar len
    print("7. Reescritura del método len")
    print(len(list_num))
    
