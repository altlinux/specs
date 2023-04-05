Name: lnk-url-open-caja
Version: 0.1.1
Release: alt1

Group: Text tools
Summary: Utility to open URLs from LNK files in Mate file manager
Url: https://git.altlinux.org/gears/l/lnk-url-open
License: GPL-2.0-or-later

Requires: /usr/bin/lnkinfo
Requires: mate-file-manager
Requires: kf5-kcoreaddons-common

BuildArch: noarch

Source: lnk-url-open-%version.tar

BuildRequires: desktop-file-utils

Conflicts: lnk-url-open

%description
%{summary}.

%prep
%setup -n lnk-url-open-%version

%install
mkdir -p %buildroot/{%_bindir,%_desktopdir}
install -m 0755 lnk-url-open %buildroot/%_bindir/
install -m 0644 lnk-url-open.desktop %buildroot/%_desktopdir/

%files
%_bindir/lnk-url-open
%_desktopdir/lnk-url-open.desktop

%changelog
* Wed Apr 05 2023 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Fork from lnk-url-open and adapt for caja.

* Tue Mar 28 2023 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- initial build
