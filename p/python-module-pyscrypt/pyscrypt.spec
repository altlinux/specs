%define oname pyscrypt

%def_with python3

Name: python-module-%oname
Version: 1.6.2
Release: alt1.git20150203.1
Summary: Pure-Python implementation of Scrypt PBKDF and scrypt file format library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyscrypt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ricmoo/pyscrypt.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pycrypto
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pycrypto
%endif

%py_provides %oname
%py_requires Crypto

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python-module-pycrypto python-module-pytest python3-module-pycrypto python3-module-pytest rpm-build-python3 time

%description
A very simple, pure-Python implementation of the scrypt password-based
key derivation function and scrypt file format library with no
dependencies beyond standard Python libraries. See README.md for API
reference and details.

%package -n python3-module-%oname
Summary: Pure-Python implementation of Scrypt PBKDF and scrypt file format library
Group: Development/Python3
%py3_provides %oname
%py3_requires Crypto

%description -n python3-module-%oname
A very simple, pure-Python implementation of the scrypt password-based
key derivation function and scrypt file format library with no
dependencies beyond standard Python libraries. See README.md for API
reference and details.

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
py.test -vv
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.git20150203
- Initial build for Sisyphus

