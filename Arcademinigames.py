 
import os, random,time

#Menu del juego
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls')
	print("\n \t\t\t\t ****** ArcadeMinigames *****")
	print("Bienvenido, selecciona un minijuego")
	print("\t1 - Piedra, Papel o Tijeras")
	print("\t2 - Ahorcado")
	print("\t3 - Triqui")
	print("\t9 - salir")


def triqui_game():
  tablero = [' ' for x in range(10)]

  def insertar_simbolo(simbolo, pos):
      tablero[pos] = simbolo

  def espacio_libre(pos):
      return tablero[pos] == ' '

  def impirmir_tablero(casilla):
      print('   |   |')
      print(' ' + casilla[1] + ' | ' + casilla[2] + ' | ' + casilla[3])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + casilla[4] + ' | ' + casilla[5] + ' | ' + casilla[6])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + casilla[7] + ' | ' + casilla[8] + ' | ' + casilla[9])
      print('   |   |')
      
  def ganador(bo, le):
      return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

  def playerMove():
      run = True
      while run:
          move = input('Selecciona una casilla para insertar una \'X\' (1-9): ')
          os.system("cls")
          try:
              move = int(move)
              if move > 0 and move < 10:
                  if espacio_libre(move):
                      run = False
                      insertar_simbolo('X', move)
                  else:
                      print('Este espacio esta ocupado')
                      impirmir_tablero(tablero)
              else:
                  print('Selecciona otra casilla')
                  impirmir_tablero(tablero)
          except:
              print('Digita una número')
              impirmir_tablero(tablero)
              

  def movimientos_computador():
      jugadas_posibles = [x for x, simbolo in enumerate(tablero) if simbolo == ' ' and x != 0]
      move = 0

      for let in ['O', 'X']:
          for i in jugadas_posibles:
              boardCopy = tablero[:]
              boardCopy[i] = let
              if ganador(boardCopy, let):
                  move = i
                  return move

      cornersOpen = []
      for i in jugadas_posibles:
          if i in [1,3,7,9]:
              cornersOpen.append(i)
              
      if len(cornersOpen) > 0:
          move = selectRandom(cornersOpen)
          return move

      if 5 in jugadas_posibles:
          move = 5
          return move

      edgesOpen = []
      for i in jugadas_posibles:
          if i in [2,4,6,8]:
              edgesOpen.append(i)
              
      if len(edgesOpen) > 0:
          move = selectRandom(edgesOpen)
          
      return move

  def selectRandom(li):
      import random
      ln = len(li)
      r = random.randrange(0,ln)
      return li[r]
      

  def tablero_lleno(board):
      if board.count(' ') > 1:
          return False
      else:
          return True

  def main():
      print('\n \t\t\t\t ****** Triqui *****')
      impirmir_tablero(tablero)

      while not(tablero_lleno(tablero)):
          if not(ganador(tablero, 'O')):
              playerMove()
          else:
              print('Has sido derrotado,la computadora \'O\' gana esta vez')
              input()
              os.system("cls")
              break

          if not(ganador(tablero, 'X')):
              move = movimientos_computador()
              if move == 0:
                  impirmir_tablero(tablero)
                  print('Empate!')
                  input()
                  os.system("cls")
              else:
                  insertar_simbolo('O', move)
                  print('El computador inserto una \'O\' en', move , ':')
                  impirmir_tablero(tablero)
          else:
              impirmir_tablero(tablero)
              print('Victoria X\'s has ganado esta partida')
              input()
              break

      if tablero_lleno(tablero):
          print('Empate!')

  while True:
      continuar = input('Quieres jugar triqui? (S/N)')
      os.system("cls")
      if continuar.lower() == 's' or continuar.lower == 'si':
          tablero = [' ' for x in range(10)]
          print('-----------------------------------')
          main()
      else:
          break



def ppt_game():
  print("\n \t\t\t\t ****** Piedra Papel o Tijeras *****")

  # Contador
  win = 0
  loss = 0
  tie = 0

  while True:
      print(f"\nVictorias: {win}\nDerrotas: {loss}\nEmpates: {tie}")

      print("""\nIngresa tu movimiento: 
              r - Piedra 
              p - Papel 
              s - Tijeras 
              q - Salir""")
      UserMove = input("¿Piedra, Papel o Tijeras? : ")
      os.system("cls")
      if UserMove == 'q':
          break   
      elif UserMove!="r" and UserMove!="p" and UserMove!="s":
          print("Opción invalida")  

      # Elección aleatoria del computador: 
      randomNumber = random.randint(1, 3)

      # Movimiento del computador 
      if randomNumber == 1:
          computerMove = 'r'
          print("\nEl bot ha lanzado: Piedra\n")
      
      elif randomNumber == 2:
          computerMove = 'p'
          print("\nEl bot ha lanzado: Papel\n")
      
      elif randomNumber == 3:
          computerMove = 's'
          print("\nEl bot ha lanzado: Tijeras\n")
          
      # Verificación de jugadas
      if UserMove == computerMove:
          print("El resultado ha sido: Empate!")
          tie += 1
      elif UserMove == 'r' and computerMove == 's':
          print("El resultado ha sido: Victoria!")
          win += 1
      elif UserMove == "p" and computerMove == 'r':
          win += 1
          print("El resultado ha sido: Victoria!")
      elif UserMove == "s" and computerMove == 'p':
          win += 1
          print("El resultado ha sido: Victoria!")
      elif UserMove == "r" and computerMove == 'p':
          loss += 1
          print("El resultado ha sido: Derrota")
      elif UserMove == "p" and computerMove == 's':
          loss += 1
          print("El resultado ha sido: Derrota")
      elif UserMove == "s" and computerMove == 'r':
          loss += 1
          print("El resultado ha sido: Derrota")



def ahorcado_game():
  def buscarPalabraAleat(listaPalabras):
      # Esta funcion retorna una palabra aleatoria.
      palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
      return listaPalabras[palabraAleatoria]

  palabras = 'perro gato camaron aguila murcielago programacion salto juego soldado maniqui cuaderno taza espejo bateria bolsa portatil pastilla esfero arbol flor juguete teclado lapiz mesa silla'.split()


  time.sleep(1)
  print("\n \t\t\t\t ****** Ahorcado *****")
  print("\nDebes adivinar la palabra completa antes de que se te agoten las vidas\n")
  time.sleep(0.5)
  palabra = buscarPalabraAleat(palabras)
  tupalabra=" "
  vidas=8

  while vidas > 0:
      fallas=0
      for letra in palabra:
          if letra in tupalabra:
              print(letra,end="")
          else:
              print(" _ ",end="")
              fallas+=1
      if fallas==0:
          input()
          print("")
          print("Felicidades, ganaste")
          input()
          break

      tuletra=input("\n\nIntroduce una letra: ")
      os.system("cls")
      tupalabra+=tuletra

      if tuletra not in palabra:
          vidas-=1
          print("Te equivocaste")
          print("Tienes ",+vidas," vidas")
      if vidas== 0:
          print("Perdiste")
          print("La palabra era:",palabra)
  else:
      input()
      print("Gracias por jugar")
      input()



 
 
while True:
  menu()

  opcionMenu=int(input("Digita un número: "))
  os.system("cls")

  if opcionMenu==1:
    ppt_game()

  elif opcionMenu==2:
    ahorcado_game()  

  elif opcionMenu==3:
    triqui_game() 

  elif opcionMenu==9:
    break

  else:
    print("Opción invalida")  