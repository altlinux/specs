Name: systemd-presets-kdesktop
Version: 1.1
Release: alt1

Group: System/Configuration/Boot and Init
Summary: Systemd services preset
Url: http://altlinux.org/
License: GPLv2+

BuildArch: noarch

Source: kdesktop.preset

%description
Systemd services preset

%prep

%install
mkdir -p %buildroot/%_presetdir
install -m 0644 %SOURCE0 %buildroot/%_presetdir/50-kdesktop.preset

%files
%_presetdir/*.preset

%changelog
* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- enable crond

* Thu Mar 14 2013 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
