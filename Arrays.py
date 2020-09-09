class SuperArray():
    def __init__(self, tamanho_max: int):
        self.__array = []
        self.__tamanho_max = tamanho_max
        self.__tipo_array = None


    def inserir_elemento(self, elemento):
        if len(self.__array) < self.__tamanho_max:
            if self.__array == []:
                self.__array.append(elemento)
                self.__tipo_array = type(elemento)
            else:
                if type(elemento) != self.__tipo_array:
                    raise Exception("Elemento é de tipo diferente")
                else:
                    self.__array.append(elemento)
        else:
            raise Exception("Array cheio")
    
    
    def inserir_elemento_posicionado(self, elemento, indice: int):
        if len(self.__array) < self.__tamanho_max:
            if self.__array == []:
                self.__array.insert(indice, elemento)
                self.__tipo_array = type(elemento)
            else:
                if type(elemento) != self.__tipo_array:
                    raise Exception("Elemento é de tipo diferente")
                else:
                    self.__array.insert(indice, elemento)
        else:
            raise Exception("Array cheio")


    def remover_elemento(self, elemento):
        if elemento in self.__array:
            self.__array.remove(elemento)
        else:
            raise Exception("Elemento não encontrado")


    def consulta_indice(self, indice: int):
        if indice <= len(self.__array):
            return self.__array[indice]
        else:
            raise Exception("Indice não encontrado")


    def consulta_elemento(self, elemento):
        if elemento in self.__array:
            return elemento
        else:
            raise Exception("Elemento não encontrado")


    def retorna_elementos(self):
        for elemento in self.__array:
            print(elemento)

    
    def lista_vazia(self):
        return len(self.__array) == 0