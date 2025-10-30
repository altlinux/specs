%define _unpackaged_files_terminate_build 1

%define soversion 1
%define apiver 1
%define soname %name-%{apiver}_%soversion

Name: foundry
Version: 1.0.1
Release: alt1

Summary: A tool that brings core features of GNOME Builder into a library and CLI tool
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
%summary.

%package -n lib%soname
Group: Development/C
Summary: A library that brings core features of GNOME Builder

%description -n lib%soname
%summary.

%package -n lib%name-devel
Group: Development/C
Summary: Headers files and library symbolic links for lib%name
Requires: lib%soname = %EVR

%description -n lib%name-devel
%summary.
This package contains headers and libs
required for building programs with lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for lib%name
Group: System/Libraries
Requires: lib%soname = %EVR

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
%_datadir/glib-2.0/schemas/
%_datadir/metainfo/app.devsuite.Foundry.metainfo.xml
%dir %_datadir/bash-completion
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/%name

%files -n lib%soname
%_libdir/lib%name-%apiver.so*
%_libdir/lib%name-gtk-%apiver.so*

%files -n lib%name-devel
%_includedir/lib%name-%apiver/
%_includedir/lib%name-gtk-%apiver/
%_pkgconfigdir/lib%name-%apiver.pc
%_pkgconfigdir/lib%name-gtk-%apiver.pc
%_libdir/lib%name-%apiver/include/

%files -n lib%name-gir
%_typelibdir/Foundry-%apiver.typelib
%_typelibdir/FoundryGtk-%apiver.typelib

%files -n lib%name-gir-devel
%_girdir/Foundry-%apiver.gir
%_girdir/FoundryGtk-%apiver.gir

%changelog
* Thu Oct 30 2025 Alexey Volkov <qualimock@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Wed Oct 01 2025 Alexey Volkov <qualimock@altlinux.org> 1.0.0-alt1
- initial build for ALT
