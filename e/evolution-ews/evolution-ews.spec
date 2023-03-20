%set_verify_elf_method rpath=relaxed
%define ver_major 3.48
%define xdg_name org.gnome.Evolution

Name: evolution-ews
Version: %ver_major.0
Release: alt1

Summary: Evolution extension for Exchange Web Services
Group: Networking/Mail
License: LGPL-2.1
Url: https://wiki.gnome.org/Apps/Evolution

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define ver_base 3.48
%define evo_ver_base %ver_base

%define evolution_ver %version
%define eds_ver %version
%define glib_ver 2.68
%define libmspack_ver 0.4
%define soup3_ver 3.0
%define json_glib_ver 1.0.4

Requires: evolution >= %evolution_ver
Requires: evolution-data-server >= %eds_ver
Requires: libmspack >= %libmspack_ver

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ intltool
BuildRequires: evolution-data-server-devel >= %eds_ver
BuildRequires: evolution-devel >= %evolution_ver
BuildRequires: libmspack-devel >= %libmspack_ver
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: libsoup3.0-devel >= %soup3_ver
BuildRequires: libsqlite3-devel libical-devel
BuildRequires: pkgconfig(json-glib-1.0) >= %json_glib_ver

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
	-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON \
	-DENABLE_SCHEMAS_COMPILE:BOOL=OFF
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
%_datadir/metainfo/%xdg_name-ews.metainfo.xml

%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.48.0-alt1
- 3.48.0

* Fri Feb 10 2023 Yuri N. Sedunov <aris@altlinux.org> 3.46.4-alt1
- 3.46.4

* Sun Jan 08 2023 Yuri N. Sedunov <aris@altlinux.org> 3.46.3-alt1
- 3.46.3

* Fri Dec 02 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.2-alt1
- 3.46.2

* Fri Oct 21 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.1-alt1
- 3.46.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 3.45.3-alt1
- 3.45.3

* Fri Aug 05 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.4-alt1
- 3.44.4

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.3-alt1
- 3.44.3

* Fri May 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.2-alt1
- 3.44.2

* Fri Apr 22 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.1-alt1
- 3.44.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Sun Feb 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.42.4-alt1
- 3.42.4

* Fri Jan 07 2022 Yuri N. Sedunov <aris@altlinux.org> 3.42.3-alt1
- 3.42.3

* Fri Dec 03 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.2-alt1
- 3.42.2

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.1-alt1
- 3.42.1

* Fri Sep 17 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Fri Aug 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.4-alt1
- 3.40.4

* Fri Jul 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.3-alt1
- 3.40.3

* Fri Jun 04 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.2-alt1
- 3.40.2

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt1
- 3.40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Fri Feb 12 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4

* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Aug 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.5-alt1
- 3.36.5

* Fri Jul 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Fri Apr 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Feb 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Fri Jan 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Feb 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.5-alt1
- 3.30.5

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Jul 30 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.5-alt1
- 3.28.5

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1.1
- fixed buildreqs

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.6-alt1
- 3.26.6

* Mon Feb 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.5-alt1
- 3.26.5

* Mon Jan 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

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

