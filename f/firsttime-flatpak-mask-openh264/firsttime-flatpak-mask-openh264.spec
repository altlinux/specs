Name: firsttime-flatpak-mask-openh264
Version: 0.2.0
Release: alt1

Group: System/Configuration/Other
Summary: Setup Flatpack against openh264
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

BuildArch: noarch

Source: %name-%version.tar

%description
Setup Flatpack against unavailable openh264.

%prep
%setup

%build

%install
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -pm755 *.sh %buildroot/%_sysconfdir/firsttime.d/

%files
%_sysconfdir/firsttime.d/*

%changelog
* Thu Oct 02 2025 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- don't require flatpak

* Wed Oct 01 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
