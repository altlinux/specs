%define _unpackaged_files_terminate_build 1

%def_with check

Name: mate-redshift
Version: 1.0.0
Release: alt1

Summary: Night light settings dialog fo MATE Desktop
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/mate-redshift

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)

Requires: rojo
Requires: /usr/bin/redshift-gtk

%description
A Night Light settings dialog for MATE that configures and controls
redshift-gtk. It appears in MATE Control Center (Personal) and does
not add a tray icon of its own: the tray icon is still plain redshift-gtk.

%prep
%setup
sed -i "s|plain redshift-gtk.|plain redshift-gtk:\n\n![](screenshot.png)|" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc README.md screenshot.png
%_bindir/mate-redshift
%_desktopdir/mate-redshift.desktop

%changelog
* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
