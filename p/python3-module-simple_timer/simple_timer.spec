%define oname simple_timer

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Makes it easy to track elapsed time
License: GPLv2.0/LGPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/simple_timer/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
A timer module. Makes it easy to track elapsed time.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A timer module. Makes it easy to track elapsed time.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=$PWD/src
%__python3 src/simple_timer/tests.py

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

