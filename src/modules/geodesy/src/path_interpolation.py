#!/usr/bin/env python

"""Interpolates path from previously plotted points"""
 
import rospy

import gps_parser
from path_interpolator_ECEF import PathInterpolatorECEF
from path_interpolator_UTM  import PathInterpolatorUTM

def main():
    rospy.init_node('interpolation_node', anonymous = True)

    chosenHeight = 30.0

    # From https://www.maps.ie/coordinates.html at SJSU
    filePath = rospy.get_param("~file_path")
    inputLatitudes, inputLongitudes, inputHeights = gps_parser.read_file_coarse_points(filePath, chosenHeight)
    # print("\ninputLatitudes: {}\ninputLongitudes: {}\ninputHeights: {}".format(inputLatitudes, inputLongitudes, inputHeights))
    
    ##### ECEF #####
    interpolatorECEF = PathInterpolatorECEF(inputLatitudes, inputLatitudes, inputHeights, chosenHeight)

    ##### ENU #####


    ##### UTM #####
    # interpolatorUTM = PathInterpolatorUTM(inputLatitudes, inputLongitudes)
    
    try:
        interpolatorECEF.interpolation_publish_ECEF()
        # interpolatorUTM.interpolation_publish_UTM()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

