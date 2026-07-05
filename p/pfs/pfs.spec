%def_enable snapshot

%define _name pfs
%define libname lib%_name
# package `libpfs' version `0.0.2-alt0.5' is less than its version `2.2.0-alt2' in `p10'
# from pfstools
%define pkg_libname libphosh-file-selector
%define ver_major 0.1
%define beta %nil
%define api_ver 0
%define namespace Pfs
%define xdg_name mobi.phosh.FileSelector
%define xdg_name1 mobi.phosh.FileOpen

%def_disable introspection
%def_disable docs
%def_enable examples
%def_enable check

%def_disable bootstrap

Name: %_name
Version: %ver_major.1
Release: alt1%beta

Summary: Phosh File Selector Library
Group: System/Libraries
License: LGPL-3.0-or-later
Url: https://gitlab.gnome.org/World/Phosh/pfs

Vcs: https://gitlab.gnome.org/World/Phosh/pfs.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Phosh/pfs/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %_name-%version-cargo.tar

%define meson_ver 1.0
%define glib_ver 2.70
%define gtk_ver 4.14
%define adwaita_ver 1.4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver rust-cargo patchelf
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_examples:BuildRequires: pkgconfig(libsystemd)}

%description
A widget for selecting files for Phosh.

%package -n %pkg_libname
Summary: %summary
Group: System/Libraries

%description -n %pkg_libname
This package provides shared Phosh File Selector library.

%package -n %pkg_libname-devel
Summary: Development files for %name
Group: Development/C
Requires: %pkg_libname = %EVR

%description -n %pkg_libname-devel
The %libname-devel package contains libraries and header files for
developing applications that use Phosh File Selector library.

%package -n %pkg_libname-gir
Summary: GObject introspection data for %_name
Group: System/Libraries
Requires: %pkg_libname = %EVR

%description -n %pkg_libname-gir
GObject introspection data for the %_name library.

%package -n %pkg_libname-gir-devel
Summary: GObject introspection devel data for %_name
Group: Development/Other
BuildArch: noarch
Requires: %pkg_libname-gir = %EVR
Requires: %pkg_libname-devel = %EVR

%description -n %pkg_libname-gir-devel
GObject introspection devel data for the Phosh File Selector library.

%package -n %pkg_libname-devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %pkg_libname < %EVR

%description -n %pkg_libname-devel-doc
This package contains development documentation for Phosh File Selector library.

%package demo
Summary: %_name widget demonstration program
Group: Development/GNOME and GTK+
Requires: %pkg_libname = %EVR

%description demo
This package contains a program that demonstrates Phosh File Selector.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' >> .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson \
    -Dshared-lib=true \
    %{subst_enable_meson_bool examples examples}
%nil
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -n %pkg_libname -f %_name.lang
%_libdir/%libname-%api_ver.so
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README* NEWS

%files -n %pkg_libname-devel
%_includedir/%_name-%api_ver/
#%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%libname-%api_ver.pc

%if_enabled introspection
%files -n %pkg_libname-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n %pkg_libname-gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled docs
%files -n %pkg_libname-devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%if_enabled examples
%files demo
%_bindir/%_name-open
%_bindir/%_name-demo
%_desktopdir/%{xdg_name}Demo.desktop
%_desktopdir/%xdg_name1.desktop
%_userunitdir/%xdg_name1.service
%_datadir/dbus-1/services/%xdg_name1.service
%_iconsdir/hicolor/*/apps/%{xdg_name1}*.svg
%_iconsdir/hicolor/*/apps/%{xdg_name}Demo*.svg
%endif

%changelog
* Sun Jun 28 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Thu May 14 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Mon Mar 30 2026 Yuri N. Sedunov <aris@altlinux.org> 0.0.8-alt1
- 0.0.8

* Sun Feb 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.0.7-alt1
- 0.0.7

* Sun Nov 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.5-alt2
- updated to v0.0.5-4-gd007e73 for 0.51.0

* Mon Sep 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.5-alt1
- 0.0.5

* Tue Jun 24 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.4-alt1
- 0.0.4

* Fri May 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1.1
- moved pfs-open to -demo subpackage (ALT #54550)

* Sun May 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- 0.0.3

* Tue Apr 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt0.5
- first build for Sisyphus

