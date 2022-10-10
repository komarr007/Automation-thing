from cfonts import render
import pandas as pd
import numpy as np
import argparse
import glob


parser = argparse.ArgumentParser(description='Prisma Automation -- skitskat.celupcelup',
                                    epilog='Make indonesia great again with this shit kind of litelature')
parser.add_argument('--file_dir', type=str ,help='input folder directory contain csv file', required=True)
parser.add_argument('--number_citation', type=int ,help='number of minimum citation', required=True)
parser.add_argument('--keywords', help='keywords for filtering record based on Title and Abstract (bitwise operant)', required=True)
args = parser.parse_args()

class PrismaAutomation:

    file_dir = args.file_dir
    number_citation = args.number_citation
    keywords = args.keywords
    report = {}

    def read_data(self) -> pd.DataFrame:
        file_list = glob.glob(self.file_dir + "/*.csv")
        main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
        for i in range(1,len(file_list)):
            data = pd.read_csv(file_list[i])
            df = pd.DataFrame(data)
            main_dataframe = pd.concat([main_dataframe,df])
        
        self.report["read"] = main_dataframe.shape[0]
        return main_dataframe

    def citation_minimum(self) -> pd.DataFrame:
        print("Filtering from citations")
        data = PrismaAutomation.read_data(self)
        query = data['Cites'] > self.number_citation
        data_citation = data[query]

        self.report["citation"] = data_citation.shape[0]

        return data_citation

    def removing_duplicate(self) -> pd.DataFrame:
        data = PrismaAutomation.citation_minimum(self)
        print("Checking for duplicate record from DOI")
        query = (data['DOI'].duplicated()) & (~data['DOI'].isna())
        data_duplicated = data[query]["DOI"]
        tampungan = [x for x in data_duplicated.index]
        print("Removing duplicated record")
        data_unduplicated = data.drop(tampungan)

        self.report["duplicate"] = len(tampungan)
        
        return data_unduplicated

    def filtering_record(self) -> pd.DataFrame:
        print("Filter data by Title and Abstract")
        data = PrismaAutomation.removing_duplicate(self)
        unused_article = data.loc[(data['Title'].str.contains(self.keywords) | data['Abstract'].str.contains(self.keywords))] #modified the filtering logic in this line
        
        self.report["filter"] = unused_article.shape[0]

        return unused_article

    def open_access_article(self) -> pd.DataFrame:
        data = PrismaAutomation.filtering_record(self)
        open_data = data.loc[~data['FullTextURL'].isna()]

        self.report["open"] = open_data.shape[0]

        return open_data

    def show_data(self, table:list) -> pd.DataFrame:
        data = PrismaAutomation.filtering_record(self)[table]

        return data

    def show_report(self) -> str:
        print("\n")
        print("REPORT".center(20,"+"))
        print("record readed {} items".format(self.report["read"]))
        print("record filtered from citation {} items".format(self.report["citation"]))
        print("record duplicate {} items".format(self.report["duplicate"]))
        print("record filtered from Title and Abstract {} items".format(self.report["filter"]))

        return "END REPORT".center(20,"+")

    def save_open_data_excel(self, filename:str) -> None:
        data = PrismaAutomation.open_access_article(self)
        data.to_excel(filename + ".xlsx")

        return "Data saved as xlsx"

    def save_data(Self, filename:str) -> None:
        data = PrismaAutomation.filtering_record()
        data.to_excel(filename + ".xlsx")

        return "Data saved as xlsx"


def main():
    output = render('PRISMA AUTOMATION', colors=['red', 'white'], align='center')
    print(output)
    print("PRISMA method automation written by skitskat.celupcelup".center(580))
    obj = PrismaAutomation()
    is_open_record = input("looking for open access record? [yes or no] ")
    is_exported_excel = input("export the record to excel? [yes or no] ")
    if (is_open_record == ("yes" or "y")) and (is_exported_excel == ("yes" or "y")):
        filename = input("name of the file: ")
        obj.save_open_data_excel(filename)
    elif (is_open_record != ("yes" or "y")) and (is_exported_excel == ("yes" or "y")):
        filename = input("name of the file: ")
        obj.save_data(filename)
    elif (is_open_record == ("yes" or "y")) and (is_exported_excel != ("yes" or "y")):
        is_show_data = input("show the data? [yes or no] ")
        if is_show_data == ("yes" or "y"):
            table = input("input the table you wanted to show: [separate with comma] ")
            table_list = table.split(",")
            print("\n")
            print("PROCESS".center(20,"-"))
            record = obj.open_access_article()
            print("END PROCESS".center(20,"-"))
            print("\n")
            print("DATA".center(20,"*"))
            print(record[table_list])
            print("\n")
            print("END DATA".center(20,"*"))
            print(obj.show_report())
        else:
            print("\n")
            print("PROCESS".center(20,"-"))
            obj.open_access_article()
            print("END PROCESS".center(20,"-"))
            print(obj.show_report())
    elif (is_open_record == "no") and (is_exported_excel == "no"):
        is_show_data = input("show the data? [yes or no] ")
        if is_show_data == ("yes" or "y"):
            table = input("input the table you wanted to show: [separate with comma] ")
            table_list = table.split(",")
            print("\n")
            print("PROCESS".center(20,"-"))
            record = obj.filtering_record()
            print("END PROCESS".center(20,"-"))
            print("\n")
            print("DATA".center(20,"*"))
            print(record[table_list])
            print("\n")
            print("END DATA".center(20,"*"))
            print(obj.show_report())
        else:
            print("\n")
            print("PROCESS".center(20,"-"))
            obj.filtering_record()
            print("END PROCESS".center(20,"-"))
            print(obj.show_report())
    else:
        print("Error input!")
            

if __name__ == "__main__":
    main()
