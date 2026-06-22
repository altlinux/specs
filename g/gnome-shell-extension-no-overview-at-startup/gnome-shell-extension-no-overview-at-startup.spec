%define _name no-overview
%define uuid %_name@fthx

Name: gnome-shell-extension-%_name-at-startup
Version: 49
Release: alt3

Summary: No overview at start-up. For GNOME Shell 40+
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/fthx/no-overview

BuildArch: noarch

# Source-url: https://github.com/fthx/no-overview/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch0: late-hide-overview.patch

Requires: gnome-shell >= 48
Requires: typelib(Adw) = 1

%description
No overview at start-up. For GNOME Shell.

%prep
%setup
%patch0 -p1

%build

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -ar *.js* %buildroot%_datadir/gnome-shell/extensions/%uuid/

%files
%_datadir/gnome-shell/extensions/%uuid/

%changelog
* Mon Jun 22 2026 Dmitry Udalov <udalov@altlinux.org> 49-alt3
- hide overview when extension is enabled after startup

* Sun Mar 22 2026 Anton Midyukov <antohami@altlinux.org> 49-alt2
- metadata.json: add gnome 50 support

* Mon Nov 03 2025 Roman Alifanov <ximper@altlinux.org> 49-alt1
- new version 49 (with rpmrb script)

* Sun Mar 16 2025 Roman Alifanov <ximper@altlinux.org> 48-alt1
- new version 48 (with rpmrb script)

* Sat Sep 21 2024 Roman Alifanov <ximper@altlinux.org> 47-alt1
- new version 47 (with rpmrb script)

* Fri Mar 22 2024 Roman Alifanov <ximper@altlinux.org> 45-alt2
- manually temporarily added version 46 to metadata.json

* Thu Sep 21 2023 Roman Alifanov <ximper@altlinux.org> 45-alt1
- new version 45 (with rpmrb script)

* Wed Aug 16 2023 Roman Alifanov <ximper@altlinux.org> 44-alt1
- Initial build for Sisyphus.
