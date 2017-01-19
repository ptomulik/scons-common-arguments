""" SConsCommonArguments.arTests

Unit tests for SConsCommonArguments.ar
"""

__docformat__ = "restructuredText"

#
# Copyright (c) 2015 by Pawel Tomulik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import SConsCommonArguments.ar as tested
import unittest

# The mock module does not come as a part of python 2.x stdlib, it has to be
# installed separatelly. Here we detect whether mock is present and if not,
# we skip all the tests that use mock.
_mock_missing = True
try:
    # Try unittest.mock first (python 3.x) ...
    import unittest.mock as mock
    _mock_missing = False
except ImportError:
    try:
        # ... then try mock (python 2.x)
        import mock
        _mock_missing = False
    except ImportError:
        # mock not installed
        pass

#############################################################################
class Test__arguments(unittest.TestCase):
    """Test constants in SConsArguments module"""
    def test_AR(self):
        "Test SConsCommonArguments.ar: AR"
        args = filter(lambda r : r['name'] == 'AR', tested._arguments)
        self.assertEqual([{
            'name'      : 'AR',
            'help'      : 'The static library archiver',
            'metavar'   : 'PROG'}],
            args)

    def test_ARFLAGS(self):
        "Test SConsCommonArguments.ar: ARFLAGS"
        args = filter(lambda r : r['name'] == 'ARFLAGS', tested._arguments)
        self.assertEqual([{
            'name'      : 'ARFLAGS',
            'help'      : 'General options passed to the static library archiver',
            'metavar'   : 'FLAGS'}],
            args)

    def test_RANLIB(self):
        "Test SConsCommonArguments.ar: RANLIB"
        args = filter(lambda r : r['name'] == 'RANLIB', tested._arguments)
        self.assertEqual([{
            'name'      : 'RANLIB',
            'help'      : 'The archive indexer',
            'metavar'   : 'PROG'}],
            args)

    def test_RANLIBFLAGS(self):
        "Test SConsCommonArguments.ar: RANLIBFLAGS"
        args = filter(lambda r : r['name'] == 'RANLIBFLAGS', tested._arguments)
        self.assertEqual([{
            'name'      : 'RANLIBFLAGS',
            'help'      : 'General options passed to the archive indexer',
            'metavar'   : 'FLAGS'}],
            args)

#############################################################################
if __name__ == "__main__":
    ldr = unittest.TestLoader()
    suite = unittest.TestSuite()
    # Load tests to test suite
    tclasses = [ Test__arguments ]

    for tclass in tclasses:
        suite.addTests(ldr.loadTestsFromTestCase(tclass))

    if not unittest.TextTestRunner(verbosity = 2).run(suite).wasSuccessful():
        sys.exit(1)

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
