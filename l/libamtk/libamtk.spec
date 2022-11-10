%define _libexecdir %_prefix/libexec

%define _name amtk
%define ver_major 5.6
%define api_ver 5

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_disable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: Actions, Menus and Toolbars Kit for GTK+3 applications
License: GPL-3.0-or-later
Group: System/Libraries
Url:  https://wiki.gnome.org/Projects/Amtk

Vcs: https://gitlab.gnome.org/swilmet/amtk.git
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

%define meson_ver 0.53
%define gtk_ver 3.22
%define gi_ver 1.42

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson >= %meson_ver gtk-doc
BuildRequires: libgtk+3-devel >= %gtk_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel}

%description
Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

%package devel
Summary: Development environment for Amtk
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the necessary components to develop with Amtk
library.

%package devel-doc
Summary: Development documentation for Amtk
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

This package contains development documentation for Amtk.

%package devel-static
Summary: Stuff for developing with Amtk
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the necessary components to develop statically
linked software for Amtk.

%package gir
Summary: GObject introspection data for the Amtk library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Amtk library.

%package gir-devel
Summary: GObject introspection devel data for the Amtk
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Amtk library.

%prep
%setup -n %_name-%version

%build
%meson 	\
    %{?_disable_gtk_doc:-Dgtk_doc=false} \
    %{?_disable_introspection:-Dintrospection=false}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name %{_name}-%api_ver

%check
%__meson_test

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/
%endif

%if_enabled static
%files devel-static
%_libdir/%name-%api_ver.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/Amtk-%api_ver.typelib

%files gir-devel
%_girdir/Amtk-%api_ver.gir
%endif

%changelog
* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 5.6.0-alt1
- 5.6.0

* Mon Oct 24 2022 Yuri N. Sedunov <aris@altlinux.org> 5.5.2-alt1
- 5.5.2

* Wed May 25 2022 Yuri N. Sedunov <aris@altlinux.org> 5.4.1-alt1
- 5.4.1

* Wed May 04 2022 Yuri N. Sedunov <aris@altlinux.org> 5.4.0-alt1
- 5.4.0

* Tue Apr 19 2022 Yuri N. Sedunov <aris@altlinux.org> 5.3.2-alt1
- 5.3.2 (ported to Meson build system)

* Thu Sep 10 2020 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- 5.2.0

* Sat Jan 25 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- 5.0.2

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- 5.0.1

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- first build for Sisyphus




