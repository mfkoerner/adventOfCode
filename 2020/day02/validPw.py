#!/usr/bin/env python3

def main():
   print( numValidA() )
   print( numValidB() )

def numValidA():
   with open( "validPw.txt" ) as f:
      inlines = [ i.rstrip( "\n" ) for i in f.readlines() ]

   # create entries of the following format
   # { "reqLetter": "p", "min": 9, "max": 11, "pw": "pppppppppxblp" }
   entries = [ decodeLine( i ) for i in inlines ]
   
   numValid = 0
   for e in entries:
      numMatch = e["pw"].count( e["reqLetter"] )
      if numMatch >= e["min"] and numMatch <= e["max"]:
         numValid+=1
   return numValid

def numValidB():
   with open( "validPw.txt" ) as f:
      inlines = [ i.rstrip( "\n" ) for i in f.readlines() ]

   # create entries of the following format
   # { "reqLetter": "p", "min": 9, "max": 11, "pw": "pppppppppxblp" }
   entries = [ decodeLine( i ) for i in inlines ]
   
   numValid = 0
   for e in entries:
      pw = e["pw"]
      minVal = e["min"]
      maxVal = e["max"]
      let = e["reqLetter"]
      if ( ( int( pw[minVal-1] == let ) +
             int( pw[maxVal-1] == let ) ) == 1 ):
         numValid += 1
   return numValid

def decodeLine( line ):
   minmaxStr, letterStr, pwStr = line.split()
   minValStr, maxValStr = minmaxStr.split( "-" )
   minVal = int( minValStr )
   maxVal = int( maxValStr )
   reqLetter = letterStr[0]
   return {
      "reqLetter": reqLetter,
      "min": minVal,
      "max": maxVal,
      "pw": pwStr,
   }

if __name__ == "__main__":
   main()
