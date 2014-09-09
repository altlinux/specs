%def_with python3
%define branch 1.11
%define oname botan

Name: lib%oname%branch
Version: %branch.10
Release: alt1.git20140526

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
BuildPreReq: python3-devel boost-python3-devel
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

%description -n python-module-%oname
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

This package contains Python module of Botan.

%package -n python3-module-%oname
Summary: Python module of Botan
Group: Development/Python3

%description -n python3-module-%oname
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

This package contains Python module of Botan.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|boost_python|boost_python3|g' \
	../python3/src/build-data/makefile/python.in
sed -i 's|\(PYTHON_INC =\).*|\1 -I%python3_includedir%_python3_abiflags|' \
	../python3/src/build-data/makefile/python.in
%endif

%build
%ifarch x86_64
LIB_SUFFIX=64
%endif

./configure.py --prefix=%prefix \
	--bindir=%_bindir \
	--libdir=%_libdir \
	--docdir=%_defaultdocdir/%name-%version \
	--includedir=%_includedir \
	--makefile-style=gmake \
	--with-bzip2 \
	--with-zlib \
	--with-gnump \
	--with-openssl \
	--with-sphinx \
	--build-relnotes \
	--with-doxygen \
	--with-boost \
	--with-sqlite3 \
	--with-lzma \
	--with-boost-python \
	--with-python-version=%_python_version

%make_build
%make_build python LIB_SUFFIX=$LIB_SUFFIX

%if_with python3
pushd ../python3
./configure.py --prefix=%prefix \
	--bindir=%_bindir \
	--libdir=%_libdir \
	--docdir=%_defaultdocdir/%name-%version \
	--includedir=%_includedir \
	--makefile-style=gmake \
	--with-bzip2 \
	--with-zlib \
	--with-gnump \
	--with-openssl \
	--with-sphinx \
	--build-relnotes \
	--with-doxygen \
	--with-boost \
	--with-sqlite3 \
	--with-lzma \
	--with-boost-python \
	--with-python-version=%_python3_version

%make_build
%make_build python LIB_SUFFIX=$LIB_SUFFIX
popd
%endif

%install
%ifarch x86_64
LIB_SUFFIX=64
%endif

%if_with python3
pushd ../python3
%make install_python DESTDIR=%buildroot LIB_SUFFIX=$LIB_SUFFIX
popd
%endif

%makeinstall_std
%make install_python DESTDIR=%buildroot LIB_SUFFIX=$LIB_SUFFIX

ln -s botan-config-1.11 %buildroot%_bindir/botan-config
ln -s botan-1.11.pc %buildroot%_pkgconfigdir/botan.pc

%files
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/botan/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc %_defaultdocdir/%name-%version

%files -n python-module-%oname
%python_sitelibdir/*

%files -n python3-module-%oname
%python3_sitelibdir/*

%changelog
* Tue Sep 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.10-alt1.git20140526
- Initial build for Sisyphus

