%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: kde-set
Version: 24.02.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Set of KDE applications
License: ALT-Public-Domain

BuildRequires(pre): rpm-macros-qt6-webengine

%description
%summary

%package -n kde5-runtime
Summary: %summary
Group: Graphical desktop/KDE
#Requires: qt5-phonon-backend
Requires: qt5-quickcontrols qt5-quickcontrols2 qt5-graphicaleffects qt5-imageformats qt5-translations qt5-wayland
Requires: kf5-kio
#Requires: kf5-kded kf5-kinit
Requires: plasma5-breeze plasma5-integration kwayland-integration
%description -n kde5-runtime
%summary

%package -n kde-runtime
Summary: %summary
Group: Graphical desktop/KDE
Requires: qt6-phonon-backend qt6-5compat qt6-declarative qt6-svg qt6-imageformats qt6-translations qt6-wayland
Requires: kf6-kio kf6-kded
Requires: plasma6-breeze plasma6-integration
%description -n kde-runtime
%summary

%package -n kde-mini
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-mini = %EVR
Obsoletes: kde5-mini < %EVR
Requires: kde-runtime
#
Requires: qt6-dbus kde-cli-tools kwin plasma-desktop kf6-kdeclarative
Requires: dolphin kdialog
%description -n kde-mini
%summary

%package -n kde-small
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-small = %EVR
Obsoletes: kde5-small < %EVR
Requires: kde-mini
Requires: kde-volume-control
Requires: kde-display-manager
%ifarch ppc64le
Requires: webclient
%else
Requires: /usr/bin/x-www-browser
%endif
#
Requires: icon-theme-breeze
Requires: kf6-kwallet kf6-kconfig kf6-kimageformats
Requires: svgpart
Requires: kf6-baloo
Requires: polkit-kde-agent kio-extras powerdevil plasma-systemmonitor
Requires: drkonqi milou systemsettings
Requires: ark konsole gwenview okular kwrite kwalletmanager
Requires: kcalc
%description -n kde-small
%summary

%package -n kde
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5 = %EVR
Obsoletes: kde5 < %EVR
Provides: kde-normal = %EVR kde-default = %EVR
Obsoletes: kde-normal < %EVR kde-default < %EVR
Requires: kde-small
Requires: kde-video-player
Requires: kde-audio-player
Requires: kde-network-manager
#
Requires: pam0_kwallet5
Requires: gtk3-theme-breeze
Requires: gtk2-theme-breeze
Requires: kf6-kguiaddons kf6-qqc2-desktop-style
Requires: plasma-applet-places-widget
Requires: oxygen-sounds
Requires: kde-gtk-config bluedevil kscreen ksshaskpass
Requires: kinfocenter kdeplasma-addons plasma-browser-integration
Requires: plasma-disks
%if_enabled qtwebengine
Requires: khelpcenter
%endif
Requires: kolourpaint kio-audiocd kgpg
Requires: kmenuedit kgamma plasma-thunderbolt
Requires: kfind filelight kcharselect kteatime spectacle
Requires: kamera kdenetwork-filesharing
Requires: kio-zeroconf sweeper
%description -n kde
%summary

%package -n kde-big
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-big = %EVR
Obsoletes: kde5-big < %EVR
Requires: kde
Requires: kde-pim
Requires: kde-email-client
Requires: kde-messenger-client
#
Requires: ktorrent
Requires: plasma6-oxygen
Requires: icon-theme-oxygen
Requires: plasma-workspace-wallpapers
Requires: kwrited
Requires: ksystemlog
Requires: krdc
Requires: kcron kruler ffmpegthumbs
Requires: kdeconnect
Requires: krfb
Requires: kdf
Requires: kid3-ui-kde
Requires: kdegraphics-thumbnailers
%description -n kde-big
%summary

%package -n kde-maxi
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-maxi = %EVR
Obsoletes: kde5-maxi < %EVR
Requires: kde-big
Requires: kde-edu
Requires: kde-games
Requires: kde-printing
Requires: kde-scanning
#
Requires: plasma-discover-maxi
Requires: keditbookmarks
Requires: ktimer
Requires: dragon
Requires: kmousetool kmag
Requires: juk kmouth
Requires: kdenlive
Requires: k3b kwave konversation
%if_enabled qtwebengine
Requires: digikam
%endif
Requires: kdebugsettings
%description -n kde-maxi
%summary

%package -n kde-somedevel
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-somedevel = %EVR
Obsoletes: kde5-somedevel < %EVR
Requires: kde-runtime
#
Requires: kate
Requires: dolphin-plugins
Requires: lokalize okteta kapptemplate kde-dev-scripts kompare
Requires: kdesdk-thumbnailers poxml umbrello
Requires: kcachegrind
%if_enabled qtwebengine
Requires: kimagemapeditor
%endif
%description -n kde-somedevel
%summary

%package -n kde-edu
Summary: Educational software based on the KDE technologies
Group: Graphical desktop/KDE
Provides: kde5-edu = %EVR
Obsoletes: kde5-edu < %EVR
Requires: kde-runtime
#
%if_enabled qtwebengine
Requires: parley
%endif
Requires: kanagram khangman
Requires: kwordquiz kturtle marble
Requires: step
%ifnarch armh
Requires: kde5-kstars
%endif
Requires: kig kmplot kalgebra cantor rocs
Requires: kbruch kgeography ktouch
Requires: minuet
%description -n kde-edu
Educational software based on the KDE technologies

%package -n kde-games
Summary: Set of KDE-based games
Group: Graphical desktop/KDE
Provides: kde5-games = %EVR
Obsoletes: kde5-games < %EVR
Requires: kde-runtime
#
Requires: lskat kmines kshisen ktuberling bovo knetwalk
Requires: katomic knavalbattle kpat kmahjongg
Requires: ksudoku kigo knights kreversi granatier
Requires: kolf ksirk palapeli
%description -n kde-games
High quality gaming and entertainment software.

%package -n kde-printing
Summary: Set of printing support applications
Group: Graphics
Provides: kde5-printing = %EVR
Obsoletes: kde5-printing < %EVR
Requires: kde-runtime
#
Requires: print-manager cups printer-drivers-X11
%description -n kde-printing
KDE printing support applications.

%package -n kde-scanning
Summary: Set of image scanning support applications
Group: Graphics
Provides: kde5-scanning = %EVR
Obsoletes: kde5-scanning < %EVR
Requires: kde-runtime
#
%if_enabled qtwebengine
Requires: skanpage
%else
Requires: skanlite
%endif
Requires: hplip-sane libsane-gphoto2 sane
%description -n kde-scanning
KDE image scanning support applications.

%package -n kde-pim
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-pim = %EVR
Obsoletes: kde5-pim < %EVR
Requires: kde-runtime
Requires: kde-email-client
#
%if_enabled qtwebengine
Requires: pim-data-exporter kdepim-addons
Requires: akregator kontact
Requires: korganizer zanshin
Requires: akonadi-calendar-tools
%endif
Requires: kalarm
# dead knotes
Requires: kaddressbook
# akonadi based email client
#Requires: akonadi-import-wizard mbox-importer pim-sieve-editor mbox-importer pim-sieve-editor grantlee-editor
%description -n kde-pim
%summary


%files -n kde5-runtime
%files -n kde-runtime
%files -n kde-mini
%files -n kde-small
%files -n kde
%files -n kde-big
%files -n kde-maxi
%files -n kde-somedevel
#
%files -n kde-edu
%files -n kde-games
%files -n kde-printing
%files -n kde-scanning
%files -n kde-pim

%changelog
* Tue Dec 10 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.2-alt1
- update requires

* Mon Dec 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.1-alt1
- update requires

* Tue Dec 03 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.0-alt1
- return kde5-runtime package for compatibility

* Thu Nov 28 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.9-alt1
- move ktorrent to kde-big

* Wed Nov 27 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.8-alt1
- relax requires

* Tue Nov 12 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.7-alt1
- update for Games

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.6-alt1
- update for Edu

* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.5-alt1
- update for Apps

* Wed Oct 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.4-alt1
- update for Apps

* Wed Oct 02 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.3-alt1
- update for PIM

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.2-alt1
- update print-manager

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.1-alt1
- update requires

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.0-alt1
- initial build
