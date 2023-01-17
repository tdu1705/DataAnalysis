    #biblioteki
import pandas as pd
import numpy
import csv

#plik csv 
    #otwieranie pliku csv
df = pd.read_csv("./files_for_analysis/file.csv",sep=",", encoding="UTF8")

    #nowy plik csv
    #tworzenie nagłówków dla pliku i nadpisywanie pliku 
                #with open ("new_roboczy_python.csv", "a - dodanie do istenijącego poliku/stworzneie nowego pliku jeżeli nie istnieje 
                #                              "w - tworzenie za każdym razem nowego pliku/nadpisanie istniejącego pliku   
header = ["Model", "Problem Code", "Counted"]
with open ("./files_after_analysis/file_counted_python.csv", "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(header)

#---------------------------------------------------------------------------------------------------------------------------------------

    #wyszczególnienie zduplikowanych wartości
df_uniq = df["Model"].unique()

    #zliczanie ile razy powtórzy się dany błąd
i=0
while i<len(df_uniq):
            #przypisanie modelu do zmiennej 
        df_count_model = df[df["Model"]==df_uniq[i]]
            #zliczanie ile razy powtarza się wartość w kolumnie "code" dla wcześniejszej wartości modelu
        df_count = df_count_model["problem_code"].value_counts()
            #resetowanie indexu, aby zostało to zapisane jako tabela, gdzie w tabeli wartość index to code a wartość code to zliczanie
        df_count = df_count.reset_index()


            #wyświetlanie nazw kolumn tabeli
        print("Model", "\t", "Problem Code", "\t", "Counted")

        #--------------------------------------------------------------------------------------------------------------------------------
            #tworzenie konkrentej zmiennej dla wartości zliczonej (wartość code oraz zliczone),
            #stworzone aby jak jest więcej wartości code (jeden lub wiecej) przypisanej do nowej zmiennej
        j = 0
        while j<len(df_count["index"].values):
            df_count2_index_code = (df_count["index"][j])
            
            df_count2_code_zlicz = (df_count["problem_code"][j])
            print(df_uniq[i], "\t", df_count2_index_code ,"\t", df_count2_code_zlicz)

            #-----------------------------------------------------------------------------------------------------------------------
            #write to csv
                #tworzenie zmiennej data do zapisu do pliku csv
            data = [df_uniq[i],df_count2_index_code,df_count2_code_zlicz]
                #with open ("new_roboczy_python.csv", "a - dodanie do istenijącego poliku/stworzneie nowego pliku jeżeli nie istnieje 
                #                              "w - tworzenie za każdym razem nowego pliku/nadpisanie istniejącego pliku   
            with open ("./files_after_analysis/file_counted_python.csv", "a",encoding="UTF8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data) 
            #-----------------------------------------------------------------------------------------------------------------------
            
                #inkrementacja pętli
            j += 1



        #-------------------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------------------------------
        print("\n")

        #-------------------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------------------------------
            #iteracja wartości do wykonania głównej pętli while
        i += 1

#Konwertowanie pliku csv do pliku XSLX

    # Reading the csv file
df_excel = pd.read_csv("./files_after_analysis/file_counted_python.csv")
    # saving xlsx file
GFG = pd.ExcelWriter("./files_after_analysis/file_counted_python.xlsx")
df_excel.to_excel(GFG, index=False)
GFG.save()