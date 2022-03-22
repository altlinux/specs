%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define ver_major 3.44
%define api_ver 4
%define xdg_name org.gnome.Sysprof%api_ver
%define _libexecdir %_prefix/libexec

%def_with sysprofd
%def_enable gtk
%ifnarch %e2k
%def_enable libunwind
%endif

Name: sysprof
Version: %ver_major.0
Release: alt1

Summary: Sysprof kernel based performance profiler for Linux
Group: Development/Tools
License: GPL-3.0
Url: http://sysprof.com

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.67.4
%define gtk_ver 3.22.0
%define systemd_ver 222
%define dazzle_ver 3.40
%define polkit_ver 0.105

BuildRequires(pre): meson
BuildRequires: gcc-c++ libappstream-glib-devel yelp-tools
BuildRequires: glib2-devel >= %glib_ver libjson-glib-devel
BuildRequires: gobject-introspection-devel
%{?_enable_gtk:BuildRequires: libgtk+3-devel >= %gtk_ver libdazzle-devel >= %dazzle_ver}
%{?_with_sysprofd:BuildRequires: pkgconfig(systemd) libpolkit-devel >= %polkit_ver}
%{?_enable_libunwind:BuildRequires: libunwind-devel}

%description
The Sysprof profiler is a statistical profiler based on hardware
performance counters in modern CPUs. Please see %url for more
information.

%package devel
Summary: Development files for GtkHex
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use GtkGHex library.

%prep
%setup

%build
%meson \
	%{?_enable_gtk:-Denable_gtk=true} \
	%{?_with_sysprofd:-Dwith_sysprofd=bundled} \
	-Ddebugdir=%prefix/lib/debug
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name

%files -f %name.lang
%_bindir/%name-cli
%_bindir/%name
%_datadir/applications/org.gnome.Sysprof3.desktop
%_datadir/glib-2.0/schemas/org.gnome.sysprof3.gschema.xml
%_iconsdir/hicolor/*/*/*
%_libdir/lib%name-%api_ver.so
%_libdir/lib%name-ui-%api_ver.so
%_libdir/lib%name-memory-%api_ver.so
%_libdir/lib%name-speedtrack-%api_ver.so

%if_with sysprofd
%_libexecdir/sysprofd
%_unitdir/sysprof2.service
%_unitdir/sysprof3.service
%_datadir/dbus-1/system-services/org.gnome.Sysprof2.service
%_datadir/dbus-1/system-services/org.gnome.Sysprof3.service
%_datadir/dbus-1/system.d/org.gnome.Sysprof2.conf
%_datadir/dbus-1/system.d/org.gnome.Sysprof3.conf
%_datadir/polkit-1/actions/org.gnome.sysprof3.policy

%_datadir/dbus-1/interfaces/org.gnome.Sysprof2.xml
%_datadir/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%_datadir/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
%endif

%_datadir/mime/packages/%name-mime.xml
%_datadir/metainfo/org.gnome.Sysprof3.appdata.xml
%doc AUTHORS NEWS README*

%files devel
%_libdir/lib%name-capture-%api_ver.a
%_includedir/%{name}-%api_ver/
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-ui-%api_ver.pc
%_pkgconfigdir/%name-capture-%api_ver.pc

%changelog
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

