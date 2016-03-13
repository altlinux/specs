%define oname repoze.whoplugins.zodb

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt3.1
Summary: ZODB authenticator and metadata plugin for repoze.who
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.whoplugins.zodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.who.plugins repoze.who repoze.zodbconn transaction
%py_requires ZODB3

%description
A repoze.who plugin to authenticate a userid and attach group
information based on information stored in a ZODB database.

%package -n python3-module-%oname
Summary: ZODB authenticator and metadata plugin for repoze.who
Group: Development/Python3
%py3_requires repoze.who.plugins repoze.who repoze.zodbconn transaction
%py3_requires ZODB3

%description -n python3-module-%oname
A repoze.who plugin to authenticate a userid and attach group
information based on information stored in a ZODB database.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.whoplugins.zodb
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
A repoze.who plugin to authenticate a userid and attach group
information based on information stored in a ZODB database.

This package contains tests for repoze.whoplugins.zodb.

%package tests
Summary: Tests for repoze.whoplugins.zodb
Group: Development/Python
Requires: %name = %version-%release

%description tests
A repoze.who plugin to authenticate a userid and attach group
information based on information stored in a ZODB database.

This package contains tests for repoze.whoplugins.zodb.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

