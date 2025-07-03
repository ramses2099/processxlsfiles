import pandas as pd
import os.path

def main():
    print("test")
    path_files = "C:\\Users\\d6920\\Sources\\Python\\processxlsfiles\\files\\EquipmentPerformanceReport-20250322_0700.xls"
    df = pd.read_excel(path_files, sheet_name='Data Source')
    print(df.head)

if __name__== "__main__":
    main()