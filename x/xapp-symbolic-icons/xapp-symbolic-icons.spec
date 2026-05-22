%define _unpackaged_files_terminate_build 1

%def_without check

Name: xapp-symbolic-icons
Version: 1.1.0
Release: alt1

Summary: Set of symbolic icons for GTK applications and projects
License: LGPL-3.0-only
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
%doc AUTHORS README.md
%_bindir/xsi-replace-adwaita-symbolic
%_datadir/xapp/xsi-adwaita-symbolic.info
%_iconsdir/hicolor/scalable/actions/xsi-*.svg

%changelog
* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Sun Jan 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.9-alt1
- New version 1.0.9.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.8-alt1
- New version 1.0.8.

* Fri Dec 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.7-alt1
- New version 1.0.7.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.6-alt1
- New version 1.0.6.

* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
