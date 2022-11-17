from pyfirmata import Arduino, SERVO
from time import sleep

porta = 'COM3'
pino = 9
board = Arduino(porta)

board.digital[pino].mode = SERVO

def girarMotor(pino, angulo):
    board.digital[pino].write(angulo)
    sleep(0.015)

while True:
    for i in range(0,180):
        girarMotor(pino, i)
    for i in range(180,0,-1):
        girarMotor(pino, i)