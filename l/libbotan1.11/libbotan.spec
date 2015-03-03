%def_without python3
%define branch 1.11
%define oname botan

Name: lib%oname%branch
Version: %branch.15
Release: alt1.git20150302

Summary: A C++ Crypto Library
License: BSD
Group: System/Libraries

Url: http://botan.randombit.net

# https://github.com/randombit/botan.git
Source: %name-%version.tar

BuildRequires: bzlib-devel gcc-c++ libgmp-devel libssl-devel
BuildRequires: python-modules-compiler python-modules-logging zlib-devel
BuildPreReq: python-module-sphinx-devel doxygen boost-python-devel
BuildPreReq: libsqlite3-devel liblzma-devel boost-filesystem-devel
BuildPreReq: boost-asio-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel boost-python3-devel python-tools-2to3
%endif

%description
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary

%package -n python-module-%oname
Summary: Python module of Botan
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description -n python-module-%oname
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

This package contains Python module of Botan.

%package -n python3-module-%oname
Summary: Python module of Botan
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description -n python3-module-%oname
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

This package contains Python module of Botan.

%prep
%setup

sed -i 's|@BRANCH@|%branch|' src/python/botan.py

%build
%ifarch x86_64
LIB_SUFFIX=64
%endif

./configure.py --prefix=%prefix \
	--bindir=%_bindir \
	--libdir=%_libdir \
	--docdir=%_defaultdocdir/%name \
	--includedir=%_includedir \
	--destdir=%buildroot \
	--makefile-style=gmake \
	--with-bzip2 \
	--with-zlib \
	--with-openssl \
	--with-sphinx \
	--with-doxygen \
	--with-boost \
	--with-sqlite3 \
	--with-lzma \
	--with-python-version=%_python_version \
	--single-amalgamation-file

%make_build

%install
%ifarch x86_64
LIB_SUFFIX=64
%endif

%makeinstall_std
chmod +x %buildroot%python_sitelibdir_noarch/botan.py

ln -s botan-%branch.pc %buildroot%_pkgconfigdir/botan.pc

%if_with python3
install -d %buildroot%python3_sitelibdir_noarch
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' src/python/botan.py
2to3 -w -n src/python/botan.py
install -m755 src/python/botan.py %buildroot%python3_sitelibdir_noarch/
%endif

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%buildroot%python_sitelibdir_noarch/botan.py

%files
%_bindir/*
%_libdir/*.so.*

%files devel
%_includedir/botan/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc %_defaultdocdir/%name

%files -n python-module-%oname
%python_sitelibdir_noarch/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir_noarch/*
%endif

%changelog
* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.15-alt1.git20150302
- Version 1.11.15

* Tue Sep 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.10-alt1.git20140526
- Initial build for Sisyphus

