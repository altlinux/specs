%define oname pycrypto

%def_without python3
%def_without check

Name: python-module-%oname
Version: 2.7
Release: alt7.a1.git20140620
Summary: Cryptographic modules for Python
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/pycrypto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dlitz/pycrypto.git
Source: %name-%version.tar
Patch: replace-time.clock-with-timeit.default_timer.patch

BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-epydoc gcc-c++ libgmp-devel libmpir-devel
BuildPreReq: gcc-c++ libgmp-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Conflicts: python-module-Crypto < %EVR
Obsoletes: python-module-Crypto < %EVR
Provides: python-module-Crypto = %EVR
%py_provides Crypto

%description
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.). The package is structured to make adding new modules easy. This
section is essentially complete, and the software interface will almost
certainly not change in an incompatible way in the future; all that
remains to be done is to fix any bugs that show up.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.). The package is structured to make adding new modules easy. This
section is essentially complete, and the software interface will almost
certainly not change in an incompatible way in the future; all that
remains to be done is to fix any bugs that show up.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
#BuildArch: noarch

%description docs
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.). The package is structured to make adding new modules easy. This
section is essentially complete, and the software interface will almost
certainly not change in an incompatible way in the future; all that
remains to be done is to fix any bugs that show up.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Cryptographic modules for Python
Group: Development/Python3
Conflicts: python3-module-Crypto < %EVR
Obsoletes: python3-module-Crypto < %EVR
Provides: python3-module-Crypto = %EVR
%py3_provides Crypto
%add_python3_req_skip Crypto.Random.OSRNG.winrandom

%description -n python3-module-%oname
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.). The package is structured to make adding new modules easy. This
section is essentially complete, and the software interface will almost
certainly not change in an incompatible way in the future; all that
remains to be done is to fix any bugs that show up.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.). The package is structured to make adding new modules easy. This
section is essentially complete, and the software interface will almost
certainly not change in an incompatible way in the future; all that
remains to be done is to fix any bugs that show up.

This package contains tests for %oname.

%prep
%setup
%patch -p1

./bootstrap.sh

# update gnu-config scripts
cp /usr/share/gnu-config/config.* build-aux/
%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
python2 setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ACKS ChangeLog README TODO LEGAL/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/SelfTest

%files tests
%python_sitelibdir/*/SelfTest

%files docs
#doc Doc/*.txt Doc/*.rst Doc/apidoc

%if_with python3
%files -n python3-module-%oname
%doc ACKS ChangeLog README TODO LEGAL/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/SelfTest

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/SelfTest
%endif

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 2.7-alt7.a1.git20140620
- Build without check.
- Build without docs.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7-alt6.a1.git20140620
- Disabled build of python-3 module.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 2.7-alt5.a1.git20140620
- Fixed FTBFS.

* Sun Feb 23 2020 Grigory Ustinov <grenka@altlinux.org> 2.7-alt4.a1.git20140620
- Fixed build with python3.8.

* Wed Feb 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7-alt3.a1.git20140620.1.1.1.1
- Update gnu-config scripts before build.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7-alt3.a1.git20140620.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.7-alt3.a1.git20140620.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7-alt3.a1.git20140620.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 25 2016 Denis Medvedev <nbr@altlinux.org> 2.7-alt3.a1.git20140620
- NMU changes for building on Python3.5.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt2.a1.git20140620
- Obsoletes python-module-Crypto and provides it

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.a1.git20140620
- Initial build for Sisyphus

