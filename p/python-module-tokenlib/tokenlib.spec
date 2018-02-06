%define oname tokenlib

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt2.git20140108.1.1
Summary: Generic support library for signed-token-based auth schemes
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/tokenlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/tokenlib.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-module-setuptools python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%endif

%py_provides %oname

%description
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Generic support library for signed-token-based auth schemes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt2.git20140108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.git20140108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.3.1-alt2.git20140108
- cleanup buildreq

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140108
- Initial build for Sisyphus

