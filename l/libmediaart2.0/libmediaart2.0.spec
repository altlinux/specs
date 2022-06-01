%def_disable snapshot

%define _name libmediaart
%define ver_major 1.9
%define api_ver 2.0
%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable check

Name: %_name%api_ver
Version: %ver_major.6
Release: alt1

Summary: Library for handling media art (2.0 API)
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Tracker

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Obsoletes: %_name < %version
Provides: %_name = %version-%release

%define meson_ver 0.56.2
%define glib_ver 2.38

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver gcc-c++ libgio-devel >= %glib_ver libgdk-pixbuf-devel zlib-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
LibMediaArt is a library tasked with managing, extracting and handling
media art caches.

%package devel
Summary: Development files for LibMediaArt
Group: Development/C++
Requires: %name = %version-%release
Obsoletes: %_name-devel < %version
Provides: %_name-devel = %version-%release

%description devel
This package contains libraries and header files needed for
development using LibMediaArt library.

%package gir
Summary: GObject introspection data for the LibMediaArt library
Group: System/Libraries
Requires: %name = %version-%release
Obsoletes: %_name-gir < %version
Provides: %_name-gir = %version-%release

%description gir
GObject introspection data for the LibMediaArt library

%package gir-devel
Summary: GObject introspection devel data for the LibMediaArt library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release
Obsoletes: %_name-gir-devel < %version
Provides: %_name-gir-devel = %version-%release

%description gir-devel
GObject introspection devel data for the LibMediaArt library

%package devel-doc
Summary: Development documentation for LibMediaArt
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release
Obsoletes: %_name-devel-doc < %version
Provides: %_name-devel-doc = %version-%release

%description devel-doc
This package contains development documentation for LibMediaArt library.

%prep
%setup -n %_name-%version
%{?_enable_snapshot:touch ChangeLog}

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	-Dimage_library=gdk-pixbuf \
	%{?_disable_introspection:-Dintrospection=false} \
	%{?_disable_vala:-Dvala=false}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%_name-%api_ver.so.*
%doc NEWS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:
%_vapidir/%_name-%api_ver.vapi
%_vapidir/%%_name-%api_ver.deps}

%if_enabled introspection
%files gir
%_typelibdir/MediaArt-%api_ver.typelib

%files gir-devel
%_girdir/MediaArt-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Wed Jun 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.6-alt1
- 1.9.6

* Sat May 22 2021 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5

* Thu Feb 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt2
- updated to 1.9.4-2-ged015a5 (fixed BGO #792272 and related ALT #36091)

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt1
- 1.9.4

* Sun Mar 05 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Sun Oct 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt2
- updated to 1.9.0-8-g52eb649
- obsoletes/provides old libmediaart-1.0 (ALT #32594)

* Sat Jan 24 2015 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Aug 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Jul 28 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed Apr 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Mar 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- first build for Sisyphus

