%define oname z3c.recipe.ldap
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Deploy an OpenLDAP server in a zc.buildout
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe zc.buildout zc.recipe.egg

%description
This recipe can be used to deploy an OpenLDAP server in a zc.buildout.
More specifically it provides for initializing an LDAP database from an
LDIF file and for setting up an LDAP instance in the buildout. This
recipe can also be used to provide an isolated LDAP instance as a test
fixture.

%package tests
Summary: Tests for z3c.recipe.ldap
Group: Development/Python
Requires: %name = %version-%release

%description tests
This recipe can be used to deploy an OpenLDAP server in a zc.buildout.
More specifically it provides for initializing an LDAP database from an
LDIF file and for setting up an LDAP instance in the buildout. This
recipe can also be used to provide an isolated LDAP instance as a test
fixture.

This package contains tests for z3c.recipe.ldap.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

