Name: kde4-telepathy
Version: 4.8.4
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE Telepathy handler
Url: http://projects.kde.org/projects/extragear/network/telepathy/
License: GPLv2+

BuildArch: noarch

Requires: telepathy-mission-control
Requires: kde4-ktp-accounts-kcm kde4-ktp-approver
Requires: kde4-ktp-auth-handler
Requires: kde4-ktp-call-ui
Requires: kde4-ktp-contact-applet kde4-ktp-contact-list kde4-ktp-contact-runner
Requires: kde4-ktp-filetransfer-handler kde4-ktp-kded-integration-module
Requires: kde4-ktp-presence-applet kde4-ktp-send-file
Requires: kde4-ktp-text-ui

%description
%summary

%files

%changelog
* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- fix requires

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- initial build
