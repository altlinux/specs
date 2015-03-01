%define pname polarssl
%define sover 7

Name: %pname%sover
Version: 1.3.9
Release: alt2

Summary: Light-weight cryptographic and SSL/TLS library
License: GPLv2
Group: System/Legacy libraries

Url: https://%pname.org/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: https://%pname.org/download/%pname-%version-gpl.tgz

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
Group: System/Legacy libraries
Provides: lib%pname = %version
Obsoletes: lib%pname

%description -n lib%name
PolarSSL is a light-weight open source cryptographic and SSL/TLS
library written in C. PolarSSL makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible. 

%prep
%setup -n %pname-%version

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
%__rm -rf %buildroot%_bindir
%__rm -rf %buildroot%_includedir
%__rm -rf %buildroot%_libdir/lib%pname.a
%__rm -rf %buildroot%_libdir/lib%pname.so

%files -n lib%name
%doc ChangeLog LICENSE README.rst
%_libdir/lib%pname.so.*

%changelog
* Sun Mar 01 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.9-alt2
- Built as legacy library

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
