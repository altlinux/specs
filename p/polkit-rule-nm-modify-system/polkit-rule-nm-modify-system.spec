Name: polkit-rule-nm-modify-system
Version: 1.0
Release: alt1

Group: System/Configuration/Other
Summary: Polkit rule to allow wheel and netadmin users modify NetworkManager system connections
URL: http://altlinux.org
License: GPL-3.0

BuildArch: noarch

Source: nm-modify-system.rules

%description
%{summary}.

%install
install -Dpm 0644 %SOURCE0 %buildroot/%_datadir/polkit-1/rules.d/org.freedesktop.NetworkManager.modify.system.rules

%files
%_datadir/polkit-1/rules.d/*.rules

%changelog
* Mon Sep 08 2025 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
