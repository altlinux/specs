%define pkgname mbedtls
%define so_tls_version 14
%define so_crypto_version 7
%define so_x509_version 1
%def_disable static

%filter_from_provides /^pkgconfig(mbedcrypto)/d
%filter_from_provides /^pkgconfig(mbedtls)/d
%filter_from_provides /^pkgconfig(mbedx509)/d

Name: %pkgname-compat
Version: 2.28.9
Release: alt1

Summary: Transport Layer Security protocol suite
License: Apache-2.0 OR GPL-2.0-or-later
Group: System/Legacy libraries

Url: https://tls.mbed.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/ARMmbed/%pkgname/archive/v%version/%pkgname-%version.tar.gz
Source: %pkgname-%version.tar

Patch0: %pkgname-alt-gcc11.patch

BuildRequires: cmake
BuildRequires: libpkcs11-helper-devel
BuildRequires: python3-dev
BuildRequires: zlib-devel

%description
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%pkgname%so_tls_version
Summary: Transport Layer Security protocol suite
Group: System/Legacy libraries
Conflicts: hiawatha

%description -n lib%pkgname%so_tls_version
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n libmbedcrypto%so_crypto_version
Summary: Cryptographic base library for mbedtls
Group: System/Legacy libraries

%description -n libmbedcrypto%so_crypto_version
This subpackage of mbedtls contains a library that exposes
cryptographic ciphers, hashes, algorithms and format support such as
AES, MD5, SHA, Elliptic Curves, BigNum, PKCS, ASN.1, BASE64.

%package -n libmbedx509-%so_x509_version
Summary: Library to work with X.509 certificates
Group: System/Legacy libraries
Conflicts: hiawatha < 10.10

%description -n libmbedx509-%so_x509_version
This subpackage of mbedtls contains a library that can read, verify
and write X.509 certificates, read/write Certificate Signing Requests
and read Certificate Revocation Lists.

%package -n lib%pkgname-compat-devel
Summary: Development files for mbed TLS
Group: Development/C
Provides: lib%{pkgname}13-devel = %EVR
Obsoletes: lib%{pkgname}13-devel <= 2.27.0-alt2
Conflicts: hiawatha
Conflicts: lib%pkgname-devel

%description -n lib%pkgname-compat-devel
Contains libraries and header files for
developing applications that use mbed TLS

%if_enabled static
%package -n lib%pkgname-compat-devel-static
Summary: Static libraries for mbed TLS
Group: Development/C
Conflicts: lib%pkgname-devel-static

%description -n lib%pkgname-compat-devel-static
Static libraries for developing applications
that use mbed TLS
%endif

%prep
%setup -n %pkgname-%version
%patch0 -p1
%ifarch %e2k
# unsupported as of lcc 1.25.17
sed -i 's,-Wformat-overflow=2,,' CMakeLists.txt
sed -i 's/-Werror/-Wno-error/' CMakeLists.txt
%add_optflags -mno-aes
%endif

%build
%cmake .. \
	-DENABLE_ZLIB_SUPPORT:BOOL=TRUE \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE \
%if_enabled static
	-DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=TRUE \
%else
	-DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=FALSE \
%endif
	-DUSE_PKCS11_HELPER_LIBRARY:BOOL=TRUE

%cmake_build

%install
%cmakeinstall_std
%__rm -rf %buildroot%_bindir

%files -n lib%pkgname%so_tls_version
%_libdir/lib%pkgname.so.*

%files -n libmbedcrypto%so_crypto_version
%_libdir/libmbedcrypto.so.*

%files -n libmbedx509-%so_x509_version
%_libdir/libmbedx509.so.*

%files -n lib%pkgname-compat-devel
%doc ChangeLog LICENSE README.md
%dir %_includedir/%pkgname
%_includedir/%pkgname
%_includedir/psa
%_includedir/everest
%_libdir/libmbedcrypto.so
%_libdir/lib%pkgname.so
%_libdir/libmbedx509.so
%_pkgconfigdir/mbedcrypto.pc
%_pkgconfigdir/mbedtls.pc
%_pkgconfigdir/mbedx509.pc

%if_enabled static
%files -n lib%pkgname-compat-devel-static
%_libdir/libmbedcrypto.a
%_libdir/lib%pkgname.a
%_libdir/libmbedx509.a
%endif

%changelog
* Fri Aug 30 2024 Nazarov Denis <nenderus@altlinux.org> 2.28.9-alt1
- Version 2.28.9

* Fri Mar 29 2024 Nazarov Denis <nenderus@altlinux.org> 2.28.8-alt1
- Version 2.28.8

* Tue Jan 30 2024 Nazarov Denis <nenderus@altlinux.org> 2.28.7-alt1
- Version 2.28.7

* Wed Nov 08 2023 Nazarov Denis <nenderus@altlinux.org> 2.28.6-alt1
- Version 2.28.6

* Sat Oct 07 2023 Nazarov Denis <nenderus@altlinux.org> 2.28.5-alt1
- Version 2.28.5

* Sun Aug 06 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.28.4-alt1.1
- Fixed build for Elbrus

* Fri Aug 04 2023 Nazarov Denis <nenderus@altlinux.org> 2.28.4-alt1
- Version 2.28.4

* Wed Mar 29 2023 Nazarov Denis <nenderus@altlinux.org> 2.28.3-alt1
- Version 2.28.3

* Fri Dec 16 2022 Nazarov Denis <nenderus@altlinux.org> 2.28.2-alt1
- Version 2.28.2

* Wed Jul 13 2022 Nazarov Denis <nenderus@altlinux.org> 2.28.1-alt1
- Version 2.28.1

* Sun Dec 19 2021 Nazarov Denis <nenderus@altlinux.org> 2.28.0-alt1
- Version 2.28.0
- Rename devel subpackage

* Sun Sep 26 2021 Nazarov Denis <nenderus@altlinux.org> 2.27.0-alt2
- Add patch to fix build on gcc11

* Thu Jul 22 2021 Michael Shigorin <mike@altlinux.org> 2.27.0-alt1.1
- E2K: avoid lcc-unsupported option

* Sat Jul 10 2021 Nazarov Denis <nenderus@altlinux.org> 2.27.0-alt1
- Version 2.27.0
- Build devel subpackage for legacy-library

* Thu Jul 08 2021 Nazarov Denis <nenderus@altlinux.org> 2.26.0-alt3
- Rename package name

* Wed Jul 07 2021 Nazarov Denis <nenderus@altlinux.org> 2.26.0-alt2
- Buid as legacy library

* Sat Mar 13 2021 Nazarov Denis <nenderus@altlinux.org> 2.26.0-alt1
- Version 2.26.0

* Fri Dec 11 2020 Nazarov Denis <nenderus@altlinux.org> 2.25.0-alt1
- Version 2.25.0

* Wed Sep 02 2020 Nazarov Denis <nenderus@altlinux.org> 2.24.0-alt1
- Version 2.24.0

* Thu Jul 02 2020 Nazarov Denis <nenderus@altlinux.org> 2.23.0-alt1
- Version 2.23.0

* Fri Jun 05 2020 Nazarov Denis <nenderus@altlinux.org> 2.16.6-alt1
- Version 2.16.6

* Wed Feb 12 2020 Nazarov Denis <nenderus@altlinux.org> 2.16.4-alt1
- Version 2.16.4

* Tue Nov 05 2019 Nazarov Denis <nenderus@altlinux.org> 2.16.3-alt2
- Fix conflict libmbedx509 with hiawatha package less than 10.10 (ALT #37417)

* Sat Nov 02 2019 Nazarov Denis <nenderus@altlinux.org> 2.16.3-alt1
- Version 2.16.3
- Fix conflict with hiawatha package (ALT #37417)

* Sun Apr 07 2019 Nazarov Denis <nenderus@altlinux.org> 2.16.1-alt1
- Version 2.16.1 (ALT #36525)
- Remove %ubt macro (ALT #36525)

* Tue Jul 24 2018 Nazarov Denis <nenderus@altlinux.org> 2.11.0-alt2%ubt
- Separate subpackages

* Sun Jul 22 2018 Nazarov Denis <nenderus@altlinux.org> 2.11.0-alt1%ubt
- Version 2.11.0

* Thu Apr 12 2018 Nazarov Denis <nenderus@altlinux.org> 2.8.0-alt2%ubt
- Build with with MBEDTLS_THREADING_PTHREAD and MBEDTLS_THREADING_C enabled

* Mon Mar 26 2018 Nazarov Denis <nenderus@altlinux.org> 2.8.0-alt1%ubt
- Version 2.8.0

* Thu Mar 08 2018 Nazarov Denis <nenderus@altlinux.org> 2.7.0-alt1%ubt
- Version 2.7.0

* Sun Nov 12 2017 Nazarov Denis <nenderus@altlinux.org> 2.6.0-alt1%ubt
- Version 2.6.0

* Sun Jul 30 2017 Nazarov Denis <nenderus@altlinux.org> 2.5.1-alt1%ubt
- Version 2.5.1

* Thu Apr 20 2017 Nazarov Denis <nenderus@altlinux.org> 2.4.2-alt0.M80P.1
- Build for branch p8

* Sun Mar 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.4.2-alt1
- Version 2.4.2

* Wed Nov 02 2016 Nazarov Denis <nenderus@altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt0.M80P.1
- Build for branch p8

* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sat Nov 07 2015 Nazarov Denis <nenderus@altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Wed Jul 29 2015 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Fri Jun 26 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.11-alt0.M70T.1
- Build for branch t7

* Tue Jun 23 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.11-alt1
- Version 1.3.11

* Mon Mar 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.10-alt1.M70P.1
- Backport new version to p7 branch

* Sat Mar 07 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.10-alt0.M70T.1
- Build for branch t7

* Sat Mar 07 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.10-alt2
- Package libmbedtls renamed according to Shared Libs Policy

* Sat Feb 28 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.10-alt1
- Renamed package to mbed TLS
- Version 1.3.10

* Sat Nov 29 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.9-alt1
- Version 1.3.9

* Thu Aug 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.8-alt1
- Version 1.3.8

* Thu May 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.7-alt1
- Version 1.3.7

* Tue Apr 22 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.6-alt1
- Version 1.3.6

* Sat Apr 05 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.5-alt1
- Version 1.3.5

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.4-alt0.M70T.1
- Build for branch t7

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.4-alt1
- Version 1.3.4

* Sun Jan 12 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.3-alt1
- Version 1.3.3

* Wed Nov 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Sun Nov 03 2013 Nazarov Denis <nenderus@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
