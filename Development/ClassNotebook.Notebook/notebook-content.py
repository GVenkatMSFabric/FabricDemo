# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

import pandas as pd
# Development Work is going on 
EmployeeInfo = [
     [101,"Venkat",4545,"Chennai","MS Fabric"],
     [102,"Ramesh",232,"Bangalore","DAX"],
     [103,"Suresh",676,"Chennai","DAX"],
     [104,"Koti",343,"Hyderabad","MS Fabric"],
     [105,"Ramu",898,"Chennai","MS Fabric"],
     [106,"Somu",454,"Bangalore","DAX"],
     [107,"Pavani",676,"Chennai","MS Fabric"],
     [108,"Jhansi",454,"Bangalore","DAX"]
]
ColumnData = ['EmpId','EmpName','EmpSalary','EmpLocation','EmpCourse']
# Here try to Create one Python Data Frame
df = pd.DataFrame(data = EmployeeInfo,columns=ColumnData)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
