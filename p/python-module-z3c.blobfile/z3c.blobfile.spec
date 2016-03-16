%define oname z3c.blobfile

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt4.1
Summary: File and Image Using Blob Support of ZODB -- Zope 3 Content Components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.blobfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 zope.app.publication zope.contenttype zope.datetime
%py_requires zope.dublincore zope.event zope.exceptions
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.schema zope.size zope.app.file zope.copy

%description
This package provides an implementation of
zope.app.file.interfaces.IFile which uses the Blob support introduced in
ZODB 3.8. It's main purpose is to provide an easy migration path for
existing instances. For more advanced file implementations see zope.file
and z3c.extfile.

The standard implementation in zope.app.file uses chunk objects to break
big files into manageable parts. These chunks flow the server caches
whereas blobs are directly consumed by the publisher. The main
difference between this blob implementation and the old zope.app.file
implementation can be seen in a replacement of the chunk objects by
Blobs.

%package -n python3-module-%oname
Summary: File and Image Using Blob Support of ZODB -- Zope 3 Content Components
Group: Development/Python3
%py3_requires ZODB3 zope.app.publication zope.contenttype zope.datetime
%py3_requires zope.dublincore zope.event zope.exceptions
%py3_requires zope.i18nmessageid zope.interface zope.publisher
%py3_requires zope.schema zope.size zope.app.file zope.copy

%description -n python3-module-%oname
This package provides an implementation of
zope.app.file.interfaces.IFile which uses the Blob support introduced in
ZODB 3.8. It's main purpose is to provide an easy migration path for
existing instances. For more advanced file implementations see zope.file
and z3c.extfile.

The standard implementation in zope.app.file uses chunk objects to break
big files into manageable parts. These chunks flow the server caches
whereas blobs are directly consumed by the publisher. The main
difference between this blob implementation and the old zope.app.file
implementation can be seen in a replacement of the chunk objects by
Blobs.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.blobfile
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.file zope.app.testing zope.app.securitypolicy
%py3_requires zope.app.zcmlfiles zope.testbrowser

%description -n python3-module-%oname-tests
This package provides an implementation of
zope.app.file.interfaces.IFile which uses the Blob support introduced in
ZODB 3.8. It's main purpose is to provide an easy migration path for
existing instances. For more advanced file implementations see zope.file
and z3c.extfile.

The standard implementation in zope.app.file uses chunk objects to break
big files into manageable parts. These chunks flow the server caches
whereas blobs are directly consumed by the publisher. The main
difference between this blob implementation and the old zope.app.file
implementation can be seen in a replacement of the chunk objects by
Blobs.

This package contains tests for z3c.blobfile.

%package tests
Summary: Tests for z3c.blobfile
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.file zope.app.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
This package provides an implementation of
zope.app.file.interfaces.IFile which uses the Blob support introduced in
ZODB 3.8. It's main purpose is to provide an easy migration path for
existing instances. For more advanced file implementations see zope.file
and z3c.extfile.

The standard implementation in zope.app.file uses chunk objects to break
big files into manageable parts. These chunks flow the server caches
whereas blobs are directly consumed by the publisher. The main
difference between this blob implementation and the old zope.app.file
implementation can be seen in a replacement of the chunk objects by
Blobs.

This package contains tests for z3c.blobfile.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.5-alt3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt2
- Enabled tests

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus

