Name: libsrtp
Version: 1.6.0
Release: alt1

Summary: Secure RTP library
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/cisco/libsrtp

Source0: %name-%version.tar

%package -n libsrtp1
Summary: Secure RTP library
Group: System/Libraries

%package devel
Summary: Development part of libsrtp
Group: Development/C

%define desc This package provides an implementation of the Secure Real-time\
Transport Protocol (SRTP), the Universal Security Transform (UST),\
and a supporting cryptographic kernel.

%description
%desc

%description -n libsrtp1
%desc

%description devel
%desc
This package contains the headers and libraries for libsrtp development.

%prep
%setup

%build
touch ar-lib
%autoreconf
%configure
%make_build shared_library

%install
%makeinstall_std

%files -n libsrtp1
%_libdir/libsrtp.so.*

%files devel
%_includedir/srtp
%_libdir/libsrtp.so
%_pkgconfigdir/libsrtp.pc

%changelog
* Thu Oct 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Mon Sep 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt2
- fixed build

* Mon Feb 08 2016 Denis Smirnov <mithraen@altlinux.ru> 1.5.4-alt1
- new version 1.5.4

* Mon Feb 08 2016 Denis Smirnov <mithraen@altlinux.ru> 1.5.3-alt2
- fix watch file

* Sat Nov 28 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.3-alt1
- 1.5.3
- CVE-2015-6360

* Mon Nov 23 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt2
- Fix shared library (ALT #31448)

* Sun Nov 08 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt1
- 1.5.2
- add watch-file
- Build shared library (ALT #31448)

* Sat Jan 17 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Thu Oct 18 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt2
- build with -fPIC

* Mon Oct 15 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt2
- cleanup spec
- add auto tests

* Sun May 28 2006 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt1
- first build for Sisyphus

