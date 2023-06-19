from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 100, 1)
    item2 = Item("Ноутбук", 1000, 3)
    item3 = Item("Кабель", 50, 5)
    item4 = Item("Мышка", 50, 5)
    item5 = Item("Клавиатура", 75, 5)


    # print(item1.calculate_total_price())  # 200000
    # print(item2.calculate_total_price())  # 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price * Item.pay_rate)  # 80.0
    print(item2.price * Item.pay_rate)  # 800.0
    print(item3.price * Item.pay_rate)
    print(item4.price * Item.pay_rate)
    print(item5.price * Item.pay_rate)

    print(Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
