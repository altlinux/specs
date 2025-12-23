#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with check
%define sover 0

Name: diodon
Version: 1.13.0
Release: alt1
Summary: Diodon is a lightweight clipboard manager for Linux
Group:   Graphical desktop/Other
License: GPL-2.0-only

URL: https://launchpad.net/diodon
VCS: https://github.com/diodon-dev/diodon

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Buildrequires(pre): rpm-macros-meson
Buildrequires: vala
Buildrequires: meson
Buildrequires: pkgconfig(ayatana-appindicator3-0.1) 
Buildrequires: pkgconfig(libpeas-1.0)
Buildrequires: pkgconfig(xtst)
Buildrequires: pkgconfig(zeitgeist-2.0)
Buildrequires: gobject-introspection-devel
Buildrequires: xvfb-run
Buildrequires: libayatana-appindicator3-vala
Buildrequires: libgdk-pixbuf-gir-devel
Buildrequires: libgtk+3-gir-devel

Requires: zeitgeist

%description
%summary.

%package -n lib%name%sover
Summary: Library for diodon
Group: System/Libraries

%description -n lib%name%sover
This package is a library for diodon.

%package devel
Summary: Development files for diodon
Group: Development/Other
Requires: lib%name%sover = %EVR

%description devel
This package provides include files, libraries and gobject introspection
devel data for diodon functions.

%package gir
Summary: GObject introspection data for the Diodon library
Group: System/Libraries
Requires: lib%name%sover = %EVR

%description gir
%summary.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
rm -rdf %buildroot%_iconsdir/*
rm %buildroot%_desktopdir/%name.desktop
%find_lang %name

%check
%meson_test

%files -f %name.lang
%doc AUTHORS COPYING README.md
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_bindir/%name
%_libdir/%name
%_man1dir/%name.1.*
%_datadir/%name
%_datadir/glib-2.0/schemas/net.launchpad.Diodon.gschema.xml

%files devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/*.pc
%_vapidir/%name.*
%_girdir/Diodon-1.0.gir

%files -n lib%name%sover
%_libdir/lib%name.so.%sover

%files gir
%_typelibdir/Diodon-1.0.typelib

%changelog
* Tue Dec 23 2025 Polina Poidenko <polipoki@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus (Closes: 57255).
