Name: libsrtp2
Version: 2.5.0
Release: alt1

Summary: Secure RTP library
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/cisco/libsrtp

Source0: %name-%version.tar

Provides: libsrtp2_1 = %version-%release
Obsoletes: libsrtp2_1

%package devel
Summary: Development part of libsrtp
Group: Development/C
Requires: %name = %version-%release

%define desc This package provides an implementation of the Secure Real-time\
Transport Protocol (SRTP), the Universal Security Transform (UST),\
and a supporting cryptographic kernel.

%description
%desc

%description devel
%desc
This package contains the headers and libraries for libsrtp development.

%prep
%setup

%build
%autoreconf
%configure
%make_build shared_library

%install
%makeinstall_std

%files
%doc LICENSE README.md
%_libdir/libsrtp2.so.*

%files devel
%doc CHANGES
%_includedir/srtp2
%_libdir/libsrtp2.so
%_pkgconfigdir/libsrtp2.pc

%changelog
* Fri Feb 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0 released

* Tue Jun 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.2-alt1
- 2.4.2 released

* Tue Oct 02 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Mon Feb 08 2016 Denis Smirnov <mithraen@altlinux.ru> 2.0.0-alt1
- 2.0.0
