#from List import *

class Heap():
    def __init__(self, size = 0, arreglo = []):
        self.__size = size
        self.__arreglo = arreglo

    def getSize(self):
        return self.__size
    
    def setSize(self, size):
        self.__size = size
    
    def getArreglo(self):
        return self.__arreglo
    
    def setArreglo(self, arreglo):
        self.__arreglo = arreglo
    
    def parent(self, i):
        padrecito = round(i/2) - 1
        if padrecito < 0:
            return 0
        else:
            return padrecito
    
    def hijoIzquierdo(self, i):
        return 2*i + 1
    
    def hijoDerecho(self, i):
        return 2*i + 2
    
    def maxHeapify(self, arreA, i, tamañoHeap):
        if self.__arreglo != None: #Verifico si el arreglo esta vacio.
            arreA = self.__arreglo
            #self.setArreglo(arreglo) Si el arreglo contiene algo lo ingresa como atributo del nuevo objeto.
            self.__size = len(arreA) #Se actualiza el tamaño para que tome el tamaño del arreglo.
            tamañoHeap = self.getSize() #variable que guarda el tamaño del heap.
        else:
            print("El arreglo que diste esta vacio. ")
        l = self.hijoIzquierdo(i) #l va a tomar el indice del hijo izquierdo.
        r = self.hijoDerecho(i) #r va a tomar el indice del hijo derecho.
        print(l)
        #print(r)
        if l <= tamañoHeap and arreA[l]>arreA[i]:          #-----
            mayor = l                                              #|
        else:                                                      #|
            mayor = i                                              #|
        if r <= tamañoHeap and arreA[r]>arreA[mayor]:          #|
            mayor = r                                              #---- Se asegura que el indice con el mayor numero quede en la posicion correcta. 
        if mayor != i:                                             #|
            temp = arreA[i]                                      #|
            arreA[i] = arreA[mayor]                            #|
            arreA[mayor] = temp                                  #|
            self.maxHeapify(arreA, mayor, tamañoHeap)                             #----- 
        return arreA
    
    def buildMaxHeap(self, arreB):
        arreB = self.__arreglo
        for i in range(len(arreB) // 2 - 1, -1, -1): #Arranca desde la mitad del arreglo.
            self.maxHeapify(None, i, len(arreB)) #Usa el método para asegurarse que el el mayor vaya siempre arriba.
        return arreB
    
    def heapSort(self, arreA):
        arreA = self.__arreglo
        #tamañoHeap2 = len(arreA)
        self.buildMaxHeap(arreA)
        for i in range(len(arreA)-1, 0, -1):
            temp = arreA[i]
            arreA[i] = arreA[0]
            arreA[0] = temp
            #self.__size = tamañoHeap2
            self.__size -= 1
            #self.setSize(tamañoHeap2)
            self.maxHeapify(arreA, 0, self.__size)
        return arreA
        

       
h1 = Heap()
arreglito = [1, 2, 3, 4, 5, 6, 7]
h1.setArreglo(arreglito)
#print(h1.maxHeapify(None, 2, None))
#print(h1.buildMaxHeap(arreglito))
print(h1.heapSort(arreglito))
#print(h1.parent(3))
#print(h1.self.__arreglo)
#print(h1.hijoDerecho(1))
    
    
        