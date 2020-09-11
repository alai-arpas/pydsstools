import pandas as pd

# from hec.script import *
# from hec.heclib.dss import *
# from hec.heclib.util import *
# from hec.io import *

PathInputfile = "F:/Varie/DSS/"

DssFileName = "F:/Varie/DSS/Misure2.dss"
Num_of_files = 1

for k in range(1, Num_of_files + 1):
    filedata = open(PathInputfile + "Pluvio_" + str(k) + ".dat", "r")
    linedata = filedata.readline()
    sline = linedata.split()  # divide la stringa
    Stz = sline[1:][0]
    Stz = Stz.replace("\n", "")

    linedata = filedata.readline()
    sline = linedata.split()
    StartDate = sline[1:][0]

    linedata = filedata.readline()
    sline = linedata.split()
    EndDate = sline[1:][0]

    linedata = filedata.readline()
    sline = linedata.split()
    DataStartTime = sline[1:][0]

    linedata = filedata.readline()
    sline = linedata.split()
    DataEndTime = sline[1:][0]

    linedata = filedata.readline()
    sline = linedata.split()
    DataTimeStep = sline[1:][0]

    linedata = filedata.readline()
    sline = linedata.split()
    DataType = sline[1:][0]

    linedata = filedata.readline()
    sline = linedata.split()
    DataUnit = sline[1:][0]

    Raindataset = []
    Raindataset = filedata.read()

    raindata = Raindataset.split()
    lendata = len(raindata)
    floatraindata = []
    for j in range(0, lendata - 1):
        floatraindata.append(float(raindata[j]))

    print(len(floatraindata))

    try:
        # myDss = HecDss.open(DssFileName)
        #
        # tsc = TimeSeriesContainer()
        # #      "A"           +"B" +    "c"        d  e              f
        MyPath = "/FLUMENDOSA/" + Stz + "/" + DataType + "//" + DataTimeStep + "/FIXED/"
        print(MyPath)
        # tsc.fullName = MyPath
        # start = HecTime(StartDate, DataStartTime)
        #
        # tsc.interval = int(DataTimeStep[:len(DataTimeStep) - 3])
        # flows = floatraindata
        # times = []
        # cnt = 0
        # for value in flows:
        #     times.append(start.value())
        #     start.add(tsc.interval)
        # tsc.times = times
        # tsc.values = flows
        # tsc.numberValues = len(flows)
        # tsc.units = DataUnit  # "CFS"
        # tsc.type = DataType  # "PER-AVER"
        # myDss.put(tsc)
    finally:
        # myDss.close()
        print("fine")
