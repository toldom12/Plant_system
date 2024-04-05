from Plant import Plant


class PlantController:

    def __init__(self):
        self.plants = []

    def add_plant(self,
                  plant: Plant):
        self.plants.append(plant)

    def water_plant(self, plant_name: str,
                    amount: float):
        pass

    def check_plant_moisture(self,
                             plant_name: str):
        pass


if __name__ == '__main__':

    controller = PlantController()
    plant_1 = Plant(name="tuja",
                    water_level=50)
    controller.add_plant(plant=plant_1)
    print(controller.plants)
