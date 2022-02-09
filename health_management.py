try:
    file1 = open("text_files/sampleFile.txt","a")
    file1.close()
except:
    import os
    os.mkdir("text_files")
def getdate():
    import datetime
    return datetime.datetime.now()
print("This is a program that is intended for the good health of our family members..")
file2 = open("text_files/aaraviExercise.txt","a")
file3 = open("text_files/chintuDiet.txt","a")
file4 = open("text_files/chintuExercise.txt","a")
file5 = open("text_files/shivaDiet.txt","a")
file6 = open("text_files/shivaExercise.txt","a")
file7 = open("text_files/momDiet.txt","a")
file8 = open("text_files/momExercise.txt","a")
file9 = open("text_files/badiMomDiet.txt","a")
file10 = open("text_files/badiMomExercise.txt","a")
file11 = open("text_files/dadDiet.txt","a")
file12 = open("text_files/dadExercise.txt","a")
file13 = open("text_files/badeDadDiet.txt","a")
file14 = open("text_files/badeDadExercise.txt","a")
file15 = open("text_files/dadiDiet.txt","a")
file16 = open("text_files/dadiExercise.txt","a")
file17 = open("text_files/dadaDiet.txt","a")
file18 = open("text_files/dadaExercise.txt","a")
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()
file11.close()
file12.close()
file13.close()
file14.close()
file15.close()
file16.close()
file17.close()
file18.close()
log_or_retrieve = int(input("Do you want to log data or retrieve it?\nPress \'1\' to log data and \'2\' to retrieve it\n=>"))
if log_or_retrieve == 1:
    print("Whose data do you want to log?")
    print("Type \'1\' for Aaravi.")
    print("Type \'2\' for Chintu.")
    print("Type \'3\' for Shiva.")
    print("Type \'4\' for Mrs. Shivani Sharma")
    print("Type \'5\' for Mr. Manoj Kumar")
    print("Type \'6\' for Mrs. Raj Laxmi")
    print("Type \'7\' for Mr. Ajay Kumar ")
    print("Type \'8\' for Mrs. Subhadra Kumari")
    print("Type \'9\' for Mr. RamPrasad Sharma")
    member = int(input("=>"))
    if member == 1:
        diet_or_exercise = int(input("Do you want to log her diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file1 = open("text_files/aaraviDiet.txt","a")
            diet = input("Please enter her diet:-\n")
            file1.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file1.close()
        elif diet_or_exercise == 2:
            file2 = open("text_files/aaraviExercise.txt","a")
            exercise = input("Please enter her exercise:-\n")
            file2.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file2.close()
    elif member == 2:
        diet_or_exercise = int(input("Do you want to log his diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file3 = open("text_files/chintuDiet.txt.txt","a")
            diet = input("Please enter his diet:-\n")
            file3.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file3.close()
        elif diet_or_exercise == 2:
            file4 = open("text_files/chintuExercise.txt","a")
            exercise = input("Please enter his exercise:-\n")
            file4.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file4.close()
    elif member == 3:
        diet_or_exercise = int(input("Do you want to log his diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file5 = open("text_files/shivaDiet.txt","a")
            diet = input("Please enter his diet:-\n")
            file5.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file5.close()
        elif diet_or_exercise == 2:
            file6 = open("text_files/shivaExercise.txt","a")
            exercise = input("Please enter his exercise:-\n")
            file6.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file6.close()
    elif member == 4:
        diet_or_exercise = int(input("Do you want to log her diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file7 = open("text_files/momDiet.txt","a")
            diet = input("Please enter her diet:-\n")
            file7.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file7.close()
        elif diet_or_exercise == 2:
            file8 = open("text_files/momExercise.txt","a")
            exercise = input("Please enter her exercise:-\n")
            file8.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file8.close()
    elif member == 5:
        diet_or_exercise = int(input("Do you want to log his diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file9 = open("text_files/dadDiet.txt","a")
            diet = input("Please enter his diet:-\n")
            file9.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file9.close()
        elif diet_or_exercise == 2:
            file10 = open("text_files/dadExercise.txt","a")
            exercise = input("Please enter his exercise:-\n")
            file10.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file10.close()
    elif member == 6:
        diet_or_exercise = int(input("Do you want to log her diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file11 = open("text_files/badiMomDiet.txt","a")
            diet = input("Please enter her diet:-\n")
            file11.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file11.close()
        elif diet_or_exercise == 2:
            file12 = open("text_files/badiMomExercise.txt","a")
            exercise = input("Please enter her exercise:-\n")
            file12.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file12.close()
    elif member == 7:
        diet_or_exercise = int(input("Do you want to log his diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file13 = open("text_files/badeDadDiet.txt","a")
            diet = input("Please enter his diet:-\n")
            file13.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file13.close()
        elif diet_or_exercise == 2:
            file14 = open("text_files/badeDadExercise.txt","a")
            exercise = input("Please enter his exercise:-\n")
            file14.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file14.close()
    elif member == 8:
        diet_or_exercise = int(input("Do you want to log her diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file15 = open("text_files/dadiDiet.txt","a")
            diet = input("Please enter her diet:-\n")
            file15.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file15.close()
        elif diet_or_exercise == 2:
            file16 = open("text_files/dadiExercise.txt","a")
            exercise = input("Please enter her exercise:-\n")
            file16.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file16.close()
    elif member == 9:
        diet_or_exercise = int(input("Do you want to log his diet or exercise?\nPress \'1\' for \"diet\"\nPress \'2\' for \"exercise\"\n=>"))
        if diet_or_exercise == 1:
            file17 = open("text_files/dadaDiet.txt","a")
            diet = input("Please enter his diet:-\n")
            file17.write("["+str(getdate())+"]"+"\t"+diet+"\n")
            file17.close()
        elif diet_or_exercise == 2:
            file18 = open("text_files/dadaExercise.txt","a")
            exercise = input("Please enter his exercise:-\n")
            file18.write("["+str(getdate())+"]"+"\t"+exercise+"\n")
            file18.close()
elif log_or_retrieve == 2:
    print("Whose data do you want to retrieve?")
    print("Type \'1\' for Aaravi.")
    print("Type \'2\' for Chintu.")
    print("Type \'3\' for Shiva.")
    print("Type \'4\' for Mrs. Shivani Sharma")
    print("Type \'5\' for Mr. Manoj Kumar")
    print("Type \'6\' for Mrs. Raj Laxmi")
    print("Type \'7\' for Mr. Ajay Kumar ")
    print("Type \'8\' for Mrs. Subhadra Kumari")
    print("Type \'9\' for Mr. RamPrasad Sharma")
    member = int(input("=>"))
    if member == 1:
        print("Press:-\n\'1\' to retreive her diet.\n\'2\' to retrieve her execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file1 = open("text_files/aaraviDiet.txt")
            for line in file1:
                print(line)
            file1.close
        elif diet_or_exercise == 2:
            file2 = open("text_files/aaraviExercise.txt")
            for line in file2:
                print(line)
            file2.close()
    elif member == 2:
        print("Press:-\n\'1\' to retreive his diet.\n\'2\' to retrieve his execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file3 = open("text_files/chintuDiet.txt")
            for line in file3:
                print(line)
            file3.close
        elif diet_or_exercise == 2:
            file4 = open("text_files/chintuExercise.txt")
            for line in file4:
                print(line)
            file4.close()
    elif member == 3:
        print("Press:-\n\'1\' to retreive his diet.\n\'2\' to retrieve his execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file5 = open("text_files/shivaDiet.txt")
            for line in file5:
                print(line)
            file5.close
        elif diet_or_exercise == 2:
            file6 = open("text_files/shivaExercise.txt")
            for line in file6:
                print(line)
            file6.close()
    elif member == 4:
        print("Press:-\n\'1\' to retreive her diet.\n\'2\' to retrieve her execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file7 = open("text_files/momDiet.txt")
            for line in file7:
                print(line)
            file7.close
        elif diet_or_exercise == 2:
            file8 = open("text_files/momExercise.txt")
            for line in file8:
                print(line)
            file8.close()
    elif member == 5:
        print("Press:-\n\'1\' to retreive his diet.\n\'2\' to retrieve his execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file9 = open("text_files/dadDiet.txt")
            for line in file9:
                print(line)
            file9.close
        elif diet_or_exercise == 2:
            file10 = open("text_files/dadExercise.txt")
            for line in file10:
                print(line)
            file10.close()
    elif member == 6:
        print("Press:-\n\'1\' to retreive her diet.\n\'2\' to retrieve her execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file11 = open("text_files/badiMomDiet.txt")
            for line in file11:
                print(line)
            file11.close
        elif diet_or_exercise == 2:
            file12 = open("text_files/badiMomiExercise.txt")
            for line in file12:
                print(line)
            file12.close()
    elif member == 7:
        print("Press:-\n\'1\' to retreive his diet.\n\'2\' to retrieve his execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file13 = open("text_files/badeDadDiet.txt")
            for line in file13:
                print(line)
            file13.close
        elif diet_or_exercise == 2:
            file14 = open("text_files/badeDadExercise.txt")
            for line in file14:
                print(line)
            file14.close()
    elif member == 8:
        print("Press:-\n\'1\' to retreive her diet.\n\'2\' to retrieve her execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file15 = open("text_files/dadiDiet.txt")
            for line in file15:
                print(line)
            file15.close
        elif diet_or_exercise == 2:
            file16 = open("text_files/dadiExercise.txt")
            for line in file16:
                print(line)
            file16.close()
    elif member == 9:
        print("Press:-\n\'1\' to retreive his diet.\n\'2\' to retrieve his execise.")
        diet_or_exercise = int(input("=>"))
        if diet_or_exercise == 1:
            file17 = open("text_files/dadaDiet.txt")
            for line in file17:
                print(line)
            file17.close
        elif diet_or_exercise == 2:
            file18 = open("text_files/dadaExercise.txt")
            for line in file18:
                print(line)
            file18.close()
    
