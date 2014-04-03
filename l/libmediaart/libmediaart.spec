%define ver_major 0.4
%define api_ver 1.0
%def_enable introspection
%def_enable gtk_doc

Name: libmediaart
Version: %ver_major.0
Release: alt1

Summary: Library for handling media art
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Tracker

Source: ftp://ftp.gnome.org/%name/%ver_major/%name-%version.tar.xz

BuildRequires: gcc-c++ libgio-devel >= 2.36 libgdk-pixbuf-devel zlib-devel
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

%description devel
This package contains libraries and header files needed for
development using LibMediaArt.

%package gir
Summary: GObject introspection data for the LibMediaArt library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the LibMediaArt library

%package gir-devel
Summary: GObject introspection devel data for the LibMediaArt library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the LibMediaArt library

%package devel-doc
Summary: Development documentation for LibMediaArt
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for LibMediaArt library.

%prep
%setup

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
%_libdir/%name-%api_ver.so.*
%doc NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.vapi

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
* Wed Apr 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Mar 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- first build for Sisyphus

