"""
The recipe book stores information about how many ingredients are needed
to prepare a dish per serving.
The program prompts the user for the number of servings for preparing these dishes
and display information about the total number of required ingredients.
Identical ingredients with different dimensions are counted separately!

"""
cook_book = {
    'салат': [
        {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
        {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
    'пицца': [
        {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
    'лимонад': [
        {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
        {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}

quantity_by_product = {}
for ingridient_list in cook_book.values():
    for ingridient in ingridient_list:
        key = f"{ingridient.get('ingridient_name').capitalize()} {ingridient.get('measure')}"
        quantity_by_product[key] = quantity_by_product.setdefault(key, 0) + ingridient.get('quantity')

portion = int(input('Введите количество порций: '))

for product, quantity_per_portion in quantity_by_product.items():
    ingridient_name = product.split(' ')[0]
    product_measure = product.split(' ')[1]
    print(f"{ingridient_name}: "
          f"{quantity_per_portion * portion}"
          f" {product_measure}")
