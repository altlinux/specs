Name: lnk-url-open
Version: 0.1.0
Release: alt1

Group: Text tools
Summary: Utility to open URLs from LNK files
Url: https://git.altlinux.org/gears/l/lnk-url-open
License: GPL-2.0-or-later

Requires: /usr/bin/lnkinfo /usr/bin/xdg-open

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: desktop-file-utils

%description
%{summary}.

%prep
%setup

%install
mkdir -p %buildroot/{%_bindir,%_desktopdir}
install -m 0755 lnk-url-open %buildroot/%_bindir/
install -m 0644 lnk-url-open.desktop %buildroot/%_desktopdir/

%files
%_bindir/lnk-url-open
%_desktopdir/lnk-url-open.desktop

%changelog
* Tue Mar 28 2023 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- initial build
