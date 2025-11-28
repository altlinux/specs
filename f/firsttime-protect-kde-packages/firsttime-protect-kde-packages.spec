Name: firsttime-protect-kde-packages
Version: 0.1.1
Release: alt1

Group: System/Configuration/Other
Summary: Protect KDE packages from removing
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

BuildArch: noarch

Source: %name-%version.tar

%description
Protect KDE packages from removing by broken updates.

%prep
%setup

%build

%install
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -pm755 *.sh %buildroot/%_sysconfdir/firsttime.d/

%files
%_sysconfdir/firsttime.d/*

%changelog
* Fri Nov 28 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- fix script startup

* Fri Nov 28 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
