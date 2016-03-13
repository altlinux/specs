%define oname z3c.saconfig

%def_with python3

Name: python-module-%oname
Version: 0.13
Release: alt2.1
Summary: Minimal SQLAlchemy ORM session configuration for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.saconfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.sqlalchemy zope.interface zope.component zope.hookable
%py_requires zope.security zope.event zope.configuration

%description
This aim of this package is to offer a simple but flexible way to
configure SQLAlchemy's scoped session support using the Zope component
architecture. This package is based on zope.sqlalchemy, which offers
transaction integration between Zope and SQLAlchemy.

We sketch out two main scenarios here:

  * one database per Zope instance.
  * one database per site (or Grok application) in a Zope instance (and
    thus multiple databases per Zope instance).

%package -n python3-module-%oname
Summary: Minimal SQLAlchemy ORM session configuration for Zope
Group: Development/Python3
%py3_requires zope.sqlalchemy zope.interface zope.component zope.hookable
%py3_requires zope.security zope.event zope.configuration

%description -n python3-module-%oname
This aim of this package is to offer a simple but flexible way to
configure SQLAlchemy's scoped session support using the Zope component
architecture. This package is based on zope.sqlalchemy, which offers
transaction integration between Zope and SQLAlchemy.

We sketch out two main scenarios here:

  * one database per Zope instance.
  * one database per site (or Grok application) in a Zope instance (and
    thus multiple databases per Zope instance).

%package -n python3-module-%oname-tests
Summary: Tests for z3c.saconfig
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This aim of this package is to offer a simple but flexible way to
configure SQLAlchemy's scoped session support using the Zope component
architecture. This package is based on zope.sqlalchemy, which offers
transaction integration between Zope and SQLAlchemy.

This package contains tests for z3c.saconfig.

%package tests
Summary: Tests for z3c.saconfig
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This aim of this package is to offer a simple but flexible way to
configure SQLAlchemy's scoped session support using the Zope component
architecture. This package is based on zope.sqlalchemy, which offers
transaction integration between Zope and SQLAlchemy.

This package contains tests for z3c.saconfig.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Initial build for Sisyphus

