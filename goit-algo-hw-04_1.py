def total_salary(path):
    total_salary_sum=0
    total_developers=0
    average_salary=0
    try:
        with open(path,"r",encoding='utf-8')as file:
            for line in file:
                salary=line.strip().split(',')
                total_salary_sum+=int(salary[1])
                total_developers+=1
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print("Помилка:",e)

    if total_developers>0:
        average_salary=total_salary_sum/total_developers
    return average_salary,total_salary_sum
average,total_sum=total_salary("salary.txt")
print("Загальна сума зарплат:",total_sum)
print("Середня зарплата:",average)