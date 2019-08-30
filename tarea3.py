#Devuelve el numero al reves
def reversa ( numero ):
  ret = 0
  while numero != 0 :
    caracter = numero % 10 
    numero = numero // 10
    ret = ret * 10 + caracter
   
  return ret    

#Cuenta los digitos de un numero
def contar_digitos(numero):
      
  if isinstance (numero, int)==False:
        return "Error: Las entradas deben ser numeros enteros"
  
  ret = 0
  while numero != 0 :
    
    numero = numero // 10
    ret = ret  + 1
   
  return ret   
      
#Haga la función elimina_digito que reciba dos argumentos, un dígito
def elimina_digito (digito, numero) :

  
  #También valide la restricción de tipo de datos entero.
  if isinstance (digito, int)==False:
    return "Error: Las entradas deben ser numeros enteros"
  if isinstance (numero, int)==False:
    return "Error: Las entradas deben ser numeros enteros"

  ##“ERROR: NÚMERO DEBE SER >= 0”. 
  if numero <= 0 : 
    return "ERROR: NÚMERO DEBE SER >= 0 "
  #(entre 0 y 9) 
  # “ERROR: DIGITO DEBE ESTAR ENTRE 0 Y 9”, en caso de no
  if digito > 9:
    return "ERROR: DIGITO DEBE ESTAR ENTRE 0 Y 9 "

  cont = 0 
  digitos = contar_digitos(numero)
  ret = 0
  while cont != digitos :   
    caracter = numero % 10 
    numero = numero // 10
    if caracter != digito :
      ret = ret * 10 + caracter
    cont = cont + 1 
  return reversa(ret) 

  #Si el resultado queda sin dígitos debe retornar el valor booleano False.

print(elimina_digito(3,3452))
