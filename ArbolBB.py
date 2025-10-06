import random #libreria para poder hacer libros random
import time #libreria pa poder meterle un segundo de delay

#clase de libro para instanciar libros con sus atributos y sus metodos
class Libro:
    #constructor de librp
    def __init__(self, titulo:str, ISBN:int, genero:str, ndpags:int,retrasodev:bool):
        self.genero = genero
        self.ndpags = ndpags
        self.ISBN = ISBN
        self.titulo = str(ISBN)
        id= titulo
        self.retrasodev = retrasodev

    #como lo dice su nombre metodo que devuelve un libro random
    def generarlibrorandom():
        genero = random.choice(["Ensayo", "Novela", "Poesia"])
        paginas = random.randint(80, 700)
        isbn = random.randint(100000, 999999)
        titulo = str(isbn)
        retraso = random.choice([True, False])
        return Libro(titulo,isbn, genero, paginas, retraso)
    
    #como lo dice su nombre metodo que devuelve un libro , pero a este le introducimos manualmente a id
    def generarlibro(generos):
        genero = random.choice(generos)
        paginas = random.randint(80, 700)
        #comprovacion de que el usuario meta bien las ID
        while True:
            isbn = input("Ingrese el número de ID del libro: ")
            try:
                int(isbn)  # Intentar convertir el input a un número entero
                break
            except ValueError:
              print("Por favor ingrese un número válido\n")
            
        titulo = str(isbn)
        retraso = random.choice([True, False])
        return Libro(titulo,isbn, genero, paginas, retraso)
    
    #como lo dice su nombre metodo que devuelve un libro de el genero concreto que quramos, tambien a este le introducimos manualmente a id
    def generarlibroselecto(genero):
        paginas = random.randint(80, 700)
        isbn = random.randint(100000, 999999)
        titulo = str(isbn)
        retraso = random.choice([True, False])
        return Libro(titulo,isbn, genero, paginas, retraso)

    def getlib(): #metodo que nos da un libro 
        
         generos = ["Ensayo", "Novela", "Poesia"]
         libroprueba = Libro.generarlibro(generos)  
         return libroprueba
    
    def getlibselecto(genero): #metodo que nos da un libro del genero que queramos
         
         libroprueba = Libro.generarlibroselecto(genero)  
         return libroprueba
    
    def getlibrandom(): #metodo que nos da un libro random
          
         libroprueba = Libro.generarlibrorandom()  
         return libroprueba
    
    

class nodo:
    #constructor de nodo
    def __init__(self,libro:Libro):
        self.libro = libro
        self.id = libro.titulo
        self.izq = None
        self.der = None
        self.padre = None 
        self.hijoder= None
        self.hijoizq = None  
   
    #metodo para que nos da si tiene el hijo izquierdo
    def tieneHijoIzquierdo(self):
        return self.hijoizq

    #metodo para que nos da si tiene el hijo derecho
    def tieneHijoDerecho(self):
        return self.hijoder

    #metodo para encontrar el sucesor derecho de un nodo
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoizq == self

    #metodo para encontrar el sucesor izquierdo de un nodo
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoder == self  
    
    #metodo vara ver si es una hoja del arbol
    def esHoja(self):
        return not (self.hijoder or self.hijoizq)
    
    #metodo que encuantra el minimo
    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoizq
        return actual

    #metodo para ver si tiene algun hijo
    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoder.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoder = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoder = self
        return suc

    #metodo para empalmar nodos en caso de borrar uno que tenga hijos
    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoizq = None
            else:
                self.padre.hijoder = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoizq = self.hijoizq
                else:
                    self.padre.hijoder = self.hijoizq
                self.hijoizq.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoizq = self.hijoder
                else:
                    self.padre.hijoder = self.hijoder
                self.hijoder.padre = self.padre
    



#clase de arboles de generos    
class ABB:
    #Constructor de arbol de genero
    def __init__(self,genero:str):
        self.raiz = None
        self.genero = genero
        self.tamano = 0
    
    #metodo para meter los libros en el arbol
    def insertar_libro(self,libro):
        id = libro.titulo
        if self.raiz:
            self._insertar_libro(id,libro,self.raiz)
        else:
            self.raiz = nodo(libro)
        self.tamano = self.tamano + 1

    #metodo para meter los libros en el arbol pero de forma recusiva para que vaya metiendo mas libros a lo largo del arbol
    def _insertar_libro(self,id,libro,nodoActual):
        if id < nodoActual.id:
            if nodoActual.tieneHijoIzquierdo():
               self._insertar_libro(id,libro,nodoActual.hijoizq)
            else:
               nodoActual.hijoizq = nodo(libro)
               nodoActual.hijoizq.padre = nodoActual 
        else:
         if nodoActual.tieneHijoDerecho():
               self._insertar_libro(id,libro,nodoActual.hijoder)
         else:
               nodoActual.hijoder = nodo(libro)
               nodoActual.hijoder.padre = nodoActual 
    
    #metodos para buscar libros en los arboles
    def buscar_libro(self,id):
        if self.raiz:
            encontrado = self._buscar_libro(id,self.raiz)
            if encontrado:
                return encontrado
            else:
                return None
        else:
            return None
    
    def _buscar_libro(self,id,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.id == id:
            return nodoActual
        elif id < nodoActual.id:
            return self._buscar_libro(id,nodoActual.hijoizq)
        else:
            return self._buscar_libro(id,nodoActual.hijoder) 
    
    #metodo para imprimir los libros de un arbol
    def imprimir_libros(self, selecion):
        if self.raiz:
       
            self._imprimir_libros(self.raiz, selecion) 
           
        else:
            print("El arbol esta vacio")
    
    def imprimir_libros(self, selecion):
        
        if self.raiz:

            if selecion == 1:
                print("Imprimir en preorden:")
                self.imprimir_preorden(self.raiz)  #comenzar desde la raíz
            elif selecion == 2:
                print("\nImprimir en inorden:")
                self.imprimir_inorden(self.raiz)  #comenzar desde la raíz
            elif selecion== 3:        
                print("\nImprimir en postorden:")
                self.imprimir_postorden(self.raiz)  #comenzar desde la raíz
            elif selecion == 4:
                print("\nImprimir en anchura:")
                self.imprimir_anchura(self.raiz)  #comenzar desde la raíz
            else:
                print("Opción no válida")
        else:
            print("El árbol está vacío")

    #metodos de impresion de las 4 formas pedidas
    def imprimir_preorden(self, nodo):
        if nodo:
            print(nodo.libro.titulo , end=" ")    #imprimir título del libro
            self.imprimir_preorden(nodo.hijoizq)  #recorrer el subárbol izquierdo
            self.imprimir_preorden(nodo.hijoder)  #recorrer el subárbol derecho

        if self.raiz == None:
            return print("El árbol está vacío")   #comprueba que si hay raiz para que no pete

    def imprimir_inorden(self, nodo):
        if nodo:
            self.imprimir_inorden(nodo.hijoizq)  #recorrer el subárbol izquierdo
            print(nodo.libro.titulo , end=" ")   #imprimir título del libro
            self.imprimir_inorden(nodo.hijoder)  #recorrer el subárbol derecho
        
        if self.raiz == None:
            return print("El árbol está vacío")  #comprueba que si hay raiz para que no pete

    def imprimir_postorden(self, nodo):
        if nodo:
            self.imprimir_postorden(nodo.hijoizq)  #recorrer el subárbol izquierdo
            self.imprimir_postorden(nodo.hijoder)  #recorrer el subárbol derecho
            print(nodo.libro.titulo , end=" ")     #imprimir título del libro

        if self.raiz == None:
            return print("El árbol está vacío")    #comprueba que si hay raiz para que no pete


    def imprimir_anchura (self, nodo):
        if self.raiz is None:
            return print("El árbol está vacío")    #comprueba que si hay raiz para que no pete
        
        cola = [self.raiz]  #creamos una cola con la raíz
        while len(cola) > 0:
            nodo = cola.pop(0)  #extraer el primer nodo de la cola             
            print(nodo.libro.titulo , end=" ")  #imprimir título del libro
            if nodo.hijoizq is not None:
                cola.append(nodo.hijoizq)  #agregar el hijo izquierdo a la cola
            if nodo.hijoder is not None:
                cola.append(nodo.hijoder)  #agregar el hijo derecho a la cola


    #metodo de eliminar libros

    def eliminar(self, id):
         
        if self.raiz is None:
           return print("el arbol esta vacio")

        #busca nodo con el ID en el árbol.
        nodoAEliminar = self.buscar_libro(id)
        if  nodoAEliminar is None:
           return print("Error, la ID no está en el árbol")
        
        #verificar si el nodo a eliminar es la raíz
        if self.raiz.id == id:
            if self.raiz.esHoja():
                self.raiz = None
            elif self.raiz.tieneHijoIzquierdo():
                self.raiz.hijoizq.padre = None
                self.raiz = self.raiz.hijoizq
            elif self.raiz.tieneHijoDerecho():
                self.raiz.hijoder.padre = None
                self.raiz = self.raiz.hijoder
            return print("Se ha eliminado el libro:", id)

        #elimina si el nodo es una hoja
        if nodoAEliminar.esHoja():
            if nodoAEliminar.esHijoIzquierdo():
                nodoAEliminar.padre.hijoizq = None
                return print("Se ha eliminado el libro :" + nodoAEliminar.id)
            else:
                nodoAEliminar.padre.hijoder = None
                return print("Se ha eliminado el libro :" + nodoAEliminar.id)

        #elimina si el nodo tiene un solo hijo
        if nodoAEliminar.tieneHijoIzquierdo():
            hijo = nodoAEliminar.hijoizq
        else:
            hijo = nodoAEliminar.hijoder
        if nodoAEliminar.esHijoIzquierdo():
            nodoAEliminar.padre.hijoizq = hijo
        else:
            nodoAEliminar.padre.hijoder = hijo
        if hijo is not None:
            hijo.padre = nodoAEliminar.padre
            return print("Se ha eliminado el libro :" + nodoAEliminar.id)

        
        #elimina si el nodo tiene ambos hijos
        else:
            sucesor = nodoAEliminar.encontrarSucesor()
            sucesor.empalmar()
            nodoAEliminar.id = sucesor.id
            nodoAEliminar.libro = sucesor.libro
            self.tamano -= 1
            return print("Se ha eliminado el libro :" + nodoAEliminar.id)

    
    #metodos para selecionar un libro random de dentro de los arboles
    def obtener_libro_aleatorio(self):
        if self.raiz:
            return self._obtener_libro_aleatorio(self.raiz)
        else:
            return None

    def _obtener_libro_aleatorio(self, nodo_actual):
       
        if not nodo_actual:
            return None  # Si no hay nodo actual, devuelve None
        # Si el nodo actual es una hoja, devuelve el libro contenido en ese nodo
        if nodo_actual.esHoja():
            return nodo_actual.libro
        
        # Genera un número aleatorio entre 0 y 2 para elegir aleatoriamente entre el nodo actual,
        # el hijo izquierdo y el hijo derecho.
        eleccion = random.randint(0, 2)
        if eleccion == 0:
            return nodo_actual.libro
        elif eleccion == 1:
            libro_izquierdo = self._obtener_libro_aleatorio(nodo_actual.hijoizq)
            if libro_izquierdo:
                return libro_izquierdo
            else:
                return self._obtener_libro_aleatorio(nodo_actual.hijoder)  # Busca en el hijo derecho si no encuentra en el izquierdo
        else:
            libro_derecho = self._obtener_libro_aleatorio(nodo_actual.hijoder)
            if libro_derecho:
                return libro_derecho
            else:
                return self._obtener_libro_aleatorio(nodo_actual.hijoizq)  # Busca en el hijo izquierdo si no encuentra en el derecho
 
        
        
         
        

class Mismetodos:
    
     def printmenu():
        print("Selecione una opcion de menu:\n")
        print("1 Insertar un libro en un ABB: 1,2,3")
        print("2 Buscar cualquier libro en un ABB: 1, 2, 3")
        print("3 Imprimir lista de libros en cualquier ABB ")
        #dependiendo si anchura, profundidad (PRE, IN, POST ORDEN)
        print("4 Borrar un libro de un arbol de genero")
        #cuyo identificador haya sido introducido por teclado , si existe en el correspondiente ABB.
        print("5 Introducir un número y crear dicha cantidad de libros al azar de un género")
        #guardándolos en el correspondiente ABB: 1,2,3
        print("6.Introducir un número y generar al azar dicha cantidad de libros")
        #que se borrarán, si existen, en los correspondientes ABB.
        print("7 Iniciar simulacion")
        print("8 Salir de la aplicacion\n")

     #segun el genero del libro nos devuelve una cosa o otra y con eso ya nos lo podemos guardar donde queramos
     def comprovador(libro:Libro): 
         
        if(libro.genero == "Poesia"):
            print("El libro es de poesia")
            return "P"
        elif(libro.genero == "Ensayo"):
            print("El libro es de ensayo")
            return "E"
        elif(libro.genero == "Novela"):
            print("El libro es de novela")
            return "N"

     #metodo para pedir la decision al usuario para saber que quiere del menu y comprbar que no meta datos mal   
     def pedirdecision(): 
        try:

            decision =  int (input("Ingrese el número de la opción que desea seleccionar: "))
            print("Usted ha elegido la opcion " , decision ,"\n")
            return decision
        except ValueError:
            print("Por favor ingrese un número valido\n")
            return Mismetodos.pedirdecision()    

def main():

    
    #instanciamos los arboles de generos 
    arbolpoe = ABB("Poesia")
    arbolensa = ABB("Ensayo")
    arbolnovela = ABB("Novela")

    #menu principal que se ejecuta en bucle
    while True:
      Mismetodos.printmenu()
      decision = Mismetodos.pedirdecision()

      #verificacion de que el usuario no meta cosas que no tocan
      if decision <= 8 :


        if (decision == 1):
            print("Usted ha seleccionado la opcion 1\n")
            #generamos el libro y lo insertamos donde toca
            libroaux = Libro.getlib()
            gen= Mismetodos.comprovador(libroaux)
            if(gen== "P"):
             arbolpoe.insertar_libro(libroaux)
            elif(gen== "E"):
             arbolensa.insertar_libro(libroaux)
            elif(gen== "N"):
             arbolnovela.insertar_libro(libroaux)
            

        elif(decision==2):
            print("Usted ha seleccionado la opcion 2\n")
            print("Que libro quiere busca")
            id = (input("Ingrese el número de ID del libro: "))
            genero =  int (input("En que genero quiere buscar el libro 1 Ensayo, 2 Novela, 3 Poesia: \n"))
            if(genero == 1):
                lib = arbolensa.buscar_libro(id)
                if lib is None:
                    print("\nNo esta el libro en el arbol") 
                elif lib is not None:
                    print("\nSi esta el libro en el arbol")   

            elif(genero == 2):

                lib = arbolnovela.buscar_libro(id)
                if lib is  None:
                    print("\nNo esta el libro en el arbol") 
                elif lib is not None:
                    print("\nSi esta el libro en el arbol")   

            elif(genero == 3):
                lib = arbolpoe.buscar_libro(id) 
                if lib is None:
                    print("\nNo esta el libro en el arbol") 
                elif lib is not None:
                    print("\nSi esta el libro en el arbol")               
                
        elif(decision==3):
            print("Usted ha seleccionado la opcion 3\n")

            selecion = int(input("De due manera quiere imprimir los arboles de genero 1 Preorden, 2 Inorden, 3 Postorden, 4 anchura: "))

            print("\nLibros de poesia")
            arbolpoe.imprimir_libros(selecion)
            print("\n")

            print("\nLibros de ensayo")
            arbolensa.imprimir_libros(selecion)
            print("\n")

            print("\nLibros de novela")
            arbolnovela.imprimir_libros(selecion)
            print("\n")

        elif(decision==4):
        #borrar libros por su identificador en el arbol
            print("Usted ha seleccionado la opcion 4\n")
            id = (input("Ingrese el número de ID del libro a borrar del arbol: \n"))
            genero =  int (input("En que genero quiere buscar el libro 1 Ensayo, 2 Novela, 3 Poesia: \n"))
            if(genero == 1):
                arbolensa.eliminar(id)
            elif(genero == 2):
                arbolnovela.eliminar(id)
            elif(genero == 3):
                arbolpoe.eliminar(id)

        elif(decision==5):
            print("Usted ha seleccionado la opcion 5\n")
            cant = int(input("Ingrese la cantidad de libros que quiere generar: "))
            generoaux =  int (input("En que genero quiere buscar el libro 1 Ensayo, 2 Novela, 3 Poesia: \n"))
            if(generoaux == 1):
                genaux = "Ensayo"
                for i in range(cant):
                    libroaux = Libro.getlibselecto(genaux)
                    arbolensa.insertar_libro(libroaux)
            elif(generoaux == 2):
                genaux = "Novela"
                for i in range(cant):
                    libroaux = Libro.getlibselecto(genaux)
                    arbolnovela.insertar_libro(libroaux)
            elif(generoaux == 3):
                genaux = "Poesia"
                for i in range(cant):
                    libroaux = Libro.getlibselecto(genaux)
                    arbolpoe.insertar_libro(libroaux)
        
        elif decision == 6:
            print("Usted ha seleccionado la opción 6\n")
            cant = int(input("Ingrese la cantidad de libros que quiere generar: "))
            generoaux2 = int(input("En qué género quiere buscar el libro 1 Ensayo, 2 Novela, 3 Poesía: \n"))
            
            contadorlib = 0

            for i in range(cant):

                if generoaux2 == 1:
                 libro = Libro.generarlibrorandom()
                # Verificar y eliminar el libro si ya existe en el árbol correspondiente
                 if arbolensa.buscar_libro(libro.titulo):
                         contadorlib += 1
                         arbolensa.eliminar(libro.titulo)
                

                elif generoaux2 == 2:
                 libro = Libro.generarlibrorandom()
                 if arbolnovela.buscar_libro(libro.titulo):
                    contadorlib += 1
                    arbolnovela.eliminar(libro.titulo)
                

                elif generoaux2 == 3:
                 libro = Libro.generarlibrorandom()
                 if arbolpoe.buscar_libro(libro.titulo):
                    contadorlib += 1
                    arbolpoe.eliminar(libro.titulo)
                
            contadorstr = str(contadorlib)
            print("\nSe han elimininado: "+ contadorstr +"\n")   

        elif (decision == 7):
            #simulacion
            print("Usted ha seleccionado la opcion 7\n") 

            print("SIMULACION INICIADA\n") 
            tiempoini = 0
            
            


            while tiempoini != 60:
                
                if tiempoini % 5 == 0 and tiempoini != 0 :
                    #generamos un libro y lo guardamos donde toca 
                    libroaux = Libro.getlibrandom()
                    gen= Mismetodos.comprovador(libroaux)
                    if(gen== "P"):
                        arbolpoe.insertar_libro(libroaux)
                        print("EVENTO: Se ha introducido el libro "+ libroaux.titulo + " de el genero de "+ libroaux.genero)
                    elif(gen== "E"):
                        arbolensa.insertar_libro(libroaux)
                        print("EVENTO: Se ha introducido el libro "+ libroaux.titulo + " de el genero de "+ libroaux.genero)
                    elif(gen== "N"):
                        arbolnovela.insertar_libro(libroaux)
                        print("EVENTO: Se ha introducido el libro "+ libroaux.titulo + " de el genero de "+ libroaux.genero)

                    #imprimimos tods los libros de los arboles
                    print("\nLibros de poesia")
                    arbolpoe.imprimir_libros(2)
                    print("\n")

                    print("\nLibros de ensayo")
                    arbolensa.imprimir_libros(2)
                    print("\n")

                    print("\nLibros de novela")
                    arbolnovela.imprimir_libros(2)
                    print("\n")        
                    
                    #generamos un libro random y lo eliminamos de un arbol si tiene retraso
                    genrandom = random.randint(1,3)
                    if genrandom == 1:
                        libselect = arbolpoe.obtener_libro_aleatorio()
                    elif genrandom == 2:
                        libselect = arbolensa.obtener_libro_aleatorio()
                    elif genrandom == 3:
                        libselect = arbolnovela.obtener_libro_aleatorio()
                    
                    while libselect is None:
                     #generamos un libro random y lo eliminamos de un arbol si tiene retraso
                     genrandom = random.randint(1,3)
                     if genrandom == 1:
                        libselect = arbolpoe.obtener_libro_aleatorio()
                     elif genrandom == 2:
                        libselect = arbolensa.obtener_libro_aleatorio()
                     elif genrandom == 3:
                        libselect = arbolnovela.obtener_libro_aleatorio()
                    
                    
                    
                    if libselect is not None:

                        if libselect.retrasodev == True:
                            print("El libro con el ID: " + libselect.titulo + " esta en retraso")
                            genselcto= Mismetodos.comprovador(libselect)
                            if(genselcto== "P"):
                                arbolpoe.eliminar(libselect.titulo)
                                print("EVENTO: Se ha elimininado el libro "+ libselect.titulo + " de el genero de "+ libselect.genero+"\n")
                            elif(genselcto== "E"):
                                arbolensa.eliminar(libselect.titulo)
                                print("EVENTO: Se ha elimininado el libro "+ libselect.titulo + " de el genero de "+ libselect.genero+"\n")
                            elif(genselcto== "N"):
                                arbolnovela.eliminar(libselect.titulo)
                                print("EVENTO: Se ha elimininado el libro "+ libselect.titulo + " de el genero de "+ libselect.genero+"\n")

                time.sleep(1)#le metemos delay de 1 s 
                tiempoini += 1 #añadimos 1 s al contador
                print("Tiempo: " + str(tiempoini) + " segundos") #printea lso segundos de la simulacion
        elif(decision== 8):
            print("Gracias por usar la aplicacion")
            SystemExit
            break
      else:
            print("Por favor ingrese un número valido\n")
            Mismetodos.printmenu()
            decision = Mismetodos.pedirdecision()
            continue

if __name__ == '__main__':
    main()