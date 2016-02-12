"""`SConsCommonArguments.CC`

Defines arguments related to C and C++ compilers.

**General Description**

This module provides standard command-line arguments that are commonly used by
C/C++ tools. The variables defined here may be easilly added to:

    - SCons environment, as construction variables (``env.subst('$variable')``),
    - SCons command line variables (``scons variable=value``),
    - SCons command line options (``scons --variable=value``).

**Quick start**

.. python::
    # SConstruct
    import SConsCommonArguments.CC

    env = Environment(tools = [])
    var = Variables()
    decls = SConsCommonArguments.CC.Declarations()
    args = decls.Commit(env, var, True)
    args.Postprocess(env, var, True)

    print env.subst("CC: ${CC}")
    print env.subst("CXX: ${CXX}")

Running examples::

    ptomulik@barakus:$ scons -Q
    CC:
    CXX:

    ptomulik@barakus:$ scons -Q CC=gcc CXX=g++
    CC: gcc
    CXX: g++

**Supported Variables**

Programs:

    CC
        A C compiler to use
    CXX
        A C++ compiler to use
    LINK
        A linker to use
    SHCC
        A C compiler used when compiling shared libraries.
    SHCXX
        A C++ compiler used when compiling shared libraries.
    SHLINK
        A linker to use when creating shared libraries

Flags for programs:

    CFLAGS
        Flags for C compiler
    CXXFLAGS
        Flags for C++ compiler
    CCFLAGS
        Flags for both C and C++ compilers
    LINKFLAGS
        Flags for linker
    SHCFLAGS
        Flags for C compiler used when compiling shared libraries
    SHCXXFLAGS
        Flags for C++ compiler used when compiling shared libraries
    SHCCFLAGS',
        Flags for both C and C++ compilers used when compiling shared libraries
    SHLINKFLAGS',
        Flags for linker used when creating shared libraries
"""

#
# Copyright (c) 2016 by Pawel Tomulik
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

import SConsArguments
import SConsCommonArguments.Util

#############################################################################
# NOTE: variable substitutions must be in curly brackets, so use ${prefix}
#       and not $prefix. This is required for proper prefixing/suffixing and
#       transforming in certain parts of library
_prog_arg_tuples = [
    # Programs
    ( 'CC',     'A C compiler to use'),
    ( 'CXX',    'A C++ compiler to use'),
    ( 'LINK',   'A linker to use'),
    ( 'SHCC',   'A C compiler used when compiling shared libraries'),
    ( 'SHCXX',  'A C++ compiler used when compiling shared libraries'),
    ( 'SHLINK', 'A linker to use when creating shared libraries'),
]

_flag_arg_tuples = [
    # Program flags
    ( 'CFLAGS',     'Flags for C compiler'),
    ( 'CXXFLAGS',   'Flags for C++ compiler'),
    ( 'CCFLAGS',    'Flags for both C and C++ compilers'),
    ( 'LINKFLAGS',  'Flags for linker'),
    ( 'SHCFLAGS',   'Flags for C compiler used when compiling shared libraries'),
    ( 'SHCXXFLAGS', 'Flags for C++ compiler used when compiling shared libraries'),
    ( 'SHCCFLAGS',  'Flags for both C and C++ compilers used when compiling shared libraries'),
    ( 'SHLINKFLAGS','Flags for linker used when creating shared libraries'),
]

#############################################################################
def Names(name_filter = lambda x : True, **kw):
    """Return list of CC argument names.

    :Parameters:
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
    :Keywords:
        include_progs
            Whether to include program variables (CC, CXX, ...)
        include_flags
            Whether to include flag variables (CFLAGS, CXXFLAGS, ...)
    :Returns:
        the list of CC argument names
    """
    names = []
    seqmap = {  'include_progs': _prog_arg_tuples,
                'inlude_flags' : _flag_arg_tuples   }
    for k,seq in seqmap.iteritems():
        cond = True
        try: cond = kw[k]
        except KeyError: pass
        if cond:
            names += SConsCommonArguments.Util.names_from_tuples(seq, name_filter)
    return names

###############################################################################
def Declarations(**kw):
    """Return declarations of SCons *arguments* for all predefined CC
    arguments.

    :Keywords:
        defaults : dict
            user-specified default values for the Arguments being declared,
        name_filter : callable
            callable object (e.g. lambda) of type ``name_filter(name) ->
            boolean`` used to filter-out unwanted variables; only these
            variables are processed, for which name_filter returns ``True``
        nameconv : `SConsArguments._ArgumentNameConv`
            a `SConsArguments._ArgumentNameConv` object used to transform
            *argument* names to *endpoint* (construction variable, command-line
            variable, command-line option) names,
        env_key_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        env_key_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        env_key_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        var_key_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        var_key_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        var_key_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_key_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_key_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_key_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`, note that
            `Declarations` sets this to ``False`` by default,
        opt_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_name_prefix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        opt_name_suffix
            passed to `SConsArguments._ArgumentNameConv.__init__()`,
        option_transform
            passed to `SConsArguments._ArgumentNameConv.__init__()`.
        include_progs
            Whether to include program variables (CC, CXX, ...)
        include_flags
            Whether to include flag variables (CFLAGS, CXXFLAGS, ...)

    :Returns:
        an instance of `SConsArguments._ArgumentDeclarations`
    """
    if not 'opt_key_transform' in kw:
        kw['opt_key_transform'] = False

    decls = SConsArguments.ArgumentDeclarations()
    seqmap = {  'include_progs': _prog_arg_tuples,
                'inlude_flags' : _flag_arg_tuples   }
    for k,seq in seqmap.iteritems():
        cond = True
        try: cond = kw[k]
        except KeyError: pass
        if cond:
            decls.update(SConsCommonArguments.Util.arguments_from_tuples(seq, **kw))
    return decls

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
