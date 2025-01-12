## Random Fake data generator for SQL //
import random
import faker
fake = faker.Faker()

education_levels = ['Primary', 'Secondary', 'Bachelor', 'Master', 'Doctorate']
departments = ['Accounting', 'Administration', 'BI', 'Facilities', 'HR', 'IT', 'Legal', 'Management']

with open('insert_data.sql', 'w') as f:
    f.write('CREATE TABLE employees (\n')
    f.write('    id INT AUTO_INCREMENT PRIMARY KEY,\n')
    f.write('    first_name VARCHAR(50),\n')
    f.write('    last_name VARCHAR(50),\n')
    f.write('    age INT,\n')
    f.write('    education VARCHAR(50),\n')
    f.write('    department VARCHAR(50),\n')
    f.write('    salary DECIMAL(10, 2)\n')
    # f.write('    phone_number VARCHAR(20)\n')
    f.write(');\n\n')

    f.write(f"INSERT INTO employees (first_name, last_name, age, education, department, salary) VALUES \n")

    for _ in range(50): ## You Can Change the range whatever you want. 
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(22, 65)
        education = random.choice(education_levels)
        department = random.choice(departments)
        salary = round(random.uniform(20000, 80000), 2)
        # phone_number = fake.phone_number() if random.random() > 0.2 else None  # 20% chance of being NULL
        # After print this you have to manually change in 'insert_data.sql'.  ( "," to ";" )
        f.write(f"('{first_name}', '{last_name}', {age}, '{education}', '{department}', {salary}), \n")

print("Data generation complete. 'insert_data.sql' created.")