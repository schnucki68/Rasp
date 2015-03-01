import RPi.GPIO as GPIO
import time


#GPIO Dekleration
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5,GPIO.LOW)

#Variablen
counter = float (0.000)
change = 0
vorherigeLitter = 0.00
Litter = 0
Timer0 = time.clock()

#LPS Variablen
LitterProStunde = 0
LPStimer = time.clock()
LPSLitter = float (0.000)
LPScounter = float (0.000)
LPSIntervall = 0
LPSIntervallAlt = 1


while 1:
    if GPIO.input(3) == 0:
        change = 1
    if GPIO.input(3) and change:
        counter = counter +1
       
        Litter = float(counter/450)
        change = 0

        LPScounter = LPScounter + 1
        LPSLitter = float(LPScounter/450)

    
        
        
    if (Litter - vorherigeLitter) > 0.01:
        LPSIntervall = time.clock()-LPStimer

        #Abfangen des Laufzeitfehlers LPSIntervall = 0
        if (time.clock()- LPStimer) == 0:
            LPSIntervall = LPSIntervallAlt
        LPSIntervallAlt = LPSIntervall
        
        LitterProStunde = LPSLitter*3600/LPSIntervall
        vorherigeLitter = Litter
        
        #Ausgabe
        print ( "Liter Gesamt: " + "%.2f" % (float(Litter)))
        print ("Zeit: " + "%.2f" % (time.clock()-Timer0))
        print ("Litter pro Stunde: " + "%.2f" % (float(LitterProStunde)))
    
    if LPSLitter > 0.1:
        LPSLitter = float (0.000) 
        LPScounter = float (0.000)
        LPStimer = time.clock()
        

    
    
    
