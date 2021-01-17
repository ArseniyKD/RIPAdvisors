class Course:
    def __init__(self, courseName, fallTimes, winterTimes, prereqs, fallConflicts, winterConflicts):
        self.courseName = courseName
        self.fallTimes = fallTimes
        self.winterTimes = winterTimes
        self.prereqs = prereqs
        self.fallConflicts = fallConflicts
        self.winterConflicts = winterConflicts

def splittingFun(time):
    iterations = len(time) // 8
    tuple_list = []
    start = 0
    end = 4
    for i in range(iterations):
        temp_tuple = (time[start:end], time[end:end + 4])
        start += 8
        end += 8
        tuple_list.append(temp_tuple)

    return tuple_list

courseNames = ["CMPUT174","CMPUT175","CMPUT201","CMPUT204","CMPUT229","CMPUT272","CMPUT291","CMPUT300","CMPUT301","CMPUT302","CMPUT304","CMPUT312","CMPUT313","CMPUT325","CMPUT328","CMPUT340","CMPUT350","CMPUT355","CMPUT361","CMPUT366","CMPUT379","CMPUT382","CMPUT391","CMPUT401","CMPUT402","CMPUT403","CMPUT404","CMPUT412","CMPUT415","CMPUT455","CMPUT466","CMPUT474","CMPUT481"]
fallString = "080009200930105011001220123013501400152015301650,09000950100010501200125014001450,1300135012301350,10001050,1000105013001350,09301050,11001220,12301350,1300135009301050,X,11001150,14001520,1100122011001220,X,X,X,17001950,11001220,08000920,X,14001520,12001250,X,09301050,09001050,X,X,X,X,14001520,09301050,12301350,X"
fallTime = fallString.split(",")
winterString = "0930105012301350,090009501000105012001250,1300135012301350,1000105011001150,09301050,0930105012301350,11001220,18302130,10001050,14001520,X,X,11001220,09301050,X,12301350,X,X,12301350,11001150,09000950,14001450,09301050,09001050,15301650,15001650,13001350,15301650,X,14001520,11001220,09301050,10001050"
winterTime = winterString.split(",")
prereqString = "X,CMPUT174,CMPUT175,CMPUT175272MATH144,CMPUT175201,CMPUT175,CMPUT175,X,CMPUT201,CMPUT301,CMPUT204MATH225STAT151,CMPUT175201204,CMPUT201204229STAT252,CMPUT201204229MATH125,CMPUT175MATH144125STAT252,CMPUT204MATH125214STAT151,CMPUT201204,CMPUT201,CMPUT201204MATH125,CMPUT204STAT151,CMPUT201204229,CMPUT201229,CMPUT201204291,CMPUT301,CMPUT301,CMPUT301,CMPUT301391,CMPUT201204340MATH214STAT252,CMPUT229,X,CMPUT340STAT151,CMPUT204229MATH225,CMPUT201379"
prereqs = prereqString.split(",")

listClasses = []


for j in range(33):
    fallList = splittingFun(fallTime[j])
    winterList = splittingFun(winterTime[j])
    x = Course(courseNames[j], fallList, winterList, prereqs[j],[],[])
    listClasses.append(x)

# for i in listClasses:
#     flag1 = False
#     for j in listClasses:
#         flag2 = False
#         if flag2:
#             break
#         for k in i.fallTimes:
#             flag3 = False
#             if flag3:
#                 break
#             for l in i.winterTimes:
#                 flag4 = False
#                 if k[0] < l[1]:
#                     if j not in i.fallConflicts:
#                         i.fallConflicts.append(j)
#                 else:
#                     if j in i.fallConflicts:
#                         i.fallConflicts.remove(j)
#                         flag2 = True
#                         flag3 = True
#                         break
stopComparing1, stopJ1, stopK1, stopL1 = False, False, False, False
for i in listClasses:
    # print("1")
    if stopComparing1:
        stopComparing1 = False
        continue
    for j in listClasses:
        # print("2")
        if i == j:
            continue
        if stopJ1:
            stopJ1 = False
            break
        for k in i.fallTimes:
            # print("3")
            if stopK1:
                stopK1 = False
                break
            for l in j.fallTimes:
                if stopL1:
                    stopL1 = False
                    break
                if k[0] < l[1]:
                    if j not in i.fallConflicts:
                        i.fallConflicts.append(j)
                        # print("conflict")
                else:
                    if j in i.fallConflicts:
                        i.fallConflicts.remove(j)
                        stopComparing1, stopJ1, stopK1, stopL1 = True, True, True, True


stopComparing2, stopJ2, stopK2, stopL2 = False, False, False, False
for i in listClasses:
    # print("1")
    if stopComparing2:
        stopComparing2 = False
        continue
    for j in listClasses:
        # print("2")
        if i == j:
            continue
        if stopJ2:
            stopJ2 = False
            break
        for k in i.winterTimes:
            # print("3")
            if stopK2:
                stopK2 = False
                break
            for l in j.winterTimes:
                if stopL2:
                    stopL2 = False
                    break
                if k[0] < l[1]:
                    if j not in i.winterConflicts:
                        i.winterConflicts.append(j)
                        # print("conflict")
                else:
                    if j in i.winterConflicts:
                        i.winterConflicts.remove(j)
                        stopComparing2, stopJ2, stopK2, stopL2 = True, True, True, True


for i in range(33):
    # print(listClasses[i].courseName)
    if len(listClasses[i].winterConflicts) > 0:
        print(listClasses[i].courseName)
        print(listClasses[i].winterConflicts[0].courseName)
        print()
