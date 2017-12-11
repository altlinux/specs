%define rname plasma-workspace

%define x11confdir %_sysconfdir/X11

%define kworkspace5_sover 5
%define libkworkspace5 libkworkspace5%kworkspace5_sover
%define plasma_geolocation_interface_sover 5
%define libplasma_geolocation_interface libplasma-geolocation-interface%plasma_geolocation_interface_sover
%define taskmanager_sover 6
%define libtaskmanager libtaskmanager%taskmanager_sover
%define weather_ion_sover 7
%define libweather_ion libweather_ion%weather_ion_sover
%define legacytaskmanager_sover 5
%define liblegacytaskmanager liblegacytaskmanager%legacytaskmanager_sover

%def_disable qalculate

Name: kf5-%rname
Version: 5.11.3
Release: alt3%ubt
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Plasma
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: /usr/share/design/current xdg-user-dirs
Requires: iso-codes
Requires: qt5-dbus qt5-tools qt5-quickcontrols qt5-virtualkeyboard dbus-tools-gui
Requires: kf5-kinit kf5-kconfig kf5-kded kf5-kglobalaccel kf5-kactivitymanagerd kf5-kdeclarative
Requires: kf5-kwallet kf5-solid kf5-kimageformats kf5-kdbusaddons kf5-kio kf5-kio-extras
Requires: kf5-polkit-kde-agent kf5-kwin kf5-kdeclarative

Source: %rname-%version.tar
Patch100: alt-startkde.patch
#
Patch102: alt-def-wallpaper-image.patch
Patch103: alt-plasma-konsole.patch
Patch104: alt-def-digital-clock.patch
Patch105: alt-lock-widgets.patch
Patch106: alt-digital-clock-date.patch
Patch107: alt-freespacenotifier.patch
#Patch108: alt-breeze-background.patch
Patch108: alt-def-background.patch
Patch109: alt-def-start-empty-session.patch
Patch110: alt-breeze-loginscreen-focus.patch
Patch111: alt-breeze-one-screen.patch
Patch112: alt-breeze-pw-renew.patch
Patch113: alt-breeze-autoupdate-username.patch
Patch114: alt-dbus-service.patch
Patch115: alt-dbus-sessionchange.patch
Patch116: alt-refresh-menu.patch
Patch117: alt-disable-ctrl-alt-r.patch

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig glib2-devel glibc-devel-static kf5-attica-devel kf5-kdoctools-devel kf5-kjs-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcln-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libwayland-server libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel libxml2-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-webkit-devel rpm-build-gir ruby ruby-stdlibs wayland-devel xml-common xml-utils xorg-fixesproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ iceauth kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-kpty-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-libksysguard-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libdbusmenu-qt5-devel libgps-devel libpam-devel libqalculate-devel libwayland-client-devel libwayland-server-devel libxapian-devel mkfontdir prison-devel python-module-google qt5-phonon-devel qt5-script-devel qt5-x11extras-devel rpm-build-ruby xmessage xprop xrdb xset xsetroot zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-phonon-devel qt5-script-devel qt5-x11extras-devel
BuildRequires: libgps-devel libpam0-devel zlib-devel
%if_enabled qalculate
libqalculate-devel
%endif
BuildRequires: libwayland-client-devel libwayland-server-devel
BuildRequires: libxapian-devel prison-devel libnm-devel
BuildRequires: libxcbutil-image-devel libxcbutil-devel
BuildRequires: iceauth xmessage xprop xrdb xset xsetroot
BuildRequires: kde5-kholidays-devel
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel
BuildRequires: kf5-kpackage-devel kf5-kparts-devel kf5-kpty-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-libksysguard-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kxmlrpcclient-devel kf5-prison-devel
BuildRequires: kf5-networkmanager-qt-devel kf5-kscreenlocker-devel

%description
KDE Plasma Workspace

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkworkspace5
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Provides: libkworkspace5 = %version-%release
Obsoletes: libkworkspace5 < %version-%release
%description -n %libkworkspace5
KF5 library

%package -n %libplasma_geolocation_interface
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Provides: libplasma_geolocation_interface = %version-%release
Obsoletes: libplasma_geolocation_interface < %version-%release
%description -n %libplasma_geolocation_interface
KF5 library

%package -n %libtaskmanager
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Provides: libtaskmanager = %version-%release
Obsoletes: libtaskmanager < %version-%release
%description -n %libtaskmanager
KF5 library

%package -n %liblegacytaskmanager
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Provides: libtaskmanager = %version-%release
Obsoletes: libtaskmanager < %version-%release
%description -n %liblegacytaskmanager
KF5 library

%package -n %libweather_ion
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Provides: libweather_ion = %version-%release
Obsoletes: libweather_ion < %version-%release
%description -n %libweather_ion
KF5 library


%prep
%setup -n %rname-%version
%patch100 -p1 -b .startkde
#
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
pushd sddm-theme
%patch112 -p1
popd
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DKDE4_COMMON_PAM_SERVICE="kf5" \
    -DKDE_COMMON_PAM_SERVICE="kf5" \
    #

%install
%K5install

%K5install_move data drkonqi ksmserver ksplash kstyle solid kdevappwizard
%K5install_move data desktop-directories doc kconf_update kio_desktop

# fix dbus service
sed -i 's|^Exec=.*|Exec=%_K5bin/krunner|' %buildroot/%_K5dbus_srv/org.kde.krunner.service

mkdir -p %buildroot/%_bindir
ln -s `relative %_kf5_bin/startkde %_bindir/startkde5` %buildroot/%_bindir/startkde5
ln -s startkde %buildroot/%_kf5_bin/startkde5

# Add chksession support
mkdir -p %buildroot/%x11confdir/wmsession.d/
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/01PLASMA
NAME=Plasma
DESC=Plasma by KDE
ICON=%_K5icon/hicolor/48x48/apps/kwin.png
EXEC=%_kf5_bin/startkde
SCRIPT:
exec %_kf5_bin/startkde
__EOF__


# Create menu session
mkdir -p %buildroot/%_menudir/
cat <<__EOF__ > %buildroot/%_menudir/kde5-session
?package(%name): needs=wm \
                        section="Session/Windowmanagers" \
			title="PLASMA" \
			longtitle="Plasma by KDE" \
			command="%_bindir/startkde5" \
			icon="kwin.png"
__EOF__

# disable annoing autostart
mkdir -p %buildroot/%_K5start/
for n in tracker-extract tracker-miner-apps tracker-miner-fs tracker-miner-user-guides tracker-store ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_K5start/$n.desktop
done
# disable annoing menus
mkdir -p %buildroot/%_kf5_xdgapp/
for n in gnome-mplayer mplayer gmplayer ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_kf5_xdgapp/$n.desktop
done


%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/*rc
%config(noreplace) %_K5xdgconf/*.*categories
%dir %_K5data/desktop-directories/

%files
%config(noreplace) %x11confdir/wmsession.d/*PLASMA*
%_menudir/kde5-session
%dir %_K5plug/plasma/
%dir %_K5plug/plasma/*/
%dir %_K5plug/phonon_platform/
%dir %_K5qml/org/kde/plasma/private/
%dir %_K5qml/org/kde/plasma/wallpapers/
%dir %_K5qml/org/kde/plasma/workspace/
#%dir %_K5qml/org/kde/private/
%_bindir/*
%_K5bin/*
%_K5exec/*
%_K5conf_bin/*
%_K5lib/libkdeinit5_*.so
%_K5plug/plasma/*/*.so
%_K5plug/phonon_platform/*.so
%_K5plug/*.so
%_K5plug/kpackage/
%_K5plug/kf5/kded/*.so
%_K5plug/kf5/kio/desktop.so
%_K5plug/plasmacalendarplugins/
%_K5qml/org/kde/plasma/private/*
%_K5qml/org/kde/plasma/wallpapers/*
%_K5qml/org/kde/plasma/workspace/*
#%_K5qml/org/kde/private/*
%_K5qml/org/kde/taskmanager/
%_K5qml/org/kde/holidayeventshelperplugin/
#%_K5data/drkonqi/
%_K5data/plasma/
%_K5data/kio_desktop/
%_K5data/ksplash/
%_K5data/kstyle/
%_K5data/ksmserver/
%_K5data/desktop-directories/*
%_K5data/solid/actions/*.desktop
%_K5xdgapp/*.desktop
%_K5start/*.desktop
%_K5notif/*.notifyrc
%_K5cfg/*.kcfg
%_K5srv/*.desktop
%_K5srv/*.protocol
%_K5srvtyp/*.desktop
%_K5dbus_srv/*.service
%_K5conf_up/*.upd
%_datadir/dbus-1/services/*.service
%_datadir/xsessions/plasma.desktop
#%_datadir/wayland-sessions/plasmawayland.desktop
%_datadir/sddm/themes/*/

%files devel
#%_K5inc/KDE/
%_K5inc/kworkspace5/
%_K5inc/plasma/
%_K5inc/taskmanager/
#%_K5inc/legacytaskmanager/
%_K5link/lib*.so
%_K5lib/cmake/KRunnerAppDBusInterface/
%_K5lib/cmake/KSMServerDBusInterface/
%_K5lib/cmake/LibKWorkspace/
%_K5lib/cmake/LibTaskManager/
#%_K5lib/cmake/LibLegacyTaskManager/
%_K5dbus_iface/*.xml
%_K5data/kdevappwizard/templates/*

%files -n %libkworkspace5
%_K5lib/libkworkspace5.so.*
%_K5lib/libkworkspace5.so.%kworkspace5_sover
%files -n %libplasma_geolocation_interface
%_K5lib/libplasma-geolocation-interface.so.*
%_K5lib/libplasma-geolocation-interface.so.%plasma_geolocation_interface_sover
%files -n %libtaskmanager
%_K5lib/libtaskmanager.so.*
%_K5lib/libtaskmanager.so.%taskmanager_sover
#%files -n %liblegacytaskmanager
#%_K5lib/liblegacytaskmanager.so.*
#%_K5lib/liblegacytaskmanager.so.%legacytaskmanager_sover
%files -n %libweather_ion
%_K5lib/libweather_ion.so.*
%_K5lib/libweather_ion.so.%weather_ion_sover

%changelog
* Mon Dec 11 2017 Oleg Solovyov <mcpain@altlinux.org> 5.11.3-alt3%ubt
- fix theme

* Mon Dec 04 2017 Oleg Solovyov <mcpain@altlinux.org> 5.11.3-alt2%ubt
- remove redundnant Password*.qml

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Wed Oct 04 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt2%ubt
- clear Ctrl+Alt+R binding

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt6%ubt
- fix system tray icon context menu (ALT#33763) (thanks darktemplar@alt)

* Tue Aug 08 2017 Oleg Solovyov <mcpain@altlinux.org> 5.10.4-alt5%ubt
- support for changing sessions from D-Bus

* Wed Aug 02 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt4%ubt
- require qt5-virtualkeyboard

* Wed Jul 26 2017 Oleg Solovyov <mcpain@altlinux.org> 5.10.4-alt3%ubt
- fix focus behavior on login screen

* Mon Jul 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt2%ubt
- fix dbus service

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Tue Jun 27 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt8%ubt
- fix package release

* Mon Jun 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt7%ubt
- update from 5.9 branch

* Fri Jun 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt6%ubt
- apply fix against KDE bugs 348390, 251222
- create ~/.local/share/kf5

* Tue Jun 13 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.5-alt5%ubt
- fix: unable to handle auth request

* Tue Jun 13 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.5-alt4%ubt
- fix autoupdate username

* Wed Jun 07 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.5-alt3%ubt
- new look for breeze theme

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2%ubt
- feel last user name in sddm

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Mon Apr 03 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt5%ubt
- fix password renew with breeze sddm theme

* Fri Mar 31 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt4%ubt
- fix start sddm with breeze theme

* Fri Mar 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt3%ubt
- add password renew support for sddm theme

* Mon Mar 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt2%ubt
- clean build requires
- build with prison
- update from 5.9 branch

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Tue Feb 28 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2%ubt
- fix login background

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt3.M80P.1
- build for M80P

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt4
- fix to upscale splash background on big screen

* Fri Oct 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2.M80P.1
- build for M80P

* Fri Oct 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt3
- set user switch screen background

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1.M80P.1
- build for M80P

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2
- set logout screen background

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt2.M80P.1
- build for M80P

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt3
- fix plasma load

* Wed Oct 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1.M80P.1
- build for M80P

* Wed Oct 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt2
- fix plasma load

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt2
- fix plasma shell startup

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt2
- add upstream fix against KDEBUG#365621

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Wed Aug 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt2
- disable hide of free space notifier

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Tue Jul 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt2
- apply upstream fix against KDEBUG#364530

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt2
- don't bold clock font by default

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Thu Apr 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt2
- fix requires

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt2
- update requires

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- fix startup splash progress

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt3
- don't lock widgets at first time
- don't save session by default
- set breeze default background

* Tue Jan 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt2
- fix XDG_*_DIRS variables for kstartupconfig5

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt4
- add compact date to digital clock

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Fri Nov 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt3
- fix krunner dbus service

* Tue Oct 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- lock widgets at login

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt3
- add default plasma action to run konsole
- don't lock screen on resume by default
- set digital clock defaults

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt2
- set default desktop wallpaper

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- fix path to startkde in session file

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt5
- rebuild with new baloo

* Thu Aug 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt4
- disable screenlocker by default

* Fri Jul 31 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt3
- move dbus service to standard place

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- change XDG data dirs order in startkde

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt2
- fix requires

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
