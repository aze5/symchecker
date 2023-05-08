# symchecker

This Python application checks the file system for files and symlinks and adds data to an SQL database accordingly. This code was written for a small business that sells electronic components online. They have over 1.3 million files on a NAS device, most of which are symbolic links to a generic image of a component's case.

## Prerequisites
- Python 3.x
- pymysql package
- MySQL Server

## Installation
1. Clone or download the project files.
2. Install pymysql using pip: `pip install pymysql`
3. Make sure you have a MySQL Server instance running.
4. Update the connection details in the cnxn variable in the symchecker.py file.

## Usage
1. Open the command prompt or terminal and navigate to the project directory.
2. Run the symchecker.py file: `python symchecker.py`

The application will iterate through the file system starting from the working_dir directory specified in the code.
Files and symlinks will be identified and data will be added to the `pictures_location_table` table in the SQL database.
The `products_table` table will be updated with the `productid` value from `pictures_location_table` where `productcode` values match.
Two CSV files will be created in the project directory: `filepath_to_file.csv` and `filepath_to_symlink.csv`. These files will contain the details of the files and symlinks found in the file system.
##### *Note*: This application will truncate the pictures_location_table table before inserting new data. Make sure you have a backup of the data before running the application.
