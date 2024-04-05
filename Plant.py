class Plant:
    name: str
    water_level: float

    def __init__(self,
                 name: str,
                 water_level: float):
        self.name = name
        self.water_level = water_level

    def check_moisture_level(self) -> str:
        pass

    def water_plant(self,
                    amount_water_mm: float):
        pass


