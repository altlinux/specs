%define _name hide-activities-button
%define uuid Hide_Activities@shay.shayel.org

Name: gnome-shell-extension-%_name
Version: 45
Release: alt1

Summary: Hides the Activities button from the status bar
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/zeten30/HideActivities

BuildArch: noarch

# Source-url: https://github.com/zeten30/HideActivities/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1

%description
Hides the Activities button from the status bar (the hot corner and keyboard shortcut keeps working).

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -ar *.js* %buildroot%_datadir/gnome-shell/extensions/%uuid/

%files
%_datadir/gnome-shell/extensions/%uuid/

%changelog
* Wed Sep 20 2023 Roman Alifanov <ximper@altlinux.org> 45-alt1
- new version 45 (with rpmrb script)

* Wed Aug 16 2023 Roman Alifanov <ximper@altlinux.org> 44-alt1
- Initial build for Sisyphus.