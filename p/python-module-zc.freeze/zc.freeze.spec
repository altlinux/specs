%define oname zc.freeze

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt3.1
Summary: Pattern for freezing objects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.freeze/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc pytz rwproperty zc.copy ZODB3 zope.annotation
%py_requires zope.cachedescriptors zope.component zope.event
%py_requires zope.interface zope.locking

%description
The zc.freeze package provides a pattern for freezing objects. State is
informational--enforcement unspecified. Some enforcement approaches and
helpers are included.

%package -n python3-module-%oname
Summary: Pattern for freezing objects
Group: Development/Python3
%py3_requires zc pytz rwproperty zc.copy ZODB3 zope.annotation
%py3_requires zope.cachedescriptors zope.component zope.event
%py3_requires zope.interface zope.locking

%description -n python3-module-%oname
The zc.freeze package provides a pattern for freezing objects. State is
informational--enforcement unspecified. Some enforcement approaches and
helpers are included.

%package -n python3-module-%oname-tests
Summary: Tests for zc.freeze
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires transaction zope.app.container zope.app.keyreference
%py3_requires zope.app.testing zope.testing

%description -n python3-module-%oname-tests
The zc.freeze package provides a pattern for freezing objects. State is
informational--enforcement unspecified. Some enforcement approaches and
helpers are included.

This package contains tests for zc.freeze.

%package tests
Summary: Tests for zc.freeze
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction zope.app.container zope.app.keyreference
%py_requires zope.app.testing zope.testing

%description tests
The zc.freeze package provides a pattern for freezing objects. State is
informational--enforcement unspecified. Some enforcement approaches and
helpers are included.

This package contains tests for zc.freeze.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

