
Name: kde5-virtual
Version: 5.1.0
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

%files -n kde5-network-manager-0-dummy
%files -n kde5-network-manager-2-etcnet
%files -n kde5-network-manager-4-nm

%files -n kde5-video-player-2-dragon
%files -n kde5-video-player-4-smplayer

%changelog
* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add kde5-video-player

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- fix requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
