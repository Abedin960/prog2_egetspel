from typing import Self


class fordon:
    def __init__(self, märke,växelda, årdsmodell, hästkraft ):
        self.märke = märke
        self.växelåda = växelda
        self.årsmodell = årdsmodell
        self.hästkraft = hästkraft
    def kör(self):
        print("fordonet körs")


class bil(fordon):
    def __init__(self, märke, växelda, årdsmodell, hästkraft, antal_dörrar):
        super().__init__(märke, växelda, årdsmodell, hästkraft)
        self.antal_dörrar = antal_dörrar

    def kör(self):
        print("Bilen kör snabbt")

class lastbil(fordon):
    def __init__(self, märke, växelda, årdsmodell, hästkraft, lastkapacitet):
        super().__init__(märke, växelda, årdsmodell, hästkraft)
        self.lastkapacitet = lastkapacitet

    def kör(self):
        print("lastbilen kör långsamt") 

class spel:
    def __init__(self, bil, motståndare):
        self.bil = bil 
        self.motståndare = motståndare

    def starta(self):
        print("=== Bil Race ===")
        print(" Du kör")
        self.bil.kör()

print("Din motståndet kör:")
self.motståndare.kör()

print("race börjar nu!")

val = input ("vill du köra eller lastbilen? (bil/lastbil): ")
