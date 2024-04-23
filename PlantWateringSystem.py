def Menu():
    from Plant import Plant
    from PlantController import PlantController
    print(f'Hello in Plant Watering system  !! ')
    while True:
        response = int(input(f'Write value : '))
        match response:
            case 0:
                print(f'Show plant list')
            case 1:
                print(f'Create a [PLANT]')
                plant_name: str = str(input(f'Give a name of plant'))
                info_about_water_lvl: float = float(input(f' info about water lvl of plant: {plant_name}'))
                new_plant = Plant(name=plant_name,
                                  water_level=info_about_water_lvl)
                name_of_plant, info_lvl_water = new_plant.base_info_plant()
                plant = PlantController()
                if isinstance(name_of_plant, str):
                    plant.add_plant(plant=new_plant)
                    pass
            case 2:
                print(f'Write expected  level of water plant in [mm]')
                pass 
            case 3:
                print(f'Check plant humidity')
            case 4:
                print(f'fill the plant')
            case 5:
                print(f'delete plant with list')
            case _:
                break


if __name__ == '__main__':
    Menu()
    pass

