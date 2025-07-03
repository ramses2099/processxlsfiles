import pandas as pd
import os


def main():
    os.system("cls")

    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)

    data_file_folder = "{0}\{1}".format(current_dir, "files")
    data_file_dest = "{0}\{1}".format(current_dir, "destination")

    df = []
    row = 0
    for file in os.listdir(data_file_folder):
        if file.endswith(".xls"):
            print("Loading file {0}...".format(file))
            full_path = "{0}\{1}".format(data_file_folder, file)
            if row == 0:
                df.append(
                    pd.read_excel(io=full_path, sheet_name="Data Source", skiprows=2)
                )
                row += 1
            else:
                df.append(
                    df.append(
                        pd.read_excel(
                            io=full_path, sheet_name="Data Source", skiprows=3
                        )
                    )
                )

    df_master = pd.concat(df, axis=0)
    # print(df_master.shape[0])
    path_file_dest = "{0}/{1}".format(data_file_dest, "data_total.csv")
    df_master.to_csv(path_file_dest, index=False)


if __name__ == "__main__":
    main()
