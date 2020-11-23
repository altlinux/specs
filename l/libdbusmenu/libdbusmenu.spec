%define ver_major 16.04
%define api_ver 0.4

# disable introspection and vala for Gtk2 build
%def_disable introspection
%{?_disable_introspection:%def_disable vala}

Name: libdbusmenu
Version: %ver_major.0
Release: alt3

Summary: A library that passes a menu structure across DBus
Group: System/Libraries
License: LGPL-2.1 and LGPL-3.0 and GPL-3.0
Url: https://launchpad.net/%name

# rev 477
#Source: %name-%version.tar
Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.gz
Patch: %name-16.04.0-alt-no-Werror.patch
Patch1: %name-16.04.0-alt-docs-build.patch

BuildRequires: intltool gtk-doc vala-tools
BuildRequires: libgtk+2-devel libgtk+3-devel libjson-glib-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
%{?_enable_introspection:BuildRequires: libgtk+2-gir-devel}

%description
%name is a small library designed to make sharing and displaying
of menu structures over DBus simple and easy to use. It works
for both QT and GTK+ and makes building menus simple.

%package devel
Summary: %summary
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for %name

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
This package provides GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR

%description gir-devel
This package provides GObject introspection devel data for the %name

%package gtk2
Summary: %summary
Group: System/Libraries
Requires: %name = %EVR

%description gtk2
This package provides shared %name-gtk2 library.

%package gtk3
Requires: %name = %EVR
Summary: %summary
Group: System/Libraries
Requires: %name = %EVR

%description gtk3
This package provides shared %name-gtk3 library.

%package gtk2-devel
Summary: Development files for %name-gtk2
Group: Development/C
Requires: %name-gtk2 = %EVR

%description gtk2-devel
This package provides libraries and header files for developing
applications that use %name-gtk2.

%package gtk2-gir
Summary: GObject introspection data for the %name-gtk2
Group: System/Libraries
Requires: %name-gtk3 = %EVR

%description gtk2-gir
This package provides GObject introspection data for the %name-gtk2.

%package gtk2-gir-devel
Summary: GObject introspection devel data for the %name-gtk2
Group: Development/Other
BuildArch: noarch
Requires: %name-gir-devel = %EVR
Requires: %name-gtk2-gir = %EVR

%description gtk2-gir-devel
This package provides GObject introspection devel data for the %name-gtk2

%package gtk3-devel
Summary: Development files for %name
Group: Development/C
Requires: %name-gtk3 = %EVR

%description gtk3-devel
The %name-gtk3-devel package contains libraries and header files for
developing applications that use %name.

%package gtk3-gir
Summary: GObject introspection data for the %name-gtk3
Group: System/Libraries
Requires: %name-gtk3 = %EVR

%description gtk3-gir
This package provides GObject introspection data for the %name-gtk3.

%package gtk3-gir-devel
Summary: GObject introspection devel data for the %name-gtk3
Group: Development/Other
BuildArch: noarch
Requires: %name-gir-devel = %EVR
Requires: %name-gtk3-gir = %EVR

%description gtk3-gir-devel
This package provides GObject introspection devel data for the %name-gtk3

%package jsonloader
Summary: Test library for %name
Group: Development/Tools
Requires: %name-devel = %EVR

%description jsonloader
%name is a small library designed to make sharing and displaying
of menu structures over DBus simple and easy to use.

This package provides the shared library for dbusmenu-jsonloader, a library
required for the %name test suites.

%package jsonloader-devel
Summary: Test lib development files for %name
Group: Development/C
Requires: %name-jsonloader = %EVR
Requires: %name = %EVR

%description jsonloader-devel
%name is a small library designed to make sharing and displaying
of menu structures over DBus simple and easy to use.

This package provides development files for dbusmenu-jsonloader, a library
required for the %name test suites.

%package devel-doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
The %name-doc package contains documentation for developing applications
that use %name.

%package tools
Summary: Development tools for the dbusmenu libraries
Group: Development/Tools
Requires: %name = %EVR

%description tools
The %name-tools package contains helper tools for developing applications
that use %name.

%prep
%setup -a0
%patch -p1
%patch1
mv %name-%version %name-gtk3
%patch -p1 -d %name-gtk3
%patch1 -d %name-gtk3

%build
%define opts --disable-static --enable-gtk-doc --disable-dumper

%autoreconf
%configure  %opts --with-gtk=2 %{?_disable_introspection:--enable-introspection=no --disable-vala}
%make_build

pushd %name-gtk3
%autoreconf
%configure %opts --with-gtk=3
%make_build
popd

%install
%makeinstall_std

pushd %name-gtk3
%makeinstall_std
popd

%files
%_libdir/%name-glib.so.*
%doc README AUTHORS

%files devel
%_includedir/%name-glib-%api_ver/
%exclude %_includedir/%name-glib-%api_ver/%name-jsonloader/
%_libdir/%name-glib.so
%_pkgconfigdir/dbusmenu-glib-%api_ver.pc
%_vapidir/Dbusmenu-%api_ver.vapi

%files gir
%_typelibdir/Dbusmenu-%api_ver.typelib

%files gir-devel
%_girdir/Dbusmenu-%api_ver.gir

%files jsonloader
%_libdir/%name-jsonloader.so.*

%files jsonloader-devel
%_includedir/%name-glib-%api_ver/%name-jsonloader/
%_libdir/%name-jsonloader.so
%_pkgconfigdir/dbusmenu-jsonloader-%api_ver.pc

%files gtk3
%_libdir/%name-gtk3.so.*

%files gtk3-gir
%_typelibdir/DbusmenuGtk3-%api_ver.typelib

%files gtk2
%_libdir/%name-gtk.so.*

%files gtk2-devel
%_includedir/%name-gtk-%api_ver/
%_libdir/%name-gtk.so
%_pkgconfigdir/dbusmenu-gtk-%api_ver.pc
%{?_enable_vala:%_vapidir/DbusmenuGtk-%api_ver.vapi}

%if_enabled introspection
%files gtk2-gir
%_typelibdir/DbusmenuGtk-%api_ver.typelib

%files gtk2-gir-devel
%_girdir/DbusmenuGtk-%api_ver.gir
%endif

%files gtk3-devel
%_includedir/%name-gtk3-%api_ver/
%_libdir/%name-gtk3.so
%_pkgconfigdir/dbusmenu-gtk3-%api_ver.pc
%_vapidir/DbusmenuGtk3-%api_ver.vapi

%files gtk3-gir-devel
%_girdir/DbusmenuGtk3-%api_ver.gir

%files devel-doc
%doc README COPYING COPYING.2.1 AUTHORS
%_datadir/gtk-doc/html/*

%files tools
%exclude %_libexecdir/dbusmenu-bench
%_libexecdir/dbusmenu-testapp
%dir %_datadir/%name/
%dir %_datadir/%name/json/
%_datadir/%name/json/test-gtk-label.json
%doc tools/README.dbusmenu-bench

%changelog
* Mon Nov 23 2020 Yuri N. Sedunov <aris@altlinux.org> 16.04.0-alt3
- gtk2: disabled introspection

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 16.04.0-alt2
- disabled -Werror
- fised docs build
- fixed License tag
- excluded python2 based %%_libexecdir/dbusmenu-bench from -tools

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 16.04.0-alt1
- 16.04.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 12.10.2-alt1
- first build for Sisyphus

