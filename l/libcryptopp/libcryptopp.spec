%def_disable static

%define oname	cryptopp
%define abiversion 9

%ifarch armh
%add_optflags -mfpu=neon
%endif

# LTO partitioning breaks the x86 inline asm labels (undefined LMulN) in integer.cpp
%ifarch %ix86
%global optflags_lto %nil
%endif

Name: libcryptopp
Version: 2026.9.1
Release: alt1

Summary: Cryptopp Library - a free C++ class library of cryptographic schemes

License: Boost Software License
Url: https://github.com/cryptopp-modern/cryptopp-modern
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/cryptopp-modern/cryptopp-modern/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jan 27 2008
BuildRequires: gcc-c++

%description
Cryptopp Library is a free C++ class library of cryptographic schemes.
This is cryptopp-modern, the maintained fork of Crypto++.

%package -n %name%abiversion
Summary: Cryptopp Library - a free C++ class library of cryptographic schemes
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name < %EVR
Provides: libcrypto++ = %EVR
Obsoletes: libcrypto++ < %EVR

%description -n %name%abiversion
Cryptopp Library is a free C++ class library of cryptographic schemes.
This is cryptopp-modern, the maintained fork of Crypto++.

This package contains the shared library.

%package devel
Summary: Files for development of applications which will use Cryptopp
Group: Development/C++
Requires: %name%abiversion = %EVR

Provides: libcrypto++-devel = %version-%release
Obsoletes: libcrypto++-devel

%description devel
Files for development of applications which will use Cryptopp.

%package devel-static
Summary: Static Cryptopp library
Group: Development/C++
Requires: %name-devel = %version-%release
Provides: %name-static
Obsoletes: %name-static

%description devel-static
Static Cryptopp library.

%package progs
Summary: Cryptopp programs
Group: File tools
Requires: %name%abiversion = %EVR

%description progs
Cryptopp programs.

%prep
%setup
%ifarch %e2k
sed -i "1i #define CRYPTOPP_DISABLE_ASM 1" include/cryptopp/config_asm.h
%endif

%build
%add_optflags -fpermissive
%make_build LDLIBS="-lpthread" CXXFLAGS="%optflags %optflags_shared" PREFIX=%prefix static dynamic cryptest.exe
%make PREFIX=%_prefix LIBDIR=%_libdir libcryptopp.pc
sed -i "s/^Version: .*/Version: %version/" libcryptopp.pc

%check
./cryptest.exe v
./cryptest.exe tv all

%install
make install DESTDIR=%buildroot PREFIX=%_prefix LIBDIR=%_libdir
mv %buildroot%_bindir/cryptest.exe %buildroot%_bindir/cryptest

%if_disabled static
rm -v %buildroot%_libdir/libcryptopp.a
%endif

mkdir -p %buildroot%_pkgconfigdir/
cat >%buildroot%_pkgconfigdir/libcrypto++.pc <<EOF
Name: libcrypto++
Description: General purpose cryptographic shared library
URL: http://www.cryptopp.com
Version: %version
Requires:
Libs: -lcryptopp
Cflags:
EOF

%files -n %name%abiversion
%doc LICENSE Readme.txt README.md
%_libdir/libcryptopp.so.%abiversion
%_libdir/libcryptopp.so.%version

%files devel
%_libdir/libcryptopp.so
%_includedir/cryptopp/
%_pkgconfigdir/*

%if_enabled static
%files devel-static
%_libdir/libcryptopp.a
%endif

%files progs
%_bindir/cryptest
#_bindir/cryptestcwd
%_datadir/cryptopp/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.9.1-alt1
- switch to the maintained fork cryptopp-modern
- new version 2026.9.1
- new soname libcryptopp.so.9: pack the library as libcryptopp9 (Shared Libs Policy)
- add upstream libcryptopp.pc
- security fixes:
  + CVE-2024-28285: fix fault injection in hybrid DL decryption (ElGamal, ECIES, DLIES).
  + CVE-2023-50980: fix DoS in BERDecodeGF2NP (strict exponent order, field degree cap).
  + CVE-2023-50981: fix DoS in ModularSquareRoot and Rabin private key decoding.
  + GHSA-9g8r-h7q5-x8pc: fix heap overflow in PKCS#1 v1.5 unpadding.

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 8.9.0-alt1
- new version 8.9.0 (with rpmrb script)

* Sun Aug 20 2023 Vitaly Lipatov <lav@altlinux.ru> 8.8.0-alt1
- new version 8.8.0 (with rpmrb script)

* Sun May 01 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 8.6.0-alt1.1
- fixed build for Elbrus

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 8.6.0-alt1
- new version 8.6.0 (with rpmrb script)

* Wed Sep 08 2021 Vitaly Lipatov <lav@altlinux.ru> 8.5.0-alt2
- disable build devel-static package (due LTO error)

* Thu Jul 01 2021 Vitaly Lipatov <lav@altlinux.ru> 8.5.0-alt1
- new version 8.5.0 (with rpmrb script)

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 8.2.0-alt1
- new version 8.2.0 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.0-alt1
- new version 6.1.0 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 5.6.5-alt1
- new version 5.6.5 (with rpmrb script)
- return to native build
- enable check during build

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 5.6.3-alt1
- new version 5.6.3 (with rpmrb script)

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.2-alt1.1
- Rebuilt with gcc5

* Wed Jul 17 2013 Evgeny Sinelnikov <sin@altlinux.ru> 5.6.2-alt1
- Update to last stable release with multiple fixes and SHA-3 implemetation
- Change license from GPL to Boost Software License 1.0

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3.qa3
- Fixed build with gcc 4.7

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Dec 13 2009 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt3
- really pack 5.6.0 (fix bug #22515)

* Wed Jul 22 2009 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt2
- fix pkgconfig file

* Mon Jul 20 2009 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- new version 5.6.0 (with rpmrb script)
- add pkgconfig file (ALT #20826)

* Sat Mar 29 2008 Vitaly Lipatov <lav@altlinux.ru> 5.5.2-alt2
- fix devel-static package name

* Fri Jan 25 2008 Vitaly Lipatov <lav@altlinux.ru> 5.5.2-alt1
- new version (5.5.2), update autoconf/automake files
- disable asm code

* Fri Jan 25 2008 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

