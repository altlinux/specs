
Name: alt-kworkstation-addon
Version: 1.1
Release: alt1

Group: System/Configuration/Other
Summary: Additional requires for ALT Workstation K
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

Requires: alterator-zram-swap system-config-printer-lib

BuildArch: noarch

#BuildRequires(pre): rpm-build-ubt

%description
%{summary}.

%prep

%files

%changelog
* Mon Jun 08 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- update requires

* Thu Jan 30 2020 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
