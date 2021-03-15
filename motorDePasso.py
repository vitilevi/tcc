import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BMC)                                                      #GPIO.BOARD para numeros diretos da placa ; GPIO.BMC para pinos BMC
GPIO.setwarnings(0)                                                         #Desabilita avisos

StepPins = [21,20,16,13]                                                    #Número dos pinos de trabalho, conforme definição BOARD ou BMC

for Pin in StepPins:                                                        #Nomeia os Pins em StepPins
    print ("Setup Pins", Pin)                                               #Mostra na tela os pinos utilizados
    GPIO.setup(Pin, GPIO.OUT)                                               #Declara os pinos como saída de dados
    GPIO.output(Pin, 0)                                                     #Declara todos os pinos como LOW

seq = [ [1,0,0,0],                                                          #Determina sequencia de ativação das bobinas
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

Passo = input("Declare o número de passos: ")                               #Recebe o valor de passo para movimento

for i in range(Passo):                                                      #Passos por revolução
    for halfstep in range(8):                                               #Declara 8 posições de ativação
        for Pin in range(4):                                                #Declara 4 pinos de controle
            GPIO.output(StepPins[Pin], seq[halfstep] [Pin])                 #Atribui a sequencia de ativação para determinado ino
        sleep(0.001)                                                        #Delay
GPIO.cleanup()                                                              #Seta todos pinos como LOW