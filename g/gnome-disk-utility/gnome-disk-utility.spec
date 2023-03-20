%define ver_major 44
%define beta %nil
%define xdg_name org.gnome.DiskUtility
%define _libexecdir %_prefix/libexec
%def_enable gsd_plugin
%def_enable libsystemd

Name: gnome-disk-utility
Version: %ver_major.0
Release: alt1%beta

Summary: Disk management application
License: LGPLv2+
Group: System/Libraries
Url: https://wiki.gnome.org/Apps/Disks

Requires: udisks2 cryptsetup
Requires: gnome-icon-theme-symbolic

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz

%define udisks_ver 2.7.6
%define glib_ver 2.31.0
%define gtk_ver 3.16.0
%define secret_ver 0.7
%define pwquality_ver 1.0.0
%define dvdread_ver 4.2.0
%define lzma_ver 5.0.5
%define handy_ver 1.5.0

Provides: gnome-disks = %EVR
Requires: udisks2 >= %udisks_ver

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: libudisks2-devel >= %udisks_ver
BuildRequires: libgio-devel  >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: libsecret-devel >= %secret_ver
BuildRequires: libpwquality-devel >= %pwquality_ver
BuildRequires: libdvdread-devel >= %dvdread_ver
BuildRequires: liblzma-devel >= %lzma_ver
BuildRequires: libnotify-devel libcanberra-gtk3-devel
%{?_enable_libsystemd:BuildRequires: pkgconfig(systemd)}
BuildRequires: xsltproc docbook-style-xsl

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc

%prep
%setup -n %name-%version%beta

%build
%meson \
	%{?_disable_gsd_plugin:-Dgsd_plugin=false} \
	%{?_disable_libsystemd:-Dlibsystemd=false}
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=global.lang %name

%files -f global.lang
%_bindir/gnome-disk-image-mounter
%_bindir/gnome-disks

%if_enabled gsd_plugin
%_libexecdir/gsd-disk-utility-notify
%_xdgconfigdir/autostart/org.gnome.SettingsDaemon.DiskUtilityNotify.desktop
%endif

%_desktopdir/gnome-disk-image-mounter.desktop
%_desktopdir/gnome-disk-image-writer.desktop
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/*.1.*


%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sun Jul 11 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sat May 01 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Thu Mar 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Thu Feb 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Dec 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Mon Jul 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Sat Mar 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Feb 17 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Apr 28 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1.1
- fixed build

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Oct 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Thu May 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Fri May 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

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

