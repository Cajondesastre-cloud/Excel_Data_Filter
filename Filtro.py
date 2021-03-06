# -*- coding: utf-8 -*
# Programa para el tratamiento de datos del catastro.
# Se le deberan de introducir los datos de los archivos del catastro en
# un archivo excel: building, building_part o similares.

# Elaborado por David Montiel López.
# e-mail: davidmontlop@gmail.com

import numpy as np
import pandas as pd
import argparse

#############################################################################
#########################  Funciones principales ############################
#############################################################################

# Se puede realizar el filtrado de datos en funcion de subconjuntos de
# encabezados de columnas. Se recomienda referencia catastral y value
# o superficie del edificio, para evitar duplicidades que puedan afectar
# al recuento final. Estos filtros se usan cuando se han
# cruzado datos entre los dos archivos mencionados en el encabezado.

def filtro(lista_args, file):
    filt = file.drop_duplicates(subset=lista_args, keep="first")
    return filt

# Tambien es posible extraer datos en funcion del tipo de suelo,
# numero de plantas, numero de edicios, numero de viviendas, etc.

def calc(lista_args, file):
    nombres = []
    valores = []
    df = file
    for i in range(len(lista_args)):
        if i%2 == 0:
            nombres.append(lista_args[i])
        else:
            try:
                valores.append(float(lista_args[i]))
            except:
                valores.append(lista_args[i])
    for i in range(len(nombres)):
        df_mask = df[nombres[i]] == valores[i]
        filt_aux = file[df_mask]
        file = filt_aux
    return filt_aux


# Una vez se ha filtrado por tipologi­a de construccion, se puede proceder a
# realizar la estadi­stica que se crea oportuna.

def stats(lista_args, file):
    for i in lista_args:
        file.describe(i).to_excel(i + "_description.xlsx")
    
# Alternativamente, es posible realizar otra serie de calculos, como por ejemplo,
# de tipologi­a constructiva en funcion del año de construccion, el numero
# de plantas, etc.

def tipo_constr(file, tipo, nombre):
    
    df = file
    df.columns
    name_list = df.columns.tolist()
    index_list = []
    for i in range(len(name_list)):
        if name_list[i].lower() == "año" or name_list[i].lower() == "year":
            index_list.append(i)
    for i in range(len(name_list)):
        if name_list[i].lower() == "value" or name_list[i].lower() == "superficie":
            index_list.append(i)
    for i in range(len(name_list)):
        if name_list[i].lower() == "plantas" or name_list[i].lower() == "floor":
            index_list.append(i)
            
    w_file = df.iloc[: , index_list].copy()

    r_table = []
    tipo_out = []
                               
    # Edificios 1-3 plantas.
        
    cond = w_file.apply(lambda x : True
        if x["Plantas"] <= 3 and x["Year"] <= 1900 else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, "<1900"])
    tipo_out.append(["M1","<1900", count*0.13])
    tipo_out.append(["M3", "<1900", count*0.09])
    tipo_out.append(["M4", "<1900", count*0.11])
    tipo_out.append(["M5L", "<1900", count*0.67])
    tipo_out.append(["M6L", "<1900", count*0])
    tipo_out.append(["RC3.1L", "<1900", count*0])
    tipo_out.append(["RC3.2preL", "<1900", count*0])
    tipo_out.append(["RC3.1-preL", "<1900", count*0])
    tipo_out.append(["RC1.1L", "<1900", count*0])
    tipo_out.append(["RC1.2L", "<1900", count*0])
    
    cond = w_file.apply(lambda x : True
        if x["Plantas"] <= 3 and x["Year"] > 1900 and x["Year"] <= 1920 else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1900 <= 1920"])                           
    tipo_out.append(["M1",">1900 <= 1920", count*0.07])
    tipo_out.append(["M3", ">1900 <= 1920", count*0.09])
    tipo_out.append(["M4", ">1900 <= 1920", count*0.07])
    tipo_out.append(["M5L", ">1900 <= 1920", count*0.77])
    tipo_out.append(["M6L", ">1900 <= 1920", count*0])
    tipo_out.append(["RC3.1L", ">1900 <= 1920", count*0])
    tipo_out.append(["RC3.2preL", ">1900 <= 1920", count*0])
    tipo_out.append(["RC3.1-preL", ">1900 <= 1920", count*0])
    tipo_out.append(["RC1.1L", ">1900 <= 1920", count*0])
    tipo_out.append(["RC1.2L", ">1900 <= 1920", count*0])
        
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1920 and x["Year"] <= 1940 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1920 <= 1940"])
    tipo_out.append(["M1",">1920 <= 1940", count*0.06])
    tipo_out.append(["M3", ">1920 <= 1940", count*0.07])
    tipo_out.append(["M4", ">1920 <= 1940", count*0.06])
    tipo_out.append(["M5L", ">1920 <= 1940", count*0.81])
    tipo_out.append(["M6L", ">1920 <= 1940", count*0])
    tipo_out.append(["RC3.1L", ">1920 <= 1940", count*0])
    tipo_out.append(["RC3.2preL", ">1920 <= 1940", count*0])
    tipo_out.append(["RC3.1-preL", ">1920 <= 1940", count*0])
    tipo_out.append(["RC1.1L", ">1920 <= 1940", count*0])
    tipo_out.append(["RC1.2L", ">1920 <= 1940", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1940 and x["Year"] <= 1950 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1940 <= 1950"])
    tipo_out.append(["M1",">1940 <= 1950", count*0.02])
    tipo_out.append(["M3", ">1940 <= 1950", count*0.03])
    tipo_out.append(["M4", ">1940 <= 1950", count*0.02])
    tipo_out.append(["M5L", ">1940 <= 1950", count*0.46])
    tipo_out.append(["M6L", ">1940 <= 1950", count*0.46])
    tipo_out.append(["RC3.1L", ">1940 <= 1950", count*0.01])
    tipo_out.append(["RC3.2preL", ">1940 <= 1950", count*0])
    tipo_out.append(["RC3.1-preL", ">1940 <= 1950", count*0])
    tipo_out.append(["RC1.1L", ">1940 <= 1950", count*0])
    tipo_out.append(["RC1.2L", ">1940 <= 1950", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1950 and x["Year"] <= 1960 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1950 <= 1960"])
    tipo_out.append(["M1",">1950 <= 1960", count*0])
    tipo_out.append(["M3", ">1950 <= 1960", count*0])
    tipo_out.append(["M4", ">1950 <= 1960", count*0])
    tipo_out.append(["M5L", ">1950 <= 1960", count*0])
    tipo_out.append(["M6L", ">1950 <= 1960", count*0.9])
    tipo_out.append(["RC3.1L", ">1950 <= 1960", count*0.1])
    tipo_out.append(["RC3.2preL", ">1950 <= 1960", count*0])
    tipo_out.append(["RC3.1-preL", ">1950 <= 1960", count*0])
    tipo_out.append(["RC1.1L", ">1950 <= 1960", count*0])
    tipo_out.append(["RC1.2L", ">1950 <= 1960", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1960 and x["Year"] <= 1970 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1960 <= 1970"])
    tipo_out.append(["M1",">1960 <= 1970", count*0])
    tipo_out.append(["M3", ">1960 <= 1970", count*0])
    tipo_out.append(["M4", ">1960 <= 1970", count*0])
    tipo_out.append(["M5L", ">1960 <= 1970", count*0])
    tipo_out.append(["M6L", ">1960 <= 1970", count*0.8])
    tipo_out.append(["RC3.1L", ">1960 <= 1970", count*0.2])
    tipo_out.append(["RC3.2preL", ">1960 <= 1970", count*0])
    tipo_out.append(["RC3.1-preL", ">1960 <= 1970", count*0])
    tipo_out.append(["RC1.1L", ">1960 <= 1970", count*0])
    tipo_out.append(["RC1.2L", ">1960 <= 1970", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1970 and x["Year"] <= 1980 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1970 <= 1980"])
    tipo_out.append(["M1",">1970 <= 1980", count*0])
    tipo_out.append(["M3", ">1970 <= 1980", count*0])
    tipo_out.append(["M4", ">1970 <= 1980", count*0])
    tipo_out.append(["M5L", ">1970 <= 1980", count*0])
    tipo_out.append(["M6L", ">1970 <= 1980", count*0.5])
    tipo_out.append(["RC3.1L", ">1970 <= 1980", count*0.2])
    tipo_out.append(["RC3.2preL", ">1970 <= 1980", count*0.1])
    tipo_out.append(["RC3.1-preL", ">1970 <= 1980", count*0.2])
    tipo_out.append(["RC1.1L", ">1970 <= 1980", count*0])
    tipo_out.append(["RC1.2L", ">1970 <= 1980", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1980 and x["Year"] <= 1996 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1980 <= 1996"])
    tipo_out.append(["M1",">1980 <= 1996", count*0])
    tipo_out.append(["M3", ">1980 <= 1996", count*0])
    tipo_out.append(["M4", ">1980 <= 1996", count*0])
    tipo_out.append(["M5L", ">1980 <= 1996", count*0])
    tipo_out.append(["M6L", ">1980 <= 1996", count*0])
    tipo_out.append(["RC3.1L", ">1980 <= 1996", count*0])
    tipo_out.append(["RC3.2preL", ">1980 <= 1996", count*0.1])
    tipo_out.append(["RC3.1-preL", ">1980 <= 1996", count*0.9])
    tipo_out.append(["RC1.1L", ">1980 <= 1996", count*0])
    tipo_out.append(["RC1.2L", ">1980 <= 1996", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 1996 and x["Year"] <= 2004 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">1996 <= 2004"])
    tipo_out.append(["M1",">1996 <= 2004", count*0])
    tipo_out.append(["M3", ">1996 <= 2004", count*0])
    tipo_out.append(["M4", ">1996 <= 2004", count*0])
    tipo_out.append(["M5L", ">1996 <= 2004", count*0])
    tipo_out.append(["M6L", ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.1L", ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.2preL", ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.1-preL", ">1996 <= 2004", count*0.1])
    tipo_out.append(["RC1.1L", ">1996 <= 2004", count*0.9])
    tipo_out.append(["RC1.2L", ">1996 <= 2004", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] <= 3 and x["Year"] > 2004 and x["Year"] <= 2021 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["1-3 plantas", count, ">2004 <= 2021"])
    tipo_out.append(["M1",">2004 <= 2021", count*0])
    tipo_out.append(["M3", ">2004 <= 2021", count*0])
    tipo_out.append(["M4", ">2004 <= 2021", count*0])
    tipo_out.append(["M5L", ">2004 <= 2021", count*0])
    tipo_out.append(["M6L", ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.1L", ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.2preL", ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.1-preL", ">2004 <= 2021", count*0])
    tipo_out.append(["RC1.1L", ">2004 <= 2021", count*0.1])
    tipo_out.append(["RC1.2L", ">2004 <= 2021", count*0.9])

    # Edificios 4-7 plantas.
        
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] <= 1900) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, "<1900"])
    tipo_out.append(["M5M","<1900", count*0.67])
    tipo_out.append(["M6M","<1900", count*0])
    tipo_out.append(["RC3.1M","<1900", count*0])
    tipo_out.append(["RC3.2preM", "<1900", count*0])
    tipo_out.append(["RC3.1-preM", "<1900", count*0])
    tipo_out.append(["RC1.1M", "<1900", count*0])
    tipo_out.append(["RC1.2M", "<1900", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1900 and x["Year"] <= 1920 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1900 <= 1920"])
    tipo_out.append(["M5M",">1900 <= 1920", count*0.77])
    tipo_out.append(["M6M",">1900 <= 1920", count*0])
    tipo_out.append(["RC3.1M",">1900 <= 1920", count*0])
    tipo_out.append(["RC3.2preM", ">1900 <= 1920", count*0])
    tipo_out.append(["RC3.1-preM", ">1900 <= 1920", count*0])
    tipo_out.append(["RC1.1M", ">1900 <= 1920", count*0])
    tipo_out.append(["RC1.2M", ">1900 <= 1920", count*0])
            
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1920 and x["Year"] <= 1940 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1920 <= 1940"])
    tipo_out.append(["M5M",">1920 <= 1940", count*0.81])
    tipo_out.append(["M6M",">1920 <= 1940", count*0])
    tipo_out.append(["RC3.1M",">1920 <= 1940", count*0])
    tipo_out.append(["RC3.2preM", ">1920 <= 1940", count*0])
    tipo_out.append(["RC3.1-preM", ">1920 <= 1940", count*0])
    tipo_out.append(["RC1.1M", ">1920 <= 1940", count*0])
    tipo_out.append(["RC1.2M", ">1920 <= 1940", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1940 and x["Year"] <= 1950 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1940 <= 1950"])
    tipo_out.append(["M5M",">1940 <= 1950", count*0.46])
    tipo_out.append(["M6M",">1940 <= 1950", count*0.46])
    tipo_out.append(["RC3.1M", ">1940 <= 1950", count*0.01])
    tipo_out.append(["RC3.2preM",  ">1940 <= 1950", count*0])
    tipo_out.append(["RC3.1-preM",  ">1940 <= 1950", count*0])
    tipo_out.append(["RC1.1M",  ">1940 <= 1950", count*0])
    tipo_out.append(["RC1.2M",  ">1940 <= 1950", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1950 and x["Year"] <= 1960 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1950 <= 1960"])
    tipo_out.append(["M5M",">1950 <= 1960", count*0])
    tipo_out.append(["M6M",">1950 <= 1960", count*0.9])
    tipo_out.append(["RC3.1M", ">1950 <= 1960", count*0.1])
    tipo_out.append(["RC3.2preM",  ">1950 <= 1960", count*0])
    tipo_out.append(["RC3.1-preM",  ">1950 <= 1960", count*0])
    tipo_out.append(["RC1.1M",  ">1950 <= 1960", count*0])
    tipo_out.append(["RC1.2M",  ">1950 <= 1960", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1960 and x["Year"] <= 1970 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1960 <= 1970"])
    tipo_out.append(["M5M",">1960 <= 1970", count*0])
    tipo_out.append(["M6M",">1960 <= 1970", count*0.8])
    tipo_out.append(["RC3.1M", ">1960 <= 1970", count*0.2])
    tipo_out.append(["RC3.2preM",  ">1960 <= 1970", count*0])
    tipo_out.append(["RC3.1-preM",  ">1960 <= 1970", count*0])
    tipo_out.append(["RC1.1M",  ">1960 <= 1970", count*0])
    tipo_out.append(["RC1.2M",  ">1960 <= 1970", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1970 and x["Year"] <= 1980 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1970 <= 1980"])
    tipo_out.append(["M5M",">1970 <= 1980", count*0])
    tipo_out.append(["M6M",">1970 <= 1980", count*0.5])
    tipo_out.append(["RC3.1M", ">1970 <= 1980", count*0.2])
    tipo_out.append(["RC3.2preM",  ">1970 <= 1980", count*0.1])
    tipo_out.append(["RC3.1-preM",  ">1970 <= 1980", count*0.2])
    tipo_out.append(["RC1.1M",  ">1970 <= 1980", count*0])
    tipo_out.append(["RC1.2M",  ">1970 <= 1980", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1980 and x["Year"] <= 1996 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1980 <= 1996"])
    tipo_out.append(["M5M",">1980 <= 1996", count*0])
    tipo_out.append(["M6M",">1980 <= 1996", count*0])
    tipo_out.append(["RC3.1M", ">1980 <= 1996", count*0])
    tipo_out.append(["RC3.2preM",  ">1980 <= 1996", count*0.1])
    tipo_out.append(["RC3.1-preM",  ">1980 <= 1996", count*0.9])
    tipo_out.append(["RC1.1M",  ">1980 <= 1996", count*0])
    tipo_out.append(["RC1.2M",  ">1980 <= 1996", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 1996 and x["Year"] <= 2004 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">1996 <= 2004"])
    tipo_out.append(["M5M",">1996 <= 2004", count*0])
    tipo_out.append(["M6M",">1996 <= 2004", count*0])
    tipo_out.append(["RC3.1M", ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.2preM",  ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.1-preM",  ">1996 <= 2004", count*0.1])
    tipo_out.append(["RC1.1M",  ">1996 <= 2004", count*0.9])
    tipo_out.append(["RC1.2M",  ">1996 <= 2004", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 3 and x["Plantas"] <= 7 and x["Year"] > 2004 and x["Year"] <= 2021 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append(["4-7 plantas", count, ">2004 <= 2021"])
    tipo_out.append(["M5M",">2004 <= 2021", count*0])
    tipo_out.append(["M6M",">2004 <= 2021", count*0])
    tipo_out.append(["RC3.1M", ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.2preM",  ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.1-preM",  ">2004 <= 2021", count*0])
    tipo_out.append(["RC1.1M",  ">2004 <= 2021", count*0.1])
    tipo_out.append(["RC1.2M",  ">2004 <= 2021", count*0.9])

    # Edificios >6 plantas.
        
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] <= 1900) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, "<1900"])
    tipo_out.append(["M5H", "<1900", count*0.67])
    tipo_out.append(["M6H", "<1900", count*0])
    tipo_out.append(["RC3.1H","<1900", count*0])
    tipo_out.append(["RC3.2preH", "<1900", count*0])
    tipo_out.append(["RC3.1-preH", "<1900", count*0])
    tipo_out.append(["RC1.1H", "<1900", count*0])
    tipo_out.append(["RC1.2H", "<1900", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1900 and x["Year"] <= 1920 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1900 <= 1920"])
    tipo_out.append(["M5H", ">1900 <= 1920", count*0.77])
    tipo_out.append(["M6H", ">1900 <= 1920", count*0])
    tipo_out.append(["RC3.1H",">1900 <= 1920", count*0])
    tipo_out.append(["RC3.2preH", ">1900 <= 1920", count*0])
    tipo_out.append(["RC3.1-preH", ">1900 <= 1920", count*0])
    tipo_out.append(["RC1.1H", ">1900 <= 1920", count*0])
    tipo_out.append(["RC1.2H", ">1900 <= 1920", count*0])
            
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1920 and x["Year"] <= 1940 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1920 <= 1940"])
    tipo_out.append(["M5H", ">1920 <= 1940", count*0.81])
    tipo_out.append(["M6H", ">1920 <= 1940", count*0])
    tipo_out.append(["RC3.1H",">1920 <= 1940", count*0])
    tipo_out.append(["RC3.2preH", ">1920 <= 1940", count*0])
    tipo_out.append(["RC3.1-preH", ">1920 <= 1940", count*0])
    tipo_out.append(["RC1.1H", ">1920 <= 1940", count*0])
    tipo_out.append(["RC1.2H", ">1920 <= 1940", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1940 and x["Year"] <= 1950 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1940 <= 1950"])
    tipo_out.append(["M5H", ">1940 <= 1950", count*0.46])
    tipo_out.append(["M6H", ">1940 <= 1950", count*0.46])
    tipo_out.append(["RC3.1H",">1940 <= 1950", count*0.01])
    tipo_out.append(["RC3.2preH", ">1940 <= 1950", count*0])
    tipo_out.append(["RC3.1-preH", ">1940 <= 1950", count*0])
    tipo_out.append(["RC1.1H", ">1940 <= 1950", count*0])
    tipo_out.append(["RC1.2H", ">1940 <= 1950", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1950 and x["Year"] <= 1960 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1950 <= 1960"])
    tipo_out.append(["M5H", ">1950 <= 1960", count*0])
    tipo_out.append(["M6H", ">1950 <= 1960", count*0.9])
    tipo_out.append(["RC3.1H",">1950 <= 1960", count*0.1])
    tipo_out.append(["RC3.2preH", ">1950 <= 1960", count*0])
    tipo_out.append(["RC3.1-preH", ">1950 <= 1960", count*0])
    tipo_out.append(["RC1.1H", ">1950 <= 1960", count*0])
    tipo_out.append(["RC1.2H", ">1950 <= 1960", count*0])
    
    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1960 and x["Year"] <= 1970 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1960 <= 1970"])
    tipo_out.append(["M5H", ">1960 <= 1970", count*0])
    tipo_out.append(["M6H", ">1960 <= 1970", count*0.8])
    tipo_out.append(["RC3.1H",">1960 <= 1970", count*0.2])
    tipo_out.append(["RC3.2preH", ">1960 <= 1970", count*0])
    tipo_out.append(["RC3.1-preH", ">1960 <= 1970", count*0])
    tipo_out.append(["RC1.1H", ">1960 <= 1970", count*0])
    tipo_out.append(["RC1.2H", ">1960 <= 1970", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1970 and x["Year"] <= 1980 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1970 <= 1980"])
    tipo_out.append(["M5H", ">1970 <= 1980", count*0])
    tipo_out.append(["M6H", ">1970 <= 1980", count*0.5])
    tipo_out.append(["RC3.1H",">1970 <= 1980", count*0.2])
    tipo_out.append(["RC3.2preH", ">1970 <= 1980", count*0.1])
    tipo_out.append(["RC3.1-preH", ">1970 <= 1980", count*0.2])
    tipo_out.append(["RC1.1H", ">1970 <= 1980", count*0])
    tipo_out.append(["RC1.2H", ">1970 <= 1980", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1980 and x["Year"] <= 1996 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1980 <= 1996"])
    tipo_out.append(["M5H", ">1980 <= 1996", count*0])
    tipo_out.append(["M6H", ">1980 <= 1996", count*0])
    tipo_out.append(["RC3.1H",">1980 <= 1996", count*0])
    tipo_out.append(["RC3.2preH", ">1980 <= 1996", count*0.1])
    tipo_out.append(["RC3.1-preH", ">1980 <= 1996", count*0.9])
    tipo_out.append(["RC1.1H", ">1980 <= 1996", count*0])
    tipo_out.append(["RC1.2H", ">1980 <= 1996", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 1996 and x["Year"] <= 2004 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">1996 <= 2004"])
    tipo_out.append(["M5H", ">1996 <= 2004", count*0])
    tipo_out.append(["M6H", ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.1H",">1996 <= 2004", count*0])
    tipo_out.append(["RC3.2preH", ">1996 <= 2004", count*0])
    tipo_out.append(["RC3.1-preH", ">1996 <= 2004", count*0.1])
    tipo_out.append(["RC1.1H", ">1996 <= 2004", count*0.9])
    tipo_out.append(["RC1.2H", ">1996 <= 2004", count*0])

    cond = w_file.apply(lambda x : True
        if (x["Plantas"] > 7 and x["Year"] > 2004 and x["Year"] <= 2021 ) else False, axis = 1)
    count = len(w_file[cond == True].index)
    r_table.append([">7 plantas", count, ">2004 <= 2021"])
    tipo_out.append(["M5H", ">2004 <= 2021", count*0])
    tipo_out.append(["M6H", ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.1H",">2004 <= 2021", count*0])
    tipo_out.append(["RC3.2preH", ">2004 <= 2021", count*0])
    tipo_out.append(["RC3.1-preH", ">2004 <= 2021", count*0])
    tipo_out.append(["RC1.1H", ">2004 <= 2021", count*0.1])
    tipo_out.append(["RC1.2H", ">2004 <= 2021", count*0.9])
    
    if nombre == "0":
        tabla_out = pd.DataFrame(r_table, columns=["Plantas", "Num. edificos", "Año"])
        tabla_out.to_excel(file + "Clasificado.xlsx")
        
    tabla_tipo = pd.DataFrame(tipo_out, columns=["Tipo", "Año", "Num. edificios"])
    tabla_tipo.sort_values("Tipo", inplace=True)
    x = str(nombre) + ".xlsx"
    tabla_tipo.to_excel(x)
    
    return 

def todo(lista, file2):
    df2 = file2
    dfmask = df2[lista[0]] == lista[1]
    filt_aux = file2[dfmask]
    df3 = filt_aux
    valores = filt_aux[lista[2]].unique()
    for i in range(len(valores)):
        print(valores[i])
        df_mask2 = df3[lista[2]] == valores[i]
        filt_aux2 = filt_aux[df_mask2]
        if lista[1] != "3_industrial":
            nom = lista[2] + str(valores[i])
            tipo_constr(filt_aux2, 1, nom)
        else:
            tipo_constr(filt_aux2, 2, nom)
    return print("Tablas generadas en directorio. Saliendo del programa.")

#############################################################################
########################  Menu Argparser principal ##########################
#############################################################################

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--read", nargs=1, help="Lee el archivo excel para trabajar.\
Se le debe pasar el nombre del excel con la extension.")
parser.add_argument("-f", "--filter", nargs="+", help="Filtrado de subconjuntos de columnas para eliminar repetidos. \
Se le pasan los nombres de las columnas que se usaran para filtrar.")
parser.add_argument("-c", "--calc", nargs="+", help="Filtrado por tipologi­as o valores concretos de ciertos campos.\
Se le pasa el nombre de la columna y el valor que debe tener.")
parser.add_argument("-s", "--stats", nargs="+", help="EstadÃ­sticas de las columnas deseadas.\
Se le pasa el nombre de la/s columna/s. ")
parser.add_argument("-t", "--type", nargs=1, help="Para la tabla objetivo se calculan tipologi­as constructivas. \
Se usara la tabla ya filtrada por defecto. Se puede modificar el cÃ³digo para elegir la tabla.")
parser.add_argument("-a", "--all", nargs=3, help="Para la tabla objetivo se calculan tipologi­as constructivas \
para todos los conjuntos definidos por valores de columna y para el tipo de construccion especificado. \
Se usara la tabla ya filtrada por defecto. Se puede modificar el cÃ³digo para elegir la tabla.")
args = parser.parse_args()


#############################################################################
############################  Salida de datos ###############################
#############################################################################

if args.read:
    file_0 = pd.read_excel(str(args.read[0]))
    
    if args.filter:
        file_1 = filtro(args.filter, file_0)
    if args.all:
        if args.filter:
            file_a = todo(args.all, file_1)
        else:
            file_a = todo(args.all, file_0)

    if args.calc:
        if args.filter:
            file_f = calc(args.calc, file_1)
            file_f.to_excel("Resultado.xlsx")

        else:
            file_f = calc(args.calc, file_0)
            file_f.to_excel("Resultado.xlsx")

    if args.stats:
        stats(args.stats, file_f)

    if args.type:
        tipo_constr(file_f, args.type[0], "0")

else:
    print("Es necesario leer un excel para trabajar. Saliendo del programa")
