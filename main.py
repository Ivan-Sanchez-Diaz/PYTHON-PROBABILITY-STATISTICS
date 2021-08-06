import os
os.system("cls")
example = [82,85,86,87,87,89,89,90,91,91,92,93,94,95,95,95,95,95,97,98,99,99,100,100,101,101,103,103,103,104,105,105,106,107,107,107,109,110,110,111]

def excel(array):

  totalClass = len(array)

  array.sort()
  print("Original:" + str(array))
  interval = int(array[0]) - int(array[totalClass-1])
  print("Interval:"+ str(abs(interval)))

  #classNumber = input("number of classes:")
  #valuesNumber = input("number of values:")
  #classNumber = int(classNumber)
  #valuesNumber = int(valuesNumber)

#In this case, 6 classes are recommended each with 5 values
  print("--We chose 6 classes of 5 values ​​because 6 times 5 is equal to 30, and it is the closest we get to 29 (the interval)--")
  classNumber = 6
  valuesNumber = 5

  classInterval = []
  off = 0

  for i in range(classNumber):
    parameter = (array[0]+off,array[0]+valuesNumber+off-1)
    classInterval.append(parameter)
    off = off + valuesNumber
  print("Class Interval: "+str(classInterval))

  middlePoint = []

  for i in classInterval:
    middlePoint.append((i[0]+i[1])/2)
  print("Middle Point: "+str(middlePoint))

  classFrequency = []

  for i in classInterval:
    count = 0
    for j in array:
      if (j>= i[0] and j<=i[1]):
        count = count + 1
    classFrequency.append(count)
  print("Class Frecuency: " + str(classFrequency))

  relativeFrequency = []

  for i in classFrequency:
    relativeFrequency.append(i/totalClass)
  print("Relative Frequency: " + str(relativeFrequency))



if __name__ == "__main__":
  excel(example)
 