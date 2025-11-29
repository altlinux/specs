%define _unpackaged_files_terminate_build 1

%def_without check

Name: xapp-symbolic-icons
Version: 1.0.5
Release: alt1

Summary: Set of symbolic icons for GTK applications and projects
License: GPL-3.0-only AND LGPL-3.0-only
Group: Graphics
URL: https://github.com/xapp-project/xapp-symbolic-icons

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: meson

Requires: hicolor-icon-theme

BuildArch: noarch

Source: %name-%version.tar

%description
A set of symbolic icons which replaces the GNOME-specific Adwaita set.
All provided icons are prefixed with xsi- and places in /usr/share/icons/hicolor.
Icon names losely follow the Adwaita names.
To search/replace Adwaita icon names in your code, run:

xsi-replace-adwaita-symbolic

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc AUTHORS ChangeLog COPYING COPYING.LESSER README.md
%_bindir/xsi-replace-adwaita-symbolic
%_datadir/xapp/xsi-adwaita-symbolic.info
%_iconsdir/hicolor/scalable/actions/xsi-*.svg

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
