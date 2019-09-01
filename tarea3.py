#Curso: Taller de programacion
#Estudiante: Katerine Guzman Flores

#Funcion: Suma dos numeros en orden sucesivo  del rango de inicio al rango de fin
#Entradas: dos numeros enteros: el inicio y el fin de la sumatoria 
#Salidas: Sumatoria de los rangos
#Restricciones: numeros naturales 
def sumatoria (x,y):
        if isinstance (x, int)==False:
                return "Error: Las entradas deben ser numeros enteros"
        if isinstance (y, int)==False:
                return "Error: Las entradas deben ser numeros enteros"
        if x>y:
                return "ERROR: EL INICIO DEL RANGO DEBE SER <= AL FIN DEL RANGO "
        #proceso sumatoria
        resultado=0
        while y>=x: #La funcion se detiene cuando el segundo numero es mayor que el primero
                resultado= resultado+x   #me suma el resultado anterior con mi nuevo numero 
                x= x+1 #aumenta el numero en 1
        return resultado #mi primer numero va en aumento hasta que llegue a y

#Funcion:  Imprime los divisores de un entero mayor o igual que dos
#Entradas: numero entero mayor que dos
#Salidas: Divisores propios
#Restricciones: numeros enteros
      
def divisores_propios (num):
          if isinstance (num, int)==False:
                return "Error: Debe ingresar un numero entero"
          if num<2:
              return "Error: El numero debe ser mayor o igual a dos"
        # proceso de divison
          divisor=1
          while divisor<10:
                  if num%divisor==0: #si el residuo entre el divisor es 0, este es un divisor propio
                          print (divisor, end= "      ") #imprime en horizontal y con espacio
                  divisor=divisor+1 #se evalua de 1 a 9 en aumento
                  
#Funcion: recibe un numero natural y retorna la suma de cada uno de su digitos
#entradas:  numero natural (0,1,2,3,...)
#Salidas suma de cada uno de los digitos
#Restricciones: sin validar
def suma_digitos (n):
        if isinstance (n, int)==False:
                return "Error: El numero debe ser un entero"
        suma=0
        n= abs(n)
        while n!=0:
            suma= suma+n%10   
            n=n//10  
        
        return suma

#4  Funcion: Reciba un entero y retorne el valor booleano True si ese número
#es palíndromo o False si no.
#Entradas: Numero entero
#Salidas: True or False
#restricciones:  numero entero

def palindromo(num):
      if isinstance (num, int)==False:
              return "Error: El numero debe ser un entero"   
      #variable que aloja el numero al revés
      reverse = 0
      temp= num
      #para que no se encicle porque ya no hay mas numeros   
      while(num > 0):  #1234 #123 #12 #1
          #saca último digito del numero
          reminder = num %10  #4  #3 #2 
          #
          reverse = (reverse *10) + reminder#0*10+4(4) #4*10+3(43) #43*10+2 (432)
          num = num //10 #1234//10=(123) #123//10(12) #12//10 (1)
      if temp==reverse:
          return True
      else:
          return False
  
# 5  Funcion: el primero va a contener la cantidad  de dígitos pares y
#el segundo la cantidad de todos los dígitos impares 
#Entradas: numero entero 
#Salidas:  cantidad digitos pares e impares 
#restricciones:numeros enteros
def contar_pares_impares (n): 
    if isinstance (n, int)==False:
                return "Error: El numero debe ser un entero"
    par=0
    impar=0
    while n!=0:
        if n%2==0:  
            par=par+1  
            n=n//10 
        else:
            impar=impar+1
            n=n//10
    return (par, impar)

# 6  Funcion: el primero va a contener todos los dígitos pares y
#el segundo  todos los dígitos impares
#Entradas: numero entero 
#Salidas: numeros pares e impares
#restricciones:numeros enteros
   
def pares_impares (n):    
    if isinstance (n, int)==False:
        return "Error: El numero debe ser un entero"
    else:
        pares=0 #guarda los numeros pares
        impares=0 #guarda los numeros impares 
        while n!=0: #hace que no se encicle la funcion
            if n%2==0:
                pares=pares*10+n%10
                n=n//10
            else:
                impares=impares*10+n%10
                n=n//10
        return pares, impares

#Funcion: Recibe un numero mayor o igual a dos y determina si es primo o no 
#Entradas: Numero entero mayor que dos 
#Salidas: Retorna true si es primo y false si no es primo  
#restricciones: Entero mayor que dos 

#  7 primo
def primo (n):
        if isinstance (n, int)==False:
         return "ERROR: DIGITO DEBE SER UN ENTERO"
        if n<2:
                return "Error: El numero debe ser mayor o igual a 2"
        d=2 #inicia a hacer la division  con 2 
        r= n//2#se saca raiz para no tener que hacer mas divisiones
        while d<=r:
                if n%d==0: #indica que no es primo 
                        return False
                d=d+1
        return True #indica que es primo

#Funcion: Recibe dos argumentos y elimina de este este número
#los dígitos que sean iguales al dígito del primer argumento
#Entradas:  Un dígito (entre 0 y 9) y un número entero (>=0).
#Salidas: Numero sin el digito en comun eliminado
#restricciones: digito entre 0 y 9. Numero mayor o igual que cero
#Devuelve el numero al reves
def elimina_digito (d,n) :
    if isinstance (d, int)==False:
        return "Error: Las entradas deben ser numeros enteros"
    if isinstance (n, int)==False:
        return "Error: Las entradas deben ser numeros enteros"
    if n <= 0 :
        return "ERROR: NÚMERO DEBE SER >= 0 "
    if d > 9:
        return "ERROR: DIGITO DEBE ESTAR ENTRE 0 Y 9"
    resultado= False
    numero=0
    contdigit=0 #cuenta los digitos de
    while n!=0:
        if n%10 != d: #si el numero es diferente
            resultado=resultado+(n%10*(10**contdigit)) #10**contador acomoda los numeros
            contdigit=contdigit+1 #el contador aumenra 
        n=n//10
    return resultado 

#Funcion:  reciba un valor que representa el tamaño de cada uno de los cuatro lados de un romboimpr
#Entradas:  Entero mayor o igual que dos 
#Salidas: Rombo  con el tamaño de sus cuatro lados dependiendo del entero
#restricciones: Entero mayor o igual a dos 

# 9  rombo
def rombo (n):
    if isinstance (n,int)==False:
        return "ERROR: EL NUMERO DEBE SER UN ENTERO"
    elif n<=1:
        return "El numero debe ser mayor o igual que dos"
    else:
        espacio=" "
        asterisco= "*"
        nEsp=n-1  #La diferencia que hay de espacios entre la entrada (n) y la cantidad de asteriscos del centro
        nAst=1 #cantidad de asteriscos que seran luego modificados en el ciclo
        cont=0 #necesario para detener el primer ciclo
        #ciclo para imprimir  la primera mitad del rombo
        while cont<n-1:
            linea=(nEsp)*espacio+nAst*asterisco+nEsp*espacio #guarda la linea
            print(linea)
            nAst=nAst+2 #aumenta la cantidad de asteriscos para el siguiente nivel
            cont+=1 #Aumentamos el contador para salir del while
            nEsp=nEsp-1 #conforma aumenta la cantidad de asteriscos disminuye la cantidad de espacios
       #ciclo para imprimir la otra mitad 
        while nAst>=0: #Dado que la variable es distinta de cero ya puedo comenzar a disminuirla 
            linea=nEsp*espacio+(nAst)*asterisco+nEsp*espacio
            print(linea)
            nAst=nAst-2  #disminuye la cantidad de asteriscos para el siguiente nivel
            nEsp+=1 #conforma disminuye la cantidad de asteriscos aumenta la cantidad de espacios
        return

#Funcion: Recibe dos números enteros y retorna un número con los dígitos que tienen en común esas entradas
#Entradas: Dos enteros 
#Salidas: Valor retornado con digitos en común sin repetirse
#restricciones: Los numeros deben ser enteros
def espejo (n): 
    result=0
    while n!=0:
       result=result*10+n%10  
       n=n//10 
    return result

def interseccion (n,nn):
    if isinstance (n, int)==False:
        return "Error: El numero dehe ser un entero"
    if isinstance (nn, int)==False:
        return "Error: El numero dehe ser un entero"
    else:
        nn= abs (nn)
        resultado=False
        dcomparador=9 #comparador para evaluar de (0-9) en n y en nn
        
    while dcomparador>=0:
        if elimina_digito (dcomparador,n)<n: # elimina el  dcomparador del n y si este es menor que el numero, entra
            if elimina_digito (dcomparador, nn)<nn:  #elimina el dcomparador de nn y si es menor entra
                resultado= resultado*10 + dcomparador # si el numero esta en ambos numeros se agrega al resultado
        dcomparador= dcomparador - 1 #el comparador pasa de 9 a 8 y asi para ir evaluando de 0 a 9
    return espejo(resultado) #se hace la función espejo para retornar en orden el resultado


#Funcion: Recibe un entero y retorna su doble factorial 
#Entradas: Entero 
#Salidas: 
#restricciones: Entero debe ser mayor o igual a cero

def doble_factorial (n):
    if n==0:
        return 1
    if isinstance (n, int)==False:
        return "Error: El numero debe ser un entero"
    if n<=0:
        return "Error: El numero debe ser mayor o igual a cero"
    resultado=n
    
    if n%2==0: #si es par
        while n>0:
            if n-2==0: #una vez que n llegue a 0 retorne resultado 
                return resultado
            else:
                resultado= resultado*(n-2)  #multilplica el numero por el numero menos dos 
                n=n-2 #disminuye n en dos
                
    else: 
        while n>1: #si es impar 
            if n-2==1:   #una vez que mi n llegue a 1 retorna resultado 
                return resultado
            else:
                resultado= resultado*(n-2)
                n=n-2
                
#Funcion: Recibe dos números enteros y retorna otro número cuyos dígitos están en el primer número pero no en el
#segundo número.
#Entradas: dos numeros enteros
#Salidas: Numeros enteros cuyos digitos estan en el primer numero y no en el segundo
#restricciones:Deben ser dos numeros enteros
                
 def diferencia (num1, num2):
    if isinstance (num1, int)==False:
         return "Error: El numero debe ser un entero"
    if isinstance (num2, int)==False:
        return "Error: El numero debe ser un entero"
    while num2!=0:
        num1=elimina_digito (num2%10,num1) #al eliminar el que tienen en comun num1 y num1 me queda la diferencia
        num2=num2//10 #se corta num2 y se repite el ciclo 
    return num1               

#Funcion: Recibe dos argumentos y crea un nuevo numero encriptado
#Entradas: Digito encriptador y digito a encriptar 
#Salidas: Nuevo numero encriptado
#restricciones: El primer digito debe ser un entero entre 0 y 9)
#y el segundo un entero entre 0 y 999 999 999.

def encriptar (dig, num):
    if isinstance (dig,int)==False:
        return "ERROR: EL DIGITO DEBE SER UN ENTERO "
    if isinstance (num,int)==False:
        return "ERROR: EL NUMERO DEBE SER UN ENTERO "
    if dig>9:
        return "ERROR : EL DIGITO DEBE ESTAR ENTRE O Y 9"
    if num>1000000000:
        return "ERROR : EL NUMERO DEBE ESTAR ENTRE O Y 999 999 999"
    else:
        contador=0
        resultado=0
        if num==0:
            return 10+dig
        while num!=0: 
            nuevo= ((num%10)+dig)%10 #9+0 # 9
            num=num//10 
            resultado= resultado+nuevo*(10**contador) #0+9
            contador=contador+1
        return contador*(10**contador)+(resultado)

#Funcion:  Toma un número encriptado y retorne el número original
#Entradas: Digito enriptador y digito encriptado 
#Salidas: Numero encriptado original 
#restricciones:  Dígito encriptador (entero entre 0 y 9) y  encriptado (entero entre 0 y 999 999 999)

def desencriptar (num1, num2):
        if isinstance (num1,int)==False:
                return "ERROR: EL DIGITO DEBE SER UN ENTERO "
        if isinstance (num2,int)==False:
                return "ERROR: EL NUMERO DEBE SER UN ENTERO "
        if num1>9:
                return "ERROR : EL DIGITO DEBE ESTAR ENTRE O Y 9"
        if num2>1000000000:
                return "ERROR : EL NUMERO DEBE ESTAR ENTRE O Y 999 999 999"
  

#Funcion:  recibe dos números enteros y retorna otro número
#cuyos dígitos pertenecen solo a uno de los números recibidos pero no a ambos.
#Entradas:  dos numeros enteros
#Salidas: numero con diferencia 
#restricciones: numeros deben ser enteros
def diferencia_simetrica (n1,n2):
        if isinstance (n1,int)==False:
                return "ERROR: EL DIGITO DEBE SER UN ENTERO "
        if isinstance (n2,int)==False:
                return "ERROR: EL NUMERO DEBE SER UN ENTERO "
                

#Funcion: Recibe dos enteros  y retorna True si el primer número
#es un subconjunto del segundo, de lo contrario retorne False. 
#Entradas: Dos numeros enteros 
#Salidas: True or False 
#restricciones: dos numeros enteros
def subconjunto (n1,n2):
        if isinstance (n1,int)==False:
                return "ERROR: EL DIGITO DEBE SER UN ENTERO "
        if isinstance (n2,int)==False:
                return "ERROR: EL NUMERO DEBE SER UN ENTERO "
                

#Funcion:  Recibe una fecha y una cantidad de días y retorna una nueva fecha 
#Entradas: fecha y dias 
#Salidas: Nueva fecha 
#restricciones:  cantidad de días (entero entre 0 y 15). Fecha en formato ddmmaaaa

#Funcion: Calcula las recargas, consumos, estados de cuenta y saldo de una cuenta prepago
#Entradas: Una opción (recargas, consumos, estado de cuenta)
#Salidas: Recargas, consumos, estado de cuenta
#restricciones: Indicar al menos una opción del menú

#Funcion: Reciba dos números enteros y retorna el valor booleano True
#si esos conjuntos son iguales o False si son diferentes.
#Entradas: dos numeros enteros 
#Salidas: true o False
#restricciones: Numeros enteros 

#Funcion: Recibe  un intervalo, el primero menor que el segundo) e imprime
# cada número semiprimo en el intervalo y los primos que lo forman
# cantidad total de semiprimos. 
#Entradas: Dos numeros enteros mayor que dos 
#Salidas: semiprimos y primos que lo conforman
#restricciones: Entrada deben ser enteros mayor que dos, el primer numero debe ser menor que el segundo

#Funcion: 
#Entradas: 
#Salidas: 
#restricciones:

#Funcion: 
#Entradas: 
#Salidas: 
#restricciones:

#Funcion: 
#Entradas: 
#Salidas: 
#restricciones:

#Funcion: 
#Entradas: 
#Salidas: 
#restricciones:

#Funcion: 
#Entradas: 
#Salidas: 
#restricciones:






        
