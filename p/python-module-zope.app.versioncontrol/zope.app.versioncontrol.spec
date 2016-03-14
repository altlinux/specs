%define oname zope.app.versioncontrol

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt3.1
Summary: A framework for managing multiple versions of objects within a ZODB database
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.versioncontrol/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app ZODB3 zope.datetime zope.location zope.security

%description
This package provides a framework for managing multiple versions of
objects within a ZODB database.

%package -n python3-module-%oname
Summary: A framework for managing multiple versions of objects within a ZODB database
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.datetime zope.location zope.security

%description -n python3-module-%oname
This package provides a framework for managing multiple versions of
objects within a ZODB database.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.versioncontrol
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.event zope.traversing zope.annotation zope.component

%description -n python3-module-%oname-tests
This package provides a framework for managing multiple versions of
objects within a ZODB database.

This package contains tests for zope.app.versioncontrol.

%package tests
Summary: Tests for zope.app.versioncontrol
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.event zope.traversing zope.annotation zope.component

%description tests
This package provides a framework for managing multiple versions of
objects within a ZODB database.

This package contains tests for zope.app.versioncontrol.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

