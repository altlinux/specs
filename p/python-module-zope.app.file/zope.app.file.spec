%define oname zope.app.file

%def_with python3

Name: python-module-%oname
Version: 3.6.1
Release: alt4.1
Summary: File and Image -- Zope 3 Content Components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires transaction ZODB3 zope.app.publication zope.contenttype
%py_requires zope.datetime zope.dublincore zope.event zope.exceptions
%py_requires zope.filerepresentation zope.i18nmessageid zope.interface
%py_requires zope.schema zope.site zope.size

%description
This package provides two basic Zope 3 content components, File and
Image, and their ZMI-compliant browser views.

%package -n python3-module-%oname
Summary: File and Image -- Zope 3 Content Components
Group: Development/Python3
%py3_requires transaction ZODB3 zope.app.publication zope.contenttype
%py3_requires zope.datetime zope.dublincore zope.event zope.exceptions
%py3_requires zope.filerepresentation zope.i18nmessageid zope.interface
%py3_requires zope.schema zope.site zope.size

%description -n python3-module-%oname
This package provides two basic Zope 3 content components, File and
Image, and their ZMI-compliant browser views.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.file
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles
%py3_requires zope.publisher zope.login

%description -n python3-module-%oname-tests
This package provides two basic Zope 3 content components, File and
Image, and their ZMI-compliant browser views.

This package contains tests for zope.app.file.

%package tests
Summary: Tests for zope.app.file
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.publisher zope.login

%description tests
This package provides two basic Zope 3 content components, File and
Image, and their ZMI-compliant browser views.

This package contains tests for zope.app.file.

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
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Moved all tests into tests package

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

