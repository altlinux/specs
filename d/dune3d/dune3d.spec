%define _unpackaged_files_terminate_build 1
%define app_id org.dune3d.dune3d

Name: dune3d
Version: 1.3.0
Release: alt1

Summary: 3D CAD application
License: GPL-3.0-or-later
Group: Graphics

Url: https://dune3d.org
Vcs: https://github.com/dune3d/dune3d
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ cmake
BuildRequires: libglm-devel
BuildRequires: opencascade-devel
BuildRequires: libglm-devel
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-pycairo-devel
BuildRequires: gir(Rsvg)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(uuid)

%description
Dune 3D is a parametric 3D CAD application that supports STEP import/export,
fillets and chamfers.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%doc README.md

%changelog
* Mon Mar 31 2025 Alexander Davydzik <paladindev@altlinux.org> 1.3.0-alt1
- initial build
