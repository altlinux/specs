%define oname m2crypto

Summary: M2Crypto: A Python crypto and SSL toolkit
Version: 0.22
Release: alt1.git20131121.1
Name: python3-module-%oname
# https://github.com/mcepl/M2Crypto.git - branch python3
Source0: %name-%version.tar
License: BSD
Group: Development/Python3
URL: https://github.com/mcepl/m2crypto

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel libssl-devel python3-module-py swig
#BuildPreReq: python3-module-setuptools-tests /proc
#BuildPreReq: python3-module-py python-tools-2to3 libnumpy-py3-devel

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libcom_err-devel libkrb5-devel pkg-config python-base python-modules python3 python3-base python3-module-numpy python3-module-setuptools swig-data
BuildRequires: libssl-devel python3-devel python3-module-pytest rpm-build-python3 swig

%description
M2Crypto is the most complete Python wrapper for OpenSSL featuring RSA,
DSA, DH, EC, HMACs, message digests, symmetric ciphers (including AES);
SSL functionality to implement clients and servers; HTTPS extensions to
Python's httplib, urllib, and xmlrpclib; unforgeable HMAC'ing
AuthCookies for web session management; FTP/TLS client and server;
S/MIME; ZServerSSL: A HTTPS server for Zope and ZSmime: An S/MIME
messenger for Zope. M2Crypto can also be used to provide SSL for
Twisted. Smartcards supported through the Engine interface.

%prep
%setup

%build
if pkg-config openssl ; then
	FLAGS="`pkg-config --cflags openssl`"
	%add_optflags $FLAGS
	LDFLAGS="$LDFLAGS`pkg-config --libs-only-L openssl`" ; export LDFLAGS
fi

# -cpperraswarn is necessary for including opensslconf-${basearch} directly
export SWIG_FEATURES=-cpperraswarn
%python3_build_debug

%install

CFLAGS="%optflags" ; export CFLAGS
if pkg-config openssl ; then
	CFLAGS="$CFLAGS `pkg-config --cflags openssl`" ; export CFLAGS
	LDFLAGS="$LDFLAGS`pkg-config --libs-only-L openssl`" ; export LDFLAGS
fi

%python3_build_install

%files
%doc CHANGES LICENCE README* demo tests doc/*
%python3_sitelibdir/*

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.22-alt1.git20131121.1
- NMU: Use buildreq for BR.

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1.git20131121
- Initial build for Sisyphus

