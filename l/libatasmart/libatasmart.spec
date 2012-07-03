Name: libatasmart
Version: 0.18
Release: alt1
Summary: ATA S.M.A.R.T. Disk Health Monitoring Library
Group: System/Libraries
License: LGPLv2+
Url: http://git.0pointer.de/?p=libatasmart.git;a=summary
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libudev-devel

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package devel
Summary: Development Files for libatasmart Client Development
Group: Development/C
Requires: %name = %version-%release

%description devel
Development Files for libatasmart Client Development

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/%name.so.*
%_sbindir/sk*

%files devel
%doc blob-examples/*
%_includedir/atasmart.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Oct 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.18-alt1
- 0.18

* Fri Aug 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.17-alt1
- 0.17

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt2
- rebuild

* Tue Sep 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt1
- 0.16

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.15-alt1
- 0.15

* Thu Aug 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13-alt2
- git snapshot 2009-08-20 (d47ccc8854c9825ba610d9bbec7dd23bee7c4b5f)

* Tue May 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13-alt1
- initial release

