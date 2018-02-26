#
# OpenISDN rpm spec file - based on rpmdevel lib template
#
Name: libisdn
Version: 0.0.1
Release: alt1
Summary: OpenISDN experimental stack

Group: System/Libraries
License: BSD-3
URL: http://www.openisdn.net/
Source0: %name-%version.tar

BuildRequires: doxygen CUnit-devel liblua5-devel libpcap-devel

%description
Experimental OpenISDN stack

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make
%make doxygen

%install
%makeinstall_std

%check
make check

%files
%doc CREDITS COPYING TODO
#_bindir/libisdn-config
%_libdir/*.so.*

%files devel
%doc CREDITS COPYING TODO docs/html
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%name.pc

%changelog
* Tue Apr 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.1-alt1
- Build for ALT
