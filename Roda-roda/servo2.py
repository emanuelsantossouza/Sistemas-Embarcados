from pyfirmata import Arduino, SERVO
import keyboard
from time import sleep

porta = 'COM3'
pino = 9
board = Arduino(porta)

board.digital[pino].mode = SERVO

def girarMotor(pino, angulo):
    board.digital[pino].write(angulo)

contador = 0
print(contador)
girarMotor(pino,0)

print('Pressione alguma tecla...')

while True:
    if keyboard.is_pressed("right arrow"):
        if contador < 180:
            print("Tecla Pressionada: »")
            contador = contador + 10
            print(f'Ângulo:{contador} graus')
            girarMotor(pino,contador)
            sleep(0.1)
    
    if keyboard.is_pressed("left arrow"):
        if contador > 0:
            print("Tecla Pressionada: «")
            contador = contador - 10
            print(f'Ângulo:{contador} graus')
            girarMotor(pino,contador)
            sleep(0.1)

    if keyboard.is_pressed("x"):
        print("Tecla Pressionada: x (sair)")
        girarMotor(pino,0)
        sleep(3)
        break
