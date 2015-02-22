%define mname zopyx.smartprintng
%define oname %mname.core
Name: python-module-%oname
Version: 2.0.0
Release: alt1
Summary: SmartPrintNG core engine
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.smartprintng.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Pillow
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zopyx.convert2
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema

%py_provides %oname
%py_requires %mname zope.component zope.pagetemplate zopyx.convert2
%py_requires zope.configuration zope.event zope.pagetemplate zope.schema
%py_requires zope.interface PIL

%description
This package contains the refactored code-base of the SmartPrintNG
product for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.app.testing

%description tests
This package contains the refactored code-base of the SmartPrintNG
product for Plone.

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
%doc *.txt docs/*
%_bindir/*
%python_sitelibdir/zopyx/smartprintng/core
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zopyx/smartprintng/core/tests

%files tests
%python_sitelibdir/zopyx/smartprintng/core/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

