%define oname zc.signalhandler

Name: python3-module-%oname
Version: 1.2.0
Release: alt4

Summary: Configurable signal handling for ZConfig
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zc.signalhandler/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%py3_requires zc ZConfig


%description
This package allows registration of signal handlers from ZConfig
configuration files within the framework provided by the Zope Toolkit.

Any number of handlers may be registered for any given signal.

%package tests
Summary: Tests for zc.signalhandler
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
This package allows registration of signal handlers from ZConfig
configuration files within the framework provided by the Zope Toolkit.

Any number of handlers may be registered for any given signal.

This package contains tests for zc.signalhandler.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

