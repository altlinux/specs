%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname plasma-workspace

%define x11confdir %_sysconfdir/X11

%define kworkspace6_sover 6
%define libkworkspace6 libkworkspace6_%kworkspace6_sover
%define libbatterycontrol libbatterycontrol%kworkspace6_sover
%define libkmpris libkmpris%kworkspace6_sover
%define plasma_geolocation_interface_sover 6
%define libplasma_geolocation_interface libplasma-geolocation-interface%plasma_geolocation_interface_sover
%define taskmanager_sover 6
%define libtaskmanager libtaskmanager%taskmanager_sover
%define weather_ion_sover 7
%define libweather_ion libweather_ion%weather_ion_sover
%define colorcorrect_sover 6
%define libcolorcorrect libcolorcorrect%colorcorrect_sover
%define notificationmanager_sover 1
%define libnotificationmanager libnotificationmanager%notificationmanager_sover
%define kfontinst_sover 6
%define libkfontinst libkfontinst%kfontinst_sover
%define kfontinstui_sover 6
%define libkfontinstui libkfontinstui%kfontinstui_sover
%define krdb_sover 6
%define libkrdb libkrdb%krdb_sover

%def_enable qalculate
%def_enable appstream

Name: %rname
Version: 6.1.5
Release: alt1
Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Plasma
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-workspace = %EVR
Obsoletes: plasma5-workspace < %EVR
Provides: plasma5-user-manager = %EVR
Obsoletes: plasma5-user-manager < %EVR
Provides: kf5-plasma-workspace = %EVR
Obsoletes: kf5-plasma-workspace < %EVR

Requires: %name-qml
Requires: /usr/share/design/current xdg-user-dirs
Requires: iso-codes
Requires: xmessage
Requires: qt6-dbus qt6-declarative qt6-virtualkeyboard dbus-tools-gui
#Requires: qt6-tools
Requires: kf6-kconfig kf6-kded kf6-kdeclarative
Requires: kf6-kwallet kf6-solid kf6-kimageformats kf6-kdbusaddons kf6-kio
#Requires: kde6-kio-extras
Requires: kf6-kquickcharts kf6-kirigami
Requires: plasma6-kpipewire plasma6-kglobalacceld
Requires: polkit-kde-agent kwin kactivitymanagerd plasma6-plasma5support
Requires: kf6-kirigami-addons
#Requires: kde6-kio-fuse
#Requires: appmenu-gtk-module

Source: %rname-%version.tar
Source1: freememorynotifier.po
Source2: libkicker-ru-add.po
Source3: plasma_lookandfeel_org.kde.lookandfeel-ru-add.po
#
Source11: freememorynotifier.tar
Source40: ssh-agent.conf
Source41: spice-vdagent.conf
Source42: obex.conf
Source43: xdg-user-dirs.conf
#
Source51: nvidia_prime_available.cpp

Patch100: alt-startkde.patch
Patch101: alt-menu-add-tooltip.patch
Patch102: alt-def-wallpaper-image.patch
Patch103: alt-wait-drkonqi.patch
Patch104: alt-def-digital-clock.patch
#
Patch106: alt-digital-clock-date.patch
Patch107: alt-freespacenotifier.patch
Patch108: alt-def-background.patch
Patch109: alt-def-start-empty-session.patch
#
Patch114: alt-menu-search-results-add-genericname.patch
#
Patch117: alt-klipper-help-url.patch
Patch118: alt-session-exclude.patch
Patch119: alt-freespace-thread-timer.patch
Patch120: alt-desktop-plasmashell.patch
Patch121: alt-freememorynotifier.patch
#
Patch123: alt-def-font.patch
#
Patch126: alt-add-using-the-altappstarter.patch
Patch127: alt-plasma-5.17-crash.patch
Patch128: alt-soname.patch
Patch129: alt-def-icons.patch
#
#Patch131: alt-kscreenlocker-theme-pam-support.patch
#Patch132: alt-fix-virtualkeyboard.patch
Patch133: alt-dont-remove-desktop-actions.patch
Patch134: alt-zonetab.patch
#Patch135: alt-fix-virtualkeyboard-size.patch
Patch136: alt-users-use-gost-yescrypt.patch
Patch137: alt-systemd-boot.patch
Patch138: alt-digital-clock-tz.patch
Patch139: alt-locales-list.patch
Patch140: alt-watch-wallpaper.patch
Patch141: alt-weather-fix-ua.patch
#
Patch143: alt-run-etc-profile.patch
Patch144: alt-def-lookandfeel.patch
Patch145: alt-add-nvidia-prime-to-menu.patch
Patch146: alt-fix-wallpaper-confirmation.patch
#
Patch150: alt-kcmusers-avatars.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel qt6-phonon-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: qt6-wayland-devel qt6-5compat-devel qt6-shadertools-devel
BuildRequires: qcoro6-devel
BuildRequires: libgps-devel libpam0-devel zlib-devel libpolkitqt6-qt6-devel
BuildRequires: python3-devel libsystemd-devel
%if_enabled qalculate
BuildRequires: libqalculate-devel
%endif
%if_enabled appstream
BuildRequires: libappstream-qt6-devel
%endif
BuildRequires: libwayland-client-devel libwayland-server-devel libwayland-egl-devel
BuildRequires: wayland-protocols plasma-wayland-protocols
BuildRequires: libdrm-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libxapian-devel libnm-devel libsysfs-devel fontconfig-devel libcanberra-devel
BuildRequires: libxcbutil-image-devel libxcbutil-devel
BuildRequires: libICE-devel libSM-devel libXcursor-devel libXfixes-devel libXft-devel libXrender-devel libXtst-devel
BuildRequires: iceauth xmessage xprop xrdb xset xsetroot
BuildRequires: libvulkan-devel
BuildRequires: kf6-baloo-devel kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel
BuildRequires: kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel
BuildRequires: kf6-kdesu-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kidletime-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-knotifyconfig-devel
BuildRequires: kf6-kpackage-devel kf6-kparts-devel kf6-kpty-devel kf6-krunner-devel kf6-kservice-devel kf6-ktexteditor-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-kirigami-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-prison-devel
BuildRequires: kf6-networkmanager-qt-devel kf6-kpeople-devel
BuildRequires: kf6-kded-devel kf6-kholidays-devel
BuildRequires: kf6-kquickcharts-devel kf6-ksvg-devel kf6-kstatusnotifieritem-devel
BuildRequires: plasma6-lib-devel plasma6-activities-devel plasma6-kwayland-devel
BuildRequires: kscreenlocker-devel plasma6-breeze-devel plasma6-layer-shell-qt-devel
BuildRequires: plasma6-kpipewire-devel kwin-devel plasma6-libkscreen-devel plasma6-libksysguard-devel
BuildRequires: plasma6-plasma5support-devel plasma6-activities-stats-devel
BuildRequires: kf6-kirigami-addons-devel
#BuildRequires: kde6-libkexiv2-devel


%description
KDE Plasma Workspace

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common
Provides: plasma5-workspace-common = %EVR
Obsoletes: plasma5-workspace-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-workspace-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %name-qml
Group: Graphical desktop/KDE
Summary: Base qml-components for plasma workspace
Requires: %name-common >= %EVR
Requires: libkf6windowsystem kf6-kdeclarative kf6-kirigami libplasmaquick6
Provides: plasma5-workspace-qml = %EVR
Obsoletes: plasma5-workspace-qml < %EVR
%description -n %name-qml
Base qml-components for plasma workspace

%package -n sddm-theme-breeze
Group: Graphical desktop/KDE
Summary: SDDM breeze theme
Requires: %name-common >= %EVR
Requires: %name-qml >= %EVR
Buildarch: noarch
%description -n sddm-theme-breeze
SDDM breeze theme

%package -n polkit-kde-plasma-workspace
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common
Provides: polkit-kde-kfontinst
%description -n polkit-kde-plasma-workspace
Common polkit files for %name

%package -n %libkworkspace6
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkworkspace6
%name library

%package -n %libplasma_geolocation_interface
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libplasma_geolocation_interface
%name library

%package -n %libtaskmanager
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libtaskmanager
%name library

%package -n %libweather_ion
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libweather_ion
%name library

%package -n %libcolorcorrect
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libcolorcorrect
%name library

%package -n %libnotificationmanager
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libnotificationmanager
%name library

%package -n %libkfontinst
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkfontinst
%name library

%package -n %libkfontinstui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkfontinstui
%name library

%package -n %libkrdb
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkrdb
%name library

%package -n %libbatterycontrol
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libbatterycontrol
%name library

%package -n %libkmpris
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkmpris
%name library


%prep
%setup -n %rname-%version
#%patch100 -p1 -b .startkde
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
#
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
#
%patch114 -p1
#
%patch117 -p1
%patch118 -p1
%patch119 -p2
%patch120 -p1
%patch121 -p2
#
%patch123 -p1
#
%patch126 -p1
%patch127 -p2
%patch128 -p1
#%patch129 -p1 -b .small_icons_size
#
#%patch131 -p2 -b .screenlocker_pam
#%patch132 -p1 -b .virtualkeyboard
%patch133 -p1
%patch134 -p1
#%patch135 -p2 -b .virtualkeyboard_size
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
#%patch140 -p1 -b .watch_wallpaper
%patch141 -p1
#
%patch143 -p1
%patch144 -p1
%patch145 -p1 -b .prime
%patch146 -p1
#
%patch150 -p1

pwd
install -m0644 %SOURCE51 applets/kicker/plugin/

install -m 0644 %SOURCE1 po/ru/freememorynotifier.po
tar xf %SOURCE11 freememorynotifier/
msgcat --use-first po/ru/libkicker.po %SOURCE2 > po/ru/libkicker.po.tmp
cat po/ru/libkicker.po.tmp > po/ru/libkicker.po
rm -f po/ru/libkicker.po.tmp
msgcat --use-first po/ru/plasma_lookandfeel_org.kde.lookandfeel.po %SOURCE3 > po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp
cat po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp > po/ru/plasma_lookandfeel_org.kde.lookandfeel.po
rm -f po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp

# disable find PackageKitQt6
sed -i 's|PackageKitQt6|PackageKitQt6_UBUNTU_ONLY|' CMakeLists.txt

if [ -d %_libdir/cmake/AppStreamQt6 -a ! -d %_libdir/cmake/AppStreamQt ] ; then
    mkdir -p cmake/AppStreamQt/
    for f in %_libdir/cmake/AppStreamQt6/*.cmake ; do
	ln -s $f cmake/AppStreamQt/`basename "$f" | sed 's|6||'`
    done
    ln -s %_includedir/AppStreamQt6 runners/appstream/AppStreamQt
    ln -s %_includedir/AppStreamQt6 applets/kicker/AppStreamQt
fi

# disable krunners by default
for d in runners/*/*.desktop ; do
    sed -i 's|^X-KDE-PluginInfo-EnabledByDefault=.*$|X-KDE-PluginInfo-EnabledByDefault=false|' $d
done
for d in runners/*/*.json ; do
    sed -i '/EnabledByDefault/s|true|false|' $d
done
# enable some krunners by default
#for d in appstream services shell
#do
#    sed -i 's|^X-KDE-PluginInfo-EnabledByDefault=.*$|X-KDE-PluginInfo-EnabledByDefault=true|' runners/${d}/plasma-runner-${d}.desktop
#done
for d in appstream services shell
do
    sed -i '/EnabledByDefault/s|false|true|' runners/${d}/plasma-runner-${d}.json
done

%build
%K6build \
    -DINCLUDE_INSTALL_DIR=%_K6inc \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DUBUNTU_PACKAGEKIT:BOOL=OFF \
    -DGLIBC_LOCALE_GENERATED:BOOL=ON \
    -DGLIBC_LOCALE_GEN:BOOL=OFF \
    -DAppStreamQt_DIR:PATH=$PWD/cmake/AppStreamQt \
    #

%install
%K6install
%K6install_move data kstyle solid kdevappwizard kpackage kglobalaccel
%K6install_move data desktop-directories doc kconf_update kio_desktop knsrcfiles
%K6install_move data kcontrol kdisplay kfontinst krunner konqsidebartng plasma/avatars locale
%K6install_move data plasma//nightcolor kio

# fix dbus service
sed -i 's|^Exec=.*|Exec=%_K6bin/krunner|' %buildroot/%_K6dbus_srv/org.kde.krunner.service

mkdir -p %buildroot/%_K6xdgconf/plasma-workspace/env/
mkdir -p %buildroot/%_K6data/kio_desktop/DesktopLinks/

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_kf6_bin

# Add chksession support
mkdir -p %buildroot/%x11confdir/wmsession.d/
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/01PLASMA
NAME=Plasma
DESC=Plasma by KDE
ICON=%_K6icon/hicolor/48x48/apps/kwin.png
EXEC=%_K6bin/startplasma-x11
SCRIPT:
exec %_K6bin/startplasma-x11
__EOF__


# Create menu session
mkdir -p %buildroot/%_menudir/
cat <<__EOF__ > %buildroot/%_menudir/session
?package(%name): needs=wm \
                        section="Session/Windowmanagers" \
			title="PLASMA" \
			longtitle="Plasma by KDE" \
			command="%_bindir/startplasma-x11" \
			icon="kwin.png"
__EOF__

# systemd user service deps
mkdir -p %buildroot/%_userunitdir/plasma-core.target.d/
mkdir -p %buildroot/%_userunitdir/plasma-workspace@.target.d/
install -m0644 -p -D %SOURCE40 %buildroot/%_userunitdir/plasma-core.target.d/ssh-agent.conf
install -m0644 -p -D %SOURCE41 %buildroot/%_userunitdir/plasma-core.target.d/spice-vdagent.conf
install -m0644 -p -D %SOURCE42 %buildroot/%_userunitdir/plasma-core.target.d/obex.conf
install -m0644 -p -D %SOURCE43 %buildroot/%_userunitdir/plasma-core.target.d/xdg-user-dirs.conf

%find_lang %name --with-kde --all-name


%files common -f %name.lang
%doc LICENSES/*
%dir %_K6data/plasma/look-and-feel/
%dir %_K6xdgconf/plasma-workspace/
%dir %_K6xdgconf/plasma-workspace/env/
%dir %_K6data/kio_desktop/DesktopLinks/
%dir %_K6plug/kf6/packagestructure/
%dir %_K6qml/org/kde/plasma/workspace/
%dir %_K6qml/org/kde/plasma/private/
%dir %_K6qml/org/kde/plasma/wallpapers/
%config(noreplace) %_K6xdgconf/*rc
%_datadir/qlogging-categories6/*.*categories
%_K6icon/hicolor/*/mimetypes/*.*
%_K6icon/hicolor/*/apps/*.*

%files
%config(noreplace) %x11confdir/wmsession.d/*PLASMA*
%_menudir/session
%dir %_K6plug/plasma/
%dir %_K6plug/plasma/*/
%dir %_K6plug/phonon_platform/
%_bindir/*
%_K6libexecdir/ba*
%_K6libexecdir/kfo*
%_K6libexecdir/ks*
%_K6libexecdir/p*
%_K6exec/kauth/*
%_K6conf_bin/*
%_K6plug/kf6/thumbcreator/
%_K6plug/plasma/*/*.so
%_K6plug/phonon_platform/*.so
%exclude %_K6plug/kf6/packagestructure/wallpaper_images.so
%_K6plug/kf6/kded/*.so
%_K6plug/kf6/kio/*.so
%_K6plug/kf6/krunner/
%_K6plug/kf6/parts/*.so
%_K6plug/plasmacalendarplugins/
%_K6plug/plasma/kcms/systemsettings/
%_K6plug/plasma/kcms/systemsettings_qwidgets/
%_K6plug/kf6/packagestructure/*.so
%_K6plug/kf6/kfileitemaction/*.so
%_K6plug/plasma5support/
%_K6plug/kcm_freememorynotifier.so
%_K6qml/org/kde/taskmanager/
%_K6qml/org/kde/colorcorrect/
%_K6qml/org/kde/notificationmanager/
%_K6data/knsrcfiles/*.knsrc
%_K6data/plasma/
%exclude %_K6data/plasma/look-and-feel/*
%exclude %_K6data/plasma/wallpapers/org.kde.image/
%_K6data/kglobalaccel/*.desktop
%_K6data/kio/servicemenus/*
%_K6data/kio_desktop/
%_K6data/krunner/
%_K6data/kstyle/
%_K6data/kfontinst/
%_K6data/konqsidebartng/
%_K6data/desktop-directories/*
%_K6data/solid/actions/*.desktop
%_K6data/plasma5support/
%_K6xdgapp/*.desktop
%_K6start/*.desktop
%_K6notif/*.notifyrc
%_K6cfg/*.kcfg
%_K6dbus_srv/*.service
%_K6dbus/system.d/*.conf
%_K6dbus_sys_srv/*.service
%_K6conf_up/*
%_datadir/xsessions/plasmax11.desktop
%_datadir/wayland-sessions/plasma.desktop
%dir %_userunitdir/plasma-core.target.d/
%_userunitdir/plasma-core.target.d/*.conf
%dir %_userunitdir/plasma-workspace@.target.d/
%_userunitdir/*.service
%_userunitdir/*.target
%_datadir/zsh/site-functions/_*
%_datadir/metainfo/*.xml

%files -n polkit-kde-plasma-workspace
%_datadir/polkit-1/actions/*fontinst*.policy

%files -n %name-qml
%_K6plug/kf6/packagestructure/wallpaper_images.so
%_K6qml/org/kde/breeze/components/
%_K6qml/org/kde/plasma/
%_K6data/plasma/look-and-feel/*
%_K6data/plasma/wallpapers/org.kde.image/

#%files -n sddm-theme-breeze
#%_datadir/sddm/themes/breeze/

%files devel
%_K6inc/*
%_K6link/lib*.so
%_K6lib/cmake/KRunnerAppDBusInterface/
%_K6lib/cmake/KSMServerDBusInterface/
%_K6lib/cmake/Lib*/
%_K6dbus_iface/*.xml
#%_K6data/kdevappwizard/templates/*

%files -n %libkworkspace6
%_K6lib/libkworkspace6.so.*
%_K6lib/libkworkspace6.so.%kworkspace6_sover
%files -n %libplasma_geolocation_interface
%_K6lib/libplasma-geolocation-interface.so.*
%_K6lib/libplasma-geolocation-interface.so.%plasma_geolocation_interface_sover
%files -n %libtaskmanager
%_K6lib/libtaskmanager.so.*
%_K6lib/libtaskmanager.so.%taskmanager_sover
%files -n %libweather_ion
%_K6lib/libweather_ion.so.*
%_K6lib/libweather_ion.so.%weather_ion_sover
%files -n %libcolorcorrect
%_K6lib/libcolorcorrect.so.*
%_K6lib/libcolorcorrect.so.%colorcorrect_sover
%files -n %libnotificationmanager
%_K6lib/libnotificationmanager.so.*
%_K6lib/libnotificationmanager.so.%notificationmanager_sover
%files -n %libkfontinst
%_K6lib/libkfontinst.so.*
%_K6lib/libkfontinst.so.%kfontinst_sover
%files -n %libkfontinstui
%_K6lib/libkfontinstui.so.*
%_K6lib/libkfontinstui.so.%kfontinstui_sover
%files -n %libkrdb
%_K6lib/libkrdb.so.*
%_K6lib/libkrdb.so.%krdb_sover
%files -n %libbatterycontrol
%_K6lib/libbatterycontrol.so.*
%_K6lib/libbatterycontrol.so.%kworkspace6_sover
%files -n %libkmpris
%_K6lib/libkmpris.so.*
%_K6lib/libkmpris.so.%kworkspace6_sover


%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.1.5-alt1
- new version

* Fri Aug 23 2024 Oleg Solovyov <mcpain@altlinux.org> 1:6.1.4-alt2
- port freememorynotifier to Qt6

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.1.2-alt1
- new version

* Fri Jul 05 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

