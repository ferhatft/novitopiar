**Preparing Project Setup Documentation:**


```markdown
# Novitopia Project Setup

## Requirements:
- Python 3.8+
- pip
- virtualenv (optional)

## Installation:

1. Clone the repository:
   ```
   git clone https://github.com/ferhatft/novitopia
   ```

2. Navigate to the project directory:
   ```
   cd novitopia
   ```

3. Set up a virtual environment (optional):
   ```
   virtualenv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Migrate the database:
   ```
   python manage.py migrate
   ```

6. Load sample data:
   ```
   python manage.py loaddata sample_data.json
   ```

7. Run the server:
   ```
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to access the project.

## API Documentation:
Access API documentation at `http://127.0.0.1:8000/swagger/`.
```

**3. Automatically Adding Sample Data on Setup:**

To provide sample data:

3.1 Dump your current database data to a JSON fixture:
```bash
python manage.py dumpdata > sample_data.json
```

This command will save the current state of your data in the `sample_data.json` file.

3.2 To load this data during setup, use:
```bash
python manage.py loaddata sample_data.json
```
# novitopia
# ferhattugrul
# novitopiar
