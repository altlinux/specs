%def_disable snapshot
%define ver_major 8.0
%define api_ver 3

Name: switchboard
%define xdg_name org.pantheon.%name
%define rdn_name io.elementary.settings
Version: %ver_major.0
Release: alt1

Summary: Modular Desktop Settings Hub for elementary OS
License: LGPL-2.1
Group: Graphical desktop/Other
Url: https://github.com/elementary/switchboard

Vcs: https://github.com/elementary/switchboard.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

Provides: %rdn_name = %EVR
Requires: lib%name = %EVR

%define granite_ver 7.0.0
%define adw_ver 1.4

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson vala-tools gcc-c++ sassc
BuildRequires: pkgconfig(granite-7) >= %granite_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: vapi(granite-7)

%description
This package provides Switchboard a system settings application for Elementary OS.

%package -n lib%name
Summary: Switchboard Library
Group: System/Libraries

%description -n lib%name
This package provides shared library needed for Switchboard to work.

%package -n lib%name-devel
Summary: Switchboard Library - development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains files that are needed to develop Switchboard plugins.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*x*/*/%rdn_name.*
%_datadir/metainfo/%rdn_name.appdata.xml

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%changelog
* Sat May 25 2024 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- 8.0.0 (ported to GTK4)

* Wed Jun 15 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.2-alt1
- 6.0.2

* Thu May 05 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- 6.0.1

* Mon Mar 28 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt2
- updated to 6.0.0-57-gdeeff7c (fixed build with meson >= 0.61,
  updated translations)

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1.1
- fixed meson options

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- 6.0.0

* Tue May 12 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.9-alt1
- 2.3.9

* Thu Jan 30 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.8-alt1
- 2.3.8

* Fri Nov 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.7-alt1
- 2.3.7

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.6-alt1
- 2.3.6

* Fri Oct 26 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Tue Jul 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt2
- rebuilt against libgranite.so.5

* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt2
- rebuilt against libgranite.so.4

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Tue Feb 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt2
- fixed pc-file

* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus


