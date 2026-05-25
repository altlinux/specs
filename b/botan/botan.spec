%define abiversion 3

Name: botan
Version: 3.11.1
Release: alt3

Summary: A C++ Crypto Library
License: BSD-2-Clause
Group: System/Libraries

Url: http://botan.randombit.net

Source: Botan-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: gcc-c++
BuildRequires: liblzma-devel bzlib-devel libtrousers-devel libtpm2-tss-devel zlib-devel libsqlite3-devel
BuildRequires: boost-asio-devel boost-beast-devel
BuildRequires: %_bindir/sphinx-build %_bindir/rst2man
%ifarch %e2k
BuildRequires: clang
%endif

Conflicts: libbotan-devel < 3

%description
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package -n lib%name%abiversion
Summary: A C++ Crypto Library
Group: Development/C++

%description -n lib%name%abiversion
%summary

%package -n lib%name-devel
Summary: Headers for libbotan
Group: Development/C++

%description -n lib%name-devel
Headers for building software that uses %name

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary

%package -n python3-module-botan
Summary: Python extensions for botan
Group: Development/Python3

%description -n python3-module-botan
Python extensions for botan

%prep
%setup -n Botan-%version
%ifarch %e2k
touch src/build-data/arch/generic.txt
%endif

%build
%ifarch loongarch64
%add_optflags -mlsx
%endif
export CXXFLAGS="${CXXFLAGS:-%optflags}"

python3 ./configure.py \
%ifarch %e2k
	--cpu=generic --cc=clang \
%endif
	--prefix=%prefix \
	--libdir=%_libdir \
	--docdir=%_defaultdocdir \
	--includedir=%_includedir \
	--disable-static-library \
	--with-debug-info \
	--with-bzip2 \
	--with-lzma \
	--with-zlib \
	--with-boost \
	--with-sqlite3 \
	--with-python-versions=%__python3_version \
	--with-documentation \
	--with-sphinx \
	--with-rst2man \
	--with-tpm \
	--with-tpm2 \
	%nil

%make_build

%install
%makeinstall_std

%check
LD_LIBRARY_PATH=. ./botan-test

%files
%_bindir/%name

%files -n lib%name%abiversion
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_cmakedir/Botan-%version
%_man1dir/botan.1*

%files doc
%doc %_defaultdocdir/botan-%version

%files -n python3-module-botan
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*

%changelog
* Tue May 26 2026 Ivan A. Melnikov <iv@altlinux.org> 3.11.1-alt3
- NMU: fix FTBFS on loongarch64

* Fri May 08 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.11.1-alt2
- e2k build fix

* Tue Apr 21 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 3.11.1-alt1
- Initial build.

