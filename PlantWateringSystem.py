def Menu():
    from Plant import Plant
    from PlantController import PlantController
    print(f'Hello in Plant Watering system  !! ')
    while True:
        print(f'Show plant list')
        print(f'-----------------')
        print(f' 0 - Show list of the [PLANTS]')
        print(f' 1 - Create a [PLANT]')
        print(f' 2 - Get Info about expected [PLANT]')
        print(f'-----------------')
        response = int(input(f'Write value : '))
        match response:
            case 0:
                p = PlantController()
                p.read_names_of_plants_with_file_txt()
            case 1:
                print(f'Create a [PLANT]')
                plant_name: str = str(input(f'Give a name of plant'))
                info_about_water_lvl: float = float(input(f' info about water lvl of plant: {plant_name}'))
                new_plant = Plant(name=plant_name,
                                  water_level=info_about_water_lvl)
                name_of_plant = new_plant.name
                water_level = new_plant.water_level
                plant = PlantController()
                if isinstance(name_of_plant, str):
                    plant.add_plant(plant=new_plant)
                    pass

            case 2:
                p = PlantController()
                result = p.find_expected_data_about_plant()
                print(f'result in find file : {result}')

            case 3:
                print(f'Write expected  level of water plant in [mm]')
                pass
            case 4:
                print(f'Check plant humidity')
            case 5:
                print(f'fill the plant')
            case 6:
                print(f'delete plant with list')
            case _:
                break


if __name__ == '__main__':
    from PlantController import Plant_not_found_name_in_file
    try:
        Menu()
    except Exception as e:
        print(f'An unexpected error occured {e}')
