
Name: kde5-set
Version: 5.0.0
Release: alt27

Group: Graphical desktop/KDE
Summary: Set of KDE 5 applications
License: Public Domain

BuildArch: noarch

%package -n kde5-runtime
Summary: %summary
Group: Graphical desktop/KDE
Requires: qt5-phonon-backend qt5-quickcontrols qt5-graphicaleffects qt5-imageformats
Requires: kf5-kio kf5-kded kf5-kwayland-integration

%package -n kde5-mini
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: qt5-dbus kf5-kwin kf5-plasma-desktop kf5-kinit kf5-kdeclarative
Requires: kde5-dolphin

%package -n kde5-small
Summary: %summary
Group: Graphical desktop/KDE
Requires: icon-theme-breeze
Requires: kde5-mini
Requires: kde5-volume-control
Requires: kde5-www-browser
Requires: kf5-sddm-kcm kf5-polkit-kde-agent kf5-kio-extras kf5-breeze kf5-powerdevil kf5-ksysguard
Requires: kf5-kwallet kf5-kconfig kf5-kglobalaccel kf5-kimageformats kf5-kde-cli-tools
Requires: kde5-ark kde5-konsole kde5-gwenview kde5-okular kde5-kwrite kde5-kwalletmanager
Requires: kde5-kdepasswd kde5-kcalc kde5-kdebugsettings kde5-kross-python
Requires: kf5-milou

%package -n kde5
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-normal = %EVR kde5-default = %EVR
Obsoletes: kde5-normal < %EVR kde5-default < %EVR
#Requires: pam0_kwallet5
Requires: kde5-small
Requires: kde5-video-player
#Requires: kde5-audio-player
Requires: kde5-network-manager
Requires: kf5-kde-gtk-config kf5-baloo kf5-bluedevil kf5-kscreen kf5-ksshaskpass kf5-oxygen
Requires: kf5-systemsettings kf5-khelpcenter kf5-khotkeys kf5-kinfocenter kf5-kdeplasma-addons
Requires: kf5-kmenuedit kf5-solid kf5-kdbusaddons kf5-kgamma
Requires: kde5-kfind kde5-filelight kde5-kcharselect kde5-kteatime kde5-ktimer kde5-spectacle
Requires: kde5-kamera kde5-network-filesharing

%package -n kde5-big
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5
#Requires: kde5-telepathy
Requires: kf5-plasma-workspace-wallpapers
Requires: kf5-kwrited
Requires: kf5-user-manager
Requires: kde5-konversation kde5-kate kde5-print-manager kde5-skanlite
Requires: kde5-pim kde5-baseapps kde5-kcron kde5-kruler kde5-ffmpegthumbs
Requires: kf5-plasma-mediacenter kde5-krfb
Requires: kid3-ui-kde5 ring-client-kde5

%package -n kde5-maxi
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-big
Requires: kdenlive
Requires: kde5-konqueror kde5-dragon kde5-connect

%package -n kde5-somedevel
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-dolphin-plugins
Requires: kde5-lokalize kde5-okteta kde5-kapptemplate kde5-dev-scripts kde5-kompare
Requires: kde5-sdk-thumbnailers kde5-poxml kde5-umbrello

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
%description -n kde5-somedevel
%summary

%files -n kde5-runtime
%files -n kde5-mini
%files -n kde5-small
%files -n kde5
%files -n kde5-big
%files -n kde5-maxi
%files -n kde5-somedevel

%changelog
* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt27
- update requires

* Wed Mar 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt26
- update requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt25
- update requires

* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt24
- update requires

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt23
- update requires

* Fri Jan 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt22
- update requires

* Tue Jan 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt21
- update requires

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt20
- update requires

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt19
- fix requires

* Tue Nov 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt18
- update requires

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt17
- update requires

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt16
- update requires

* Fri Oct 02 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt15
- move development tools to separate package

* Thu Oct 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt14
- update requires

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
