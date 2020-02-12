%define oname pyutilib

Name: python3-module-%oname
Version: 4.8
Release: alt3

Summary: A Python Utility Library
License: BSD, LGPL
Group: Development/Python3
Url: https://software.sandia.gov/trac/pyutilib

BuildArch: noarch

# https://software.sandia.gov/svn/public/pyutilib
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3


%description
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

%package R
Summary: This Python package includes utilities that use R
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description R
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use R.

%package autotest
Summary: Facility for automatically configuring tests
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.component.core pyutilib.misc pyutilib.th
%py3_requires pyutilib.subprocess
Conflicts: python-module-autotest

%description autotest
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

The ``pyutilib.autotest`` package provides a facility for automatically
configuring tests that are executed with Python's unittest package.  This
capability is tailored for tests where one or more *solvers* are 
applied to one or more *problems*.  This testing structure is particularly
useful for evaluating the execution of external executables on datasets.

%package common
Summary: Commonly used PyUtilib definitions and commands
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description common
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes commonly used PyUtilib definitions and
commands.  For example, this package includes PyUtilib-specific 
exception definitions.

%package component-app
Summary: Application interfaces that simplify the use of the PyUtilib Component Architecture
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release
%py3_requires pyutilib.component.config

%description component-app
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package defines application interfaces that simplify the
use of the PyUtilib Component Architecture.

%package component-config
Summary: Utilities to configure the PyUtilib Component Architecture
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release

%description component-config
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities to configure
the PyUtilib Component Architecture.  This includes facilities for using
configuration files, controlling logging, and specifying component
options.

%package component-core
Summary: Modular component framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description component-core
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package provides a modular component framework.

%package component-executables
Summary: A PyUtilib plugin for managing executables in an application
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release
%py3_requires pyutilib.misc pyutilib.component.config

%description component-executables
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

A PyUtilib plugin for managing executables in an application.

%package component-loader
Summary: Plugins to support loading of PCA components
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release
%py3_requires pyutilib.component.config

%description component-loader
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes plugins to support loading of
PCA components from external Python packages and EGG files.

%package dev
Summary: Scripts for developing PyUtilib
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.subprocess
Conflicts: python-module-dev

%description dev
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes scripts that are used for
developing PyUtilib within virtual Python installations.

%package dev-tests
Summary: Tests for scripts for developing PyUtilib
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-dev = %version-%release
%py3_requires pyutilib.subprocess
Conflicts: python-module-dev-tests

%description dev-tests
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes test scripts that are used for
developing PyUtilib within virtual Python installations.

%package enum
Summary: A variant of the PyPI 'enum' package
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description enum
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package is a variant of the PyPI 'enum' package. This
package has been modified to support pickling of enum objects, which
required a weakening of the comparison semantics. Also, this class
supports helper functions that allow enumeration objects to be retrieved
given the enumeration constant value.

%package excel
Summary: Utilities that use Excel spreadsheets
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.common

%description excel
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Excel spreadsheets.

%package math
Summary: PyUtilib math utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description math
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes math utilities.

%package misc
Summary: PyUtilib miscellaneous utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.common

%description misc
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes miscellaneous utilities.

%package ply
Summary: Utilities that use Ply
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires ply

%description ply
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Ply.

%package pyro
Summary: Utilities that use Pyro
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Conflicts: python-module-pyro

%description pyro
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Pyro.

%package services
Summary: General services that are supported by PyUtilib plugins
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.component.config pyutilib.component.executables

%description services
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package defines general services that are supported by
PyUtilib plugins.  For example, PyUtilib plugins are used to manage
temporary files in a general manner.

%package subprocess
Summary: Utilies to execute subprocesses in a robust manner
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.services

%description subprocess
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilies to execute subprocesses in a robust
manner.

%package subprocess-tests
Summary: Tests for utilies to execute subprocesses in a robust manner
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-subprocess = %version-%release

%description subprocess-tests
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes tests for utilies to execute subprocesses
in a robust manner.

%package svn
Summary: Subversion-related utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Conflicts: python-module-svn

%description svn
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

A PyUtilib package for subversion-related utilities.

%package th
Summary: Utilities for testing Python software
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.misc

%description th
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities for testing Python software.  The
main component of this package is an extension of **unittest** to
support new testing capabilities (e.g. tests that perform comparison
with baseline data, and dynamic registration of test methods).

%package virtualenv
Summary: The **vpy_create** script
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires virtualenv
Conflicts: python-module-virtualenv

%description virtualenv
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes the **vpy_create** script, which is
used to create **virtualenv** bootstrap scripts that automate the
installation of **virtualenv** along with other Python packages.

%package workflow
Summary: Simple workflow management system
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.component.core pyutilib.misc pyutilib.services
%py3_requires pyutilib.component.config pyutilib.subprocess

%description workflow
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes a simple workflow management system.  This
is inspired by other open-source workflow tools, such as pyphant and
spiffworkflow.  What distinguished pyutilib.workflow is that it is
not strongly dependent on the datatypes being managed (e.g. the use of
scipy or numpy types).  Also, pyutilib.workflow is designed to support
Python-level definitions of the workflow (rather than a separate XML
specification).

%package autodist
Summary: PyUtilib definitions and commands
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description autodist
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes commonly used PyUtilib definitions and
commands.  For example, this package includes PyUtilib-specific
exception definitions.

%prep
%setup
rm -fR %oname.skel
find -type d -name tags -exec rm -fR '{}' +

find ./ -type f -name '*.py' -exec \
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
pushd devel
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
2to3 -w -n reconfig
%__python3 reconfig
popd

for i in %{oname}*
do
    pushd $i/trunk
    %python3_build
    popd
done

%install
for i in %{oname}*
do
    pushd $i/trunk
    %python3_install
    popd
done
for i in dev/replaceCopyright.py svn/external_manager.py \
    pyro/worker.py pyro/dispatcher.py pyro/client.py
do
    2to3 -w -n %buildroot%python3_sitelibdir/pyutilib/$i
done
install %oname/trunk/%oname/* %buildroot%python3_sitelibdir/%oname
touch %buildroot%python3_sitelibdir/%oname/component/__init__.py

%files
%doc %oname/trunk/*.txt
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/__init__.py*
%python3_sitelibdir/PyUtilib*

%files R
%doc %oname.R/trunk/*.txt
%python3_sitelibdir/%oname.R*
%python3_sitelibdir/%oname/R

%files autotest
%doc %oname.autotest/trunk/*.txt
%python3_sitelibdir/%oname.autotest*
%python3_sitelibdir/%oname/autotest
%_bindir/pyutilib_test_driver

%files common
%doc %oname.common/trunk/*.txt
%python3_sitelibdir/%oname.common*
%python3_sitelibdir/%oname/common

%files component-app
%doc %oname.component.app/trunk/*.txt
%python3_sitelibdir/%oname.component.app*
%python3_sitelibdir/%oname/component/app

%files component-config
%doc %oname.component.config/trunk/*.txt
%python3_sitelibdir/%oname.component.config*
%python3_sitelibdir/%oname/component/config

%files component-core
%doc %oname.component.core/trunk/*.txt
%python3_sitelibdir/%oname.component.core*
%dir %python3_sitelibdir/%oname/component
%dir %python3_sitelibdir/%oname/component/__pycache__
%python3_sitelibdir/%oname/component/__init__.py
%python3_sitelibdir/%oname/component/__pycache__/__init__.*
%python3_sitelibdir/%oname/component/core
%python3_sitelibdir/%oname.component.doc*
%python3_sitelibdir/%oname/component/doc

%files component-executables
%doc %oname.component.executables/trunk/*.txt
%python3_sitelibdir/%oname.component.executables*
%python3_sitelibdir/%oname/component/executables

%files component-loader
%doc %oname.component.loader/trunk/*.txt
%python3_sitelibdir/%oname.component.loader*
%python3_sitelibdir/%oname/component/loader

%files dev
%doc %oname.dev/trunk/*.txt
%python3_sitelibdir/%oname.dev*
%python3_sitelibdir/%oname/dev
%exclude %python3_sitelibdir/%oname/dev/runtests.py*
%_bindir/lpython
%_bindir/pypi_downloads
%_bindir/lbin
%_bindir/svnpm
%_bindir/checkCopyright
%_bindir/replaceCopyright

%files dev-tests
%python3_sitelibdir/%oname/dev/runtests.py*
%_bindir/test.%oname

%files enum
%doc %oname.enum/trunk/*.txt
%python3_sitelibdir/%oname.enum*
%python3_sitelibdir/%oname/enum

%files excel
%doc %oname.excel/trunk/*.txt
%python3_sitelibdir/%oname.excel*
%python3_sitelibdir/%oname/excel

%files math
%doc %oname.math/trunk/*.txt
%python3_sitelibdir/%oname.math*
%python3_sitelibdir/%oname/math

%files misc
%doc %oname.misc/trunk/*.txt
%python3_sitelibdir/%oname.misc*
%python3_sitelibdir/%oname/misc

%files ply
%doc %oname.ply/trunk/*.txt
%python3_sitelibdir/%oname.ply*
%python3_sitelibdir/%oname/ply

%files pyro
%doc %oname.pyro/trunk/*.txt
%doc %oname.pyro/trunk/example
%python3_sitelibdir/%oname.pyro*
%python3_sitelibdir/%oname/pyro
%_bindir/dispatch_srvr

%files services
%doc %oname.services/trunk/*.txt
%python3_sitelibdir/%oname.services*
%python3_sitelibdir/%oname/services

%files subprocess
%doc %oname.subprocess/trunk/*.txt
%python3_sitelibdir/%oname.subprocess*
%python3_sitelibdir/%oname/subprocess
%exclude %python3_sitelibdir/%oname/subprocess/tests

%files subprocess-tests
%python3_sitelibdir/%oname/subprocess/tests

%files svn
%doc %oname.svn/trunk/*.txt
%python3_sitelibdir/%oname.svn*
%python3_sitelibdir/%oname/svn
%_bindir/svn-timemachine

%files th
%doc %oname.th/trunk/*.txt
%python3_sitelibdir/%oname.th*
%python3_sitelibdir/%oname/th

%files virtualenv
%doc %oname.virtualenv/trunk/*.txt
%doc %oname.virtualenv/trunk/example
%python3_sitelibdir/%oname.virtualenv*
%python3_sitelibdir/%oname/virtualenv
%_bindir/vpy_install
%_bindir/vpy_create

%files workflow
%doc %oname.workflow/trunk/*.txt
%python3_sitelibdir/%oname.workflow*
%python3_sitelibdir/%oname/workflow

%files autodist
%doc %oname.autodist/trunk/*.txt
%python3_sitelibdir/%oname.autodist*
%python3_sitelibdir/%oname/autodist


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.8-alt3
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.8-alt2.svn20140714.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.8-alt2.svn20140714.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt2.svn20140714
- Added modules for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt1.svn20140714
- Version 4.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt1.svn20131118
- Version 4.7

* Wed Sep 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1.svn20130903
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1.svn20130329
- Version 4.6

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.svn20120831
- Version 4.2

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1.svn20111215
- Version 3.8

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5-alt1.svn20110507.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.svn20110507
- Version 3.5

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.svn20101107
- Version 3.4

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20100911.4
- Rebuilt with Pyro4 4.2

* Tue Sep 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20100911.3
- Fixed simple in component-app and plugin_eggLoader in component-loader

* Tue Sep 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20100911.2
- Added:
  + necessary requirements
  + excel subpackage
  + some fixes

* Mon Sep 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20100911.1
- Assigned %python_sitelibdir/%oname/component to %name-component-core

* Mon Sep 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20100911
- Initial build for Sisyphus

