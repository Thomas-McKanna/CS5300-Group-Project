# CS 5300 Group Project

## Files

- `inventory.csv`: original, UTF-8 encoded data
- `schema_creation.sql`: static file while creates the tables
- `reports.sql`: static file to make reports
- `clean.py`: script to read data from `inventory.csv`, clean it, and output to `cleaned.csv`
- `generate_sql.py`: script to read data from `cleaned.csv` (currently set up to read from `test_data.csv`) and translate data into a series of SQL queries in `book_collection.sql`
- `test_data.csv`: some sample data to verify if SQL generator and queries are working correctly

## How to use files

1. Use `clean.py` to generate `cleaned.csv`. 
2. Run `generate_sql.py` to generate `book_collection.sql`. 
3. Concatenate `schema_creation.sql` with `book_collection.sql` and run in DBeaver.
4. Run report queries from `reports.sql` to generate report tables.
