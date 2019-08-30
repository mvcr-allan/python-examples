
#Haga la función elimina_digito que reciba dos argumentos, un dígito
def elimina_digito (digito, numero) :

  print(digito)
  #También valide la restricción de tipo de datos entero.
  if isinstance (digito, int)==False:
    return "Error: Las entradas deben ser numeros enteros"
  if isinstance (numero, int)==False:
    return "Error: Las entradas deben ser numeros enteros"

  ##“ERROR: NÚMERO DEBE SER >= 0”. 
  if numero >= 0 : 
    return "ERROR: NÚMERO DEBE SER >= 0 "
  #(entre 0 y 9) 
  # “ERROR: DIGITO DEBE ESTAR ENTRE 0 Y 9”, en caso de no
  if digito > 9:
    return "ERROR: DIGITO DEBE ESTAR ENTRE 0 Y 9 "

  cont = 0 
  digitos = 4 #falta funcion
  ret = 0
  while cont!= digitos :
    caracter = num % 10 
    print(caracter)
    num = num // 10
    if caracter != digito :
      ret = ret * 10 + caracter
    cont = cont + 1 
  return ret 

  #Si el resultado queda sin dígitos debe retornar el valor booleano False.

elimina_digito(2,3452)