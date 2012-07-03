%define _libexecdir %_prefix/libexec

Name: gnome-disk-utility
Version: 3.4.1
Release: alt1

Summary: Disk management application
License: LGPLv2+
Group: System/Libraries
URL: http://git.gnome.org/cgit/gnome-disk-utility
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: udisks2 cryptsetup

Source: %name-%version.tar.xz

%define udisks_ver 1.91.0
%define glib_ver 2.31.0
%define gtk_ver 3.3.11

BuildRequires: gnome-common intltool
BuildPreReq: libudisks2-devel >= %udisks_ver
BuildPreReq: libgio-devel  >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome --output=global.lang %name palimpsest

%files -f global.lang
%_bindir/palimpsest
%_desktopdir/palimpsest.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Sep 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- updated from HEAD
- potentially fixed ALT #26191

* Wed Aug 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Wed Apr 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.32.1-alt2
- updated build dependencies

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.1-alt1
- 2.32.1

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Sun Aug 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt2
- disabled gtk-doc

* Tue Mar 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Tue Mar 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Sun Mar 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.90-alt1
- 2.29.90

* Sun Nov 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Fri Sep 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt2
- fixed requires

* Thu Aug 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt1
- 0.5

* Tue May 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3-alt1
- initial release

