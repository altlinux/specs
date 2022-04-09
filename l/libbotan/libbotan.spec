# [armh] hash: [armh] /usr/src/tmp/rpm-tmp.97635: line 128: 754225 Segmentation fault
%ifarch armh
%def_without test
%endif
%define _unpackaged_files_terminate_build 1

Name: libbotan
Version: 2.19.1
Release: alt1

Summary: A C++ Crypto Library
License: BSD
Group: System/Libraries

Url: http://botan.randombit.net

# Source-url: https://github.com/randombit/botan/archive/%version.tar.gz
Source: %name-%version.tar
Patch2000: %name-e2k-simd.patch

BuildRequires: rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: liblzma-devel bzlib-devel libssl-devel zlib-devel
BuildRequires: boost-asio-devel
BuildRequires: %_bindir/sphinx-build %_bindir/rst2man.py

%description
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %EVR
Conflicts: libbotan1.11-devel

%description devel
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
Requires: %name = %EVR

%description -n python3-module-botan
Python extensions for botan

%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
export CXXFLAGS="${CXXFLAGS:-%optflags}"

python3 ./configure.py \
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
	--with-openssl \
	--with-python-versions=%__python3_version \
	--with-documentation \
	--with-sphinx \
	--with-rst2man \
	%nil

%make_build

%install
%makeinstall_std

rm -rf %buildroot%_defaultdocdir/botan-%version/manual/{.doctrees,.buildinfo}

%check
LD_LIBRARY_PATH=. ./botan-test

%files
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man1dir/botan.1*

%files doc
%doc %_defaultdocdir/botan-%version

%files -n python3-module-botan
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*

%changelog
* Sat Apr 09 2022 Vitaly Lipatov <lav@altlinux.ru> 2.19.1-alt1
- new version 2.19.1 (with rpmrb script)
- disable test on armh (segfault)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.18.1-alt2
- use /usr/bin/rst2man.py

* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 2.18.1-alt1
- new version 2.18.1 (with rpmrb script)

* Thu Jun 03 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.18.0-alt2
- added SIMD patch for Elbrus

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt1
- new version 2.18.0 (with rpmrb script)

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2.17.3-alt1
- new version 2.17.3 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2.17.2-alt1
- new version 2.17.2 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.17.0-alt1
- new version 2.17.0 (with rpmrb script)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 2.16.0-alt1
- new version 2.16.0 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Mon Feb 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- restore package, build new version

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.0-alt1
- Updated to upstream version 2.9.0.

* Tue Sep 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.0-alt1
- Updated to upstream version 2.7.0.

* Tue Jun 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.17-alt1.1
- Rebuild for aarch64.

* Tue Apr 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.17-alt1
- Updated to upstream version 1.10.17.
- Fixed pkg-config file.

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

