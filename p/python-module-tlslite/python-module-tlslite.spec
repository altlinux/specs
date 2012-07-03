%define oname tlslite

Name: python-module-%oname
Version: 0.3.8
Release: alt2.1.1

Summary: Python library that implements TLS/SSL

License: Public domain
Group: Development/Python
Url: http://trevp.net/tlslite/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://trevp.net/tlslite/%oname-%version.tar.bz2

%setup_python_module %oname

%description
TLS Lite is a free python library that implements SSL 3.0, TLS 1.0, and
TLS 1.1. TLS Lite supports non-traditional authentication methods such as
SRP, shared keys, and cryptoIDs in addition to X.509 certificates. TLS
Lite is pure Python, however it can access OpenSSL, cryptlib, pycrypto,
and GMPY for faster crypto operations. TLS Lite integrates with httplib,
xmlrpclib, poplib, imaplib, smtplib, SocketServer, asyncore, and Twisted.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc readme.txt
%_bindir/tls.py
%_bindir/tlsdb.py
%python_sitelibdir/tlslite/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.8-alt2.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt2.1
- Rebuilt with python 2.6

* Sat Feb 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt2
- cleanup spec, fix build on x86_64 (thanks to Dmitry Levin)

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt1
- initial build for ALT Linux Sisyphus
