%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: kde-set
Version: 24.01.1
Release: alt1

Group: Graphical desktop/KDE
Summary: Set of KDE applications
License: ALT-Public-Domain

BuildRequires(pre): rpm-macros-qt6-webengine

%description
%summary

%package -n kde-runtime
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-runtime = %EVR
Obsoletes: kde5-runtime < %EVR
#
Requires: qt6-phonon-backend qt6-5compat qt6-declarative qt6-svg qt6-imageformats qt6-translations qt6-wayland
Requires: kf6-kio kf6-kded
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
Requires: kde5-dolphin kde5-kdialog
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
Requires: kde5-svgpart
Requires: kf6-baloo
Requires: polkit-kde-agent kde5-kio-extras plasma6-breeze powerdevil plasma-systemmonitor
Requires: drkonqi milou systemsettings plasma6-integration
Requires: kde5-ark kde5-konsole kde5-gwenview kde5-okular kde5-kwrite kde5-kwalletmanager
Requires: kde5-kcalc kde5-kross-python
#
Requires: plasma5-breeze plasma5-integration
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
Requires: kde5-khelpcenter kde5-kolourpaint kde5-kio-audiocd kde5-kgpg
Requires: kmenuedit kgamma plasma-thunderbolt
Requires: kde5-kfind kde5-filelight kde5-kcharselect kde5-kteatime kde5-spectacle
Requires: kde5-kamera kde5-network-filesharing kde5-ktorrent
Requires: kde5-kio-zeroconf kde5-sweeper
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
Requires: plasma6-oxygen
Requires: icon-theme-oxygen
Requires: plasma-workspace-wallpapers
Requires: kwrited
Requires: kde5-ksystemlog
Requires: kde5-krdc
Requires: kde5-kcron kde5-kruler kde5-ffmpegthumbs
Requires: kde5-connect
Requires: kde5-krfb
Requires: kde5-kdf
Requires: kid3-ui-kde5
Requires: kde5-graphics-thumbnailers
#
Requires: plasma5-oxygen
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
Requires: kde5-keditbookmarks
Requires: kde5-kfloppy kde5-ktimer
Requires: kde5-dragon
Requires: kde5-kmousetool kde5-kmag
Requires: kde5-juk kde5-kmouth
Requires: kdenlive
Requires: kde5-k3b kde5-kwave kde5-konversation
Requires: kde5-digikam
Requires: kde5-kdebugsettings
%description -n kde-maxi
%summary

%package -n kde-somedevel
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-somedevel = %EVR
Obsoletes: kde5-somedevel < %EVR
Requires: kde-runtime
#
Requires: kde5-kate
Requires: kde5-dolphin-plugins
Requires: kde5-lokalize kde5-okteta kde5-kapptemplate kde5-dev-scripts kde5-kompare
Requires: kde5-sdk-thumbnailers kde5-poxml kde5-umbrello
Requires: kde5-kcachegrind
%if_enabled qtwebengine
Requires: kde5-kimagemapeditor
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
Requires: kde5-parley
%endif
Requires: kde5-kanagram kde5-khangman
Requires: kde5-kwordquiz kde5-kturtle kde5-marble
Requires: kde5-step
%ifnarch armh
Requires: kde5-kstars
%endif
Requires: kde5-kig kde5-kmplot kde5-kalgebra kde5-cantor kde5-rocs
Requires: kde5-kbruch kde5-kgeography kde5-ktouch
Requires: kde5-minuet
%description -n kde-edu
Educational software based on the KDE technologies

%package -n kde-games
Summary: Set of KDE-based games
Group: Graphical desktop/KDE
Provides: kde5-games = %EVR
Obsoletes: kde5-games < %EVR
Requires: kde-runtime
#
Requires: kde5-lskat kde5-kmines kde5-kshisen kde5-ktuberling kde5-bovo kde5-knetwalk
Requires: kde5-katomic kde5-knavalbattle kde5-kpat kde5-kmahjongg
Requires: kde5-ksudoku kde5-kigo kde5-knights kde5-kreversi kde5-granatier
Requires: kde5-kolf kde5-ksirk kde5-palapeli
%description -n kde-games
High quality gaming and entertainment software.

%package -n kde-printing
Summary: Set of printing support applications
Group: Graphics
Provides: kde5-printing = %EVR
Obsoletes: kde5-printing < %EVR
Requires: kde-runtime
#
Requires: kde5-print-manager cups printer-drivers-X11
%description -n kde-printing
KDE printing support applications.

%package -n kde-scanning
Summary: Set of image scanning support applications
Group: Graphics
Provides: kde5-scanning = %EVR
Obsoletes: kde5-scanning < %EVR
Requires: kde-runtime
#
Requires: kde5-skanpage
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
Requires: kde5-pim-data-exporter kde5-pim-addons
Requires: kde5-akregator kde5-kontact
Requires: kde5-korganizer kde5-zanshin
Requires: kde5-akonadi-calendar-tools
%endif
Requires: kde5-kalarm kde5-knotes
Requires: kde5-kaddressbook
# akonadi based email client
#Requires: kde5-akonadi-import-wizard kde5-mbox-importer kde5-pim-sieve-editor kde5-mbox-importer kde5-pim-sieve-editor kde5-grantlee-editor
%description -n kde-pim
%summary


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
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.1-alt1
- update requires

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.01.0-alt1
- initial build
