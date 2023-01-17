import os
import csv
import pymysql

# Connect to the database
cnxn = pymysql.connect(host='localhost', user='root', password='', db='')
# Create a cursor
cursor = cnxn.cursor()

def sql_executor(add_row):
  # Execute a SQL command
  cursor.execute(add_row)

  # commit transaction
  cnxn.commit()

  # Close the cursor and connection
  cursor.close()
  cnxn.close()


# path to the working directory
working_dir = 'filepath'
   
   

# write to csv
with open('filepath_to_file_csv', 'w', encoding = 'utf-8') as f1, open('filepath_to_symlink_csv', 'w', encoding = 'utf-8') as f2:
  fwriter = csv.writer(f1)
  lwriter = csv.writer(f2)
  
  # write header
  fwriter.writerow(['name', 'link', 'path'])
  lwriter.writerow(['name', 'link', 'path'])

  # truncate from database
  sql_executor("TRUNCATE pictures_location_table;")

  # assign temporary variable to path, direcory, and file names
  for (root,dirs,files) in os.walk(working_dir):
    for name in files:
      current_path = os.path.join(root, name)
      if os.path.islink(current_path):
        # assign path string
        link_path = os.readlink(os.path.join(root, name))
        # format row and write to csv
        lwriter.writerow([name, 'L', link_path])
        # remove last 6 characters from file name
        format_str = "INSERT INTO pictures_location_table (productcode, loc, filetype) VALUES ('{name}', '{loc}', 'L');".format(name=name[:-6], loc=link_path)
        # run command on sql
        sql_executor(format_str)
      else:
        fwriter.writerow([name, 'F', 'N/A'])
        format_str = "INSERT INTO pictures_location_table (productcode, loc, filetype) VALUES ('{name}', '{loc}', 'F');".format(name=name[:-6], loc=current_path)
        sql_executor(format_str)

  sql_executor("UPDATE products_table, pictures_location_table SET pictures_location_table.productid = products_table.productid WHERE products_table.productcode = pictures_location_table.productcode;")


