def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break  
                cats = line.strip().split(',')
                info = {"id": cats[0], "name": cats[1], "age": cats[2]}
                cats_info.append(info)
    except PermissionError:
        print("У вас немає дозволу на читання файлу")
    except Exception as e:
        print("Помилка:", e)
    return cats_info

cats_info = get_cats_info("cats_inform.txt")
for cat in cats_info:
    print(cat)