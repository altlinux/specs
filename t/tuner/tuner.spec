%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tuner
%define api_ver 1

%def_enable docs

Name: tuner
Version: 0.1.1
Release: alt1

Summary: Extensible control center
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/Tuner
Vcs: https://altlinux.space/alt-gnome/Tuner
Source: %name-%version.tar

Requires: lib%name = %EVR

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: gir(Peas)
BuildRequires: gir(Gee)
BuildRequires: gir(Adw)
BuildRequires: gobject-introspection-devel
%{?_enable_docs:BuildRequires: valadoc}

%description
Extensible control center for GNOME desktop

%package -n lib%name
Summary: Versatile library for creating extensible apps and plugins for them
Group: System/Libraries

%description -n lib%name
lib%name is a library designed to support both core application development
and plugin integration. It provides several build-in widgets and API to
create and extend pages. It also provides API to add plugins to your own app.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains development libraries and header files
that are needed to write applications that use lib%name.

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the lib%name.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the lib%name
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the lib%name.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool docs docs}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%doc README.md

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name-%api_ver.h
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/Tuner-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Tuner-%api_ver.gir

%if_enabled docs
%files -n lib%name-devel-doc
%_datadir/doc/%name/*
%endif

%changelog
* Mon May 12 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt1
- fixed opening panels at mobile layout
- added panels sorting

* Wed Apr 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.0-alt1
- initial build
