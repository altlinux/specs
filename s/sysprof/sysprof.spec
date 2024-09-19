%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define ver_major 47
%define beta %nil
%define api_ver 6
%define service_ver 3
%define capture_ver 4
%define xdg_name org.gnome.Sysprof
%define _libexecdir %_prefix/libexec

%def_enable sysprofd
%def_enable gtk
%ifnarch %e2k
%def_enable libunwind
%endif

Name: sysprof
Version: %ver_major.0
Release: alt1%beta

Summary: Sysprof kernel based performance profiler for Linux
Group: Development/Tools
License: GPL-3.0-or-later
Url: http://sysprof.com

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.80
%define gtk_ver 4.15.2
%define adw_ver 1.6
%define dex_ver 0.6
%define panel_ver 1.7
%define systemd_ver 222
%define polkit_ver 0.105

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ /usr/bin/appstream-util yelp-tools
BuildRequires: glib2-devel >= %glib_ver libjson-glib-devel
BuildRequires: libdex-devel >= %dex_ver
BuildRequires: libpanel-devel >= %panel_ver
BuildRequires: gobject-introspection-devel
%{?_enable_gtk:BuildRequires: libgtk4-devel >= %gtk_ver pkgconfig(libadwaita-1) >= %adw_ver}
%{?_enable_sysprofd:BuildRequires: pkgconfig(systemd) libpolkit-devel >= %polkit_ver}
%{?_enable_libunwind:BuildRequires: libunwind-devel}

%description
The Sysprof profiler is a statistical profiler based on hardware
performance counters in modern CPUs. Please see %url for more
information.

%package devel
Summary: Development files for GtkHex
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use GtkGHex library.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{subst_enable_meson_bool gtk gtk} \
    %{?_enable_sysprofd:-Dsysprofd=bundled}
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name

%files -f %name.lang
%_bindir/%name-cli
%_bindir/%name
%_bindir/%name-agent
%_datadir/applications/%xdg_name.desktop
%_iconsdir/hicolor/*/*/*
%_libdir/lib%name-%api_ver.so.*
%_libdir/lib%name-memory-%api_ver.so
%_libdir/lib%name-speedtrack-%api_ver.so
%_libdir/lib%name-tracer-%api_ver.so

%if_enabled sysprofd
%_libexecdir/sysprofd
%_unitdir/sysprof3.service
%_datadir/dbus-1/system-services/%{xdg_name}%{service_ver}.service
%_datadir/dbus-1/system.d/%{xdg_name}%{service_ver}.conf
%_datadir/polkit-1/actions/org.gnome.sysprof%{service_ver}.policy

%_datadir/dbus-1/interfaces/%{xdg_name}%{service_ver}.Profiler.xml
%_datadir/dbus-1/interfaces/%{xdg_name}%{service_ver}.Service.xml
%_datadir/dbus-1/interfaces/%{xdg_name}.Agent.xml
%endif

%_datadir/mime/packages/%name-mime.xml
%_datadir/metainfo/org.gnome.Sysprof.appdata.xml
%doc AUTHORS NEWS README*

%files devel
%_libdir/lib%name-capture-%capture_ver.a
%_libdir/lib%name-%api_ver.so
%_includedir/%{name}-%api_ver/
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-capture-%capture_ver.pc

%changelog
* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Sat Mar 16 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Wed Feb 07 2024 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Tue Oct 24 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sat Sep 02 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt0.9.rc
- 45.rc

* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.48.0-alt1
- 3.48.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Thu Nov 04 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.1-alt1
- 3.42.1

* Wed Sep 22 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0-1-gb113c89

* Tue Sep 14 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt2.1
- E2K: disabled libunwind support

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt2
- updated to 3.40.1-5-g5f25540
- added -ffat-lto-objects to %%optflags_lto

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt1
- 3.40.1

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0-2-g6f167d7

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sat Sep 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Wed Nov 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1 (3.22.1-1-g4b95b38)

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed May 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- first build for sisyphus

