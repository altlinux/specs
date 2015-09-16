
Name: kde5-set
Version: 5.0.0
Release: alt13

Group: Graphical desktop/KDE
Summary: Set of KDE 5 applications
License: Public Domain

BuildArch: noarch

%package -n kde5-runtime
Summary: %summary
Group: Graphical desktop/KDE
Requires: kf5-kio kf5-kded qt5-phonon-backend qt5-quickcontrols kf5-kwayland-integration

%package -n kde5-mini
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: qt5-dbus kf5-kwin kf5-kactivities kf5-plasma-desktop kf5-kinit kf5-kdeclarative
Requires: kde5-dolphin

%package -n kde5-small
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-mini
Requires: kde5-volume-control
Requires: kde5-www-browser
Requires: kf5-sddm-kcm kf5-polkit-kde-agent kf5-kio-extras kf5-breeze kf5-powerdevil kf5-ksysguard
Requires: kf5-kwallet kf5-kconfig kf5-kglobalaccel kf5-kimageformats kf5-kde-cli-tools
Requires: kde5-ark kde5-konsole kde5-gwenview kde5-kwrite
Requires: kde5-kdepasswd

%package -n kde5
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-normal = %EVR kde5-default = %EVR
Obsoletes: kde5-normal < %EVR kde5-default < %EVR
Requires: kde5-small
Requires: kde5-video-player
#Requires: kde5-audio-player
#Requires: pam0_kwallet5
Requires: kf5-kde-gtk-config kf5-baloo kf5-bluedevil kf5-kscreen kf5-ksshaskpass kf5-oxygen
Requires: kf5-systemsettings kf5-khelpcenter kf5-khotkeys kf5-kinfocenter kf5-kdeplasma-addons
Requires: kf5-kmenuedit kf5-solid kf5-kdbusaddons kde5-kwalletmanager
Requires: kde5-kfind

%package -n kde5-big
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5
Requires: kf5-kwrited kf5-milou kf5-plasma-nm-maxi
Requires: kf5-user-manager
Requires: kde5-konversation kde5-kate kde5-print-manager
Requires: kde5-pim kde5-baseapps

%package -n kde5-maxi
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-big
#Requires: kde5-telepathy

%description
%summary
%description -n kde5-runtime
%summary
%description -n kde5-mini
%summary
%description -n kde5-small
%summary
%description -n kde5
%summary
%description -n kde5-big
%summary
%description -n kde5-maxi
%summary

%files -n kde5-runtime
%files -n kde5-mini
%files -n kde5-small
%files -n kde5
%files -n kde5-big
%files -n kde5-maxi

%changelog
* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt13
- update requires

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt12
- update requires

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt11
- clean requires

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt10
- update requires

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt9
- update requires

* Thu Aug 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt8
- update requires

* Wed Aug 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt7
- update requires

* Wed Jul 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt6
- update requires

* Wed Apr 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt5
- update requires

* Mon Apr 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt4
- update requires

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt3
- update requires

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt2
- update requires

* Mon Apr 20 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
