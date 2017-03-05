%def_disable snapshot

%define _name libmediaart
%define ver_major 1.9
%define api_ver 2.0
%def_enable introspection
%def_enable gtk_doc

Name: %_name%api_ver
Version: %ver_major.1
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

BuildRequires: gcc-c++ libgio-devel >= 2.38 libgdk-pixbuf-devel zlib-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}
BuildRequires: libvala-devel vala-tools intltool gtk-doc
# for check
BuildRequires: /proc dbus-tools-gui

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
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_libdir/%_name-%api_ver.so.*
%doc NEWS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.vapi

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

