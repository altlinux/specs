Name: polarssl
Version: 1.3.3
Release: alt1

Summary: Light-weight cryptographic and SSL/TLS library
License: GPLv2
Group: System/Libraries

Url: https://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: https://%name.org/download/%name-%version-gpl.tgz

BuildRequires: cmake
BuildRequires: pkcs11-helper-devel
BuildRequires: zlib-devel

%description
PolarSSL is a light-weight open source cryptographic and SSL/TLS
library written in C. PolarSSL makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%name
Summary: Light-weight cryptographic and SSL/TLS library
Group: System/Libraries

%description -n lib%name
PolarSSL is a light-weight open source cryptographic and SSL/TLS
library written in C. PolarSSL makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%name-devel
Summary: Development files for PolarSSL
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: hiawatha

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use PolarSSL.

%package utils
Summary: Utilities for PolarSSL
Group: Development/Tools
Requires: lib%name = %version-%release

%description utils
Cryptographic utilities based on PolarSSL. 

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
	-DUSE_SHARED_POLARSSL_LIBRARY:BOOL=TRUE \
	-DUSE_PKCS11_HELPER_LIBRARY:BOOL=TRUE \
	-DCMAKE_BUILD_TYPE:STRING="Release"

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__mkdir_p %buildroot%_libexecdir/%name
%__mv %buildroot%_bindir/* %buildroot%_libexecdir/%name
%__rm -rf %buildroot%_bindir

%files -n lib%name
%doc ChangeLog LICENSE README.rst
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so

%files utils
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Sun Jan 12 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.3-alt1
- Version 1.3.3

* Wed Nov 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Sun Nov 03 2013 Nazarov Denis <nenderus@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
