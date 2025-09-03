# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-gnome/Foldy to altlinux branch

%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Foldy
%define service_name org.altlinux.FoldyService
%define gir_name Foldy
%define glib_min_version 2.76
%define api_version 5
%define minor_version 0

Name: foldy
Version: %api_version.%minor_version
Release: alt1

Summary: Folder manager aimed to mobile devices
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.space/alt-gnome/Foldy
Vcs: https://altlinux.space/alt-gnome/Foldy.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name%api_version = %EVR
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
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: blueprint-compiler
BuildRequires: gobject-introspection-devel
BuildRequires: gettext-devel
%{?_enable_check:BuildRequires: appstream desktop-file-utils}

%description
%summary.

%package service
Summary: Service for categories fix in GNOME and phosh
Group: Other

Requires: lib%name%api_version = %EVR

%description service
%summary.

%package -n lib%name%api_version
Summary: Foldy library
Group: System/Libraries

%description -n lib%name%api_version
%summary.

%package -n lib%name-devel
Summary: Foldy devel files
Group: Development/C

Provides: lib%name-devel
Requires: lib%name%api_version = %EVR

%description -n lib%name-devel
%summary.

%package -n lib%name%api_version-gir
Summary: Foldy typelib files
Group: System/Libraries

Requires: lib%name%api_version = %EVR

%description -n lib%name%api_version-gir
%summary.

%package -n lib%name-gir-devel
Summary: Foldy devel gir files
Group: Development/Other

BuildArch: noarch
Requires: lib%name%api_version-gir = %EVR

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
%find_lang %service_name

%check
export AS_VALIDATE_NONET="true"
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/org.altlinux.Foldy.svg
%_iconsdir/hicolor/*/apps/org.altlinux.Foldy-symbolic.svg
%doc README.md

%files service -f %service_name.lang
%_bindir/%service_name
%_datadir/metainfo/%service_name.metainfo.xml
%_datadir/dbus-1/services/%service_name.service
%_desktopdir/%service_name.desktop
%_xdgconfigdir/autostart/%service_name.desktop
%_iconsdir/hicolor/*/apps/%service_name.svg
%_iconsdir/hicolor/*/apps/%service_name-symbolic.svg

%files -n lib%name%api_version
%_libdir/lib%name-%api_version.so.%api_version
%_libdir/lib%name-%api_version.so.%api_version.*

%files -n lib%name-devel
%_libdir/lib%name-%api_version.so
%_pkgconfigdir/lib%name-%api_version.pc
%_includedir/lib%name-%api_version.h
%_vapidir/lib%name-%api_version.deps
%_vapidir/lib%name-%api_version.vapi

%files -n lib%name%api_version-gir
%_typelibdir/%gir_name-%api_version.typelib

%files -n lib%name-gir-devel
%_girdir/%gir_name-%api_version.gir

%changelog
* Wed Sep 03 2025 Vladimir Vaskov <rirusha@altlinux.org> 5.0-alt1
- New version: 5.0.
- Fixed empty window on folder deletion (closes: 55479).

* Tue May 20 2025 Vladimir Vaskov <rirusha@altlinux.org> 4.2-alt1
- New version: 4.2.

* Thu May 08 2025 Vladimir Vaskov <rirusha@altlinux.org> 4.1-alt1
- New version: 4.1.

* Thu Apr 10 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.12-alt1
- New version: 3.12.
- Changed upstream remote URL and VCS.

* Mon Mar 24 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.8-alt1
- New version: 3.8.

* Tue Mar 04 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.6-alt1
- New version: 3.6.

* Fri Feb 21 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.5-alt1
- New version: 3.5.

* Wed Feb 12 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.4-alt1
- New version: 3.4.

* Tue Feb 11 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.3-alt1
- New version: 3.3.

* Tue Feb 11 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.2-alt1
- Initial build.
