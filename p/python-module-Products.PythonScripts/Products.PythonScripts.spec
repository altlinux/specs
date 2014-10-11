%define oname Products.PythonScripts

%def_disable check

Name: python-module-%oname
Version: 2.13.2
Release: alt1
Summary: Provides support for restricted execution of Python scripts in Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PythonScripts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-AccessControl python-module-Acquisition
BuildPreReq: python-module-DateTime python-module-DocumentTemplate
BuildPreReq: python-module-RestrictedPython python-module-zExceptions

%py_provides %oname
Requires: python-module-Zope2

%description
The Python Scripts product provides support for restricted execution of
Python scripts, exposing them as callable objects within the Zope
environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The Python Scripts product provides support for restricted execution of
Python scripts, exposing them as callable objects within the Zope
environment.

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
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Initial build for Sisyphus

