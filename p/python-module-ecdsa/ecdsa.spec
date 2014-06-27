%define oname ecdsa
Name: python-module-%oname
Version: 0.11
Release: alt1
Summary: ECDSA cryptographic signature library (pure python)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ecdsa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel

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
%python_build_debug

%install
%python_install

%files
%doc NEWS README.md
%python_sitelibdir/*

%changelog
* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

