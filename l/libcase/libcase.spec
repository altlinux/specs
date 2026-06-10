# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libcase to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define app_id_demo space.rirusha.CaseDemo
%define girname Case
%define soversion 0

Name: libcase
Version: %soversion.1
Release: alt1

Summary: Unofficial Yandex Music client (Devel build)
License: GPL-3.0-or-later
Group: Sound
URL: https://altlinux.space/rirusha/libcase
VCS: https://altlinux.space/rirusha/libcase.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-vala
BuildRequires: rpm-build-gir
BuildRequires: meson
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel
BuildRequires: blueprint-compiler
BuildRequires: gir(Adw) = 1
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: gettext-devel

%description
%summary.

%package demo
Summary: %name demo application
Group: Other

%description demo
%summary.

%package -n %name%soversion
Summary: Base objects for API libraries
Group: Development/C

%description -n %name%soversion
%summary.

%package devel
Summary: Development files for %name
Group: Development/C

Requires: %name%soversion = %EVR

%description devel
%summary.

%package -n %name%soversion-gir
Summary: Typelib files for %name
Group: System/Libraries

Requires: %name%soversion = %EVR

%description -n %name%soversion-gir
%summary.

%package gir-devel
Summary: Development gir files for %name for various bindings
Group: Development/Other
BuildArch: noarch

Requires: %name%soversion-gir = %EVR

%description gir-devel
%summary.

%prep
%setup

%build
%meson -Dwith_demo=true
%meson_build

%install
%meson_install
%find_lang %name
%find_lang %name-demo

%check
%meson_test

%files -n %name%soversion -f %name.lang
%_libdir/%name-%soversion.so.*

%files demo -f %name-demo.lang
%_bindir/%name-demo
%_datadir/metainfo/%app_id_demo.metainfo.xml
%_desktopdir/%app_id_demo.desktop
%_iconsdir/hicolor/*/apps/%app_id_demo.svg
%_iconsdir/hicolor/*/apps/%app_id_demo-symbolic.svg

%files devel
%_libdir/%name-%soversion.so
%_includedir/%name-%soversion.h
%_pkgconfigdir/%name-%soversion.pc
%_vapidir/%name-%soversion.vapi
%_vapidir/%name-%soversion.deps

%files -n %name%soversion-gir
%_typelibdir/%girname-%soversion.typelib

%files gir-devel
%_girdir/%girname-%soversion.gir

%changelog
* Mon Jun 08 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1-alt1
- Initial build: 0.1.
- Widgets:
  + ComboRow, combo row with adaptive popover
  + MenuButton, menu button with adaptive popover
  + ListView/GridView, list view/grid view with header/footer
  + Badge, private Badge from libadwaita
  + IndicatorBin, private IndicatorBin from libadwata
- Full release notes:
  https://altlinux.space/rirusha/libcase/releases/tag/v0.1.
