# -*- coding: utf-8 -*-
import collections

# Cargar reglas desde un archivo
def cargar_reglas(archivo):
    condiciones = []
    resultados = []
    with open(archivo, encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas:
            # Eliminar el salto de línea
            linea = linea.strip('\n')
            if linea:
                datos = linea.split(' ')
                condiciones.append(datos[:-1])
                resultados.append(datos[-1])
    return condiciones, resultados

# Ordenamiento topológico
def ordenamiento_topologico(condiciones, resultados):
    regla = collections.OrderedDict()
    ind_list = []
    for i in condiciones:
        suma = 0
        for x in i:
            if resultados.count(x) > 0:
                suma += resultados.count(x)
        ind_list.append(suma)

    while (1):
        if ind_list.count(-1) == len(ind_list):
            break

        for i, ind in enumerate(ind_list):
            if ind == 0:
                regla[tuple(condiciones[i])] = resultados[i]
                ind_list[i] = -1
                for j, cond in enumerate(condiciones):
                    if resultados[i] in cond:
                        ind_list[j] -= 1
    return regla

# Inferencia
def inferir(entrada, regla, mostrar=False):
    resultado = []
    flag = False
    proceso = ''
    for key in regla.keys():
        if lista_en_conjunto(key, entrada):
            entrada.append(regla[key])
            resultado.append(regla[key])
            proceso += '{key} infiere {value}\n'.format(key=key, value=entrada[-1])
            flag = True

    if flag:
        if mostrar:
            return proceso + '\n' + 'Resultado final: ' + str(resultado[-1])
        else:
            return 'Resultado final: ' + str(resultado[-1])
    else:
        return 'No se puede inferir'

def lista_en_conjunto(lista, conjunto):
    for i in lista:
        if i not in conjunto:
            return False
    return True

def ejecutar(texto, mostrar):
    if mostrar == 'true':
        dis = True
    else:
        dis = False
    entrada = texto.split(' ')
    condiciones, resultados = cargar_reglas('data.txt')
    regla = ordenamiento_topologico(condiciones, resultados)
    return inferir(entrada, regla, mostrar=dis)

if __name__ == '__main__':
    print('Cada característica debe estar separada por un solo espacio. Utilice el nombre completo de cada característica.')
    print('Por ejemplo: Ave->Clase de ave, Blanco y negro->Negro y blanco')
    print('Ingrese 1 para salir')
    while (1):
        print('Ingrese las características:')
        texto = input()
        if texto == '1':
            break
        print(ejecutar(texto, mostrar='true'))
