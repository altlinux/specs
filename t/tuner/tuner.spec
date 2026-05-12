%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tuner
%define namespace Tuner
%define api_ver 1

%def_enable docs

Name: tuner
Version: 0.6.8
Release: alt1

Summary: Extensible control center
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/Tuner
Vcs: https://altlinux.space/alt-gnome/Tuner
Source: %name-%version.tar

Requires: lib%name%api_ver = %EVR

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gir(Peas) = 2
BuildRequires: gir(Gee) = 0.8
BuildRequires: gir(Adw) = 1
BuildRequires: gobject-introspection-devel
%{?_enable_docs:BuildRequires: valadoc}

%description
Tuner is the home for your additional system settings, components,
applications, and whatever else you want!

Extended control over the interface and functions using plugins.
The interface is adapted to different device sizes.
Easy installation from the repository.
You can create your own plugins without affecting the main program code.
Easy creation of plugins working with dconf and unlimited plugin functionality
thanks to libpeas.

%package -n lib%name%api_ver
Summary: Versatile library for creating extensible apps and plugins for them
Group: System/Libraries
Requires: libpeas2-python3-loader

%description -n lib%name%api_ver
lib%name is a library designed to support both core application development
and plugin integration. It provides several build-in widgets and API to
create and extend pages. It also provides API to add plugins to your own app.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name%api_ver = %EVR

%description -n lib%name-devel
This package contains development libraries and header files
that are needed to write applications that use lib%name.

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
Conflicts: lib%name%api_ver < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the lib%name
Group: System/Libraries
Requires: lib%name%api_ver = %EVR

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
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%files -n lib%name%api_ver
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name-%api_ver.h
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%namespace-%api_ver.gir

%if_enabled docs
%files -n lib%name-devel-doc
%_datadir/doc/%name/*
%endif

%changelog
* Tue May 12 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.8-alt1
- added more icons

* Wed Mar 11 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.6-alt1
- added more icons
- updated links

* Thu Feb 26 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.5-alt1
- fixed wrong version in about dialog

* Thu Feb 19 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.4-alt1
- added more icons
- added animation to sidebar size changes
- added saving and loading current tuner configuration

* Thu Jan 29 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.3-alt1
- changed size bar width
- fixed page skipping on small screens

* Thu Jan 22 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.2-alt1
- added more icons

* Tue Jan 13 2026 Alexander Davydzik <paladindev@altlinux.org> 0.6.1-alt1
- added import & export config
- fixed subpage building
- added api version to library

* Fri Dec 05 2025 Alexander Davydzik <paladindev@altlinux.org> 0.6.0-alt1
- updated translations
- new plugin api features

* Tue Aug 12 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1.1
- specified versions of gir() build dependencies

* Thu Jul 03 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.1-alt1
- fixed warning in terminal output if no plugins loaded

* Thu Jul 03 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.0-alt1
- new plugin api features

* Thu Jun 26 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.1-alt1
- show plugins list button when all plugins disabled (Closes: 54933)
- translations improvements

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.0-alt1
- new plugins api features
- added plugins list dialog

* Mon May 26 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.6-alt1
- fixed segfault
- improved adaptivity

* Fri May 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.5-alt1
- improved translations
- changed app icon
- updated metadata (Closes: 54409)
- fixed reset button behaviour at some places (Closes: 54413)
- updated plugin loading order (Closes: 54427)
- added more info about installed plugins

* Mon May 19 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.4-alt1
- improved no plugins page
- improved translations
- added plugins list reloading
- added metainfo

* Wed May 14 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.3-alt1
- added python plugin support
- display loaded plugins at credits section

* Tue May 13 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.2-alt1
- added conflicts warnings
- added more methods to PanelPage

* Mon May 12 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt1
- fixed opening panels at mobile layout
- added panels sorting

* Wed Apr 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.0-alt1
- initial build
