%define oname pyscrypt

%def_with python3

Name: python-module-%oname
Version: 1.6.2
Release: alt2.git20150203
Summary: Pure-Python implementation of Scrypt PBKDF and scrypt file format library
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pyscrypt/

# https://github.com/ricmoo/pyscrypt.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-pycrypto python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-pycrypto python3-module-pytest
%endif

%py_provides %oname
%py_requires Crypto

%description
A very simple, pure-Python implementation of the scrypt password-based
key derivation function and scrypt file format library with no
dependencies beyond standard Python libraries. See README.md for API
reference and details.

%if_with python3
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
%endif

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
PYTHONPATH=%buildroot%python_sitelibdir python tests/run-tests-file.py
PYTHONPATH=%buildroot%python_sitelibdir python tests/run-tests-hash.py

%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/run-tests-file.py
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/run-tests-hash.py
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
* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt2.git20150203
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.2-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.git20150203
- Initial build for Sisyphus

