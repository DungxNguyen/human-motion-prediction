from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from six.moves import xrange # pylint: disable=redefined-builtin
import copy

import data_utils


def main():
    generate_linear_angle_movement()


def generate_linear_angle_movement(steps=1000, cycle=150):
    J0 = np.array([0, 0, 0])
    J1 = np.array([0, -1, 1])

    i = 0
    while True:
        for k in range(cycle):
            theta = np.pi / cycle * k - np.pi / 4 *3
            J2 = np.array([0, np.sin(theta), np.cos(theta)])
            print(data_utils.xyz2expmap(J0, J1, J2))

            i += 1
            if (i >= steps):
                break
    
        if (i >= steps):
            break

if __name__ == "__main__":
    main()
