%define oname ecdsa

Name: python3-module-%oname
Version: 0.17.0
Release: alt1

Summary: ECDSA cryptographic signature library (pure python)

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ecdsa/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4

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

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune
rm -rfv %buildroot%python3_sitelibdir/ecdsa/test_*.py

%files
%doc NEWS README.md
%python3_sitelibdir/*

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt1
- new version 0.17.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- new version 0.16.1 (with rpmrb script)

* Fri Nov 06 2020 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Fri Nov 06 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt2
- build python3 package separately, cleanup spec

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.13-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

