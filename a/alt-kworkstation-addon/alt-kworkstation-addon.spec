
Name: alt-kworkstation-addon
Version: 11.1.0
Release: alt1

Group: System/Configuration/Other
Summary: Additional requires for ALT Workstation K
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

BuildArch: noarch

Requires: theme-kworkstation
Requires: polkit-rule-packagekit-allow-install

%description
%{summary}.

%files

%changelog
* Mon Jul 21 2025 Sergey V Turchin <zerg@altlinux.org> 11.1.0-alt1
- require polkit-rule-packagekit-allow-install

* Mon Dec 23 2024 Sergey V Turchin <zerg@altlinux.org> 11.0.1-alt1
- update requires

* Thu Dec 05 2024 Sergey V Turchin <zerg@altlinux.org> 11.0-alt1
- update requires

* Mon Apr 01 2024 Sergey V Turchin <zerg@altlinux.org> 10.2-alt1
- clean requires

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
