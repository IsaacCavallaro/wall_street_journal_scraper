# Wall Street Journal Scraper

This project scrapes the Wall Street Journal website for the price of the US dollar and news headlines, and analyzes the data to see if there is any correlation between the headlines and the economy.


## Setup Database

1. Install Homebrew (if you haven't already) by running the following command in your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

2. Install PostgreSQL using Homebrew by running the following command:

```bash
brew install postgresql
```

---

3. Start the PostgreSQL service using Homebrew:
```bash
brew services start postgresql
```

---

4. Create a new database by running the following command:
```
psql -d postgres -U your_username -f sql/create_database.sql
```
- Replace `your_username` with your actual username.

---

5. Create the necessary tables by running the following command:
```bash
psql -d your_database_name -U your_username -f sql/create_tables.sql
```

- Replace `your_database_name` with the name of the database you created in step 4, and `your_username` with your actual username.


TEMP EDIT FOR RENAMING REPO TO PASS LINTING