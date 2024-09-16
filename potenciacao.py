#alta ordem
def aplica_func_numeros(func, numeros):
    return [func(n) for n in numeros]

#closure
def potenciacao(expoente):
    def aplica_potenciacao(n):
        return n ** expoente
    return aplica_potenciacao

#lambda
eh_impar = lambda x: x % 2 != 0

#list comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = [x for x in numeros if eh_impar(x)]

#closure
eleva_cubo = potenciacao(3)
numeros_elevados = aplica_func_numeros(eleva_cubo, numeros_impares)

#testes
def test_numeros_impares():
    assert numeros_impares == [1, 3, 5, 7, 9], f"Expected [1, 3, 5, 7, 9], got {numeros_impares}"

def test_numeros_elevados_cubo():
    assert numeros_elevados == [1, 27, 125, 343, 729], f"Expected [1, 27, 125, 343, 729], got {numeros_elevados}"

#execução de testes
if __name__ == "__main__":
    test_numeros_impares()
    test_numeros_elevados_cubo()
    print("Todos os testes passaram com sucesso!")
