import random
import sys
islands = {
        "軍艦島" : 6,
        "屋久島" : 6,
        "小豆島" : 6,
        "種子島" : 6,
        "佐渡島" : 6
        }

def selectIsland () :
    selectIsland = random.choice(list(islands.keys()))
    islands[selectIsland] -= 1
    print(selectIsland) #select island
    if islands[selectIsland] is 0:
        del islands[selectIsland]

for i in range(1, 255):
    try:
        selectIsland()
    except Exception:
        print('Done')
        sys.exit()
