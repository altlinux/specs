%define oname z3c.optionstorage

%def_with python3

Name: python-module-%oname
Version: 1.0.7
Release: alt3.1
Summary: Optional Storages -- Persistent, Managable Vocabularies
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.optionstorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 zope.annotation zope.browserpage zope.component
%py_requires zope.configuration zope.i18n zope.interface zope.proxy
%py_requires zope.schema zope.security zope.traversing zope.app.form

%description
Option Storages are vocabularies that store their values in the ZODB and
can be managed during application runtime.

%package -n python3-module-%oname
Summary: Optional Storages -- Persistent, Managable Vocabularies
Group: Development/Python3
%py3_requires ZODB3 zope.annotation zope.browserpage zope.component
%py3_requires zope.configuration zope.i18n zope.interface zope.proxy
%py3_requires zope.schema zope.security zope.traversing zope.app.form

%description -n python3-module-%oname
Option Storages are vocabularies that store their values in the ZODB and
can be managed during application runtime.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.optionstorage
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Option Storages are vocabularies that store their values in the ZODB and
can be managed during application runtime.

This package contains tests for z3c.optionstorage.

%package tests
Summary: Tests for z3c.optionstorage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Option Storages are vocabularies that store their values in the ZODB and
can be managed during application runtime.

This package contains tests for z3c.optionstorage.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.7-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus

