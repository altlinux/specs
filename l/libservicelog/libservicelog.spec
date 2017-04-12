Name: libservicelog
Version: 1.1.17
Release: alt1
Summary: Servicelog Database and Library
Group: System/Libraries
License: LGPLv2 and GPLv2+
URL: http://linux-diag.sourceforge.net/libservicelog

Source: %name-%version.tar.gz
Patch0: libservicelog-1.1.9-libs.patch

BuildRequires: libsqlite3-devel librtas-devel

%description
The libservicelog package contains a library to create and maintain a
database for storing events related to system service.  This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the system.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
Contains header files for building with libservicelog.

%prep
%setup -q
%patch0 -p1 -b .libs

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%pre
%_sbindir/groupadd -r -f service

%files
%doc AUTHORS COPYING
%_libdir/libservicelog-*.so.*
%dir %attr(755,root,service) %_localstatedir/servicelog
%config(noreplace) %attr(644,root,service) %_localstatedir/servicelog/servicelog.db

%files devel
%_includedir/servicelog-1
%_libdir/*.so
%_pkgconfigdir/servicelog-1.pc

%changelog
* Wed Apr 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.1.17-alt1
- initial release

