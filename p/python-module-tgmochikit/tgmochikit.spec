%define oname tgmochikit

%def_with python3

Name: python-module-%oname
Version: 1.4.2
Release: alt2.1
Summary: MochiKit packaged as TurboGears widgets
License: AFL/MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/tgMochiKit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
MochiKit packaged as TurboGears widgets.

%package -n python3-module-%oname
Summary: MochiKit packaged as TurboGears widgets
Group: Development/Python3

%description -n python3-module-%oname
MochiKit packaged as TurboGears widgets.

%package -n python3-module-%oname-tests
Summary: Tests for tgMochiKit
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
MochiKit packaged as TurboGears widgets.

This package contains tests for tgMochiKit.

%package tests
Summary: Tests for tgMochiKit
Group: Development/Python
Requires: %name = %version-%release

%description tests
MochiKit packaged as TurboGears widgets.

This package contains tests for tgMochiKit.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ChangeLog PKG-INFO *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog PKG-INFO *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

