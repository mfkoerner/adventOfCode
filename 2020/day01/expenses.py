#!/usr/bin/env python3

def main():
   print( getProd2() )
   print( getProd3() )

def getProd2():
   with open( "expenses.txt" ) as f:
      expenses = [ int( i.rstrip("\n") ) for i in f.readlines() ]

   n = len( expenses )
   for i in range( n ):
      for j in range( i + 1, n ):
         if expenses[ i ] + expenses[ j ] == 2020:
            return( expenses[ i ] * expenses[ j ] )

def getProd3():
   with open( "expenses.txt" ) as f:
      expenses = [ int( i.rstrip("\n") ) for i in f.readlines() ]

   n = len( expenses )
   for i in range( n ):
      for j in range( i + 1, n ):
         for k in range( j + 1, n ):
            if expenses[ i ] + expenses[ j ] + expenses[ k ] == 2020:
               return( expenses[ i ] * expenses[ j ] * expenses[ k ] )

if __name__ == "__main__":
   main()
