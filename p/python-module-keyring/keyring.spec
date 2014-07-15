%define oname keyring

%def_with python3

Name: python-module-%oname
Version: 3.8
Release: alt2

Summary: Store and access your passwords safely
License: PSF
Group: Development/Python

Url: https://pypi.python.org/pypi/keyring

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%setup_python_module %oname

%description
Store and access your passwords safely.

%package -n python3-module-%oname
Summary: Store and access your passwords safely
Group: Development/Python3

%description -n python3-module-%oname
Store and access your passwords safely.

%package -n python3-module-%oname-tests
Summary: Tests for keyring
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Store and access your passwords safely.

This package contains tests for keyring.

%package tests
Summary: Tests for keyring
Group: Development/Python
Requires: %name = %EVR

%description tests
Store and access your passwords safely.

This package contains tests for keyring.

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

%files
%doc *.rst *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Version 3.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

