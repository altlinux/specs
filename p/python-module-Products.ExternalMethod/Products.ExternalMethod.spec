%define oname Products.ExternalMethod

#def_disable check

Name: python-module-%oname
Version: 2.14
Release: alt2.dev0.git20150618
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
python setup.py test -v
python -m unittest %oname.tests.testExternalMethod

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14-alt2.dev0.git20150618
- Enabled check

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14-alt1.dev0.git20150618
- Version 2.14.dev0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1.git20141102
- Version 2.13.2

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

