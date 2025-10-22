# Author: Chloe Gerhardson
# Interplanetary Weights

#Declare Constants for calculations 


fMERCURY = 0.38
fVENUS = 0.91
fMOON = 0.165
fMARS = 0.38
fJUPITER = 2.34
fSATURN = 0.93
fURANUS = 0.92
fNEPTUNE = 1.12
fPLUTO = 0.066

#Get inputs from user for name and weight

sName = input("Hello. What is your name?")
fEarthWeight = float(input("Hi " + sName + " How much do you weigh on Earth?"))

#Calculate weights for each planet

fMercuryWeight = fEarthWeight * fMERCURY
fVenusWeight = fEarthWeight * fVENUS
fMoonWeight = fEarthWeight * fMOON
fMarsWeight = fEarthWeight * fMARS
fJupiterWeight = fEarthWeight * fJUPITER
fSaturnWeight = fEarthWeight * fSATURN
fUranusWeight = fEarthWeight * fURANUS
fNeptuneWeight = fEarthWeight * fNEPTUNE
fPlutoWeight = fEarthWeight * fPLUTO

#Output to screen with column formatting

print(sName, "here are your weights on our Solar System's planets:")

print(format("Weight on Mercury","20"),format(fMercuryWeight,"10.2f"))
print(format("Weight on Venus","20"),format(fVenusWeight, "10.2f"))
print(format("Weight on our Moon","20"),format(fMoonWeight,"10.2f"))
print(format("Weight on Mars","20"),format(fMarsWeight,"10.2f"))
print(format("Weight on Jupiter","20"),format(fJupiterWeight,"10.2f"))
print(format("Weight on Saturn","20"),format(fSaturnWeight,"10.2f"))
print(format("Weight on Uranus","20"),format(fUranusWeight,"10.2f"))
print(format("Weight on Neptune","20"),format(fNeptuneWeight,"10.2f"))
print(format("Weight on Pluto","20"),format(fPlutoWeight,"10.2f"))



