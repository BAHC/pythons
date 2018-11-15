ppm2017 = 404.13
ppm2018 = 409.18
ppmEnd = 10000
ppmCurrent = ppm2018
ppmPerYear = ppm2018/ppm2017
year = 2018

while ppmCurrent < ppmEnd:
    ppmCurrent *= ppmPerYear

    year += 1
    if ppmCurrent%(ppmEnd/2) <= 100:
        print("Year {}: ppm={}".format(year, round(ppmCurrent,2)))

print(f"End of Life in 8 hours: {year}")