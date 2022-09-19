
#obtener los datos
import pandas as pd
import openpyxl
import numpy as np

#muestra columnas
pd.set_option("display.max_columns", 20)
#asigna dataframe (tabla) a df
df= pd.read_excel("pruebapa.xlsx")


#_______
#análisis de datos

#se crea lista de pathways disponibles
pathway=[]
for i in range(len(df)):
  
  pathway_actual=df.iloc[i]["Pathway "]
  if pathway_actual not in pathway:
    pathway.append(pathway_actual)

#imprime en pantalla el numero de pathways y su nombre
print("numero de pathways detectados", len(pathway))
print("Se listan a continuación:")

a=1
for i in pathway:
  
  print(f"{a}. {i}")
  a+=1

#__________________

#elegir pathway

eleccion= 3
via=[]
for i in range(len(df)):
  
  pathway_actual=df.iloc[i]["Pathway "]
  if pathway_actual == eleccion:
    via_temp= df.iloc[i].to_numpy(copy=True)
    via.append(via_temp)

#via contiene las copias de cada renglon en excel que corresponda con el pathway
#_____________
#inicia análisis para crear las permutaciones
ruta= 0
via_tmp={}
rutas={}
for i in via:
  #temporizador y clave
  a=0
  aa=1
  ruta_comb={}
  comb=0
  neutro=0
  if i[1] != ruta :
    ruta=i[1]
    print("ruta:", ruta)
    if len(via_tmp) != 0: #and a <= len(via_tmp):
      
      for vias in via_tmp:
        #print(vias)
        if len(via_tmp[vias]) != 1:
          #print(vias)  
          neutro2=1    
          #for i in via_tmp[vias]:
          neutro=0
          
          if vias== 1:
            comb= len(via_tmp[vias])
            
            for combinacion in range(1,comb+1):
              key= int(combinacion)
              
              value= via_tmp[vias][combinacion-1]
              ruta_comb[key]=[]
              ruta_comb[key].append(value)
              #print(ruta_comb)
          #if len(ruta_comb)<1:
          #  comb+=1
          #  key= int(combinacion)
          #  value= i
          #  ruta_comb[key]=[]
          #  ruta_comb[key].append(value)
          
          if len(ruta_comb)>0 and vias != 1:
            #print("hola1")
            while len(via_tmp[vias]) * comb > neutro+comb:
              for combinacion in range(1,comb+1):
                #print(neutro)
                neutro+=1
                key= neutro+comb
                value2= ruta_comb.get(combinacion)
                value= value2.copy()
                ruta_comb.update({key: value})
                
                #print(ruta_comb)
                
            for via_via in via_tmp[vias]:
              
              if comb> len(ruta_comb):
                break
              for combinacion in range(comb-len(via_tmp[vias-1])+1,comb+1):
                
                key= (combinacion)
                
                value= via_via
                
                

                ruta_comb[key].append(value)
              
              comb=comb+len(via_tmp[vias-1]) 
              
              continue
                
          #comb= comb+neutro
          neutro=0
          #print(ruta_comb)
          
          
          
          
              
         
          #prueba_______________________________
          #comb+=1
          #key = int(comb)
          #print(ruta_comb)
          #value = i 
          #if i not in ruta_comb.values() and len(ruta_comb) <1:
          #  ruta_comb[key]=[]
          #if i not in ruta_comb.values() and len(ruta_comb) >0:
          #  ruta_comb[key]= ruta_comb[1]
              
          #ruta_comb[key].append(value)
        a+=1
        aa+=1 
        
        
        
        
          
      
      #key= int(comb)
      #value=via_tmp[aa]
      #if value not in ruta_comb.values():
      #  ruta_comb[key]=[]
      #ruta_comb[key].append(value)
      #comb+=1
        #print(ruta_comb)
        #print(vias)
        if len(via_tmp[vias]) == 1:
          for combinacion in range(1,len(ruta_comb)+1):
            key= int(combinacion)
            
            value2= via_tmp[vias]
            value= value2.copy()
            ruta_comb[key].append(value)
          a+=1
          aa+=1
        #print(ruta_comb) 
    
    #codigo de guardado
    print(len(ruta_comb)) 
    aaa=0
    for rutas_combinadas in ruta_comb:
      aaa+=1
      print(aaa,".- Ruta")
      for i in ruta_comb[rutas_combinadas]: print("-> ", i)
      
  #bucle captura valores de orden y nombre de proteina en una lista    
  if i[1] == ruta:
    key= int(i[2])
    value= i[6]
    if key not in via_tmp:
      via_tmp[key]=[]
    via_tmp[key].append(value)
    
  






#_________________
#codigo basura
#import xlrd
#filePath= "C:\\Users\\Hp\\Downloads\\sendkegg.xlsx"
#filePath= "pruebaA.xlsx"
#openFile = xlrd.open_workbook(filePath)

#sheet=openFile.sheet_by_name("Hoja1")

#print("Filas ", sheet.nrows)

#______________

  