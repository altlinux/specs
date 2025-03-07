%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Foldy
%define service_name org.altlinux.FoldyService
%define gir_name Foldy
%define glib_min_version 2.76
%define api_version 3
%define minor_version 6

Name: foldy
Version: 3.6
Release: alt1

Summary: Folder manager aimed to mobile devices
License: GPL-3.0-or-later
Group: Other
Url: https://github.com/alt-gnome/Foldy
Vcs: https://github.com/alt-gnome/Foldy.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: lib%name-%api_version = %EVR
Requires: %name-service = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-vala rpm-build-gir rpm-build-xdg
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libadwaita-1) >= 1.6
BuildRequires: pkgconfig(gio-unix-2.0) >= %glib_min_version
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: vapi(gee-0.8)
BuildRequires: gir(Gee) = 0.8
BuildRequires: blueprint-compiler
BuildRequires: gobject-introspection-devel
%{?_enable_check:BuildRequires: appstream desktop-file-utils}

%description
%summary.

%package service
Summary: Service for categories fix in GNOME and phosh
Group: Other

Requires: lib%name-%api_version = %EVR

%description service
%summary.

%package -n lib%name-%api_version
Summary: Foldy library
Group: System/Libraries

%description -n lib%name-%api_version
%summary.

%package -n lib%name-%api_version-devel
Summary: Foldy devel files
Group: Development/C

Requires: lib%name-%api_version = %EVR

%description -n lib%name-%api_version-devel
%summary.

%package -n lib%name-%api_version-devel-vala
Summary: Foldy devel files for vala
Group: Development/Other

BuildArch: noarch
Requires: lib%name-%api_version-devel = %EVR

%description -n lib%name-%api_version-devel-vala
%summary.

%package -n lib%name-%api_version-gir
Summary: Foldy typelib files
Group: System/Libraries

Requires: lib%name-%api_version = %EVR

%description -n lib%name-%api_version-gir
%summary.

%package -n lib%name-%api_version-gir-devel
Summary: Foldy devel gir files
Group: Development/Other

BuildArch: noarch
Requires: lib%name-%api_version-gir = %EVR

%description -n lib%name-%api_version-gir-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
export AS_VALIDATE_NONET="true"
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/*.svg
%doc README.md

%files service
%_bindir/%service_name
%_datadir/dbus-1/services/%service_name.service
%_desktopdir/%service_name.desktop
%_xdgconfigdir/autostart/%service_name.desktop

%files -n lib%name-%api_version
%_libdir/lib%name-%api_version.so.*

%files -n lib%name-%api_version-devel
%_libdir/lib%name-%api_version.so
%_pkgconfigdir/lib%name-%api_version.pc
%_includedir/lib%name-%api_version.h

%files -n lib%name-%api_version-devel-vala
%_vapidir/lib%name-%api_version.deps
%_vapidir/lib%name-%api_version.vapi

%files -n lib%name-%api_version-gir
%_typelibdir/%gir_name-%api_version.typelib

%files -n lib%name-%api_version-gir-devel
%_girdir/%gir_name-%api_version.gir

%changelog
* Tue Mar 04 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.6-alt1
- New version: 3.6

* Fri Feb 21 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.5-alt1
- New version: 3.5

* Wed Feb 12 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.4-alt1
- New version: 3.4

* Tue Feb 11 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.3-alt1
- New version: 3.3

* Tue Feb 11 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.2-alt1
- Initial build.

