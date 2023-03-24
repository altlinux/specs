%define _unpackaged_files_terminate_build 1

%define ver_major 44
%define beta %nil
%define api_ver_major 4
%define api_ver %api_ver_major.0
%define libname gtkhex-%api_ver_major
%define xdg_name org.gnome.GHex

%def_enable introspection
%def_disable check

Name: ghex
Version: %ver_major.0
Release: alt1%beta

Summary: Binary editor for GNOME
Group: Development/Tools
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Ghex

Vcs: https://gitlab.gnome.org/GNOME/ghex.git
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major%beta/%name-%version%beta.tar.xz

%define glib_ver 2.68
%define gtk4_ver 4.4.0

Requires: libgtkhex = %EVR
Requires: dconf yelp

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson glib2-devel >= %glib_ver libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: yelp-tools
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk4-gir-devel}
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstream-util}

%description
GHex is a hex editor for the GNOME desktop.

GHex can load raw data from binary files and display them for editing in
the traditional hex editor view. The display is split in two columns,
with hexadecimal values in one column and the ASCII representation in
the other. A useful tool for working with raw data.

%package -n libgtkhex
Summary: GtkHex shared library
Group: System/Libraries

%description -n libgtkhex
This package provides shared librarys needed for GtkGHex to work.

%package -n libgtkhex-devel
Summary: Development files for GtkHex
Group: Development/C
Requires: libgtkhex = %EVR

%description -n libgtkhex-devel
This package contains libraries and header files for
developing applications that use GtkGHex library.

%package -n libgtkhex-gir
Summary: GObject introspection data for the GtkGHex
Group: System/Libraries
Requires: libgtkhex = %EVR

%description -n libgtkhex-gir
GObject introspection data for the GtkGHex library.

%package -n libgtkhex-gir-devel
Summary: GObject introspection devel data for the GtkGHex
Group: System/Libraries
BuildArch: noarch
Requires: libgtkhex-gir = %EVR
Requires: libgtkhex-devel = %EVR

%description -n libgtkhex-gir-devel
GObject introspection devel data for the GtkGHex library.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_disable_introspection:-Dintrospection=false}
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %name-%api_ver

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS README*

%files -n libgtkhex
%dir %_libdir/gtkhex-%api_ver
%_libdir/gtkhex-%api_ver/libhex-buffer-mmap.so
%_libdir/gtkhex-%api_ver/libhex-buffer-direct.so
%_libdir/lib%libname.so.*

%files -n libgtkhex-devel
%_includedir/%libname/
%_libdir/lib%libname.so
%_pkgconfigdir/%libname.pc

%if_enabled introspection
%files -n libgtkhex-gir
%_typelibdir/Hex-%api_ver_major.typelib

%files -n libgtkhex-gir-devel
%_girdir/Hex-%api_ver_major.gir
%endif

%changelog
* Fri Mar 24 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Fri Feb 10 2023 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Oct 05 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Mon Jun 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Tue Apr 26 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Sat Apr 16 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Wed Apr 06 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0 (ported to GTK4)

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 4-alt0.5.beta.1
- 4.beta.1

* Sat Dec 04 2021 Yuri N. Sedunov <aris@altlinux.org> 3.41.1-alt1
- 3.41.1

* Fri Sep 24 2021 Yuri N. Sedunov <aris@altlinux.org> 3.41.0-alt1
- 3.41.0

* Sat Jul 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4 (ported to Meson build system)

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Jun 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2
- new libgtkhex{,-devel} subpackages

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Sep 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.90-alt1
- 3.5.90

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91-alt1
- 3.3.91

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus

