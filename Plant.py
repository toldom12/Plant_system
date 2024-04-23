class Plant:

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

    def base_info_plant(self) -> tuple[str, float]:
        return self.name, self.water_level
