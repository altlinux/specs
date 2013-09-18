%define oname nss
Name: python-module-%oname
Version: 0.14.0
Release: alt1
Summary: Python binding for NSS
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Python
Url: http://www.mozilla.org/projects/security/pki/python-nss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ libnss-devel

%description
python-nss is a Python binding for NSS (Network Security Services) and
NSPR (Netscape Portable Runtime). NSS provides cryptography services
supporting SSL, TLS, PKI, PKIX, X509, PKCS*, etc. NSS is an alternative
to OpenSSL and used extensively by major software projects. NSS is
FIPS-140 certified.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc LICENSE* README doc/ChangeLog doc/examples
%python_sitelibdir/*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Mon Sep 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Initial build for Sisyphus

