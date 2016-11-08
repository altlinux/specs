%define ver_major 3.22
%define _name org.gnome.DiskUtility
%define _libexecdir %_prefix/libexec

Name: gnome-disk-utility
Version: %ver_major.1
Release: alt1

Summary: Disk management application
License: LGPLv2+
Group: System/Libraries
URL: http://git.gnome.org/%name

Requires: udisks2 cryptsetup
Requires: gnome-icon-theme-symbolic

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: %name-3.16.0-alt-lfs.patch

%define udisks_ver 2.1.1
%define glib_ver 2.31.0
%define gtk_ver 3.12.0
%define secret_ver 0.7
%define pwquality_ver 1.0.0
%define gsd_ver 3.6
%define dvdread_ver 4.2.0
%define lzma_ver 5.0.5

BuildRequires: autoconf-archive intltool xsltproc libappstream-glib-devel
BuildPreReq: libudisks2-devel >= %udisks_ver
BuildPreReq: libgio-devel  >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libsecret-devel >= %secret_ver
BuildPreReq: libpwquality-devel >= %pwquality_ver
BuildPreReq: gnome-settings-daemon-devel >= %gsd_ver
BuildPreReq: libdvdread-devel >= %dvdread_ver
BuildPreReq: liblzma-devel >= %lzma_ver
BuildRequires: libnotify-devel libcanberra-gtk3-devel
BuildRequires: systemd-devel libsystemd-devel
BuildRequires: xsltproc docbook-style-xsl

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=global.lang %name palimpsest

%files -f global.lang
%_bindir/gnome-disk-image-mounter
%_bindir/gnome-disks
%_desktopdir/gnome-disk-image-mounter.desktop
%_desktopdir/gnome-disk-image-writer.desktop
%_desktopdir/%_name.desktop
%_datadir/dbus-1/services/%_name.service
%_datadir/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/appdata/%_name.appdata.xml
%_man1dir/*.1.*
# gsd plugin
%_libdir/gnome-settings-daemon-3.0/gdu-sd-plugin.gnome-settings-plugin
%_libdir/gnome-settings-daemon-3.0/libgdu-sd.so
%_datadir/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gdu-sd.gschema.xml

%exclude %_libdir/gnome-settings-daemon-3.0/libgdu-sd.la


%changelog
* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3.1-alt1
- 3.18.3.1

* Sat Nov 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun May 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Sat Apr 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri May 31 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Oct 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Sep 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

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

