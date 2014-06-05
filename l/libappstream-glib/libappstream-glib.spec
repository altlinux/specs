%define _name appstream-glib
%define api_ver 1.0

Name: lib%_name
Version: 0.1.6
Release: alt1

Summary: Library for AppStream metadata
Group: System/Libraries
License: LGPLv2+
Url: http://people.freedesktop.org/~hughsient/%_name/

Source: http://people.freedesktop.org/~hughsient/%_name/releases/%_name-%version.tar.xz

BuildRequires: glib2-devel >= 2.16.1
BuildRequires: libarchive-devel libsoup-devel libgdk-pixbuf-devel
BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel
BuildRequires: gtk-doc docbook-utils docbook-dtds
BuildRequires: gperf

%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package devel
Summary: GLib Libraries and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
GLib headers and libraries for appstream-glib.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the AppStream metadata library.

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the AppStream metadata library.

%prep
%setup -n %_name-%version

%build
%configure \
        --enable-gtk-doc \
        --disable-static

%make_build

%install
%makeinstall_std

%files
%_bindir/appstream-util
%_libdir/%name.so.*
%doc README.md AUTHORS NEWS

%files devel
%_libdir/*.so
%_pkgconfigdir/%_name.pc
%_includedir/%name/
%_datadir/gtk-doc/html/%_name/

%files gir
%_typelibdir/AppStreamGlib-%api_ver.typelib

%files gir-devel
%_girdir/AppStreamGlib-%api_ver.gir

%changelog
* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- first build for Sisyphus

