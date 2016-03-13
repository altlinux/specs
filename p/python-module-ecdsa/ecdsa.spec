%define oname ecdsa

%def_with python3

Name: python-module-%oname
Version: 0.13
Release: alt1.1
Summary: ECDSA cryptographic signature library (pure python)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ecdsa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

This library provides key generation, signing, and verifying, for five
popular NIST "Suite B" GF(p) curves, with key lengths of 192, 224, 256,
384, and 521 bits. The "short names" for these curves, as known by the
OpenSSL tool, are: prime192v1, secp224r1, prime256v1, secp384r1, and
secp521r1. No other curves are included, but it would not be too hard to
add more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

This library provides key generation, signing, and verifying, for five
popular NIST "Suite B" GF(p) curves, with key lengths of 192, 224, 256,
384, and 521 bits. The "short names" for these curves, as known by the
OpenSSL tool, are: prime192v1, secp224r1, prime256v1, secp384r1, and
secp521r1. No other curves are included, but it would not be too hard to
add more.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: ECDSA cryptographic signature library (pure python)
Group: Development/Python3

%description -n python3-module-%oname
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

This library provides key generation, signing, and verifying, for five
popular NIST "Suite B" GF(p) curves, with key lengths of 192, 224, 256,
384, and 521 bits. The "short names" for these curves, as known by the
OpenSSL tool, are: prime192v1, secp224r1, prime256v1, secp384r1, and
secp521r1. No other curves are included, but it would not be too hard to
add more.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is an easy-to-use implementation of ECDSA cryptography (Elliptic
Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly
create keypairs (signing key and verifying key), sign messages, and
verify the signatures. The keys and signatures are very short, making
them easy to handle and incorporate into other protocols.

This library provides key generation, signing, and verifying, for five
popular NIST "Suite B" GF(p) curves, with key lengths of 192, 224, 256,
384, and 521 bits. The "short names" for these curves, as known by the
OpenSSL tool, are: prime192v1, secp224r1, prime256v1, secp384r1, and
secp521r1. No other curves are included, but it would not be too hard to
add more.

This package contains tests for %oname.
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

%files
%doc NEWS README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc NEWS README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

