#!/usr/bin/env python
# -*- coding: utf-8 -*-

from polaris_tools_modules.base import Dust


"""Add your defined classes to this dictionary with a unique name
 to use it with PolarisTools.
"""


def update_dust_dict(dictionary):
    dust_dict = {
        'custom': CustomDust,
    }
    dictionary.update(dust_dict)


class CustomDust(Dust):
    """Change this to the dust component you want to use.
    """

    def __init__(self, file_io, parse_args):
        """Initialisation of the dust parameters.

        Args:
            file_io : Handles file input/output and all necessary paths.
        """
        Dust.__init__(self, file_io, parse_args)

        # Define the dust catalog file in the POLARIS standard file format
        # (relative to the polaris/input/ directory)
        self.parameter['dust_cat_file'] = 'custom.dat'
        # Relative fraction of this dust composition to mix multiple dust compositions
        self.parameter['fraction'] = 1.0
        # Material density of the custom composition [kg/m^3]
        self.parameter['material_density'] = 2500
        # Minimum dust grain size
        self.parameter['amin'] = 5e-9
        # Maximum dust grain size
        self.parameter['amax'] = 250e-9
        # Possible dust size distributions 'plaw', 'plaw-ed', 'logn'
        self.parameter['size_keyword'] = 'plaw'
        # List of size parameter for dust size distribution (plaw -> [exponent])
        self.parameter['size_parameter'] = [-3.5]

    def get_command(self):
        """Provides dust component command line for POLARIS .cmd file.

        Note:
            This demonstrates how to mix multiple dust components together.

        Returns:
            str: Command line to consider the custom dust component.
        """
        # This shows how to mix multiple dust components and use them as one
        new_command_line = str()
        dust = self.dust_chooser.get_module_from_name('silicate_oblate')
        dust.parameter['fraction'] = 0.625
        new_command_line += dust.get_command_line()
        dust = self.dust_chooser.get_module_from_name('graphite_oblate')
        dust.parameter['fraction'] = 0.375
        new_command_line += dust.get_command_line()
        return new_command_line
