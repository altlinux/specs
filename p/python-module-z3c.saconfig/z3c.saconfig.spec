%define oname z3c.saconfig
Name: python-module-%oname
Version: 0.13
Release: alt1
Summary: Minimal SQLAlchemy ORM session configuration for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.saconfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Initial build for Sisyphus

