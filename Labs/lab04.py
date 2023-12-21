#Get the number of days and loop through this number
Day = int(input())
for D in range(1, Day + 1):
    #Getting the number of Fighting Pairs and initializing an 2d array to store them
    PossFights = int(input())
    FightPairs = [[0 for i in range(2)] for j in range(PossFights)]
    for i in range(PossFights):
        FightPairs[i] = input().split()
    #Getting the procedures string and spliting it into lists for the number of them and the procedure itself
    Procedures = input().split()
    size = len(Procedures)
    Procedure = []
    NProcedure = []
    i = 0
    while i < size:
        Procedure.append(Procedures[i])
        i += 1
        NProcedure.append(Procedures[i])
        i += 1
    j = 0
    size2 = len(NProcedure)
    #Casting the number of avaliable procedures into int
    while j < size2:
        NProcedure[j] = int(NProcedure[j])
        j += 1
    #Getting the number of dogs and getting their name and desired procedure
    NumDogs = int(input())
    Dog = []
    DogProcedure = []
    for k in range(NumDogs):
        DogString = input().split()
        Dog.append(DogString[0])
        DogProcedure.append(DogString[1])
    #Creating a list with all 0's to see how many times a procedure has already been done
    NDogProcedures = [0] * size2
    #Algorithm to separate dogs into those that were attended, those who were not, and those that desired procedures who were not avaliable
    AttendedDogs = []
    NotAttendedDogs = []
    NoProcedureDogs = []
    #This loops through all dogs and see if the desired procedure is avaliable for the day
    for k in range(NumDogs):
        for l in range(size2):
            if DogProcedure[k] == Procedure[l]:
                if NDogProcedures[l] > NProcedure[l] - 1:
                    NotAttendedDogs.append(Dog[k])
                else:
                    AttendedDogs.append(Dog[k])
                NDogProcedures[l] += 1
        if DogProcedure[k] not in Procedures:
            NoProcedureDogs.append(Dog[k])
    #Algorithm to check if there are any pair of dogs that fight on the same day
    l = 0
    NFights = 0
    while l < PossFights:
        if all(item in Dog for item in FightPairs[l]) == 1:
            NFights += 1
        l += 1
    #Printing the output
    print("Dia:", D)
    print("Brigas:", NFights)
    if len(AttendedDogs) > 0:
        print("Animais atendidos: ", end = '')
        print(*AttendedDogs, sep = ', ', end = '')
        print()
    if len(NotAttendedDogs) > 0:
        print("Animais não atendidos: ", end = '')
        print(*NotAttendedDogs, sep = ', ', end = '')
        print()
    for x in range(len(NoProcedureDogs)):
        print("Animal", NoProcedureDogs[x], "solicitou procedimento não disponível.")
    print()