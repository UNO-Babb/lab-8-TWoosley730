#ProcessData.py
#Name: Trevor Woosley
#Date: 04/06/2025
#Assignment: Names

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    student_id = makeID(data[0], data[1], data[3])
    print(student_id)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  
  idLen = len(idNum)
  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + idNum[idLen - 3: ]

  return id
  


if __name__ == '__main__':
  main()
