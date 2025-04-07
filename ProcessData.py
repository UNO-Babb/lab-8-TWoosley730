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
  line = inFile.readline()


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  print(first, last, idNum)
  


if __name__ == '__main__':
  main()
