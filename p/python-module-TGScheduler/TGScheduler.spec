%define oname TGScheduler

%def_with python3

Name: python-module-%oname
Version: 1.6.3
Release: alt3.1
Summary: Turbogears Scheduler
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/TGScheduler
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires dateutil

%description
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

%package -n python3-module-%oname
Summary: Turbogears Scheduler
Group: Development/Python3
%py3_requires dateutil

%description -n python3-module-%oname
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

%package -n python3-module-%oname-tests
Summary: Tests for Turbogears Scheduler
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

This package contains tests for Turbogears Scheduler.

%package tests
Summary: Tests for Turbogears Scheduler
Group: Development/Python
Requires: %name = %EVR

%description tests
This scheduler package is based on the TurboGears 1 built-in scheduler
which is based on Kronos by Irmen de Jong. The scheduler makes it easy
to have one-time or recurring tasks run as needed.

This package contains tests for Turbogears Scheduler.

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
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.3-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt3
- Added necessary requirements

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt2
- Added module for Python 3

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1
- Initial build for Sisyphus

