
def make_car(manufacturer, model, **car_info):
    car_attribute ={}
    car_attribute['manufacturer'] = manufacturer
    car_attribute['model'] = model

    for key, value in car_info.items():
            car_attribute[key] = value
    return car_attribute

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)