import os

file = "skripsi"
print("\n###############################################################################")
print("#                                     START                                   #")
print("###############################################################################")
os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode \"" + file +"\".tex")
os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode \"" + file +"\".tex")
print("\n###############################################################################")
print("#                                    FINISH                                   #")
print("###############################################################################")
print("DELETE del *.aux *.log *.out *.lot *.lof *.txt *.toc *.gz")
os.system("del *.aux *.log *.out *.lot *.lof *.txt *.toc *.gz")
print("\n###############################################################################")
print("#                               CLEANUP DONE                                  #")
print("###############################################################################")