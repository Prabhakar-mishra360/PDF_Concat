import sys
import os

# Trying to import PyPDF2, if not it will install automatically

try:
    import PyPDF2 as pdf
except:
    print("It seem you Don't have required module\n")
    try:
        os.system("pip install PyPDF2")
        import PyPDF2 as pdf
    except:
        print("pip not installed or No Internet Connection!\n \
            Aborting....")
       exit(0)
       
# Trying to import tqdm, if not it will install automatically

try:
    from tqdm import tqdm
except:
    print("It seem you Don't have required module\n")
    try:
        os.system("pip install tqdm")
        from tqdm import tqdm
    except:
        print("pip not installed or No Internet Connection!\n \
            Aborting....")
        exit(0)

# If any error occur this function will be called and program will terminate safetly
def call():
    merger.close()
    print("Process Terminated")
    exit()

# Help Section
if(len(sys.argv)==1 or sys.argv[1] == "-h" or sys.argv[1] == "--help"):
   print("Discription:")
   print("This is a command line utility, made by using PyPDF2. Using this utility one can concatinate many PDF file into one PDF.\n")
   print('Usage:')
   print(">combine file1.pdf file2.pdf\n")
   print("Combine both file and merge into output.pdf by default in working directory. You can concatinate more than 2 files at once.\n")
   print("Note:\n")
   print("     Full path must be given if files are in other location than in directory of program. In our case our program and files are in same directory.\n")
   print("Press ENTER to exit...")
   input()

# Merging Section
else:
    n = len(sys.argv)
    if n>2:     #Checking if processing is required or not
        for i in range(1,n):
            if sys.argv[i][-1:-5:-1] == "fdp.":  #Checking if all files are pfd or not
                continue
            else:
                print("Given file must be PDF only")
                exit()
        merger = pdf.PdfFileMerger(False)
        try:        
            #Trying to merge all files
            for file_num in tqdm(range(1,n)):
                merger.append(sys.argv[file_num])
            merger.write("OUTPUT_sfhdshbsdhcbdsjcucdbcsjb.pdf")

        except FileNotFoundError:
            print("Some File Not Found")
            call()

        except:
            print("Make sure Files have appropiate Permission and Not Corrupted")
            call()

        merger.close()
        print("Sucessfully Concatinated")

    else:
        print("Nothing To Do")
