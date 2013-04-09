Name: libatasmart
Version: 0.19
Release: alt1
Summary: ATA S.M.A.R.T. Disk Health Monitoring Library
Group: System/Libraries
License: LGPLv2+
Url: http://git.0pointer.de/?p=libatasmart.git;a=summary

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
Development Files for libatasmart Client Development.

%prep
%setup
%patch -p1

mkdir -p m4

%build
%autoreconf
%define docdir %_docdir/%name-%version
%configure --disable-static --docdir=%docdir
%make_build

%install
%makeinstall_std
cp -a blob-examples %buildroot%docdir/

%files
%_libdir/%name.so.*
%_sbindir/sk*
%dir %docdir
%docdir/README

%files devel
%_includedir/atasmart.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_datadir/vala/vapi/atasmart.vapi
%dir %docdir
%docdir/blob-examples

%changelog
* Tue Apr 09 2013 Dmitry V. Levin <ldv@altlinux.org> 0.19-alt1
- Updated to 0.19.
- Built with libudev1.

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

