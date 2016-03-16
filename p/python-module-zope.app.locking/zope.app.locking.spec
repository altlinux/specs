%define oname zope.app.locking

%def_with python3

Name: python-module-%oname
Version: 3.5.0
Release: alt3.1
Summary: Simple Object Locking Framework for Zope 3 applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.locking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.security zope.app.keyreference zope.app.i18n
%py_requires zope.interface zope.schema zope.component zope.app.i18n
%py_requires ZODB3 zope.event zope.traversing zope.size

%description
This package provides a framework for object locking. The implementation
is intended to provide a simple general-purpose locking architecture
upon which other locking applications can be built (WebDAV locking, for
example).

%package -n python3-module-%oname
Summary: Simple Object Locking Framework for Zope 3 applications
Group: Development/Python3
%py3_requires zope.security zope.app.keyreference zope.app.i18n
%py3_requires zope.interface zope.schema zope.component zope.app.i18n
%py3_requires ZODB3 zope.event zope.traversing zope.size

%description -n python3-module-%oname
This package provides a framework for object locking. The implementation
is intended to provide a simple general-purpose locking architecture
upon which other locking applications can be built (WebDAV locking, for
example).

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.locking
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing zope.app.file zope.site

%description -n python3-module-%oname-tests
This package provides a framework for object locking. The implementation
is intended to provide a simple general-purpose locking architecture
upon which other locking applications can be built (WebDAV locking, for
example).

This package contains tests for zope.app.locking.

%package tests
Summary: Tests for zope.app.locking
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing zope.app.file zope.site

%description tests
This package provides a framework for object locking. The implementation
is intended to provide a simple general-purpose locking architecture
upon which other locking applications can be built (WebDAV locking, for
example).

This package contains tests for zope.app.locking.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

