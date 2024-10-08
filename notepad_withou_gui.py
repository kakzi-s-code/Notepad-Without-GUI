import os
import shutil
import send2trash

class notepad():
        class writting():
            def creating_defult_name_file(self) -> None:
                # becuse of we use excusive mode[x-mode] for creatig file if file exis with same name it give error 
                # to save from error we frist check file exist or not and if it is exist the we not create that file else it create file as untitle.txt
                    if os.path.exists(f"{os.getcwd()}\\untitle.txt"):
                        pass
                    else:
                        creating = open("untitle.txt","x") # we are make file untitled always that help use to same as microsoft notepad
                        creating.close()

            def asking_user_data(self) -> None:
                 # after creating untitle.txt we are make add data in that for that we are open file foe writting mode[w-mode] to write data in side our created file
                    self.asking_data = input("Enetr Your File Data Here:- ")
                    with open("untitle.txt","w") as f:
                            f.write(self.asking_data)
            
            def saving_file(self):
                def defult_save(self) -> None:
                    self.defult_file_name = self.asking_data[0:]
                    os.rename("untitle.txt",self.defult_file_name)
                defult_save(self)
                    
                def user_way_saving(self) -> None:
                    # this section is used to save files.
                    change_file_name = input("If You Want To Change File Name Or Go With DeFult[say yes to change ans say no to defult]:- ")
                    if change_file_name.lower() == "yes":
                        FileName = input("Enter Name Of Your File:- ") # take users file name
                        FileExtenstion = input("Enetr your file extenstion [ex :- for python your file extenstion was \".py\"]:- ") # taking users file extenstion

                        def file_rename(self) -> None:
                            # here, we are rename file name by using os modul remame method.
                            os.rename(self.defult_file_name,FileName + FileExtenstion)
                        file_rename(self)

                        def file_location() -> None:
                            # we use os.getcwd that give current location parth to give a idea of user where is file
                            print("This Is Your Current Path:- ",os.getcwd())
                            # becuse of we are change location of file we need to take shutil modul it have move method that help us to moving file 
                            # and move take two parameter frist was old location and second was new location
                            old_location = f"{os.getcwd()}\{FileName + FileExtenstion}" # old location meeans our current location
                            new_location = input("Enter New Location For File:- ") # new location give by user to cahnge file location
                            shutil.move(old_location,new_location)# and shutil.move help us to moving files
                        file_location()
                user_way_saving(self)
    
        class reading():
            def __init__(self,asking_for_file_name,asking_for_location) -> None:
                        self.asking_for_file_name = asking_for_file_name                
                        self.asking_for_location = asking_for_location
                
            def checking_required_data_give_options(self) -> None:
                        if os.path.exists(self.asking_for_location):# checking path is existing or not
                            os.chdir(self.asking_for_location) # we need now change our location to any location becuse of user file are whrer we have no idea.
                            print() # now we give some option to user to read a file 
                            print("press 1 :-  on your keybord for reading whole file data") # option - 1
                            print("press 2 :- on your keyboard for reding some lines of data") # option -2
                            print()
                    
            def give_options(self,asking_user_how_to_read) -> None:
                            with open(self.asking_for_file_name,"r") as read_file: # open File for reading data
                                if asking_user_how_to_read == "1": # and if user choose 1 that means he/she read whole file 
                                    print(read_file.read()) # that why we use read method that help us to read whole file at a time
                                elif asking_user_how_to_read == "2": # and if user choose 2 that means he/she read some lines of data from file.
                                    ask_user_how_many_lines = int(input("Enter How Many Lines Do You Want To Read:- ")) # asking user for how many lines he/she want to print

                                    def redaing_way(asking_user_whrer_to_read) -> None:
                                        # here we use "counting variable & ask use line" for our :- logic
                                        if str(asking_user_whrer_to_read).lower() == "top": # if user choose top lines reading then run.
                                            # here we read our file from top to bottom for that we use readlines that give use list of data lines
                                            reading_line = read_file.readlines()
                                            print()
                                            # here becuse we now use want start from 1 that why our range start postion was 1 to user give value and +1 becuse last one was exlusive value
                                            count = 1 # counting for showing lines number
                                            # becuse we are iterating iteem from list that why we are use 0:to till our use wanted lines
                                            for i in reading_line[0:ask_user_how_many_lines]:  # iterating form list to print line by 0 to till user want line data
                                                if ask_user_how_many_lines <= count: # if user want to reding less line from file then do not worry we can print that lines
                                                        print(f"{count}.   {i}",end="")  # printing count number and line data
                                                        count += 1        # increment on count 
                                                        print()
                                                        break # becuse of here less line that why we can to print any messege that why we use break for breaking loop
                                                elif ask_user_how_many_lines >= count:# if user want print more then line that file are not present then we provied message
                                                        print(f"{count}.   {i}",end="")  # printing count number and line data
                                                        count += 1        # increment on count
                                                        # becuse of here more line that why we need to print messege that why we are not use break here for breaking loop
                                                else: # else use for only printing messge when use want more then lines then file have.
                                                    print()  # becuse of in elif print()function we are use end="" that why we need to print 2 time here
                                                    print()
                                                    print(f"\t\"sorry becuse of you file have only {count-1} lines and you want to read more then that lines. that was {ask_user_how_many_lines} line. it not posibal that why we print all file data\"".expandtabs(20))
                                                    print()    
                                                
                                        # here we use "len(our selected file)"" for our :- logic                    
                                        elif str(asking_user_whrer_to_read).lower() == "bottom": # if user choose bottom lines reading then run
                                            # here we read our file from bottom to top for that we use logic has count all lines of file that why we use readlines() method that give us list of data lines that file have.
                                            reading_line = read_file.readlines() 
                                            # becuse for we need our reading lines we get from subtracting by [len(lines) - user want reading lines ] 
                                            # it give use a line to start reading a file.
                                            count_file_lines = len(reading_line) - ask_user_how_many_lines 
                                            print()
                                            if ask_user_how_many_lines <= len(reading_line): # if user want less line then file have then this if are work
                                                    # becuse of here we are showing less number that why we use count as user asking lines
                                                    count = ask_user_how_many_lines  # counting for showing lines number
                                                    for i in reading_line[count_file_lines:]: # iterating form list to print line by user want lines to till whi=ole file line data
                                                            print(f"{count}.   {i}",end="")  # printing count number and line data
                                                            count -= 1        # decriment in count
                                                    print()  # becuse of in print()function we are use end="" that why we need to print 2 time here
                                                    print()
                                        
                                            elif ask_user_how_many_lines >= len(reading_line):  # if user want more line then file have then this elif are work
                                                countin_number = [] # we are collect 1 to user wanted lines
                                                for i in range(0,ask_user_how_many_lines+1):# iterating value 0 to ask user line 
                                                    # here we are add but as revers odd for that we are use ask user line to i meas ex :- 30 - 0 = 30 , 30 - 1 , 30 -2 = 29
                                                    # now , why reversing this list element becuse it is used in next loop
                                                    countin_number.append(f"{(ask_user_how_many_lines - i)}") 
                
                                                count = ask_user_how_many_lines - len(reading_line) # count value are ask user - our file length ex :- user ask line = 40 and your file have only 9 lines 
                                                # count = 40 - 9 = 31 now this 31 help use to go with list iterating
                                                for i in reading_line[count_file_lines:]: # iterating loop to upper give count file lines value
                                                    print(f"{countin_number[int(count)]}.   {i}",end="") # here we are use ourrevers list number 
                                                    # list[31] now in this postion you have your file length number 
                                                    count += 1 # now we need incresing our count to get next list item throgh there position
                                                else: # else use for only printing messge when use want more then lines then file have.
                                                    print()  # becuse of in print()function we are use end="" that why we need to print 2 time here
                                                    print()
                                                    print(f"\t\"sorry becuse of you file have only {len(reading_line)} lines and you want to read more then that lines. that was {ask_user_how_many_lines} line. it not posibal that why we print all file data\"".expandtabs(20))
                                                    print()                   
                                
                                    redaing_way(asking_user_whrer_to_read = input(f"Which {ask_user_how_many_lines} lines [Top , Bottom]:- "))  # taking user input for where to user want to start reading

        class updateing():
                    def __init__(self,asking_for_file_name,asking_for_location) -> None:
                        self.asking_for_file_name = asking_for_file_name                
                        self.asking_for_location = asking_for_location
                    
                    def adding_new_data(self) -> None:
                            os.chdir(self.asking_for_location) # we need now change our location to any location becuse of user file are whrer we have no idea.
                            if os.path.exists(self.asking_for_location):# checking path is existing or not
                                print()
                                print("If You Need New Line In Beetween Continu line Then Write Forvesslash '\\'") # printing one small messsge for making new line
                                print()
                                asking_what_u_add = input("Enetr What Do You Like To Append:- ") # taking user new data for adding in file.
                                sepret_data = asking_what_u_add.split("\\") # we are break from here to add after forwardslash line in to newline
                                with open(f"{self.asking_for_file_name}","a") as append_file: # opeing file as a mode that is append mode
                                    for j in sepret_data: # iterating loop in sepreter data list that retun by split() method
                                        if j[0] == " ": # if buy chabge user add some speace to after foewardslash we did not take that space 
                                            append_file.write(f"\n{j[1:]}")# now we didi not space ok becuse of this is the list that why we are performing slicing that start as 1 position to till becuse space are in 0 position
                                        else:
                                            append_file.write(f"\n{j}")# and if there is no space in start that means we did not remove any value for that we use else  
                                
        class deleting():    
                    def __init__(self,asking_for_file_name,asking_for_location) -> None:
                        self.asking_for_file_name = asking_for_file_name                
                        self.asking_for_location = asking_for_location

                    def deleting_filses(self) -> None:
                        os.chdir(self.asking_for_location) # we need now change our location to any location becuse of user file are whrer we have no idea.
                        if os.path.exists(self.asking_for_location):# checking path is existing or not
                            print()
                            ask_agin_toDelet = input("Plase conform are Your Sure to Delet File[say 'y :- yes' or 'n :- no']:- ")
                            if ask_agin_toDelet.lower() == "y":
                                print()
                                print("Press 1 :- To Delet File Permenetliy[it direclty delet file Not move in trush bin]")
                                print("Press 2 :- To Move file in trush bin")
                                print()
                                deleting_pefrence = input("What Is Your Deleting Prefrence like:- ")
                                if deleting_pefrence == "1":
                                    os.remove(self.asking_for_file_name)
                                    print()
                                    print("Thank You For Conformathion we are delet your file.")
                                elif deleting_pefrence == "2":
                                    send2trash.send2trash(self.asking_for_file_name)
                                    print()
                                    print("Thank You For Conformathion we are moving your file in you trush bin.")
        
                            elif ask_agin_toDelet.lower() == "n":
                                 print()
                                 print("Thank You For Conformathion we are not delet your file.")

n = notepad()
option_list = ["writting","reading","updateing","deleting"]
file_open = None
while file_open not in option_list:
        file_open = input("Enter What Would You like To Do [\" Writting \",\" Reading \",\" updateing \",\" Deleting \"]:- ")


if file_open.lower() == "writting":
    w = n.writting()
    w.creating_defult_name_file()
    w.saving_file()

elif file_open.lower() == "reading":
    r = n.reading(input("Enter Your File Name [Plase Provied Your File Name With .extenstion (ex :- if your file is pyhton file that means extenstion was \".py\")]:- ")\
                ,input("We Need Your File Location to search A file[Plase Do Not Provied File Name]:- "))
    r.checking_required_data_give_options()
    r.give_options(asking_user_how_to_read = input("Enter How To Read Files:- ")) # now we ask user which opetion he/she like to read a file) 
            
elif file_open.lower() == "updateing":
    u = n.updateing(input("Enter Your File Name [Plase Provied Your File Name With .extenstion (ex :- if your file is pyhton file that means extenstion was \".py\")]:- ")\
                ,input("We Need Your File Location to search A file[Plase Do Not Provied File Name]:- "))
    u.adding_new_data()

elif file_open.lower() == "deleting":
    d = n.deleting(input("Enter Your File Name [Plase Provied Your File Name With .extenstion (ex :- if your file is pyhton file that means extenstion was \".py\")]:- ")\
                ,input("We Need Your File Location to search A file[Plase Do Not Provied File Name]:- "))
    d.deleting_filses()
