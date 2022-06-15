import ForEV as evc
import ForStats as statc

print("[1] Calculate Stats")
print("[2] Calculate EV")

PokemonNature_Attack = 1
PokemonNature_Defense = 1
PokemonNature_SPAttack = 1
PokemonNature_SPDefense = 1
PokemonNature_Speed = 1

index = int(input("Enter: "))


if index == 1:
    print("STATS CALCULATOR")

    Pokemon = str(input("Pokemon's Name: "))

    PokemonLevel = int(input("Pokemon's level: "))

    PokemonNature = str.lower(input("Pokemon's Nature: "))

    PokemonBase = int(input("Pokemon's Base: "))

    PokemonIV2 = int(input("Pokemon's IV: "))

    PokemonEV2 = int(input("Pokemon's EV: "))

    #This Section is for Neutral Nature
    if PokemonNature in ['quirky','bashful','serious','docile','hardy']:
        PokemonNature_Attack = 1
        PokemonNature_Defense = 1
        PokemonNature_SPAttack = 1
        PokemonNature_SPDefense = 1
        PokemonNature_Speed = 1
    #This Section is for Attack Nature
    elif PokemonNature in ['lonely','brave','adamant','naughty']:
        PokemonNature_Attack = 1.1
        if PokemonNature in ['lonely']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['brave']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['adamant']:
            PokemonNature_SPAttack = 0.9
        elif PokemonNature in ['naughty']:
            PokemonNature_SPDefense = 0.9
    #This Section is for Defense Nature
    elif PokemonNature in ['bold','relaxed','impish','lax']:
        PokemonNature_Defense = 1.1
        if PokemonNature in ['bold']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['relaxed']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['impish']:
            PokemonNature_SPAttack = 0.9
        elif PokemonNature in ['lax']:
            PokemonNature_SPDefense = 0.9
    #This Section is for Speed Nature
    elif PokemonNature in ['timid','hasty','jolly','naive']:
        PokemonNature_Speed = 1.1
        if PokemonNature in ['timid']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['hasty']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['jolly']:
            PokemonNature_SPAttack = 0.9
        elif PokemonNature in ['naive']:
            PokemonNature_SPDefense = 0.9
    #Pokemon Special Attack Nature
    elif PokemonNature in ['modest','mild','quiet','rash']:
        PokemonNature_SPAttack = 1.1
        if PokemonNature in ['modest']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['mild']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['quiet']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['rash']:
            PokemonNature_SPDefense = 0.9
    #This Section is for Special Defense Nature
    elif PokemonNature in ['calm','gentle','sassy','careful']:
        PokemonNature_SPDefense = 1.1
        if PokemonNature in ['calm']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['gentle']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['sassy']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['careful']:
            PokemonNature_SPAttack = 0.9
    
    print("\n[1] HP")
    print("[2] Attack")
    print("[3] Defense")
    print("[4] Special Attack")
    print("[5] Special Defense")
    print("[6] Speed")
    
    ind = int(input("Enter index: "))

    if ind == 1:
        PokemonBase_HP = int(input("\nEnter Base HP: "))
        PokemonIV = int(input("Pokemon IV: "))
        PokemonEV = int(input("Pokemon EV: "))
        print("Total HP: ", statc.ForStats.Stat_HP(PokemonBase_HP,PokemonIV,PokemonEV,PokemonLevel),"\n")
    if ind == 2:
        PokemonBase_Attack = int(input("\nEnter Base Attack Points: "))
        PokemonIV = int(input("Pokemon IV: "))
        PokemonEV = int(input("Pokemon EV: "))
        print("Total Attack Points: ", statc.ForStats.OtherStat_Attack(PokemonBase_Attack,PokemonIV,PokemonEV,PokemonLevel,PokemonNature_Attack),"\n")
    if ind == 3:
        PokemonBase_Defense = int(input("\nEnter Base Defense Points: "))
        PokemonIV = int(input("Pokemon IV: "))
        PokemonEV = int(input("Pokemon EV: "))
        print("Total Defense Points: ", statc.ForStats.OtherStat_Defense(PokemonBase_Defense,PokemonIV,PokemonEV,PokemonLevel,PokemonNature_Defense),"\n")    
    if ind == 4:
        PokemonBase_SPAttack = int(input("\nEnter Base Special Attack Points: "))
        PokemonIV = int(input("Pokemon IV: "))
        PokemonEV = int(input("Pokemon EV: "))
        print("Total Special Attack Points: ", statc.ForStats.OtherStat_SPAttack(PokemonBase_SPAttack,PokemonIV,PokemonEV,PokemonLevel,PokemonNature_SPAttack),"\n")
    if ind == 5:
        PokemonBase_SPDefense = int(input("\nEnter Base Special Defense Points: "))
        PokemonIV = int(input("Pokemon IV: "))
        PokemonEV = int(input("Pokemon EV: "))
        print("\nTotal Special Defenes Points: ", statc.ForStats.OtherStat_SPDefense(PokemonBase_SPDefense,PokemonIV,PokemonEV,PokemonLevel,PokemonNature_SPDefense),"\n")
    if ind == 6:
        PokemonBase_Speed = int(input("\nEnter Base Speed Points: "))
        PokemonIV = int(input("Pokemon IV: "))
        PokemonEV = int(input("Pokemon EV: "))
        print("Total Speed Points: ", statc.ForStats.Other_Stat_Speed(PokemonBase_Speed,PokemonIV,PokemonEV,PokemonLevel,PokemonNature_Speed),"\n")

respond = True
PokemonLevel =0
PokemonStat = ["HP","Attack","Defense","Special Attack","Special Defenes","Speed"]
PokemonBase = [6]
PokemonIV2 = [6]
PokemonEV2 = [6]

if index == 2:
    print("Evs")

    while respond:
        PokemonLevel = int(input("Pokemon's level: "))
        if PokemonLevel > 0 and PokemonLevel < 101:
            respond = False
    
    
    PokemonNature = str.lower(input("Enter Pokemon's Nature: "))

    print("Base Stats: ")   
    for x in range(1, 6):
        PokemonBase.append(int(input("Enter "+ PokemonStat[x] + ": ")))
    
    print("Pokemon IV on each Stat: ")    
    i = 1
    while i < 7:
        PokemonIV2.append(int(input("Enter "+PokemonStat[i]+" IV: ")))
        if (PokemonIV2[i] < 0 or PokemonIV2[i] > 31):
            i = i - 1
            print("value should be between 0 and 31")
        i = i + 1

            

    print("Pokemon EV on each Stat: ")
    j = 1
    while j < 7:
        PokemonEV2.append(int(input("Enter "+PokemonStat[j]+" EV: ")))
        if (PokemonEV2[j] < 0 or PokemonEV2[j] > 255):
            j = j - 1
            print("value should be between 0 and 255")
        j = j + 1    

    #Neutral Nature
    if PokemonNature in ['quirky','bashful','serious','docile','hardy']:
        PokemonNature_Attack = 1
        PokemonNature_Defense = 1
        PokemonNature_SPAttack = 1
        PokemonNature_SPDefense = 1
        PokemonNature_Speed = 1
    #Attack Nature
    elif PokemonNature in ['lonely','brave','adamant','naughty']:
        PokemonNature_Attack = 1.1
        if PokemonNature in ['lonely']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['brave']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['adamant']:
            PokemonNature_SPAttack = 0.9
        elif PokemonNature in ['naughty']:
            PokemonNature_SPDefense = 0.9
    #Defense Nature
    elif PokemonNature in ['bold','relaxed','impish','lax']:
        PokemonNature_Defense = 1.1
        if PokemonNature in ['bold']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['relaxed']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['impish']:
            PokemonNature_SPAttack = 0.9
        elif PokemonNature in ['lax']:
            PokemonNature_SPDefense = 0.9
    #Speed Nature
    elif PokemonNature in ['timid','hasty','jolly','naive']:
        PokemonNature_Speed = 1.1
        if PokemonNature in ['timid']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['hasty']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['jolly']:
            PokemonNature_SPAttack = 0.9
        elif PokemonNature in ['naive']:
            PokemonNature_SPDefense = 0.9
    #Special Attack Nature
    elif PokemonNature in ['modest','mild','quiet','rash']:
        PokemonNature_SPAttack = 1.1
        if PokemonNature in ['modest']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['mild']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['quiet']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['rash']:
            PokemonNature_SPDefense = 0.9
    #Special Defense Nature
    elif PokemonNature in ['calm','gentle','sassy','careful']:
        PokemonNature_SPDefense = 1.1
        if PokemonNature in ['calm']:
            PokemonNature_Attack = 0.9
        elif PokemonNature in ['gentle']:
            PokemonNature_Defense = 0.9
        elif PokemonNature in ['sassy']:
            PokemonNature_Speed = 0.9
        elif PokemonNature in ['careful']:
            PokemonNature_SPAttack = 0.9

    
    print("[1] Attack")
    print("[2] Defense")
    print("[3] Special Attack")
    print("[4] Special Defense")
    print("[5] Speed")
    
    ind = int(input("Enter index: "))

    if ind == 1:
        Modifier = PokemonNature_Attack
    if ind == 2:
        Modifier = PokemonNature_Defense
    if ind == 3:
        Modifier = PokemonNature_SPAttack
    if ind == 4:
        Modifier = PokemonNature_SPDefense
    if ind == 5:
        Modifier = PokemonNature_Speed

    IncreaseValue = int(input("Enter Desired Increase: "))

    call = evc.ForEV.ForEV_call( PokemonBase[ind+1],PokemonIV2[ind+1],PokemonEV2[ind+1],PokemonLevel)

    NeedEV = evc.ForEV.Need4EV( IncreaseValue,Modifier,call,PokemonLevel)

    print("The total amount of Evs needed for your pokemon ", NeedEV)
