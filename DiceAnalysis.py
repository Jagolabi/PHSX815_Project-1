import sys
import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s" % sys.argv[0])
        print ("   -input [filename]  name of file for data")
        print
        sys.exit(1)
        
    haveInput = False
        
    if '-input' in sys.argv:
        p = sys.argv.index('-input')
        InputFile = sys.argv[p+1]
        haveInput = True
           
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")	
        print ("   -input [filename]  name of file for data")
    
    # Lets import data.txt
    filename = 'Generated.txt'
    dat = np.loadtxt(filename)
    flat = dat.flatten()
    add=np.sum(dat,axis=0)

    plt.figure()
    # creates histogram
    n, bins, patches = plt.hist(flat, bins=range(20), alpha=0.7 ,rwidth=0.95, density = True, facecolor = "brown")

    # plot formating options
    plt.xlabel('face number of dice rolls')
    plt.ylabel('Probablity')
    plt.title(str(len(flat))+ ' dice rolls')
    plt.grid(axis='y', alpha=0.75)
    plt.xlim(xmin=0.5, xmax = 12)
    #plt.xticks(range(9))
    # show figure (program only ends once closed
    plt.show()


    # creates histogram
    n, bins, patches = plt.hist(flat, bins=range(20) , alpha=0.7, rwidth=0.95, density = True, facecolor = "red")

    # plot formating options
    plt.xlabel('Sum of the face numbers for each experiment')
    plt.ylabel('Probability')
    plt.title(str(len(flat))+' experiments of '+' dice rolls')
    plt.grid(axis='y', alpha=0.75)
    plt.xlim([len(flat[0]), 9.0*len(flat[0])+2])
    #plt.xticks(range(len(dat[0])-1,9*len(dat[0])+2))
    # show figure (program only ends once closed
    plt.show()
