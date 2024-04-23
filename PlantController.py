from Plant import Plant


class PlantController:
    def __init__(self):
        self.plants = []

    def add_plant(self,
                  plant: Plant):
        self.plants.append(plant)
        pass

    def water_plant(self, plant_name: str,
                    amount: float):
        pass

    def check_plant_moisture(self,
                             plant_name: str):
        pass


