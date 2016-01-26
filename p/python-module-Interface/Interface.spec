%define oname Interface
%def_disable check

Name: python-module-%oname
Version: 2.11.1
Release: alt2
Summary: Interface implementation
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Interface/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-pytest python-module-zope.schema python-module-zope.testing
#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-zope.schema
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.testing

%py_provides %oname
#%py_requires zope.interface zope.schema
#%add_python_req_skip Basic Util

%description
This package provides an interface implementation for Python as it was
used in Zope 2. Unless you need it for legacy Zope 2 applications, you
probably want to use the more modern zope.interface package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing

%description tests
This package provides an interface implementation for Python as it was
used in Zope 2. Unless you need it for legacy Zope 2 applications, you
probably want to use the more modern zope.interface package.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
rm -fR build
py.test

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.11.1-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.11.1-alt1
- Initial build for Sisyphus

