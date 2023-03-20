%def_disable snapshot

%define _name gnome-autoar
%define ver_major 0.4
%define api_ver_base 0
%define api_ver %api_ver_base.1
%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable check

Name: lib%_name
Version: %ver_major.4
Release: alt1

Summary: Automatic archives creating and extracting library
Group: System/Libraries
License: LGPL-2.1
Url: https://gitlab.gnome.org/GNOME/gnome-autoar

%if_disabled snapshot
Source: https://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/gnome-autoar.git
Source: %_name-%version.tar
%endif

%define glib_ver 2.38
%define gi_ver 1.30
%define gtk_ver 3.2
%define archive_ver 3.4.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libarchive-devel >= %archive_ver
%{?_enable_introspection:
BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel}
%{?_enable_vala:
BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: dbus-tools-gui}

%description
%_name provides functions, widgets, and gschemas for GNOME
applicatsions which want to use archives as a method to transfer
directories over the Internet.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name library.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library


%prep
%setup -n %_name-%version

%build
%meson \
    %{?_disable_introspection:-Dintrospection=disabled} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_vala:-Dvapi=true} \
    %{?_enable_check:-Dtests=true}
%nil
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_libdir/lib%_name-%api_ver_base.so.*
%_libdir/lib%_name-gtk-%api_ver_base.so.*
%doc NEWS README*

%files devel
%_includedir/%_name-%api_ver_base/
%_libdir/lib%_name-%api_ver_base.so
%_libdir/lib%_name-gtk-%api_ver_base.so
%_pkgconfigdir/%_name-%api_ver_base.pc
%_pkgconfigdir/%_name-gtk-%api_ver_base.pc
%{?_enable_vala:
%_vapidir/%_name-%api_ver_base.deps
%_vapidir/%_name-%api_ver_base.vapi
%_vapidir/%_name-gtk-%api_ver_base.deps
%_vapidir/%_name-gtk-%api_ver_base.vapi}

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/GnomeAutoar-%api_ver.typelib
%_typelibdir/GnomeAutoarGtk-%api_ver.typelib

%files gir-devel
%_girdir/GnomeAutoar-%api_ver.gir
%_girdir/GnomeAutoarGtk-%api_ver.gir
%endif


%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Fri Jan 07 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Sat Oct 30 2021 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Aug 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0 (ported to Meson build system)

* Fri Jun 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Sat Mar 13 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Feb 12 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0 (fixed CVE-2020-36241)

* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Sun Feb 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Fri Mar 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Sep 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Tue Feb 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus


