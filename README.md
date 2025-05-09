# ETL Pipeline

This project implements a simple ETL (Extract, Transform, Load) pipeline for processing product data. It includes unit tests to ensure the functionality of each stage.

## Project Structure

The project is organized as follows:

ETL_pipeline/
├── tests/

│   ├── test_extract.py

│   ├── test_load.py

│   └── test_transform.py

└── utils/

├── extract.py

├── load.py

└── transform.py

└── README.md


* `utils/`: Contains the core logic for each stage of the ETL process.
    * `extract.py`:  Extracts data (currently this might be a placeholder as the actual data source isn't defined in the tests).
    * `transform.py`:  Transforms the extracted data, cleaning and converting it as needed.
    * `load.py`:  Loads the transformed data into a CSV file.
* `tests/`: Contains unit tests for the functions in `utils/`.
    * `test_extract.py`: Tests the data extraction process.
    * `test_load.py`: Tests the data loading process.
    * `test_transform.py`: Tests the data transformation process.

##  Requirements

beautifulsoup4==4.13.4
gspread==6.2.0
gspread_dataframe==4.0.0
pandas==2.2.3
protobuf==4.25.3
Requests==2.32.3


## Setup

1.  Clone the repository:

    ```bash
    git clone <your_repository_url>
    cd ETL_pipeline
    ```

2.  (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages (pandas):

    ```bash
    pip install pandas
    ```

## Running Tests

To run the unit tests and check code coverage, use the following commands:

```bash
# Run the tests
python -m unittest discover tests

# Run tests with coverage (requires the 'coverage' package)
# You may need to install it: pip install coverage
coverage run -m unittest discover tests

# Generate a coverage report
coverage report -m