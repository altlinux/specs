%define oname repoze.zodbconn

%def_with python3

Name: python-module-%oname
Version: 0.15
Release: alt2.git20130722.1
Summary: Open databases from URI specifications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.zodbconn
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.zodbconn.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze ZODB3 ZConfig

%description
A library which allows ZODB databases to be constructed from URI
specifications.

%package -n python3-module-%oname
Summary: Open databases from URI specifications
Group: Development/Python3
%py3_requires repoze ZODB3 ZConfig

%description -n python3-module-%oname
A library which allows ZODB databases to be constructed from URI
specifications.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.zodbconn
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
A library which allows ZODB databases to be constructed from URI
specifications.

This package contains tests for repoze.zodbconn.

%package tests
Summary: Tests for repoze.zodbconn
Group: Development/Python
Requires: %name = %version-%release

%description tests
A library which allows ZODB databases to be constructed from URI
specifications.

This package contains tests for repoze.zodbconn.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15-alt2.git20130722.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt2.git20130722
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.git20130722
- Version 0.15

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.git20121206
- Version 0.14

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110722
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt1.git20110604.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110604.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110604
- Initial build for Sisyphus

