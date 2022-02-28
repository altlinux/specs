%define _name libwnck
%define ver_major 40
%define api_ver 3.0

%def_enable introspection
%def_enable startup_notification
%def_enable gtk_doc
%def_enable install_tools
%def_enable check

Name: %{_name}3
Version: %ver_major.1
Release: alt1

Summary: libwnck is a Window Navigator Construction Kit
License: LGPL-2.0
Group: System/Libraries
Url: http://www.gnome.org

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires(pre): meson rpm-build-gnome
BuildRequires: libX11-devel libXres-devel libXi-devel pkgconfig(cairo-xlib-xrender)
BuildRequires: libgtk+3-devel >= 3.22.0
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: gtk-doc >= 1.9
%{?_enable_startup_notification:BuildRequires: libstartup-notification-devel >= 0.4}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use for
writing pagers and taskslists and stuff.

%package devel
Summary: Header and development libraries for %name
Group: Development/C
Requires: %name = %EVR
Provides: %{name}2.22-devel = %EVR
Provides: %{name}2.20-devel = %EVR
Obsoletes: %{name}2.22-devel
Obsoletes: %{name}2.20-devel

%description devel
This package contains header and development libraries for %name

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the Window Navigator Construction Kit library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the Window Navigator Construction Kit library

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_disable_startup_notification:-Dstartup-notification=disabled} \
    %{?_disable_introspection:--Dintrospection=disabled} \
    %{?_disable_install_tools:-Dinstall_tools=false} \
    %{?_enable_gtk_doc:-Dgtk_doc=true}
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test


%files -f %_name.lang
%{?_enable_install_tools:
%_bindir/wnck-urgency-monitor
%_bindir/wnckprop}
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif


%changelog
* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Mon May 10 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Thu Mar 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0 (ported to Meson build system)

* Wed May 01 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.4-alt1
- 3.31.4

* Tue Sep 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 3.24.1-alt1.1
- NMU: Rebuilt for e2k.

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Thu Jun 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Jun 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Jun 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Sep 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.4.9-alt1
- 3.4.9

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.7-alt1
- 3.4.7

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.5-alt1
- 3.4.5

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4

* Fri Sep 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.92-alt1
- 2.91.92

* Wed Feb 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.6-alt1
- first build for Sisyphus

