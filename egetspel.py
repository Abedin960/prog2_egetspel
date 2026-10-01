class fordon:
    def __init__(self, märke,växelda, årdsmodell, hästkraf ):
        self.märke = märke
        self.växelåda = växelda
        self.årsmodell = årdsmodell
        self.hästkraft = hästkraf
class bil (fordon):
    def __init__(self, märke, växelda, årdsmodell, hästkraf, antal_dörrar):
        super().__init__(märke, växelda, årdsmodell, hästkraf)
        self.antal_dörrar = antal_dörrar 