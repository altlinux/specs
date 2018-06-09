%define oname pycryptopp

Name: python-module-%oname
Version: 0.7.1
Release: alt1

Summary: Python wrappers for a few algorithms from the Crypto++ library
License: GPLv2+ or other (see copyright)
Group: Development/Python
Url: https://pypi.python.org/pypi/pycryptopp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-git: https://github.com/tahoe-lafs/pycryptopp.git
Source: %name-%version.tar

# fix build with libcryptopp >= 6 https://gist.github.com/skydrome/bb9665fc0b449167bb25a57b45829ca8
Patch1: libcryptopp-6.patch

BuildPreReq: gcc-c++ git-core
BuildPreReq: libcryptopp-devel >= 6
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-ecdsa python-module-ed25519

%py_provides %oname
%py_requires ecdsa ed25519

%description
pycryptopp is a python wrapper around a few algorithms from the Crypto++
and python-Ed25519 libraries.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pycryptopp is a python wrapper around a few algorithms from the Crypto++
and python-Ed25519 libraries.

This package contains tests for %oname.

%prep
%setup
%patch1

sed -i 's|@VERSION@|%version|' \
	src/pycryptopp/publickey/ed25519/_version.py
git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "%oname-%version"
git tag %oname-%version -m "%oname-%version"

%build
%python_build_debug --disable-embedded-cryptopp

%install
%python_install
rm -rf %_docdir/pycryptopp/

%check
python setup.py test

%files
%doc COPYING* copyright *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/bench

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/bench

%changelog
* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- build new version
- rebuild with libcryptopp-6.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt3.git20130916.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt3.git20130916.2
- NMU: autorebuild with libcryptopp-5.6.5

* Wed Jan 18 2017 Michael Shigorin <mike@altlinux.org> 0.6.0-alt3.git20130916.1
- it's not git, it's git-core!

* Mon Feb 01 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt3.git20130916
- rebuild with cryptopp-5.6.3

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.git20130916
- Rebuilt with gcc5

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20130916
- Initial build for Sisyphus

