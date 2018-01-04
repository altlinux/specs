%set_verify_elf_method rpath=relaxed
%define ver_major 3.26
#%%define xdg_name org.gnome.Evolution
%define xdg_name evolution

Name: evolution-ews
Version: %ver_major.3
Release: alt2

Group: Networking/Mail
Summary: Evolution extension for Exchange Web Services
License: LGPLv2
Url: https://wiki.gnome.org/Apps/Evolution

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define ver_base 3.26
%define evo_ver_base %ver_base

%define evolution_ver 3.26.3
%define eds_ver 3.26.3
%define glib_ver 2.40
%define libmspack_ver 0.4
%define soup_ver 2.42

Requires: evolution >= %evolution_ver
Requires: evolution-data-server >= %eds_ver
Requires: libmspack >= %libmspack_ver

BuildRequires: cmake gcc-c++ intltool
BuildRequires: gnome-common rpm-build-gnome gtk-doc
BuildRequires: evolution-data-server-devel >= %eds_ver
BuildRequires: evolution-devel >= %evolution_ver
BuildRequires: libmspack-devel >= %libmspack_ver
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: libsqlite3-devel libical-devel

# following unusual reqs needed to link against evolution >= 3.13.6 libraries
BuildRequires: libchamplain-gtk3-devel libgail3-devel gcr-libs-devel libp11-kit-devel
BuildRequires: libgnome-desktop3-devel libdbus-devel libdbus-glib-devel libgeocode-glib-devel
BuildRequires: libgeoclue-devel libgtkspell3-devel libgnome-autoar-devel
BuildRequires: libcanberra-gtk3-devel libcryptui-devel

%description
This package allows Evolution to interact with Microsoft Exchange servers,
versions 2007 and later, through its Exchange Web Services (EWS) interface.

%prep
%setup

%build
# reenable RPATH* to link against private libraries
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

# Remove files we don't want packaged (no devel subpackage).
rm -rf %buildroot%_includedir/evolution-data-server
find %buildroot%_libdir -name '*.la' -exec rm {} \;
rm -f %buildroot%_libdir/evolution-data-server/*.so

%find_lang %name

%files -f %name.lang
%doc COPYING NEWS README
%_libdir/%name/*.so
%_libdir/evolution-data-server/camel-providers/*
%_libdir/evolution-data-server/addressbook-backends/*.so
%_libdir/evolution-data-server/calendar-backends/*.so
%_libdir/evolution-data-server/registry-modules/*.so
%_libdir/evolution/modules/*.so
%_datadir/evolution/errors/*.error
%_datadir/evolution-data-server/ews/windowsZones.xml
%_datadir/appdata/%xdg_name-ews.metainfo.xml

%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt2
- rebuilt against libical.so.3

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Aug 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.5-alt1
- 3.24.5

* Mon Jul 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.4-alt1
- 3.24.4

* Mon Jun 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Mar 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt1
- 3.22.6

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Mon Dec 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Sep 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Mon Aug 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.5-alt1
- 3.20.5

* Mon Jul 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Feb 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.5-alt1
- 3.18.5

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt2
- rebuilt against libical.so.2

* Mon Jan 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Aug 11 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.5-alt1
- 3.16.5

* Tue Jun 09 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.3-alt1
- 3.16.3

* Wed May 13 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Tue Jan 13 2015 Alexey Shabalin <shaba@altlinux.ru> 3.12.10-alt1
- 3.12.10

* Wed Dec 17 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.9-alt1
- 3.12.9

* Tue Nov 11 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.8-alt1
- 3.12.8

* Mon Oct 13 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.7-alt1
- 3.12.7

* Wed Aug 27 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.5-alt1
- 3.12.5

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.4-alt1
- 3.12.4

* Wed Jun 11 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 3.10.4-alt1
- initial build

