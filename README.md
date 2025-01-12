# Random Fake Data Generator for SQL

This project is a Python script designed to generate random fake data for populating an SQL table. The script creates a `insert_data.sql` file containing a `CREATE TABLE` statement and `INSERT` statements for an `employees` table.

## Features

- **Table Schema**: Automatically creates an SQL table schema for an `employees` table with fields:
  - `id` (Primary Key)
  - `first_name` (String)
  - `last_name` (String)
  - `age` (Integer)
  - `education` (String)
  - `department` (String)
  - `salary` (Decimal)
- **Random Data Generation**: Populates the table with randomized fake data using the [Faker](https://faker.readthedocs.io/) library and Python's `random` module.
- **Customizable**: Easily adjust the number of rows to generate by modifying the range in the loop.

## Prerequisites

- Python 3.6 or higher
- The `faker` library

### Install Dependencies

To install the required library, run:

```bash
pip install faker
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python fake-data-generator.py
```

3. The script will generate a file named `insert_data.sql` in the same directory.
4. Use the generated SQL file to populate your database.

### Notes

- After running the script, you may need to manually replace the trailing commas (`,`) in the last row of the `INSERT` statements with a semicolon (`;`).
- Adjust the range in the loop to change the number of rows generated (default is 50).

## Customization

- Modify the list of `education_levels` and `departments` in the script to include more values.
- Uncomment the `phone_number` section to include an additional field for phone numbers.

## Example Output

The script generates an SQL file with content like:

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    education VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (first_name, last_name, age, education, department, salary) VALUES
('John', 'Doe', 34, 'Master', 'IT', 45000.75),
('Jane', 'Smith', 28, 'Bachelor', 'HR', 32000.50);
```

## Contributions

Feel free to open an issue or submit a pull request if you have any suggestions or improvements!

## License

This project is open-source and available under the [MIT License](LICENSE).
