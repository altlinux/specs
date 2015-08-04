Name: kde5-telepathy
Version: 15.4.3
Release: alt2

Group: Graphical desktop/KDE
Summary: KDE Telepathy handler
Url: http://projects.kde.org/projects/extragear/network/telepathy/
License: GPLv2+

BuildArch: noarch

Requires: mjpegtools
#
Requires: telepathy-mission-control
Requires: telepathy-gabble
Requires: telepathy-haze
Requires: telepathy-idle
Requires: telepathy-rakia
Requires: telepathy-salut
#
Requires: kde5-ktp-accounts-kcm
Requires: kde5-ktp-approver
Requires: kde5-ktp-auth-handler
Requires: kde5-ktp-desktop-applets
Requires: kde5-ktp-contact-list
Requires: kde5-ktp-contact-runner
Requires: kde5-ktp-filetransfer-handler
Requires: kde5-ktp-kded-module
Requires: kde5-ktp-send-file
Requires: kde5-ktp-text-ui
#Requires: kde5-ktp-call-ui
#
Requires: kde5-signon-kwallet-extension
Requires: kde5-kaccounts-providers

%description
%summary

%files

%changelog
* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt2
- update requires

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
