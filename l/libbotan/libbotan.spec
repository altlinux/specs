Name: libbotan
Version: 1.10.9
Release: alt1

Summary: A C++ Crypto Library
License: BSD
Group: System/Libraries

Url: http://botan.randombit.net

Source: %name-%version.tar

BuildRequires: bzlib-devel gcc-c++ libgmp-devel libssl-devel python-modules-compiler python-modules-logging zlib-devel

%description
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release
Conflicts: libbotan1.11-devel

%description devel
Headers for building software that uses %name

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary

%prep
%setup

%build
./configure.py --prefix=%prefix \
	--libdir=%_libdir \
	--docdir=%_defaultdocdir \
	--includedir=%_includedir \
	--with-bzip2 \
	--with-zlib \
	--with-gnump \
	--with-openssl

%make_build

%install
install -d %buildroot%_defaultdocdir/botan-%version
cp -rp readme.txt doc/examples %buildroot%_defaultdocdir/botan-%version/
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/botan/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc %_defaultdocdir/botan-%version

%changelog
* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 1.10.9-alt1
- New version
- Rebuilt for gcc5 C++11 ABI

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.5-alt1
- Version 1.10.5

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.8.10-alt2.1.qa1
- NMU: rebuilt for updated dependencies.

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt2.1
- Rebuilt with gmp 5.0.5

* Wed Mar 30 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.10-alt2
- Add build dependency on zlib-devel for fix building.

* Mon Oct 11 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.10-alt1
- Initial build for Sisyphus.

