%def_disable snapshot

%define _name gudev
%define ver_major 237
%define api_ver 1.0

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_disable vala
%def_enable umockdev
%def_enable check

Name: lib%_name
Version: %ver_major
Release: alt1
Epoch: 1

Summary: UDev GObject bindings
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/%name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define udev_ver 199
%define glib_ver 2.38
# https://github.com/martinpitt/umockdev/issues/69
%define umockdev_ver 0.11.2

BuildRequires(pre): meson
BuildRequires: libudev-devel >= %udev_ver
BuildRequires: libgio-devel >= %glib_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: libumockdev-devel >= %umockdev_ver}

%description
%name is a library with GObject bindings to libudev, now made
independent, after being part of udev itself, and later systemd.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%name is a library with GObject bindings to libudev, now made
independent, after being part of udev itself, and later systemd.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
%name is a library with GObject bindings to libudev, now made
independent, after being part of udev itself, and later systemd.

This package provides development documentations for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup -n %name-%version

%build
%meson \
%{?_disable_introspection:-Dintrospection=disabled} \
%{?_disable_vala:-Dvapi=disabled} \
%{?_enable_gtk_doc:-Dgtk_doc=true} \
%{?_disable_check:-Dtests=disabled}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README* NEWS

%files devel
%_includedir/%_name-%api_ver
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:
%_vapidir/%_name-%api_ver.*}

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/GUdev-%api_ver.typelib

%files gir-devel
%_girdir/GUdev-%api_ver.gir
%endif


%changelog
* Sun Aug 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1:237-alt1
- 237

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1:236-alt1
- 236 (ported to Meson build system)

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 1:234-alt1
- 234

* Sat Aug 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1:233-alt1
- 233

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1:232-alt3
- required umockdev >= 0.11.2 for check

* Fri Feb 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1:232-alt2
- updated to 232-4-gbf8664a (fixed BGO ##792845, 787314)
- disabled check while umockdev not fixed for systemd-237

* Fri Sep 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1:232-alt1
- 232

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1:231-alt1
- 231

* Sun Jun 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1:230-alt1
- 230

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1:219-alt3
- first build separate from systemd

