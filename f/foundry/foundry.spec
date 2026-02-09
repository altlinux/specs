%define _unpackaged_files_terminate_build 1

%define soversion 1
%define apiver %soversion

Name: foundry
Version: 1.0.1
Release: alt4

Summary: Foundry provides a platform for developer tools in GNOME
License: LGPL-2.1
Group: Development/Tools
Url: https://gitlab.gnome.org/GNOME/foundry
VCS: https://gitlab.gnome.org/GNOME/foundry

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(template-glib-1.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gom-1.0)
BuildRequires: pkgconfig(libdex-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(vte-2.91-gtk4)
BuildRequires: pkgconfig(libcmark)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(editorconfig)
BuildRequires: pkgconfig(libspelling-1)
BuildRequires: pkgconfig(gobject-introspection-1.0)

BuildRequires: gobject-introspection-devel

BuildRequires: gir(Dex)
BuildRequires: gir(Peas)
BuildRequires: gir(Json)
BuildRequires: gir(Gtk)
BuildRequires: gir(GtkSource)

%description
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

Why?

Because it seems like there is an opportunity to bring many of the automatic
IDE features of Builder to a command line environment.
To do this, foundry works similar to other developer environments where you
source a bunch of things into your sub-shell. Except, in Foundry's case, there
is a persistent program that lives above that sub-shell which may be interacted
with using the foundry commands.
This persistent ancestor process allows for a build manager, LSP management,
SDK tooling, device management and more to run while you are in your shell.

%package -n lib%name
Group: Development/C
Summary: A library that brings core features of GNOME Builder
Obsoletes: libfoundry-1_1

%description -n lib%name
%summary.

%package -n lib%name-devel
Group: Development/C
Summary: Headers files and library symbolic links for lib%name
Requires: lib%name = %EVR

%description -n lib%name-devel
%summary.
This package contains headers and libs
required for building programs with lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
%summary.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for lib%name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files
%_bindir/%name
%_datadir/%name/
%_datadir/bash-completion/completions/%name
%_datadir/metainfo/app.devsuite.Foundry.metainfo.xml

%files -n lib%name
%_libdir/lib%name-%apiver.so.%{soversion}*
%_libdir/lib%name-gtk-%apiver.so.%{soversion}*
%_datadir/glib-2.0/schemas/app.devsuite.foundry*

%files -n lib%name-devel
%_includedir/lib%name-%apiver/
%_includedir/lib%name-gtk-%apiver/
%_libdir/lib%name-%apiver.so
%_libdir/lib%name-%apiver/
%_libdir/lib%name-gtk-%apiver.so
%_pkgconfigdir/lib%name-%apiver.pc
%_pkgconfigdir/lib%name-gtk-%apiver.pc

%files -n lib%name-gir
%_typelibdir/Foundry-%apiver.typelib
%_typelibdir/FoundryGtk-%apiver.typelib

%files -n lib%name-gir-devel
%_girdir/Foundry-%apiver.gir
%_girdir/FoundryGtk-%apiver.gir

%changelog
* Mon Feb 09 2026 Alexey Volkov <qualimock@altlinux.org> 1.0.1-alt4
- remove api version and soversion
- update Summary and Description

* Tue Jan 20 2026 Alexey Volkov <qualimock@altlinux.org> 1.0.1-alt3
- fix files paths

* Thu Jan 15 2026 Alexey Volkov <qualimock@altlinux.org> 1.0.1-alt2
- move GSchema files to libfoundry

* Thu Oct 30 2025 Alexey Volkov <qualimock@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Wed Oct 01 2025 Alexey Volkov <qualimock@altlinux.org> 1.0.0-alt1
- initial build for ALT
