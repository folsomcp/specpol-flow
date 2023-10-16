#!/usr/bin/python3
#
#A wrapper for quickly plotting a set of LSD profiles from the command line

import matplotlib.pyplot as plt
try:
    import specpolFlow as pol
except ModuleNotFoundError:
    #If specpolFlow is not installed or in the python path
    #try guessing the location and adding it temporarily
    import sys
    import os
    #loc0 = sys.path[0] #try this module's directory from the Python path list
    #try getting this module's directory from a predefined attribute
    loc0 = os.path.dirname(__file__) 
    sys.path.insert(0, os.path.join(loc0, '..', '..'))
    import specpolFlow as pol


#For running as a terminal program
if __name__ == "__main__":
    #Take input file names as command line arguments,
    #with some additional optional control parameters.
    import argparse
    parser = argparse.ArgumentParser(description='Plot a set of LSD profiles.')
    parser.add_argument("fileList", nargs='*',
                        help="LSD profile files to plot, can be more than one file.")
    parser.add_argument("-l", "--legend", action='store_true',
                        help="Optionally, show a legend of file names")
    parser.add_argument("-s", "--save", default=None,
                        help="Optionally, save the plot to this file")
    args = parser.parse_args()
    #Process the command line parameters
    fileList = []
    for fileName in args.fileList:
        fileList += [fileName]
    showLegend = args.legend
    saveName = args.save

    fig = None
    axs = None
    for fileName in fileList:
        lsd = pol.read_lsd(fileName)
        fig, axs = lsd.plot(fig=fig, ls='-', label=fileName)

    if showLegend:
        axs[-1].legend(loc='lower left')
    if saveName is not None:
        print('saving to', saveName)
        fig.savefig(saveName)
    
    plt.show()