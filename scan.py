#!/usr/bin/env python2

""" Mass scan. """

from MassScan import MassScan

if __name__ == "__main__":
    X = [200*i for i in range(1, 11)]
    Y = [10*i for i in range(8, 19)]

    MY_SCAN = MassScan()
    MY_SCAN.set_threshold(.001)
    MY_SCAN.l_prmtr_x = X
    MY_SCAN.l_prmtr_y = Y
    MY_SCAN.set_parameter_add_scale_x(2, 2.)

    MY_SCAN.set_parameter(1, 23)

    output = 'output76_higgsino'
    name = 'higgsino-scan-mum1m2'

    PLOTS = MY_SCAN.do_scan()
    PLOTS.set_rootfile('{}/{}.root'.format(output, name))
    PLOTS.set_directory('{}/{}'.format(output, name))
    #PLOTS.set_star(-1071.46632, 534.761347)
    PLOTS.plot()
