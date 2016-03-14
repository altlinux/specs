
Name: kde5-virtual
Version: 5.0.0
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
%description -n kde5-network-manager-0-dummy
%summary

%package -n kde5-network-manager-2-etcnet
Group: Graphical desktop/KDE
Summary: /etc/net network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-etcnet = %EVR
Requires: etcnet alterator-net-wifi alterator-net-l2tp alterator-net-openvpn alterator-net-pppoe alterator-net-pptp
%description -n kde5-network-manager-2-etcnet
%summary

%package -n kde5-network-manager-4-nm
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-nm = %EVR
Requires: kf5-plasma-nm-maxi
%description -n kde5-network-manager-4-nm
%summary

%files -n kde5-network-manager-0-dummy
%files -n kde5-network-manager-2-etcnet
%files -n kde5-network-manager-4-nm

%changelog
* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
