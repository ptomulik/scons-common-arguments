#
# Copyright (c) 2012-2015 by Pawel Tomulik
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

__docformat__ = "restructuredText"

"""
Tests SConsCommonArguments.CC.Declarations() with no arguments, verify
the help strings it generates
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture('../../../SConsCommonArguments', 'site_scons/SConsCommonArguments')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsCommonArguments.CC

env = Environment(tools = [])
var = Variables()
decls = SConsCommonArguments.CC.Declarations()
args = decls.Commit(env, var, True)

AddOption('--help-variables', dest='help_variables', action='store_true',
          help='print help for CLI variables')
if GetOption('help_variables'):
    print args.GenerateVariablesHelpText(var, env)
""")

test.run('-Q --help-variables')

lines = [
r"""CC: A C compiler to use""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHLINKFLAGS: Flags for linker used when creating shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHLINK: A linker to use when creating shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHCXX: A C++ compiler used when compiling shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""LINKFLAGS: Flags for linker""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHCFLAGS: Flags for C compiler used when compiling shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHCC: A C compiler used when compiling shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""CXXFLAGS: Flags for C++ compiler""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""CXX: A C++ compiler to use""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""CCFLAGS: Flags for both C and C++ compilers""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""CFLAGS: Flags for C compiler""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHCCFLAGS: Flags for both C and C++ compilers used when compiling shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""LINK: A linker to use""",
r"""    default: UNDEFINED""",
r"""    actual: None""",

r"""SHCXXFLAGS: Flags for C++ compiler used when compiling shared libraries""",
r"""    default: UNDEFINED""",
r"""    actual: None""",
]

test.must_contain_all_lines(test.stdout(), lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
