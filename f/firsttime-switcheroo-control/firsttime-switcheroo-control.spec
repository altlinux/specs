Name: firsttime-switcheroo-control
Version: 0.1.0
Release: alt1

Group: System/Configuration/Other
Summary: Enable switcheroo-control service
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

BuildArch: noarch

Source: %name-%version.tar

%description
Enable switcheroo-control service when needed.

%prep
%setup

%build

%install
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -pm755 *.sh %buildroot/%_sysconfdir/firsttime.d/

%files
%_sysconfdir/firsttime.d/*

%changelog
* Fri Feb 20 2026 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
