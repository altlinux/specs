%define sover 35

Name: wolfssl
Version: 5.5.4
Release: alt1

Summary: Embedded SSL/TLS Library
License: GPL-2.0
Group: System/Libraries

Url: https://www.%name.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/wolfSSL/%name/archive/v%version-stable/%name-%version-stable.tar.gz
Source: %name-%version-stable.tar

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
%autoreconf
%configure \
	--enable-distro \
	--enable-writedup
%make_build

%install
%makeinstall_std
%__rm -f %buildroot%_libdir/lib%name.a

%files -n lib%name%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_bindir/%name-config
%dir %_defaultdocdir/%name
%_defaultdocdir/%name/*
%dir %_includedir/cyassl
%_includedir/cyassl/*
%dir %_includedir/%name
%_includedir/%name/*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Dec 22 2022 Nazarov Denis <nenderus@altlinux.org> 5.5.4-alt1
- Version 5.5.4

* Sun Nov 06 2022 Nazarov Denis <nenderus@altlinux.org> 5.5.3-alt1
- Version 5.5.3

* Sat Oct 29 2022 Nazarov Denis <nenderus@altlinux.org> 5.5.2-alt1
- Version 5.5.2

* Wed Sep 28 2022 Nazarov Denis <nenderus@altlinux.org> 5.5.1-alt1
- Version 5.5.1

* Wed Aug 31 2022 Nazarov Denis <nenderus@altlinux.org> 5.5.0-alt1
- Version 5.5.0

* Wed Jul 13 2022 Nazarov Denis <nenderus@altlinux.org> 5.4.0-alt1
- Version 5.4.0

* Wed May 04 2022 Nazarov Denis <nenderus@altlinux.org> 5.3.0-alt1
- Version 5.3.0

* Mon Feb 21 2022 Nazarov Denis <nenderus@altlinux.org> 5.2.0-alt1
- Version 5.2.0

* Mon Jan 03 2022 Nazarov Denis <nenderus@altlinux.org> 5.1.1-alt1
- Version 5.1.1

* Tue Dec 28 2021 Nazarov Denis <nenderus@altlinux.org> 5.1.0-alt1
- Version 5.1.0

* Tue Nov 02 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.0-alt1
- Version 5.0.0

* Mon Nov 01 2021 Nazarov Denis <nenderus@altlinux.org> 4.8.1-alt2
- Enable write duplication for compatibility with RPCS3

* Mon Jul 26 2021 Nazarov Denis <nenderus@altlinux.org> 4.8.1-alt1
- Version 4.8.1

* Tue Jul 13 2021 Nazarov Denis <nenderus@altlinux.org> 4.8.0-alt1
- Version 4.8.0

* Thu Jul 08 2021 Nazarov Denis <nenderus@altlinux.org> 4.7.0-alt2
- Build with configure

* Tue Feb 16 2021 Nazarov Denis <nenderus@altlinux.org> 4.7.0-alt1
- Version 4.7.0

* Thu Feb 04 2021 Nazarov Denis <nenderus@altlinux.org> 4.6.0-alt2
- Build with cmake

* Wed Feb 03 2021 Nazarov Denis <nenderus@altlinux.org> 4.6.0-alt1
- Version 4.6.0

* Fri Nov 06 2020 Nazarov Denis <nenderus@altlinux.org> 4.5.0-alt1
- Initial build for ALT Linux
