class Node:
    def __init__(self):
        self.value = 0
        self.next = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def insert(self , lista , value):
        novo = Node()
        novo.value = value
        novo.next = None

        if lista.inicio == None:
            lista.inicio = novo

        else:
            lista.fim.next = novo

        lista.fim = novo

    def remove(self , lista):
        aux = Node()
        aux = lista.inicio

        if lista.inicio == None:
            return

        if lista.inicio.next == None:
            lista.inicio = None
            lista.fim = None

        else:
            while aux != None:
                if aux.next.next == None:
                    aux.next = None
                    lista.fim = aux

                aux = aux.next

    def print_lista(self , lista):
        count = Node()
        count = lista.inicio
        while count != None:
            print(count.value)
            count = count.next

        print()
 
