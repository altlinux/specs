%define oname z3c.recipe.ldap

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt3.1
Summary: Deploy an OpenLDAP server in a zc.buildout
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.recipe zc.buildout zc.recipe.egg

%description
This recipe can be used to deploy an OpenLDAP server in a zc.buildout.
More specifically it provides for initializing an LDAP database from an
LDIF file and for setting up an LDAP instance in the buildout. This
recipe can also be used to provide an isolated LDAP instance as a test
fixture.

%package -n python3-module-%oname
Summary: Deploy an OpenLDAP server in a zc.buildout
Group: Development/Python3
%py3_requires z3c.recipe zc.buildout zc.recipe.egg

%description -n python3-module-%oname
This recipe can be used to deploy an OpenLDAP server in a zc.buildout.
More specifically it provides for initializing an LDAP database from an
LDIF file and for setting up an LDAP instance in the buildout. This
recipe can also be used to provide an isolated LDAP instance as a test
fixture.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.recipe.ldap
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This recipe can be used to deploy an OpenLDAP server in a zc.buildout.
More specifically it provides for initializing an LDAP database from an
LDIF file and for setting up an LDAP instance in the buildout. This
recipe can also be used to provide an isolated LDAP instance as a test
fixture.

This package contains tests for z3c.recipe.ldap.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

