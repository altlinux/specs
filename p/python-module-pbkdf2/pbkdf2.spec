%define oname pbkdf2

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1
Summary: PKCS#5 v2.0 PBKDF2 Module
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pbkdf2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
This module implements the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%if_with python3
%package -n python3-module-%oname
Summary: PKCS#5 v2.0 PBKDF2 Module (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This module implements the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

