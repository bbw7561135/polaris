#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from polaris_tools_modules.base import StellarSource

"""Add your defined classes to this dictionary with a unique name
 to use it with PolarisTools.
"""


def update_sources_dict(dictionary):
    sources_dict = {
        'custom': CustomStar,
    }
    dictionary.update(sources_dict)


class CustomStar(StellarSource):
    """Change this to the star you want to use.
    """

    def __init__(self, file_io, parse_args):
        """Initialisation of the radiation source parameters.

        Args:
            file_io : Handles file input/output and all necessary paths.
        """
        StellarSource.__init__(self, file_io, parse_args)

        # Position of the star [m, m, m]
        self.parameter['position'] = [0, 0, 0]
        # Effective temperature of the star [K]
        self.parameter['temperature'] = 4000
        # Radius of the star [R_sun] or luminosity [L_sun]
        self.parameter['radius'] = 2.0
        # Number of photons if no number is chosen via --photons
        self.parameter['nr_photons'] = 1e6
        # Can the velocity field be calculated by only this star in the center?
        self.parameter['kepler_usable'] = True
        # Mass of the star [M_sun] (for Keplerian rotation)
        self.parameter['mass'] = 0.7

    def get_command(self):
        """Provides radiation source command line for POLARIS .cmd file.

        Returns:
            str: Command line to consider the stellar source.
        """
        '''To add multiple stars, use the following:
        new_command_line = str()
        self.parameter['temperature'] = 8000
        self.parameter['radius'] = 4.0
        new_command_line += self.get_command_line()
        self.parameter['temperature'] = 5000
        self.parameter['radius'] = 3.0
        new_command_line += self.get_command_line()
        return new_command_line
        '''
        return self.get_command_line()
