%define sover 24

Name: wolfssl
Version: 4.6.0
Release: alt2

Summary: Embedded SSL/TLS Library
License: GPL-2.0
Group: System/Libraries

Url: https://www.%name.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/wolfSSL/%name/archive/v%version-stable/%name-%version-stable.tar.gz
Source: %name-%version-stable.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
The wolfSSL embedded SSL library is a lightweight SSL/TLS library written in ANSI C and targeted for embedded, RTOS, and resource-constrained environments - primarily because of its small size, speed, and feature set.  It is commonly used in standard operating environments as well because of its royalty-free pricing and excellent cross platform support.  wolfSSL supports industry standards up to the current TLS 1.3 and DTLS 1.2 levels, is up to 20 times smaller than OpenSSL, and offers progressive ciphers such as ChaCha20, Curve25519, NTRU, and Blake2b.  User benchmarking and feedback reports dramatically better performance when using wolfSSL over OpenSSL.

%package -n lib%name%sover
Summary: Embedded SSL/TLS Library
Group: System/Libraries

%description -n lib%name%sover
The wolfSSL embedded SSL library is a lightweight SSL/TLS library written in ANSI C and targeted for embedded, RTOS, and resource-constrained environments - primarily because of its small size, speed, and feature set.  It is commonly used in standard operating environments as well because of its royalty-free pricing and excellent cross platform support.  wolfSSL supports industry standards up to the current TLS 1.3 and DTLS 1.2 levels, is up to 20 times smaller than OpenSSL, and offers progressive ciphers such as ChaCha20, Curve25519, NTRU, and Blake2b.  User benchmarking and feedback reports dramatically better performance when using wolfSSL over OpenSSL.

%package -n lib%name-devel
Summary: Header files and development libraries for %name
Group: Development/C

%description -n lib%name-devel
This package contains the header files and development libraries for %name.

%prep
%setup -n %name-%version-stable

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DBUILD_SHARED_LIBS:BOOL=TRUE

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files -n lib%name%sover
%_libdir/lib%name.so.*
%dir %_defaultdocdir/%name
%_defaultdocdir/%name/*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/*.cmake
%_libdir/lib%name.so

%changelog
* Thu Feb 04 2021 Nazarov Denis <nenderus@altlinux.org> 4.6.0-alt2
- Build with cmake

* Wed Feb 03 2021 Nazarov Denis <nenderus@altlinux.org> 4.6.0-alt1
- Version 4.6.0

* Fri Nov 06 2020 Nazarov Denis <nenderus@altlinux.org> 4.5.0-alt1
- Initial build for ALT Linux
