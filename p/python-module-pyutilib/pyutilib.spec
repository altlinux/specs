%define oname pyutilib

%def_with python3

Name: python-module-%oname
Version: 4.8
Release: alt2.svn20140714.1
Summary: A Python Utility Library
License: BSD, LGPL
Group: Development/Python
Url: https://software.sandia.gov/trac/pyutilib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://software.sandia.gov/svn/public/pyutilib
Source: %oname-%version.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

BuildArch: noarch

%description
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

%package -n python3-module-%oname
Summary: A Python Utility Library
Group: Development/Python3

%description -n python3-module-%oname
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
%add_findreq_skiplist %python_sitelibdir/%oname/component/core/core3.py

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

%package autodist
Summary: PyUtilib definitions and commands
Group: Development/Python
Requires: %name = %version-%release

%description autodist
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes commonly used PyUtilib definitions and
commands.  For example, this package includes PyUtilib-specific
exception definitions.

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

%package -n python3-module-%oname-R
Summary: This Python package includes utilities that use R
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-R
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use R.

%package -n python3-module-%oname-autotest
Summary: Facility for automatically configuring tests
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.component.core pyutilib.misc pyutilib.th
%py3_requires pyutilib.subprocess

%description -n python3-module-%oname-autotest
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

%package -n python3-module-%oname-common
Summary: Commonly used PyUtilib definitions and commands
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-common
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes commonly used PyUtilib definitions and
commands.  For example, this package includes PyUtilib-specific 
exception definitions.

%package -n python3-module-%oname-component-app
Summary: Application interfaces that simplify the use of the PyUtilib Component Architecture
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release
%py3_requires pyutilib.component.config

%description -n python3-module-%oname-component-app
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package defines application interfaces that simplify the
use of the PyUtilib Component Architecture.

%package -n python3-module-%oname-component-config
Summary: Utilities to configure the PyUtilib Component Architecture
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release

%description -n python3-module-%oname-component-config
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities to configure
the PyUtilib Component Architecture.  This includes facilities for using
configuration files, controlling logging, and specifying component
options.

%package -n python3-module-%oname-component-core
Summary: Modular component framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-component-core
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package provides a modular component framework.

%package -n python3-module-%oname-component-executables
Summary: A PyUtilib plugin for managing executables in an application
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release
%py3_requires pyutilib.misc pyutilib.component.config

%description -n python3-module-%oname-component-executables
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

A PyUtilib plugin for managing executables in an application.

%package -n python3-module-%oname-component-loader
Summary: Plugins to support loading of PCA components
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-component-core = %version-%release
%py3_requires pyutilib.component.config

%description -n python3-module-%oname-component-loader
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes plugins to support loading of
PCA components from external Python packages and EGG files.

%package -n python3-module-%oname-dev
Summary: Scripts for developing PyUtilib
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.subprocess

%description -n python3-module-%oname-dev
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes scripts that are used for
developing PyUtilib within virtual Python installations.

%package -n python3-module-%oname-dev-tests
Summary: Tests for scripts for developing PyUtilib
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-dev = %version-%release
%py3_requires pyutilib.subprocess

%description -n python3-module-%oname-dev-tests
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes test scripts that are used for
developing PyUtilib within virtual Python installations.

%package -n python3-module-%oname-enum
Summary: A variant of the PyPI 'enum' package
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-enum
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

%package -n python3-module-%oname-excel
Summary: Utilities that use Excel spreadsheets
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.common

%description -n python3-module-%oname-excel
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Excel spreadsheets.

%package -n python3-module-%oname-math
Summary: PyUtilib math utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-math
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes math utilities.

%package -n python3-module-%oname-misc
Summary: PyUtilib miscellaneous utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.common

%description -n python3-module-%oname-misc
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes miscellaneous utilities.

%package -n python3-module-%oname-ply
Summary: Utilities that use Ply
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires ply

%description -n python3-module-%oname-ply
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Ply.

%package -n python3-module-%oname-pyro
Summary: Utilities that use Pyro
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-pyro
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities that use Pyro.

%package -n python3-module-%oname-services
Summary: General services that are supported by PyUtilib plugins
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.component.config pyutilib.component.executables

%description -n python3-module-%oname-services
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package defines general services that are supported by
PyUtilib plugins.  For example, PyUtilib plugins are used to manage
temporary files in a general manner.

%package -n python3-module-%oname-subprocess
Summary: Utilies to execute subprocesses in a robust manner
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.services

%description -n python3-module-%oname-subprocess
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilies to execute subprocesses in a robust
manner.

%package -n python3-module-%oname-subprocess-tests
Summary: Tests for utilies to execute subprocesses in a robust manner
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: python3-module-%oname-subprocess = %version-%release

%description -n python3-module-%oname-subprocess-tests
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes tests for utilies to execute subprocesses
in a robust manner.

%package -n python3-module-%oname-svn
Summary: Subversion-related utilities
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-svn
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

A PyUtilib package for subversion-related utilities.

%package -n python3-module-%oname-th
Summary: Utilities for testing Python software
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.misc

%description -n python3-module-%oname-th
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes utilities for testing Python software.  The
main component of this package is an extension of **unittest** to
support new testing capabilities (e.g. tests that perform comparison
with baseline data, and dynamic registration of test methods).

%package -n python3-module-%oname-virtualenv
Summary: The **vpy_create** script
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires virtualenv

%description -n python3-module-%oname-virtualenv
The PyUtilib project supports the development of an ensemble of Python
packages that include a wide variety of utilities, including a
well-developed component architecture. PyUtilib has been developed to
support several Python projects under development at Sandia National
Laboratories, including  Coopr and  FAST.

This Python package includes the **vpy_create** script, which is
used to create **virtualenv** bootstrap scripts that automate the
installation of **virtualenv** along with other Python packages.

%package -n python3-module-%oname-workflow
Summary: Simple workflow management system
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pyutilib.component.core pyutilib.misc pyutilib.services
%py3_requires pyutilib.component.config pyutilib.subprocess

%description -n python3-module-%oname-workflow
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

%package -n python3-module-%oname-autodist
Summary: PyUtilib definitions and commands
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-autodist
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
%endif

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

%if_with python3
pushd ../python3
pushd devel
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
2to3 -w -n reconfig
python3 reconfig
popd

for i in %{oname}*
do
	pushd $i/trunk
	%python3_build
	popd
done
popd
%endif

%install
%if_with python3
pushd ../python3
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
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

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
%_bindir/checkCopyright
%_bindir/replaceCopyright

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
%exclude %_bindir/*.py3

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

%files autodist
%doc %oname.autodist/trunk/*.txt
%python_sitelibdir/%oname.autodist*
%python_sitelibdir/%oname/autodist

%if_with python3
%files -n python3-module-%oname
%doc %oname/trunk/*.txt
%dir %python3_sitelibdir/%oname
%dir %python3_sitelibdir/%oname/__pycache__
%python3_sitelibdir/%oname/__init__.py
%python3_sitelibdir/%oname/__pycache__/__init__.*
%python3_sitelibdir/PyUtilib*

%files -n python3-module-%oname-R
%doc %oname.R/trunk/*.txt
%python3_sitelibdir/%oname.R*
%python3_sitelibdir/%oname/R

%files -n python3-module-%oname-autotest
%doc %oname.autotest/trunk/*.txt
%python3_sitelibdir/%oname.autotest*
%python3_sitelibdir/%oname/autotest
%_bindir/pyutilib_test_driver.py3

%files -n python3-module-%oname-common
%doc %oname.common/trunk/*.txt
%python3_sitelibdir/%oname.common*
%python3_sitelibdir/%oname/common

%files -n python3-module-%oname-component-app
%doc %oname.component.app/trunk/*.txt
%python3_sitelibdir/%oname.component.app*
%python3_sitelibdir/%oname/component/app

%files -n python3-module-%oname-component-config
%doc %oname.component.config/trunk/*.txt
%python3_sitelibdir/%oname.component.config*
%python3_sitelibdir/%oname/component/config

%files -n python3-module-%oname-component-core
%doc %oname.component.core/trunk/*.txt
%python3_sitelibdir/%oname.component.core*
%dir %python3_sitelibdir/%oname/component
%dir %python3_sitelibdir/%oname/component/__pycache__
%python3_sitelibdir/%oname/component/__init__.py
%python3_sitelibdir/%oname/component/__pycache__/__init__.*
%python3_sitelibdir/%oname/component/core
%python3_sitelibdir/%oname.component.doc*
%python3_sitelibdir/%oname/component/doc

%files -n python3-module-%oname-component-executables
%doc %oname.component.executables/trunk/*.txt
%python3_sitelibdir/%oname.component.executables*
%python3_sitelibdir/%oname/component/executables

%files -n python3-module-%oname-component-loader
%doc %oname.component.loader/trunk/*.txt
%python3_sitelibdir/%oname.component.loader*
%python3_sitelibdir/%oname/component/loader

%files -n python3-module-%oname-dev
%doc %oname.dev/trunk/*.txt
%python3_sitelibdir/%oname.dev*
%python3_sitelibdir/%oname/dev
%exclude %python3_sitelibdir/%oname/dev/runtests.py*
%_bindir/lpython.py3
%_bindir/pypi_downloads.py3
%_bindir/lbin.py3
%_bindir/svnpm.py3
%_bindir/checkCopyright.py3
%_bindir/replaceCopyright.py3

%files -n python3-module-%oname-dev-tests
%python3_sitelibdir/%oname/dev/runtests.py*
%_bindir/test.%oname.py3

%files -n python3-module-%oname-enum
%doc %oname.enum/trunk/*.txt
%python3_sitelibdir/%oname.enum*
%python3_sitelibdir/%oname/enum

%files -n python3-module-%oname-excel
%doc %oname.excel/trunk/*.txt
%python3_sitelibdir/%oname.excel*
%python3_sitelibdir/%oname/excel

%files -n python3-module-%oname-math
%doc %oname.math/trunk/*.txt
%python3_sitelibdir/%oname.math*
%python3_sitelibdir/%oname/math

%files -n python3-module-%oname-misc
%doc %oname.misc/trunk/*.txt
%python3_sitelibdir/%oname.misc*
%python3_sitelibdir/%oname/misc

%files -n python3-module-%oname-ply
%doc %oname.ply/trunk/*.txt
%python3_sitelibdir/%oname.ply*
%python3_sitelibdir/%oname/ply

%files -n python3-module-%oname-pyro
%doc %oname.pyro/trunk/*.txt
%doc %oname.pyro/trunk/example
%python3_sitelibdir/%oname.pyro*
%python3_sitelibdir/%oname/pyro
%_bindir/dispatch_srvr*.py3

%files -n python3-module-%oname-services
%doc %oname.services/trunk/*.txt
%python3_sitelibdir/%oname.services*
%python3_sitelibdir/%oname/services

%files -n python3-module-%oname-subprocess
%doc %oname.subprocess/trunk/*.txt
%python3_sitelibdir/%oname.subprocess*
%python3_sitelibdir/%oname/subprocess
%exclude %python3_sitelibdir/%oname/subprocess/tests

%files -n python3-module-%oname-subprocess-tests
%python3_sitelibdir/%oname/subprocess/tests

%files -n python3-module-%oname-svn
%doc %oname.svn/trunk/*.txt
%python3_sitelibdir/%oname.svn*
%python3_sitelibdir/%oname/svn
%_bindir/svn-timemachine.py3

%files -n python3-module-%oname-th
%doc %oname.th/trunk/*.txt
%python3_sitelibdir/%oname.th*
%python3_sitelibdir/%oname/th

%files -n python3-module-%oname-virtualenv
%doc %oname.virtualenv/trunk/*.txt
%doc %oname.virtualenv/trunk/example
%python3_sitelibdir/%oname.virtualenv*
%python3_sitelibdir/%oname/virtualenv
%_bindir/vpy_install.py3
%_bindir/vpy_create.py3

%files -n python3-module-%oname-workflow
%doc %oname.workflow/trunk/*.txt
%python3_sitelibdir/%oname.workflow*
%python3_sitelibdir/%oname/workflow

%files -n python3-module-%oname-autodist
%doc %oname.autodist/trunk/*.txt
%python3_sitelibdir/%oname.autodist*
%python3_sitelibdir/%oname/autodist
%endif

%changelog
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

