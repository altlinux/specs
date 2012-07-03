%define oname pyutilib
Name: python-module-%oname
Version: 3.8
Release: alt1.svn20111215
Summary: A Python Utility Library
License: BSD, LGPL
Group: Development/Python
Url: https://software.sandia.gov/trac/pyutilib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://software.sandia.gov/svn/public/pyutilib
Source: %oname-%version.tar.gz

BuildPreReq: python-devel python-module-setuptools
BuildArch: noarch

%description
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

%package R
Summary: This Python package includes utilities that use R
Group: Development/Python
Requires: %name = %version-%release

%description R
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use R.

%package autotest
Summary: Facility for automatically configuring tests
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.component.core pyutilib.misc pyutilib.th
%py_requires pyutilib.subprocess

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
Group: Development/Python
Requires: %name = %version-%release

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
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-component-core = %version-%release
%py_requires pyutilib.component.config

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
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-component-core = %version-%release

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
Group: Development/Python
Requires: %name = %version-%release

%description component-core
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package provides a modular component framework.

%package component-executables
Summary: A PyUtilib plugin for managing executables in an application
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-component-core = %version-%release
%py_requires pyutilib.misc pyutilib.component.config

%description component-executables
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

A PyUtilib plugin for managing executables in an application.

%package component-loader
Summary: Plugins to support loading of PCA components
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-component-core = %version-%release
%py_requires pyutilib.component.config

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
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.subprocess

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
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-dev = %version-%release
%py_requires pyutilib.subprocess

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
Group: Development/Python
Requires: %name = %version-%release

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
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.common

%description excel
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Excel spreadsheets.

%package math
Summary: PyUtilib math utilities
Group: Development/Python
Requires: %name = %version-%release

%description math
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes math utilities.

%package misc
Summary: PyUtilib miscellaneous utilities
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.common

%description misc
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes miscellaneous utilities.

%package ply
Summary: Utilities that use Ply
Group: Development/Python
Requires: %name = %version-%release
%py_requires ply

%description ply
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Ply.

%package pyro
Summary: Utilities that use Pyro
Group: Development/Python
Requires: %name = %version-%release

%description pyro
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Pyro.

%package services
Summary: General services that are supported by PyUtilib plugins
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.component.config pyutilib.component.executables

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
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.services

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
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-subprocess = %version-%release

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
Group: Development/Python
Requires: %name = %version-%release

%description svn
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

A PyUtilib package for subversion-related utilities.

%package th
Summary: Utilities for testing Python software
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.misc

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
Group: Development/Python
Requires: %name = %version-%release
%py_requires virtualenv

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
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyutilib.component.core pyutilib.misc pyutilib.services
%py_requires pyutilib.component.config pyutilib.subprocess

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

%package workflow-doc
Summary: Documentation for simple workflow management system
Group: Development/Documentation

%description workflow-doc
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This package contains documentation for simple workflow management
system.

%prep
%setup
rm -fR %oname.skel

%build
pushd devel
python reconfig
popd

for i in %{oname}*
do
	pushd $i/trunk
	%python_build
	popd
done

%install
for i in %{oname}*
do
	pushd $i/trunk
	%python_install
	popd
done

install %oname/trunk/%oname/* %buildroot%python_sitelibdir/%oname
touch %buildroot%python_sitelibdir/%oname/component/__init__.py

%files
%doc %oname/trunk/*.txt
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/__init__.py*
%python_sitelibdir/PyUtilib*

%files R
%doc %oname.R/trunk/*.txt
%python_sitelibdir/%oname.R*
%python_sitelibdir/%oname/R

%files autotest
%doc %oname.autotest/trunk/*.txt
%python_sitelibdir/%oname.autotest*
%python_sitelibdir/%oname/autotest
%_bindir/pyutilib_test_driver

%files common
%doc %oname.common/trunk/*.txt
%python_sitelibdir/%oname.common*
%python_sitelibdir/%oname/common

%files component-app
%doc %oname.component.app/trunk/*.txt
%python_sitelibdir/%oname.component.app*
%python_sitelibdir/%oname/component/app

%files component-config
%doc %oname.component.config/trunk/*.txt
%python_sitelibdir/%oname.component.config*
%python_sitelibdir/%oname/component/config

%files component-core
%doc %oname.component.core/trunk/*.txt
%python_sitelibdir/%oname.component.core*
%dir %python_sitelibdir/%oname/component
%python_sitelibdir/%oname/component/__init__.py*
%python_sitelibdir/%oname/component/core
%python_sitelibdir/%oname.component.doc*
%python_sitelibdir/%oname/component/doc

%files component-executables
%doc %oname.component.executables/trunk/*.txt
%python_sitelibdir/%oname.component.executables*
%python_sitelibdir/%oname/component/executables

%files component-loader
%doc %oname.component.loader/trunk/*.txt
%python_sitelibdir/%oname.component.loader*
%python_sitelibdir/%oname/component/loader

%files dev
%doc %oname.dev/trunk/*.txt
%python_sitelibdir/%oname.dev*
%python_sitelibdir/%oname/dev
%exclude %python_sitelibdir/%oname/dev/runtests.py*
%_bindir/lpython
%_bindir/pypi_downloads
%_bindir/lbin
%_bindir/svnpm

%files dev-tests
%python_sitelibdir/%oname/dev/runtests.py*
%_bindir/test.%oname

%files enum
%doc %oname.enum/trunk/*.txt
%python_sitelibdir/%oname.enum*
%python_sitelibdir/%oname/enum

%files excel
%doc %oname.excel/trunk/*.txt
%python_sitelibdir/%oname.excel*
%python_sitelibdir/%oname/excel

%files math
%doc %oname.math/trunk/*.txt
%python_sitelibdir/%oname.math*
%python_sitelibdir/%oname/math

%files misc
%doc %oname.misc/trunk/*.txt
%python_sitelibdir/%oname.misc*
%python_sitelibdir/%oname/misc

%files ply
%doc %oname.ply/trunk/*.txt
%python_sitelibdir/%oname.ply*
%python_sitelibdir/%oname/ply

%files pyro
%doc %oname.pyro/trunk/*.txt
%doc %oname.pyro/trunk/example
%python_sitelibdir/%oname.pyro*
%python_sitelibdir/%oname/pyro
%_bindir/dispatch_srvr*

%files services
%doc %oname.services/trunk/*.txt
%python_sitelibdir/%oname.services*
%python_sitelibdir/%oname/services

%files subprocess
%doc %oname.subprocess/trunk/*.txt
%python_sitelibdir/%oname.subprocess*
%python_sitelibdir/%oname/subprocess
%exclude %python_sitelibdir/%oname/subprocess/tests

%files subprocess-tests
%python_sitelibdir/%oname/subprocess/tests

%files svn
%doc %oname.svn/trunk/*.txt
%python_sitelibdir/%oname.svn*
%python_sitelibdir/%oname/svn
%_bindir/svn-timemachine

%files th
%doc %oname.th/trunk/*.txt
%python_sitelibdir/%oname.th*
%python_sitelibdir/%oname/th

%files virtualenv
%doc %oname.virtualenv/trunk/*.txt
%doc %oname.virtualenv/trunk/example
%python_sitelibdir/%oname.virtualenv*
%python_sitelibdir/%oname/virtualenv
%_bindir/vpy_install
%_bindir/vpy_create

%files workflow
%doc %oname.workflow/trunk/*.txt
%python_sitelibdir/%oname.workflow*
%python_sitelibdir/%oname/workflow

%files workflow-doc
%doc %oname.workflow/trunk/doc/*

%changelog
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

