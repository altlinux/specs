%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.sqlalchemy

%def_with python3

Name: python-module-%oname
Version: 0.7.7
#Release: alt1.1
Summary: Minimal Zope/SQLAlchemy transaction integration
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/14/95/47ef5f5fbf5f18dc95d6d39b7dbd690818b541afa724d14ed176e415b134/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope SQLAlchemy transaction zope.interface zc.buildout

%description
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it
seeks only to provide a data manager and makes no attempt to define a
zopeish way to configure engines.

For WSGI applications, Zope style automatic transaction management is
available with repoze.tm2, a part of Repoze BFG and Turbogears 2.

%package -n python3-module-%oname
Summary: Minimal Zope/SQLAlchemy transaction integration
Group: Development/Python3
%py3_requires zope SQLAlchemy transaction zope.interface zc.buildout

%description -n python3-module-%oname
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it
seeks only to provide a data manager and makes no attempt to define a
zopeish way to configure engines.

For WSGI applications, Zope style automatic transaction management is
available with repoze.tm2, a part of Repoze BFG and Turbogears 2.

%package -n python3-module-%oname-tests
Summary: Tests for zope.sqlalchemy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing
%add_python3_req_skip pysqlite2

%description -n python3-module-%oname-tests
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it
seeks only to provide a data manager and makes no attempt to define a
zopeish way to configure engines.

For WSGI applications, Zope style automatic transaction management is
available with repoze.tm2, a part of Repoze BFG and Turbogears 2.

This package contains tests for zope.sqlalchemy.

%package tests
Summary: Tests for zope.sqlalchemy
Group: Development/Python
Requires: %name = %version-%release
%py_requires pysqlite2 zope.testing

%description tests
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it
seeks only to provide a data manager and makes no attempt to define a
zopeish way to configure engines.

For WSGI applications, Zope style automatic transaction management is
available with repoze.tm2, a part of Repoze BFG and Turbogears 2.

This package contains tests for zope.sqlalchemy.

%prep
%setup -q -n %{oname}-%{version}

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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.7-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.5-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1
- Version 0.7.5
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1
- Version 0.7.3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

