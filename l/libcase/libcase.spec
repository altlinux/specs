# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libcase to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define girname Case
%define soversion 0

Name: libcase
Version: %soversion.2
Release: alt3

Summary: Library with various useful widgets for your application
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

%package -n %name%soversion
Summary: Library with various useful widgets for your application
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
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -n %name%soversion -f %name.lang
%_libdir/%name-%soversion.so.*

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
* Wed Aug 19 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt3
- Dropped demo.
- Don't use Gtk.Svg.

* Thu Aug 06 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt2
- Fixed summary.

* Thu Jul 30 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt1
- ComboRow: Added navigation-sidebar style to nested ListView.
- ComboRow: Added sheet-title property.
- Added InfinityCarousel.
- Full release notes:
  https://altlinux.space/rirusha/libcase/releases/tag/v0.2.

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
