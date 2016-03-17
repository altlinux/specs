%define oname zope.app.i18n

%def_with python3

Name: python-module-%oname
Version: 3.6.4
Release: alt2.1
Summary: Persistent translation domains and message catalogs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app zope.publisher zope.component zope.container
%py_requires zope.configuration zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.security ZODB3

%description
This package provides placeful persistent translation domains and
message catalogs along with ZMI views for managing them.

%package -n python3-module-%oname
Summary: Persistent translation domains and message catalogs
Group: Development/Python3
%py3_requires zope.app zope.publisher zope.component zope.container
%py3_requires zope.configuration zope.i18n zope.i18nmessageid
%py3_requires zope.interface zope.security ZODB3

%description -n python3-module-%oname
This package provides placeful persistent translation domains and
message catalogs along with ZMI views for managing them.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.i18n
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.component

%description -n python3-module-%oname-tests
This package provides placeful persistent translation domains and
message catalogs along with ZMI views for managing them.

This package contains tests for zope.app.i18n.

%package tests
Summary: Tests for zope.app.i18n
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.component

%description tests
This package provides placeful persistent translation domains and
message catalogs along with ZMI views for managing them.

This package contains tests for zope.app.i18n.

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
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.4-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.4-alt1
- Version 3.6.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Initial build for Sisyphus

