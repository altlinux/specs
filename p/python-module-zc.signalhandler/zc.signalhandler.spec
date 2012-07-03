%define oname zc.signalhandler
Name: python-module-%oname
Version: 1.2.0
Release: alt2.1
Summary: Configurable signal handling for ZConfig
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.signalhandler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc ZConfig

%description
This package allows registration of signal handlers from ZConfig
configuration files within the framework provided by the Zope Toolkit.

Any number of handlers may be registered for any given signal.

%package tests
Summary: Tests for zc.signalhandler
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package allows registration of signal handlers from ZConfig
configuration files within the framework provided by the Zope Toolkit.

Any number of handlers may be registered for any given signal.

This package contains tests for zc.signalhandler.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

