%define so_tls_version 23
%define so_crypto_version 18
%define so_x509_version 9
%define so_tfpsacrypto_version 2

%define mbedtls_version 4.1.0
%define tf_psa_crypto_version 1.1.0

%def_disable static

Name: mbedtls
Version: %mbedtls_version
Release: alt1

Summary: Transport Layer Security protocol suite
License: Apache-2.0 OR GPL-2.0-or-later
Group: System/Libraries

Url: https://www.trustedfirmware.org/projects/mbed-tls/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/ARMmbed/%name/archive/%name-%version/%name%name-%version.tar.gz
Source0: %name-%name-%version.tar
# https://github.com/Mbed-TLS/TF-PSA-Crypto/archive/tf-psa-crypto-%tf_psa_crypto_version/TF-PSA-Crypto-tf-psa-crypto-%tf_psa_crypto_version.tar.gz
Source1: TF-PSA-Crypto-tf-psa-crypto-%tf_psa_crypto_version.tar
# https://github.com/Mbed-TLS/%name-framework/archive/%name-%version_tf-psa-crypto-%tf_psa_crypto_version/%name-framework-%name-%{version}_tf-psa-crypto-%tf_psa_crypto_version.tar.gz
Source2: %name-framework-%name-%{version}_tf-psa-crypto-%tf_psa_crypto_version.tar

BuildRequires: ctest
BuildRequires: libssl-devel
BuildRequires: python3-dev
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-jsonschema

%description
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%name%so_tls_version
Summary: Transport Layer Security protocol suite
Group: System/Libraries
Version: %mbedtls_version
Conflicts: hiawatha

%description -n lib%name%so_tls_version
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n libmbedcrypto%so_crypto_version
Summary: Cryptographic base library for mbedtls
Group: System/Libraries
Version: %mbedtls_version

%description -n libmbedcrypto%so_crypto_version
This subpackage of mbedtls contains a library that exposes
cryptographic ciphers, hashes, algorithms and format support such as
AES, MD5, SHA, Elliptic Curves, BigNum, PKCS, ASN.1, BASE64.

%package -n libmbedx509-%so_x509_version
Summary: Library to work with X.509 certificates
Group: System/Libraries
Version: %mbedtls_version
Conflicts: hiawatha < 10.10

%description -n libmbedx509-%so_x509_version
This subpackage of mbedtls contains a library that can read, verify
and write X.509 certificates, read/write Certificate Signing Requests
and read Certificate Revocation Lists.

%package -n libtfpsacrypto%so_tfpsacrypto_version
Summary: PSA Cryptographic library for mbedtls
Group: System/Libraries
Version: %tf_psa_crypto_version

%description -n libtfpsacrypto%so_tfpsacrypto_version
This subpackage of mbedtls contains a library that exposes
cryptographic ciphers, hashes, algorithms and format support such as
AES, MD5, SHA, Elliptic Curves, BigNum, PKCS, ASN.1, BASE64.

%package -n lib%name-devel
Summary: Development files for mbed TLS
Group: Development/C
Version: %mbedtls_version
Conflicts: hiawatha

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use mbed TLS

%package -n libtfpsacrypto-devel
Summary: Development files for TF PSA Crypto
Group: Development/C
Version: %tf_psa_crypto_version
Conflicts: hiawatha

%description -n libtfpsacrypto-devel
Contains libraries and header files for
developing applications that use TF PSA Crypto


%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for mbed TLS
Group: Development/C
Version: %mbedtls_version

%description -n lib%name-devel-static
Static libraries for developing applications
that use mbed TLS

%package -n libtfpsacrypto-devel-static
Summary: Static libraries for TF PSA Crypto
Group: Development/C
Version: %tf_psa_crypto_version

%description -n libtfpsacrypto-devel-static
Static libraries for developing applications
that use TF PSA Crypto
%endif

%package utils
Summary: Utilities for PolarSSL
Group: Development/Tools
Version: %mbedtls_version

%description utils
Cryptographic utilities based on mbed TLS

%prep
%setup -n %name-%name-%version -b 1 -b 2
%__mv -Tf ../TF-PSA-Crypto-tf-psa-crypto-%tf_psa_crypto_version tf-psa-crypto
%__cp -Tr ../%name-framework-%name-%{version}_tf-psa-crypto-%tf_psa_crypto_version framework
%__mv -Tf ../%name-framework-%name-%{version}_tf-psa-crypto-%tf_psa_crypto_version tf-psa-crypto/framework
%ifarch aarch64
%add_optflags -Wno-error=array-bounds
%endif
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' CMakeLists.txt
%add_optflags -mno-aes
%endif

%build
%cmake .. \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE \
%if_enabled static
	-DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=TRUE
%else
	-DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=FALSE
%endif

%cmake_build

%install
%cmakeinstall_std
%__ln_s -r %buildroot%_libdir/libmbedcrypto.so.%so_crypto_version %buildroot%_libdir/libmbedcrypto.so
%__ln_s -r %buildroot%_libdir/libmbedcrypto.so.%version %buildroot%_libdir/libmbedcrypto.so.%so_crypto_version
mkdir -p %buildroot%_libexecdir/%name
mv %buildroot%_bindir/* %buildroot%_libexecdir/%name
rm -rf %buildroot%_bindir

%check
%ctest ||:

%files -n lib%name%so_tls_version
%_libdir/lib%name.so.%so_tls_version
%_libdir/lib%name.so.%version

%files -n libmbedcrypto%so_crypto_version
%_libdir/libmbedcrypto.so.%so_crypto_version
%_libdir/libmbedcrypto.so.%version

%files -n libmbedx509-%so_x509_version
%_libdir/libmbedx509.so.%so_x509_version
%_libdir/libmbedx509.so.%version

%files -n libtfpsacrypto%so_tfpsacrypto_version
%_libdir/libtfpsacrypto.so.%so_tfpsacrypto_version
%_libdir/libtfpsacrypto.so.%tf_psa_crypto_version

%files -n lib%name-devel
%doc BRANCHES.md BUGS.md CONTRIBUTING.md ChangeLog LICENSE README.md SECURITY.md SUPPORT.md
%_includedir/%name
%_includedir/psa
%_libdir/libmbedcrypto.so
%_libdir/lib%name.so
%_libdir/libmbedx509.so
%_libdir/cmake/MbedTLS
%_pkgconfigdir/mbedcrypto.pc
%_pkgconfigdir/mbedtls.pc
%_pkgconfigdir/mbedx509.pc

%files -n libtfpsacrypto-devel
%doc tf-psa-crypto/BRANCHES.md tf-psa-crypto/BUGS.md tf-psa-crypto/ChangeLog tf-psa-crypto/LICENSE tf-psa-crypto/README.md tf-psa-crypto/SECURITY.md tf-psa-crypto/SUPPORT.md
%_includedir/tf-psa-crypto
%_libdir/libtfpsacrypto.so
%_libdir/cmake/TF-PSA-Crypto
%_pkgconfigdir/tfpsacrypto.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libmbedcrypto.a
%_libdir/lib%name.a
%_libdir/libmbedx509.a

%files -n libtfpsacrypto-devel-static
%_libdir/libtfpsacrypto.a
%endif

%files utils
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Tue Mar 31 2026 Nazarov Denis <nenderus@altlinux.org> 4.1.0-alt1
- Update mbedTLS to 4.1.0
- Update TF PSA Crypto to 1.1.0

* Wed Oct 15 2025 Nazarov Denis <nenderus@altlinux.org> 4.0.0-alt1
- New version 4.0.0.

* Tue Jul 01 2025 Nazarov Denis <nenderus@altlinux.org> 3.6.4-alt1
- New version 3.6.4.

* Tue May 13 2025 Nazarov Denis <nenderus@altlinux.org> 3.6.3.1-alt1
- New version 3.6.3.1.

* Mon Mar 24 2025 Nazarov Denis <nenderus@altlinux.org> 3.6.3-alt1
- New version 3.6.3.
- Security fixes:
  + CVE-2025-27809
  + CVE-2025-27810

* Tue Oct 15 2024 Nazarov Denis <nenderus@altlinux.org> 3.6.2-alt1
- New version 3.6.2.

* Mon Apr 08 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.0-alt1.1
- Fixed build for Elbrus

* Fri Mar 29 2024 Nazarov Denis <nenderus@altlinux.org> 3.6.0-alt1
- New version 3.6.0.
- Fix url (ALT #47976)

* Tue Jan 30 2024 Nazarov Denis <nenderus@altlinux.org> 3.5.2-alt1
- New version 3.5.2.

* Wed Nov 08 2023 Nazarov Denis <nenderus@altlinux.org> 3.5.1-alt1
- New version 3.5.1.

* Thu Oct 05 2023 Nazarov Denis <nenderus@altlinux.org> 3.5.0-alt1
- New version 3.5.0.

* Fri Aug 04 2023 Nazarov Denis <nenderus@altlinux.org> 3.4.1-alt1
- New version 3.4.1.

* Thu Mar 30 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.4.0-alt1.1
- Fixed build for Elbrus

* Wed Mar 29 2023 Nazarov Denis <nenderus@altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Thu Dec 15 2022 Nazarov Denis <nenderus@altlinux.org> 3.3.0-alt1
- Version 3.3.0

* Wed Jul 13 2022 Nazarov Denis <nenderus@altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Sat Dec 18 2021 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt1
- Version 3.1.1

* Thu Jul 22 2021 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1.1
- E2K: avoid lcc-unsupported option

* Wed Jul 07 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Version 3.0.0

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
