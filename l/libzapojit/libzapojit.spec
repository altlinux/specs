%define ver_major 0.0
%define api_ver 0.0
%def_disable gtk_doc
%def_enable introspection

Name: libzapojit
Version: %ver_major.2
Release: alt1

Summary: GLib/GObject wrapper for the SkyDrive and Hotmail REST APIs
Group: System/Libraries
License: LGPLv2+
Url: http://live.gnome.org/Zapojit

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: glib2-devel >= 2.28 libsoup-devel >= 2.38  libjson-glib-devel
BuildRequires: libgnome-online-accounts-devel librest-devel
BuildRequires: gtk-doc intltool
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libsoup-gir-devel librest-gir-devel libjson-glib-gir-devel}

%description
GLib/GObject wrapper for the SkyDrive and Hotmail REST APIs. It supports
SkyDrive file and folder objects, and the following SkyDrive operations:
  - Deleting a file, folder or photo.
  - Listing the contents of a folder.
  - Reading the properties of a file, folder or photo.
  - Uploading files and photos.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use Zapojit library.

%package gir
Summary: GObject introspection data for the Zapojit library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Zapojit library.

%package gir-devel
Summary: GObject introspection devel data for the Zapojit library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Zapojit library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use the Zapojit library.


%prep
%setup

%build
%configure \
  --disable-static \
  %{?_enable_gtk_doc:--enable-gtk-doc} \
  %{?_enable_introspection:--enable-introspection=yes}

%make_build

%install
%makeinstall_std

rm -rf %buildroot%_datadir/doc/%name

%files
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_libdir/pkgconfig/zapojit-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Zpj-%api_ver.typelib

%files gir-devel
%_girdir/Zpj-%api_ver.gir
%endif

%files devel-doc
%_datadir/gtk-doc/html/%name-%api_ver


%changelog
* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt1
- first build for Sisyphus

