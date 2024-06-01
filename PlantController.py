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
            print(f'-------------------------------------------------')
            self.file.write(f'Plant_name:  {plant.name} , Plant amount of water: {plant.water_level}\n')
            print(f'-------------------------------------------------')

    def read_names_of_plants_with_file_txt(self):
        with open(self.path, mode='r') as self.file:
            lines = self.file.readlines()
            for index, row in enumerate(lines):
                row = row.split()
                expected_name = row[1].replace(',', '')
                print(index, expected_name)

    def read_plant_info_with_file_txt(self, index: int = 0):
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
                            return row
                        elif len(lines) == index and return_value != 0:
                            return None
                        elif return_value != 0:
                            pass
            except IOError as y:
                print(f'ERROR : {y}')

    def find_expected_data_about_plant(self) -> bool:
        try:
            expected_row = self.read_plant_info_with_file_txt()
            if not isinstance(expected_row, str):
                raise Plant_not_found_name_in_file()
            expected_row = expected_row.split()
            name = expected_row[1].replace(',', '')
            amount_of_water = float(expected_row[6])
            print(f'name: {name}')
            print(f'Amount of water: {amount_of_water}')
            return True
        except Plant_not_found_name_in_file as f:
            print(f'ERROR : {f} ')
            return False

    def water_plant(self, plant_name: str,
                    amount: float):
        pass

    def check_plant_moisture(self,
                             plant_name: str):
        pass


a = PlantController()
a.read_names_of_plants_with_file_txt()
pass
