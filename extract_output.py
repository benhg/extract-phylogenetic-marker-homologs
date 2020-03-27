import os
from os import sys
import sys

def extract_output(prefix):
    directory = f'/home/users/glick/extract-phylogenetic-marker-homologs/{prefix}_star_out/'
    os.chdir(directory)
    os.system("echo 'name 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22' >> output.txt")
    for filename in [i for i in os.listdir(directory) if os.path.isdir(i)]:
        print(filename)
        if os.path.isdir(directory + filename):
            print("is dir")
            svalue = filename
            var = os.path.join(directory, filename)
            print("changing dir")
            os.chdir(var)

            for i in range(1, 23):
                total = 0
                newvalue = i
                uniquely = (os.popen("awk 'FNR == 9{print $6}' " + str(newvalue) + "Log.final.out").read()).strip()
                if uniquely != '': 
                    uniquely = int(uniquely)
                else:
                    uniquely = 0

                multi = (os.popen("awk 'FNR == 24{print $9}' " + str(newvalue) + "Log.final.out").read()).strip()
                if multi != '': 
                    multi = int(multi)
                else: 
                    multi = 0
                total = uniquely + multi
                if i == 0: zero = total
                elif i == 1: one = total
                elif i == 2: two = total
                elif i == 3: three = total
                elif i == 4: four = total
                elif i == 5: five = total
                elif i == 6: six = total
                elif i == 7: seven = total
                elif i == 8: eight = total
                elif i == 9: nine = total
                elif i == 10: ten = total
                elif i == 11: eleven = total
                elif i == 12: twelve = total
                elif i == 13: thirteen = total
                elif i == 14: fourteen = total
                elif i == 15: fifteen = total
                elif i == 16: sixteen = total
                elif i == 17: seventeen = total
                elif i == 18: eighteen = total
                elif i == 19: nineteen = total
                elif i == 20: twenty = total
                elif i == 21: twentyone = total
                elif i == 22: twentytwo = total
                os.chdir(directory)


                print("writing to file ")
                with open("output.txt", "a") as file:
                    print(f"{svalue} {zero} {one} {two} {three} {four} {five} {six} {seven} {eight} {nine} {ten}")
                    file.write(f"{svalue} {zero} {one} {two} {three} {four} {five} {six} {seven} {eight} {nine} {ten} {eleven} {twelve} {thirteen} {fourteen} {fifteen} {sixteen} {seventeen} {eighteen} {nineteen} {twenty} {twentyone} {twentytwo}\n")

if __name__ == '__main__':
    prefix = sys.argv[1]
    extract_output(prefix)
