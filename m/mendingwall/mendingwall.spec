%define _unpackaged_files_terminate_build 1

Name: mendingwall
Version: 0.3.6
Release: alt1
Summary: Linux distributions offer a choice of desktop environment, but installing more than one can break themes and clutter menus. 
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/lawmurray/mendingwall

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: blueprint-compiler
BuildRequires: libgtk4-devel
BuildRequires: meson
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: libadwaita-devel
BuildRequires: appstream
BuildRequires: desktop-file-utils

%description
Mending Wall is a Linux application to fix issues when hopping between
multiple desktop environments, such as tiny/huge cursors,
tiny/huge fonts, light/dark mode switches and scaling issues.
It also tidies application menus, showing core applications in their
native environment only.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%doc *.md
%_bindir/%name
%_bindir/mendingwallcli
%_bindir/mendingwalld
%_datadir/dbus-1/services/*
%_datadir/%name
%_datadir/glib-2.0/schemas/org.indii.mendingwall.gschema.xml
%_datadir/applications/org.indii.mendingwall.desktop
%_datadir/icons/hicolor/scalable/apps/org.indii.mendingwall.svg
%_datadir/icons/hicolor/symbolic/apps/org.indii.mendingwall-symbolic.svg
%_datadir/metainfo/org.indii.mendingwall.metainfo.xml

%changelog
* Fri Oct 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus
