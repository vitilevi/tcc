import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)                                                      #GPIO.BOARD para numeros diretos da placa ; GPIO.BCM para pinos BMC
GPIO.setwarnings(0)                                                         #Desabilita avisos

'Setup'
STEP1 = 1
STEP2= 7
STEP3 = 8
STEP4 = 25
DIR1 = 26
DIR2 = 19
DIR3 = 13
DIR4 = 6
CW = 1
CCW = 0
MODE = (21, 20, 16)

MOTOR = { '1': (STEP1, DIR1),
          '2': (STEP2, DIR2),
          '3': (STEP3, DIR3),
          '4': (STEP4, DIR4)}

'Parâmetros'
res = 1                                                                     #Resolução, 1 para full step
passo = 100*res                                                             #Número de passos
delay1 = 0.03*res                                                           #Delay entre bobinas
delay2 = 0.5                                                                #Delay entre motores
delay3 = 2                                                                  #Delay entre movimento

RESOLUTION = {'1': (0, 0, 0),
              '2': (1, 0, 0),
              '3': (0, 1, 0),
              '4': (1, 1, 0),
              '5': (0, 0, 1),
              '6': (1, 0, 1)}

GPIO.setup(MOTOR[1, 2, 3, 4], GPIO.output)
GPIO.output(MODE, RESOLUTION[res])

rep = int(input('Insira o número de repetições: '))

def mov1(motor1, pindir1, direcao1):
    for i in range(passo):
        GPIO.output(pindir1, direcao1)
        GPIO.output(motor1, GPIO.HIGH)
        GPIO.output(motor1, GPIO.LOW)
        sleep(delay1)

def mov2(motor2, pindir2, direcao1):
    for i in range(passo):
        GPIO.output(pindir2, direcao1)
        GPIO.output(motor2, GPIO.HIGH)
        GPIO.output(motor2, GPIO.LOW)
        sleep(delay1)

for t in range(rep):
    print('Repetição {}.'.format(t + 1))
    mov1(motor[1], CW)
    sleep(delay2)
    mov2(motor[2], CCW)
    sleep(delay3)

GPIO.cleanup()