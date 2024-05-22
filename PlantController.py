from Plant import Plant


def save_plant_to_file_txt(plant: Plant):
    with open(r'E:\Projekty_programowanie\Plant_system\plant_data.txt', mode='a+') as file:
        file.write(f'Plant_name:  {plant.name} Plant amount of water: {plant.water_level}\n')


class PlantController:
    def __init__(self):
        self.plants = []

    def add_plant(self,
                  plant: Plant):
        self.plants.append(plant)
        save_plant_to_file_txt(plant=plant)

    def water_plant(self, plant_name: str,
                    amount: float):
        pass

    def check_plant_moisture(self,
                             plant_name: str):
        pass
