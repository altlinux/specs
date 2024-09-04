%def_disable snapshot

%define _name geoclue
%define xdg_name org.freedesktop.GeoClue2
%define ver_major 2.7
%define api_ver 2.0
%define _libexecdir %_prefix/libexec

%def_enable 3g
%def_enable nmea
%def_enable gtk_doc
%def_enable introspection
%def_enable vala
%def_enable check

Name: %{_name}2
Version: %ver_major.2
Release: alt1

Summary: The Geoinformation Service
Group: System/Libraries
License: GPL-2.0-or-later and LGPL-2.1-or-later
Url: https://geoclue.freedesktop.org/

Vcs: https://gitlab.freedesktop.org/geoclue/geoclue.git

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/%_name/%_name/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.74
%define mm_ver 1.12
%define soup3_ver 3.0

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson yelp-tools gtk-doc libgio-devel >= %glib_ver
BuildRequires: libjson-glib-devel libsoup3.0-devel >= %soup3_ver
BuildRequires: libdbus-devel libnotify-devel systemd-devel
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_nmea:BuildRequires: libavahi-glib-devel}
%{?_enable_3g:BuildRequires: libmm-glib-devel >= %mm_ver}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
GeoClue is a D-Bus geoinformation service. The goal of the Geoclue
project is to make creating location-aware applications as simple as
possible.

%package devel
Summary: Development package for GeoClue
Group: Development/C
Requires: %name = %EVR

%description devel
Files for development with GeoClue.

%package -n lib%name
Summary: GeoClue Convenience Library
Group: System/Libraries

%description -n lib%name
This package provides convenience shared library that makes interacting with
Geoclue very easy.

%package -n lib%name-devel
Summary: Header files for GeoClue library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides development files for GeoClue library.

%package -n lib%name-gir
Summary: GObject introspection data for the GeoClue library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the GeoClue library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GeoClue library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the GeoClue library.

%package devel-doc
Summary: Developer documentation for GeoClue
Group: Development/Documentation
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Developer documentation for GeoClue.

%package -n lib%name-devel-doc
Summary: Developer documentation for GeoClue library
Group: Development/Documentation
Conflicts: lib%name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
Developer documentation for GeoClue library.

%package demo
Summary: Demo programs for GeoClue
Group: Development/C
Requires: %name = %EVR
Requires: lib%name = %EVR

%description demo
This package contains demo programs for GeoClue.

%prep
%setup -n %_name-%version
rm -f demo/*.desktop.in

%build
%meson \
    -Ddbus-srv-user=%_name \
    %{subst_enable_meson_bool nmea nmea-source} \
    %{subst_enable_meson_bool 3g 3g-source} \
    %{subst_enable_meson_bool gtk_doc gtk-doc} \
    %{subst_enable_meson_bool introspection introspection} \
    -Ddemo-agent=true
%nil
%meson_build

%install
%meson_install
mkdir -p %buildroot%_localstatedir/%_name
mkdir -p %buildroot%_sysconfdir/%_name/conf.d

echo 'd %_localstatedir/%_name 0755 %_name %_name' | \
install -D -m644 /dev/stdin %buildroot%_tmpfilesdir/%_name.conf

%check
%__meson_test

%pre
%_sbindir/groupadd -r -f %_name
%_sbindir/useradd -r -g %_name -d %_localstatedir/%_name -s /dev/null \
    -c 'User for GeoClue service' %_name >/dev/null 2>&1 ||:

%files
%_libexecdir/%_name
%dir %_sysconfdir/%_name/conf.d
%_datadir/dbus-1/system.d/%xdg_name.conf
%_datadir/dbus-1/system.d/%xdg_name.Agent.conf
%_datadir/dbus-1/interfaces/%xdg_name.Agent.xml
%_datadir/dbus-1/interfaces/%xdg_name.Client.xml
%_datadir/dbus-1/interfaces/%xdg_name.Location.xml
%_datadir/dbus-1/interfaces/%xdg_name.Manager.xml
%_datadir/dbus-1/interfaces/%xdg_name.xml
%_datadir/dbus-1/system-services/%xdg_name.service
%_datadir/polkit-1/rules.d/%xdg_name.rules
%systemd_unitdir/%_name.service
%config %_sysconfdir/%_name/%_name.conf
%attr(755,%_name,%_name) %dir %_localstatedir/%_name
%_tmpfilesdir/%_name.conf
%_man5dir/%_name.5*
%doc README* NEWS

%files devel
%_pkgconfigdir/%_name-%api_ver.pc

%files -n lib%name
%_libdir/lib%_name-2.so.*

%files -n lib%name-devel
%_includedir/lib%_name-%api_ver/
%_libdir/lib%_name-2.so
%_pkgconfigdir/lib%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/lib%_name-%api_ver.deps
%_vapidir/lib%_name-%api_ver.vapi}

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Geoclue-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Geoclue-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/lib%_name/
%endif

%files demo
%_libexecdir/%_name-%api_ver/demos/
%_desktopdir/*.desktop
%_xdgconfigdir/autostart/%_name-demo-agent.desktop

%changelog
* Wed Sep 04 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2

* Tue Sep 12 2023 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- 2.7.1

* Sat Jan 28 2023 Yuri N. Sedunov <aris@altlinux.org> 2.7.0-alt1
- 2.7.0

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sat Dec 26 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.7-alt1
- 2.5.7

* Sun Mar 15 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.6-alt1
- 2.5.6

* Wed Oct 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.5-alt1
- updated to 2.5.5-4-g1a00809

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.3-alt1
- 2.5.3

* Fri Mar 15 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt2
- added config for systemd-tmpfiles

* Tue Jan 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt1
- 2.5.2

* Tue Nov 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt1
- updated to 2.5.1-13-g225d5f9

* Mon Oct 15 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.13-alt1
- 2.4.13

* Fri Aug 17 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.12-alt1
- 2.4.12

* Fri Jul 27 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt1
- 2.4.11

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.10-alt1
- 2.4.10

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.8-alt1
- 2.4.8

* Wed May 31 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.7-alt1
- 2.4.7

* Sun Apr 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt1
- 2.4.6

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.5-alt1
- 2.4.5

* Sun Sep 11 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Tue Mar 01 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Thu Dec 17 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0
- new libgeoclue2-* subpackages

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Jan 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.10-alt1
- 2.1.10

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- 2.1.9

* Mon Apr 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.8-alt1
- 2.1.8

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Fri Mar 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- 2.1.6

* Fri Dec 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- create new geoclue group and user in %%pre

* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0
- new -devel-doc subpackage

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.99.4-alt1
- 1.99.4

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 1.99.2-alt1
- first build for Sisyphus

