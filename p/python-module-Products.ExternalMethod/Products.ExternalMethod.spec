%define oname Products.ExternalMethod

Name: python-module-%oname
Version: 2.13.1
Release: alt1.dev.git20130313
Summary: Provides support for external Python methods within a Zope 2 environment
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ExternalMethod/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.ExternalMethod.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ZODB3

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3

%description
The External Method package provides support for external Python
methods, exposing them as callable objects within a Zope 2 environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The External Method package provides support for external Python
methods, exposing them as callable objects within a Zope 2 environment.

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
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

