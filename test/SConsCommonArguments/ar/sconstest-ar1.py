#
# Copyright (c) 2012-2017 by Pawel Tomulik
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
Tests SConsCommonArguments for 'ar' tool.
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture('../../../SConsCommonArguments', 'site_scons/SConsCommonArguments')
#test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsCommonArguments.CC

env = Environment(tools = [])
env.Replace(CC = 'org_cc', CXXFLAGS = 'org_cxxflags')
var = Variables()
decls = SConsCommonArguments.CC.Declarations()
args = decls.Commit(env, var, True)
args.Postprocess(env, var, True)

proxy = args.EnvProxy(env)
for k in SConsCommonArguments.CC.Names():
    print proxy.subst("%s : ${%s}" % (k, k))
""")

test_tab = [
  (
    [],
    [
        """CC : org_cc""",
        """CXXFLAGS : org_cxxflags""",
    ]
  ),
  (
    ['CC=new_cc'],
    [
        """CC : new_cc""",
        """CXXFLAGS : org_cxxflags""",
    ]
  ),
  (
    ['CXXFLAGS=new_cxxflags'],
    [
        """CC : org_cc""",
        """CXXFLAGS : new_cxxflags""",
    ]
  ),
]

for cli_vars, chk_lines in test_tab:
    test.run(['-Q'] + cli_vars)
    test.must_contain_all_lines(test.stdout(), chk_lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
