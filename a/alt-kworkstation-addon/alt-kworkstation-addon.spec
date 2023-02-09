
Name: alt-kworkstation-addon
Version: 10.1
Release: alt1

Group: System/Configuration/Other
Summary: Additional requires for ALT Workstation K
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

Requires: systemd-ssh-agent

BuildArch: noarch

#BuildRequires(pre): rpm-build-ubt

%description
%{summary}.

%prep

%files

%changelog
* Thu Feb 09 2023 Sergey V Turchin <zerg@altlinux.org> 10.1-alt1
- update requires
- bump version to match distro

* Fri Jun 03 2022 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- update requires

* Mon Jun 15 2020 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- update requires

* Mon Jun 08 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- update requires

* Thu Jan 30 2020 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
