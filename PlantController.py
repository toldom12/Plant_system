from Plant import Plant


class Plant_not_found_name_in_file(Exception):
    def __init__(self,
                 communicate: str = 'name not find in file'):
        self.communicate = communicate
        super().__init__(self.communicate)


class PlantController:
    def __init__(self):
        self.plants = []
        self.path: str = r'E:\Projekty_programowanie\Plant_system\plant_data.txt'

    def add_plant(self,
                  plant: Plant):
        self.plants.append(plant)
        self.save_plant_to_file_txt(plant=plant)

    def save_plant_to_file_txt(self, plant: Plant):
        with open(self.path, mode='a+') as self.file:
            self.file.write(f'Plant_name:  {plant.name},  Plant amount of water: {plant.water_level}\n')

    def read_plant_with_file_txt(self, index: int = 0):
        name = input(str(f'Write name of plant'))
        if isinstance(name, str):
            try:
                with open(self.path, mode='r') as self.file:
                    lines = self.file.readlines()
                    for row in lines:
                        index += 1
                        line = row.split()
                        return_value = line[1].find(name)
                        if return_value == 0:
                            print(row)
                            break
                        elif len(lines) == index and return_value != 0:
                            raise Plant_not_found_name_in_file()
                        elif return_value != 0:
                            pass
            except Plant_not_found_name_in_file as e:
                print(f'Error: {e}')

    def water_plant(self, plant_name: str,
                    amount: float):
        pass

    def check_plant_moisture(self,
                             plant_name: str):
        pass


# a = PlantController()
# a.read_plant_with_file_txt()
# pass
