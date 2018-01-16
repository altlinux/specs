%def_disable snapshot

%define ver_major 0.5
%define api_ver %ver_major
%def_enable introspection
%def_disable gtk_doc

Name: libgepub
Version: %ver_major.3
Release: alt1

Summary: Simple library to read epub files using glib
Group: System/Libraries
License: LGPLv2+
Url: https://git.gnome.org/browse/libgepub

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires: meson gcc-c++ gtk-doc libwebkit2gtk-devel libarchive-devel libxml2-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libwebkit2gtk-gir-devel}

%description
%name is a GObject based library for handling and rendering epub
documents.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup

%build
%meson %{?_enable_introspection:-Denable-introspection=true}

%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%name.so.*
%doc AUTHORS README TODO

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%if_enabled introspection
%files gir
%_typelibdir/Gepub-%api_ver.typelib

%files gir-devel
%_girdir/Gepub-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%changelog
* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Wed Jul 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Wed Aug 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Thu Jun 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt0.1
- first build for Sisyphus (0.3-32-g1495f30)

