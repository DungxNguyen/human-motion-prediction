from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from six.moves import xrange # pylint: disable=redefined-builtin
import copy

import data_utils


def main():
    xyz2rotmat_test()


def xyz2rotmat_test():
    J0 = np.random.rand(3)
    J1 = np.random.rand(3)
    J2 = np.random.rand(3)

    u = data_utils.norm_vec(J1 - J0)
    v = data_utils.norm_vec(J2 - J0)

    np.testing.assert_allclose(np.matmul(data_utils.xzy2rotmat(J0, J1, J2), u), v, rtol=1e-05, atol=1e-08)


if __name__ == "__main__":
    main()
