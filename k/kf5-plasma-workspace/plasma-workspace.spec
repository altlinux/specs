%define rname plasma-workspace

%define x11confdir %_sysconfdir/X11

%define kworkspace5_sover 5
%define libkworkspace5 libkworkspace5%kworkspace5_sover
%define plasma_geolocation_interface_sover 5
%define libplasma_geolocation_interface libplasma-geolocation-interface%plasma_geolocation_interface_sover
%define taskmanager_sover 5
%define libtaskmanager libtaskmanager%taskmanager_sover
%define weather_ion_sover 7
%define libweather_ion libweather_ion%weather_ion_sover

%def_disable qalculate

Name: kf5-%rname
Version: 5.4.0
Release: alt2
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Plasma
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: qt5-dbus qt5-tools qt5-quickcontrols dbus-tools-gui
Requires: kf5-kinit kf5-kconfig kf5-kded kf5-kglobalaccel kf5-kactivities kf5-kdeclarative
Requires: kf5-kwallet kf5-solid kf5-kimageformats kf5-kdbusaddons kf5-kio kf5-kio-extras
Requires: kf5-polkit-kde-agent kf5-kwin kf5-kdeclarative

Source: %rname-%version.tar
Source10: pam-kf5-screensaver
Patch100: alt-startkde.patch
Patch101: alt-disable-screenlocker.patch

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig glib2-devel glibc-devel-static kf5-attica-devel kf5-kdoctools-devel kf5-kjs-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcln-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libwayland-server libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel libxml2-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-webkit-devel rpm-build-gir ruby ruby-stdlibs wayland-devel xml-common xml-utils xorg-fixesproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ iceauth kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-kpty-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-libksysguard-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libdbusmenu-qt5-devel libgps-devel libpam-devel libqalculate-devel libwayland-client-devel libwayland-server-devel libxapian-devel mkfontdir prison-devel python-module-google qt5-phonon-devel qt5-script-devel qt5-x11extras-devel rpm-build-ruby xmessage xprop xrdb xset xsetroot zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-phonon-devel qt5-script-devel qt5-x11extras-devel
BuildRequires: libdbusmenu-qt5-devel libgps-devel libpam0-devel zlib-devel
%if_enabled qalculate
libqalculate-devel
%endif
BuildRequires: libwayland-client-devel libwayland-server-devel
BuildRequires: libxapian-devel prison-devel
BuildRequires: iceauth xmessage xprop xrdb xset xsetroot
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel
BuildRequires: kf5-kpackage-devel kf5-kparts-devel kf5-kpty-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-libksysguard-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kxmlrpcclient-devel
BuildRequires: kf5-networkmanager-qt-devel libnm-devel

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
%patch101 -p1

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DKDE4_COMMON_PAM_SERVICE="kf5" \
    -DKDE_COMMON_PAM_SERVICE="kf5" \
    -DKDE4_KSCREENSAVER_PAM_SERVICE="kf5-screensaver" \
    -DKDE_KSCREENSAVER_PAM_SERVICE="kf5-screensaver" \
    -DKSCREENSAVER_PAM_SERVICE="kf5-screensaver" \
    #

%install
%K5install

%K5install_move data drkonqi ksmserver ksplash kstyle solid
%K5install_move data desktop-directories doc kconf_update kio_desktop

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

# Install kde pam configuration files
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE10 %buildroot/%_sysconfdir/pam.d/kf5-screensaver

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/*rc
%dir %_K5data/desktop-directories/

%files
%config(noreplace) %x11confdir/wmsession.d/*PLASMA*
%config(noreplace) %_sysconfdir/pam.d/kf5-screensaver
%_menudir/kde5-session
%dir %_K5plug/plasma/
%dir %_K5plug/plasma/*/
%dir %_K5plug/phonon_platform/
%dir %_K5qml/org/kde/plasma/private/
%dir %_K5qml/org/kde/plasma/wallpapers/
%dir %_K5qml/org/kde/plasma/workspace/
%dir %_K5qml/org/kde/private/
%_bindir/*
%_K5bin/*
%_K5exec/*
%attr(2711,root,chkpwd) %_K5exec/kcheckpass
%_K5lib/libkdeinit5_*.so
%_K5plug/plasma/*/*.so
%_K5plug/phonon_platform/*.so
%_K5plug/*.so
%_K5plug/kpackage/
%_K5plug/kf5/kio/desktop.so
%_K5qml/org/kde/plasma/private/*
%_K5qml/org/kde/plasma/wallpapers/*
%_K5qml/org/kde/plasma/workspace/*
%_K5qml/org/kde/private/*
%_K5data/drkonqi/
%_K5data/plasma/
%_K5data/kio_desktop/
%_K5data/ksplash/
%_K5data/kstyle/
%_K5data/ksmserver/
%_K5data/kconf_update/*
%_K5data/desktop-directories/*
%_K5data/solid/actions/*.desktop
%_K5xdgapp/*.desktop
%_K5start/*.desktop
%_K5notif/*.notifyrc
%_K5cfg/*.kcfg
%_K5srv/*.desktop
%_K5srv/*.protocol
%_K5srv/kded/*.desktop
%_K5srvtyp/*.desktop
%_K5dbus_srv/*.service
%_datadir/dbus-1/services/*.service
%_datadir/xsessions/plasma.desktop
%_datadir/sddm/themes/*/

%files devel
#%_K5inc/plasma-workspace_version.h
%_K5inc/KDE/
%_K5inc/kworkspace5/
%_K5inc/plasma/
%_K5inc/taskmanager/
%_K5link/lib*.so
%_K5lib/cmake/KRunnerAppDBusInterface
%_K5lib/cmake/KSMServerDBusInterface
%_K5lib/cmake/LibKWorkspace
%_K5lib/cmake/LibTaskManager
%_K5lib/cmake/ScreenSaverDBusInterface
#%_K5archdata/mkspecs/modules/qt_Plasma-Workspace.pri
%_K5dbus_iface/*.xml

%files -n %libkworkspace5
%_K5lib/libkworkspace5.so.*
%_K5lib/libkworkspace5.so.%kworkspace5_sover
%files -n %libplasma_geolocation_interface
%_K5lib/libplasma-geolocation-interface.so.*
%_K5lib/libplasma-geolocation-interface.so.%plasma_geolocation_interface_sover
%files -n %libtaskmanager
%_K5lib/libtaskmanager.so.*
%_K5lib/libtaskmanager.so.%taskmanager_sover
%files -n %libweather_ion
%_K5lib/libweather_ion.so.*
%_K5lib/libweather_ion.so.%weather_ion_sover

%changelog
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
