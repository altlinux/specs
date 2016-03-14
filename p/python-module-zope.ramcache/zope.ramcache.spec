%define oname zope.ramcache

%def_with python3

Name: python-module-%oname
Version: 2.1.0
Release: alt1.1
Summary: Zope RAM Cache
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.ramcache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.interface zope.location zope.testing ZODB3

%description
This package provides a RAM cache implementation for Zope.

%package -n python3-module-%oname
Summary: Zope RAM Cache
Group: Development/Python3
%py3_requires zope zope.interface zope.location zope.testing ZODB3

%description -n python3-module-%oname
This package provides a RAM cache implementation for Zope.

%package -n python3-module-%oname-tests
Summary: Tests for Zope RAM Cache
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a RAM cache implementation for Zope.

This package contains tests for Zope RAM Cache.

%package tests
Summary: Tests for Zope RAM Cache
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a RAM cache implementation for Zope.

This package contains tests for Zope RAM Cache.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

