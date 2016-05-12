
Name: kde5-virtual
Version: 5.3.1
Release: alt1

Group: Graphical desktop/KDE
Summary: Virtual packages for KDE 5
License: Public Domain

BuildArch: noarch

%description
%summary

%package -n kde5-network-manager-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-network-manager-0-dummy
%summary

%package -n kde5-network-manager-2-etcnet
Group: Graphical desktop/KDE
Summary: /etc/net network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-etcnet = %EVR
Requires: kf5-filesystem
Requires: etcnet alterator-net-wifi alterator-net-openvpn alterator-net-pppoe alterator-net-pptp alterator-net-l2tp
%description -n kde5-network-manager-2-etcnet
%summary

%package -n kde5-network-manager-4-nm
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-nm = %EVR
Requires: kf5-filesystem
Requires: kf5-plasma-nm-maxi
%description -n kde5-network-manager-4-nm
%summary

%package -n kde5-video-player-2-dragon
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-dragon = %EVR
Requires: kf5-filesystem
Requires: kde5-dragon
%description -n kde5-video-player-2-dragon
%summary

%package -n kde5-video-player-4-smplayer
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-smplayer = %EVR
Requires: kf5-filesystem
Requires: kde5-smplayer
%description -n kde5-video-player-4-smplayer
%summary

%package -n kde5-volume-control-2-kmix
Group: Graphical desktop/KDE
Summary: KMix volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-kmix = %EVR
Requires: kf5-filesystem
Requires: kde5-kmix
%description -n kde5-volume-control-2-kmix
%summary

%package -n kde5-volume-control-4-plasmapulse
Group: Graphical desktop/KDE
Summary: Plasma applet volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-plasmapulse = %EVR
Requires: kf5-filesystem
Requires: kf5-plasma-pa
%description -n kde5-volume-control-4-plasmapulse
%summary

%package -n kde5-email-client-2-kmail
Group: Graphical desktop/KDE
Summary: KMail email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-kmail = %EVR
Requires: kf5-filesystem
Requires: kde5-pim-kmail kde5-pim-addons-kmail kde5-pim-addons-plugins
%description -n kde5-email-client-2-kmail
%summary

%package -n kde5-email-client-4-thunderbird
Group: Graphical desktop/KDE
Summary: Thunderbird email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-thunderbird = %EVR
Requires: kf5-filesystem
Requires: thunderbird thunderbird-ru
%description -n kde5-email-client-4-thunderbird
%summary

%package -n kde5-audio-player-4-qmmp
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-audio-player = %EVR
Provides: kde5-audio-player-qmmp = %EVR
Requires: kf5-filesystem
Requires: qmmp1
%description -n kde5-audio-player-4-qmmp
%summary

%files -n kde5-network-manager-0-dummy
%files -n kde5-network-manager-2-etcnet
%files -n kde5-network-manager-4-nm

%files -n kde5-video-player-2-dragon
%files -n kde5-video-player-4-smplayer

%files -n kde5-volume-control-2-kmix
%files -n kde5-volume-control-4-plasmapulse

%files -n kde5-email-client-2-kmail
%files -n kde5-email-client-4-thunderbird

%files -n kde5-audio-player-4-qmmp

%changelog
* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- update requires

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- add kde5-audio-player

* Fri Apr 22 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- add kde5-volume-control and kde5-email-client

* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add kde5-video-player

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- fix requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
