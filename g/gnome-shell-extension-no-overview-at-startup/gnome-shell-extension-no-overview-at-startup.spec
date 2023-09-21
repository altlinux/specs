%define _name no-overview
%define uuid %_name@fthx

Name: gnome-shell-extension-%_name-at-startup
Version: 45
Release: alt1

Summary: No overview at start-up. For GNOME Shell 40+
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/fthx/no-overview

BuildArch: noarch

# Source-url: https://github.com/fthx/no-overview/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1

%description
No overview at start-up. For GNOME Shell 45+.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -ar *.js* %buildroot%_datadir/gnome-shell/extensions/%uuid/

%files
%_datadir/gnome-shell/extensions/%uuid/

%changelog
* Thu Sep 21 2023 Roman Alifanov <ximper@altlinux.org> 45-alt1
- new version 45 (with rpmrb script)

* Wed Aug 16 2023 Roman Alifanov <ximper@altlinux.org> 44-alt1
- Initial build for Sisyphus.