# from bs4 import BeautifulSoup
from day1 import day_1


def advent_day_1():
    for item_1 in day_1:
        val_1 = item_1['input']
        for item_2 in day_1:
            val_2 = item_2['input']
            res = val_1+val_2
            if res == 2020:
                print('val_1', val_1)
                print('val_2', val_2)
                print('added together', res)
                print('multiplied together', val_1 * val_2)
                return


advent_day_1()
