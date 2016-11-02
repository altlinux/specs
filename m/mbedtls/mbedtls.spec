%define soversion 10
%def_disable static

Name: mbedtls
Version: 2.4.0
Release: alt1

Summary: Light-weight cryptographic and SSL/TLS library
License: Apache
Group: System/Libraries

Url: https://tls.mbed.org/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: https://tls.mbed.org/download/%name-%version-apache.tgz

BuildRequires: cmake
BuildRequires: pkcs11-helper-devel
BuildRequires: zlib-devel

%description
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%name%soversion
Summary: Light-weight cryptographic and SSL/TLS library
Group: System/Libraries
Conflicts: hiawatha
Provides: lib%name = %version-%release

%description -n lib%name%soversion
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%name-devel
Summary: Development files for mbed TLS
Group: Development/C
Conflicts: hiawatha

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use mbed TLS

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for mbed TLS
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static libraries for developing applications
that use mbed TLS
%endif

%package utils
Summary: Utilities for PolarSSL
Group: Development/Tools
Requires: lib%name = %version-%release

%description utils
Cryptographic utilities based on mbed TLS 

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DENABLE_ZLIB_SUPPORT:BOOL=TRUE \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE \
	-DUSE_PKCS11_HELPER_LIBRARY:BOOL=TRUE \
	-DCMAKE_BUILD_TYPE:STRING="Release"

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__mkdir_p %buildroot%_libexecdir/%name
%__mv %buildroot%_bindir/* %buildroot%_libexecdir/%name
%__rm -rf %buildroot%_bindir

%files -n lib%name%soversion
%doc apache-2.0.txt ChangeLog LICENSE README.md
%_libdir/libmbedcrypto.so.*
%_libdir/lib%name.so.*
%_libdir/libmbedx509.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/libmbedcrypto.so
%_libdir/lib%name.so
%_libdir/libmbedx509.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libmbedcrypto.a
%_libdir/lib%name.a
%_libdir/libmbedx509.a
%endif

%files utils
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Wed Nov 02 2016 Nazarov Denis <nenderus@altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt0.M80P.1
- Build for branc p8

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
