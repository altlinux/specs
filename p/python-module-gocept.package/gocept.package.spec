%define mname gocept
%define oname %mname.package
Name: python-module-%oname
Version: 1.3
Release: alt1
Summary: A paste.script template following gocept Python package conventions
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/gocept.package/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-sphinx
BuildPreReq: python-module-PasteScript python-module-pkginfo
BuildPreReq: python-module-gocept.testing python-module-unittest2
BuildPreReq: python-module-PasteDeploy

%py_provides %oname
%py_requires %mname paste.script sphinx

%description
This package generates Python packages following conventions used at
gocept.

It consists of two parts: a paster template that creates the boilerplate
for a Python package, and a Python module that is used to configure
Sphinx, along with the necessary package dependencies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires gocept.testing unittest2

%description tests
This package generates Python packages following conventions used at
gocept.

It consists of two parts: a paster template that creates the boilerplate
for a Python package, and a Python module that is used to configure
Sphinx, along with the necessary package dependencies.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/*/*/*/tests

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/*/*/*/tests

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

