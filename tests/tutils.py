######################################################################
#                                                                    #
#  Copyright 2009-2019 Lucas Heitzmann Gabrielli.                    #
#  This file is part of gdspy, distributed under the terms of the    #
#  Boost Software License - Version 1.0.  See the accompanying       #
#  LICENSE file or <http://www.boost.org/LICENSE_1_0.txt>            #
#                                                                    #
######################################################################

import pytest
import gdspy


@pytest.fixture
def target():
    return gdspy.GdsLibrary(infile='tests/test.gds').cell_dict

def assertsame(c1, c2):
    d1 = c1.get_polygons(by_spec=True)
    d2 = c2.get_polygons(by_spec=True)
    for key in d1:
        assert key in d2
        result = gdspy.boolean(d1[key], d2[key], 'xor', precision=1e-6, layer=key[0] + 1)
        if result is not None:
            c1.add(result)
            c2.add(result)
            result = gdspy.offset(result, -1e-6, precision=1e-7)
            if result is not None:
                gdspy.LayoutViewer(cells=[c1, c2])
        assert result is None

