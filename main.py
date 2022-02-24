#!/usr/bin/python3

import pprint # pretty print object

from util import generateOutputFile
from util import readBuildingFloorFile
from util import readMaterialFile
from util import sendEmail

def main():
    building_floor_dict = readBuildingFloorFile()
    material_dict = readMaterialFile()

    # pp = pprint.PrettyPrinter(indent = 4)
    # pp.pprint(building_floor_dict)
    # pp.pprint(material_dict)

    generateOutputFile(building_floor_dict,material_dict)
    sendEmail()

if __name__ == "__main__":
    main()
