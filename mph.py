fCONVERSION = 0.6214

print("MPH\t","KPH")
for iSpeed in range (0,151,5):
    fKPH = iSpeed / fCONVERSION
    print(iSpeed,"\t", format(fKPH, ".0f"))
