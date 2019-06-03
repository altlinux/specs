%define oname zope.viewlet

%def_with python3

Name: python-module-%oname
Version: 4.2.1
Release: alt1

Summary: Zope Viewlets

License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.viewlet/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/z/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-zope.size

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-zope.browserpage
BuildPreReq: python3-module-zope.configuration
BuildPreReq: python3-module-zope.contentprovider
BuildPreReq: python3-module-zope.event
BuildPreReq: python3-module-zope.i18nmessageid
BuildPreReq: python3-module-zope.location
BuildPreReq: python3-module-zope.publisher
BuildPreReq: python3-module-zope.schema
BuildPreReq: python3-module-zope.security
BuildPreReq: python3-module-zope.traversing-tests
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-zope.testrunner
BuildPreReq: python3-module-zope.size
%endif

%py_requires zope zope.browserpage zope.component zope.configuration
%py_requires zope.contentprovider zope.event zope.i18nmessageid
%py_requires zope.interface zope.location zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
Viewlets provide a generic framework for building pluggable user
interfaces.

%package -n python3-module-%oname
Summary: Zope Viewlets
Group: Development/Python3
%py3_requires zope zope.browserpage zope.component zope.configuration
%py3_requires zope.contentprovider zope.event zope.i18nmessageid
%py3_requires zope.interface zope.location zope.publisher zope.schema
%py3_requires zope.security zope.traversing

%description -n python3-module-%oname
Viewlets provide a generic framework for building pluggable user
interfaces.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Viewlets
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.size zope.traversing.testing

%description -n python3-module-%oname-tests
Viewlets provide a generic framework for building pluggable user
interfaces.

This package contains tests for Zope Viewlets.

%package tests
Summary: Tests for Zope Viewlets
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.size zope.traversing.testing

%description tests
Viewlets provide a generic framework for building pluggable user
interfaces.

This package contains tests for Zope Viewlets.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
popd
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
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version (4.2.1) with rpmgs script
- switch to build from tarball

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150613
- Version 4.0.1.dev0
- Enabled check

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

