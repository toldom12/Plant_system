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
                print(f'Add plant to table')
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

    # controller = PlantController()
    # plant_1 = Plant(name="tuja",
    #                 water_level=50)
    # controller.add_plant(plant=plant_1)
    # print(controller.plants)
