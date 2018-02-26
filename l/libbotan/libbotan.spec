Name: libbotan
Version: 1.8.10
Release: alt2

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
	--docdir=%_defaultdocdir/%name-%version \
	--includedir=%_includedir \
	--with-bzip2 \
	--with-zlib \
	--with-gnump \
	--with-openssl

%make_build

%install
install -d %buildroot%_defaultdocdir/%name-%version
cp -rp readme.txt doc/{examples,scripts} %buildroot%_defaultdocdir/%name-%version/
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/botan/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc %_defaultdocdir/%name-%version

%changelog
* Wed Mar 30 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.10-alt2
- Add build dependency on zlib-devel for fix building.

* Mon Oct 11 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.10-alt1
- Initial build for Sisyphus.

