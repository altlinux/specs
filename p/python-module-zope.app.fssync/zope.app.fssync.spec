%define oname zope.app.fssync

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt2.1
Summary: Filesystem synchronization utility for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.fssync/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires paramiko zope.dublincore zope.fssync zope.i18nmessageid
%py_requires zope.interface zope.proxy zope.testbrowser zope.traversing
%py_requires zope.xmlpickle zope.app.catalog zope.app.component
%py_requires zope.app.dtmlpage zope.app.file zope.app.folder
%py_requires zope.app.module zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.app.zptpage zope.app

%description
The FSSync project (zope.app.fssync) provides support for filesystem
synchronization of Zope3 content that resides in a ZODB. This package
defines a Web-based API with basic support for some standard zope.app
content types and the standard security policy.

This project is build on top of the more general zope.fssync package
which provides object serialization and deserialization tools. If you
need a pure Python API which is independent of the ZODB and the Zope3
security machinery you should look at zope.fssync.

%package -n python3-module-%oname
Summary: Filesystem synchronization utility for Zope 3
Group: Development/Python3
%py3_requires paramiko zope.dublincore zope.fssync zope.i18nmessageid
%py3_requires zope.interface zope.proxy zope.testbrowser zope.traversing
%py3_requires zope.xmlpickle zope.app.catalog zope.app.component
%py3_requires zope.app.dtmlpage zope.app.file zope.app.folder
%py3_requires zope.app.module zope.app.securitypolicy zope.app.zcmlfiles
%py3_requires zope.app.zptpage zope.app

%description -n python3-module-%oname
The FSSync project (zope.app.fssync) provides support for filesystem
synchronization of Zope3 content that resides in a ZODB. This package
defines a Web-based API with basic support for some standard zope.app
content types and the standard security policy.

This project is build on top of the more general zope.fssync package
which provides object serialization and deserialization tools. If you
need a pure Python API which is independent of the ZODB and the Zope3
security machinery you should look at zope.fssync.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.fssync
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The FSSync project (zope.app.fssync) provides support for filesystem
synchronization of Zope3 content that resides in a ZODB. This package
defines a Web-based API with basic support for some standard zope.app
content types and the standard security policy.

This project is build on top of the more general zope.fssync package
which provides object serialization and deserialization tools. If you
need a pure Python API which is independent of the ZODB and the Zope3
security machinery you should look at zope.fssync.

This package contains tests for zope.app.fssync.

%package tests
Summary: Tests for zope.app.fssync
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The FSSync project (zope.app.fssync) provides support for filesystem
synchronization of Zope3 content that resides in a ZODB. This package
defines a Web-based API with basic support for some standard zope.app
content types and the standard security policy.

This project is build on top of the more general zope.fssync package
which provides object serialization and deserialization tools. If you
need a pure Python API which is independent of the ZODB and the Zope3
security machinery you should look at zope.fssync.

This package contains tests for zope.app.fssync.

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
%exclude %python_sitelibdir/*/*/*/*test*
%exclude %python_sitelibdir/*/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*/*test*
%python_sitelibdir/*/*/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*test*
%python3_sitelibdir/*/*/*/*/*test*
%python3_sitelibdir/*/*/*/*/*/*test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Version 3.6.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1
- Initial build for Sisyphus

