%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 3.34
%define api_ver 3
%define xdg_name org.gnome.Sysprof%api_ver
%define _libexecdir %_prefix/libexec

%def_with sysprofd
%def_enable gtk

Name: sysprof
Version: %ver_major.0
Release: alt1

Summary: Sysprof kernel based performance profiler for Linux
Group: Development/Tools
License: GPLv2+
Url: http://sysprof.com

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.62.0
%define gtk_ver 3.22.0
%define systemd_ver 222
%define dazzle_ver 3.30.0

BuildRequires(pre): meson
BuildRequires: gcc-c++ libappstream-glib-devel yelp-tools
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: gobject-introspection-devel
%{?_enable_gtk:BuildRequires: libgtk+3-devel >= %gtk_ver libdazzle-devel >= %dazzle_ver}
%{?_with_sysprofd:BuildRequires: pkgconfig(systemd) libpolkit-devel}

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
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/org.gnome.sysprof%{api_ver}.gschema.xml
%_iconsdir/hicolor/*/*/*
%_libdir/lib%name-%api_ver.so
%_libdir/lib%name-ui-%api_ver.so

%if_with sysprofd
%_libexecdir/sysprofd
%_unitdir/sysprof%{api_ver}.service
%_unitdir/sysprof2.service
%_datadir/dbus-1/system-services/%xdg_name.service
%_datadir/dbus-1/system-services/org.gnome.Sysprof2.service
%_datadir/dbus-1/system.d/%xdg_name.conf
%_datadir/dbus-1/system.d/org.gnome.Sysprof2.conf
%_datadir/polkit-1/actions/org.gnome.sysprof%{api_ver}.policy

%_datadir/dbus-1/interfaces/org.gnome.Sysprof2.xml
%_datadir/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%_datadir/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
%endif

%_datadir/mime/packages/%name-mime.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS README* TODO

%files devel
%_libdir/lib%name-capture-%api_ver.a
%_includedir/%{name}-%api_ver/
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-ui-%api_ver.pc
%_pkgconfigdir/%name-capture-%api_ver.pc

%changelog
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

