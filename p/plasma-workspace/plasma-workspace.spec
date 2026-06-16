%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname plasma-workspace

%define x11confdir %_sysconfdir/X11

%define sover 6
%define libkworkspace6 libkworkspace6_%sover
%define libbatterycontrol libbatterycontrol%sover
%define libkmpris libkmpris%sover
%define libtaskmanager libtaskmanager%sover
%define libkfontinst libkfontinst%sover
%define libkfontinstui libkfontinstui%sover
%define libkrdb libkrdb%sover
%define libklipper libklipper%sover
%define libklookandfeel libklookandfeel%sover
%define notificationmanager_sover 1
%define libnotificationmanager libnotificationmanager%notificationmanager_sover

%def_enable qalculate
%def_enable appstream
%def_disable bootstrap

Name: %rname
Version: 6.6.5
Release: alt2
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

Requires(pre,postun): alternatives
Requires: %name-qml
Requires: /usr/share/design/current xdg-user-dirs
Requires: iso-codes icc-profiles
Requires: xmessage
Requires: qt6-dbus qt6-declarative qt6-virtualkeyboard dbus-tools-gui
Requires: libqt6-location
Requires: kf6-kconfig kf6-kded kf6-kdeclarative
Requires: kf6-kwallet kf6-solid kf6-kimageformats kf6-kdbusaddons kf6-kio
#Requires: kio-extras
Requires: kf6-kquickcharts kf6-kirigami
Requires: plasma6-kpipewire plasma6-kglobalacceld milou knighttime
Requires: polkit-kde-agent kactivitymanagerd plasma6-plasma5support
Requires: kwin kwin-x11
Requires: kf6-kirigami-addons
#Requires: kio-fuse
#Requires: vala-panel-appmenu-gtk-module

Source: %rname-%version.tar
Source1: freememorynotifier.po
Source2: libkicker-ru-add.po
Source3: plasma_lookandfeel_org.kde.lookandfeel-ru-add.po
#
Source11: freememorynotifier.tar
Source40: ssh-agent.conf
Source41: xdg-user-dirs.conf
Source42: obex.conf
#
Source51: dri_prime_available.cpp

Patch100: alt-startkde.patch
Patch101: alt-menu-add-tooltip.patch
Patch102: alt-bookmarks-browsers.patch
Patch103: alt-wait-drkonqi.patch
Patch104: alt-def-digital-clock.patch
Patch105: alt-menu-no-comment.patch
Patch106: alt-digital-clock-date.patch
Patch107: alt-freespacenotifier.patch
Patch108: alt-def-background.patch
Patch109: alt-def-start-empty-session.patch
Patch110: alt-check-donat-auth.patch
Patch111: alt-return-trash-desktop.patch
Patch112: alt-desktopnames.patch
Patch113: alt-menueditor.patch
Patch114: alt-menu-search-results-add-genericname.patch
Patch115: alt-zone-map-hide.patch
#
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
#
Patch143: alt-run-etc-profile.patch
Patch144: alt-def-lookandfeel.patch
Patch145: alt-add-dri-prime-to-menu.patch
Patch146: alt-fix-wallpaper-confirmation.patch
#
Patch150: alt-kcmusers-avatars.patch
Patch151: alt-manage-notification-thumbnail-display.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-location-devel qt6-phonon-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: qt6-wayland-devel qt6-5compat-devel qt6-shadertools-devel qt6-positioning-devel
BuildRequires: qcoro6-devel
BuildRequires: libudev-devel libpam0-devel zlib-devel libpolkitqt6-qt6-devel
BuildRequires: python3-devel libsystemd-devel
%if_enabled qalculate
BuildRequires: libqalculate-devel
%endif
%if_enabled appstream
BuildRequires: libappstream-qt6-devel
%endif
%if_disabled bootstrap
BuildRequires: kde6-libkexiv2-devel
%endif
BuildRequires: packagekit-qt6-devel
BuildRequires: libwayland-client-devel libwayland-server-devel libwayland-egl-devel
BuildRequires: wayland-protocols plasma-wayland-protocols
BuildRequires: libdrm-devel libcups-devel
BuildRequires: pipewire-libs-devel
BuildRequires: libxapian-devel libnm-devel libsysfs-devel fontconfig-devel libcanberra-devel
BuildRequires: libxcbutil-image-devel libxcbutil-devel libxcbutil-cursor-devel
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
BuildRequires: plasma6-plasma5support-devel plasma6-activities-stats-devel knighttime-devel
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
Requires: libkf6windowsystem kf6-kdeclarative kf6-kirigami
Requires: qml6(org.kde.plasma.components)
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

%package -n %libtaskmanager
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libtaskmanager
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

%package -n %libklipper
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libklipper
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

%package -n %libklookandfeel
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libklookandfeel
%name library


%prep
%setup -n %rname-%version
%patch100 -p1 -b .startkde
%patch101 -p1
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
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
#
%patch118 -p1
#%patch119 -p2
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
#
%patch143 -p1
%patch144 -p1
%patch145 -p1 -b .prime
%patch146 -p1
#
%patch150 -p1
%patch151 -p1

pwd
install -m0644 %SOURCE51 applets/kicker/

install -m 0644 %SOURCE1 po/ru/freememorynotifier.po
tar xf %SOURCE11 freememorynotifier/
msgcat --use-first po/ru/libkicker.po %SOURCE2 > po/ru/libkicker.po.tmp
cat po/ru/libkicker.po.tmp > po/ru/libkicker.po
rm -f po/ru/libkicker.po.tmp
msgcat --use-first po/ru/plasma_lookandfeel_org.kde.lookandfeel.po %SOURCE3 > po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp
cat po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp > po/ru/plasma_lookandfeel_org.kde.lookandfeel.po
rm -f po/ru/plasma_lookandfeel_org.kde.lookandfeel.po.tmp

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
for d in appstream services shell
do
    sed -i '/EnabledByDefault/s|false|true|' runners/${d}/plasma-runner-${d}.json
done
# disable some applets by default
for d in clipboard
do
    sed -i '/EnabledByDefault/s|true|false|' applets/${d}/metadata.json
done

%build
%K6build \
    -DINCLUDE_INSTALL_DIR=%_K6inc \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DUBUNTU_PACKAGEKIT:BOOL=OFF \
    -DGLIBC_LOCALE_GENERATED:BOOL=ON \
    -DGLIBC_LOCALE_GEN:BOOL=OFF \
    -DAppStreamQt_DIR:PATH=$PWD/cmake/AppStreamQt \
    -DPACKAGEKIT_OFFLINE_UPDATES:BOOL=ON \
    #

%install
%K6install
%K6install_move data kstyle solid kdevappwizard kpackage kglobalaccel
%K6install_move data desktop-directories doc kconf_update kio_desktop knsrcfiles
%K6install_move data kcontrol kdisplay kfontinst krunner konqsidebartng plasma/avatars locale
%K6install_move data plasma//nightcolor kio

# fix dbus service
sed -i 's|^Exec=.*|Exec=%_K6bin/krunner|' %buildroot/%_K6dbus_srv/org.kde.krunner.service

# add service alias
ALIAS=`grep '^Alias=' %buildroot/%_userunitdir/plasma-kcminit.service | tail -n 1 | sed 's|Alias=||'`
[ -n "$ALIAS" ] || exit 1
ln -s plasma-kcminit.service "%buildroot/%_userunitdir/$ALIAS"

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

# menu alternative
mv %buildroot/%_K6xdgmenu/plasma-applications.menu{,.plasma}
ln -sr %buildroot/%_K6xdgmenu/plasma-applications.menu{.plasma,}
mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name<<EOF
%_K6xdgmenu/plasma-applications.menu %_K6xdgmenu/plasma-applications.menu.plasma 10
%_K6xdgmenu/plasma-applications.menu %_xdgmenusdir/applications.menu 20
EOF

# systemd user service deps
mkdir -p %buildroot/%_userunitdir/plasma-core.target.d/
mkdir -p %buildroot/%_userunitdir/plasma-workspace@.target.d/
install -m0644 -p -D %SOURCE40 %buildroot/%_userunitdir/plasma-core.target.d/ssh-agent.conf
install -m0644 -p -D %SOURCE41 %buildroot/%_userunitdir/plasma-core.target.d/xdg-user-dirs.conf
install -m0644 -p -D %SOURCE42 %buildroot/%_userunitdir/plasma-core.target.d/obex.conf

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
%config(noreplace) %_altdir/%name
%config(noreplace) %x11confdir/wmsession.d/*PLASMA*
%config(noreplace) %_K6xdgmenu/plasma-applications.menu
%config(noreplace) %_K6xdgmenu/plasma-applications.menu.plasma
%_menudir/session
%dir %_K6plug/plasma/
%dir %_K6plug/plasma/*/
%_bindir/*
%_K6libexecdir/ba*
%_K6libexecdir/kfo*
%_K6libexecdir/ks*
%_K6libexecdir/p*
%_K6exec/kauth/*
%_K6conf_bin/*
%_K6plug/kf6/thumbcreator/
%_K6plug/plasma/*/*.so
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
%_K6plug/kcm_freememorynotifier.so
%_K6qml/org/kde/taskmanager/
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
%_K6data/kxmlgui?/kfontview/
%_K6data/kxmlgui?/kfontviewpart/
%_K6data/solid/actions/*.desktop
%dir %_K6data/timezonefiles/
%_K6data/timezonefiles/timezones.json
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
%_datadir/xdg-desktop-portal/kde-portals.conf

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
%_K6lib/cmake/Krdb/
%_K6dbus_iface/*.xml
#%_K6data/kdevappwizard/templates/*

%files -n %libkworkspace6
%_K6lib/libkworkspace6.so.*
%_K6lib/libkworkspace6.so.%sover
%files -n %libtaskmanager
%_K6lib/libtaskmanager.so.*
%_K6lib/libtaskmanager.so.%sover
%files -n %libklookandfeel
%_K6lib/libklookandfeel.so.*
%_K6lib/libklookandfeel.so.%sover
%files -n %libnotificationmanager
%_K6lib/libnotificationmanager.so.*
%_K6lib/libnotificationmanager.so.%notificationmanager_sover
%files -n %libkfontinst
%_K6lib/libkfontinst.so.*
%_K6lib/libkfontinst.so.%sover
%files -n %libkfontinstui
%_K6lib/libkfontinstui.so.*
%_K6lib/libkfontinstui.so.%sover
%files -n %libkrdb
%_K6lib/libkrdb.so.*
%_K6lib/libkrdb.so.%sover
%files -n %libklipper
%_K6lib/libklipper.so.*
%_K6lib/libklipper.so.%sover
%files -n %libbatterycontrol
%_K6lib/libbatterycontrol.so.*
%_K6lib/libbatterycontrol.so.%sover
%files -n %libkmpris
%_K6lib/libkmpris.so.*
%_K6lib/libkmpris.so.%sover


%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.6.5-alt2
- drop spice-vdagent.conf to fix startup spice-vdagent

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.6.3-alt1
- new version

* Thu Mar 19 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1:6.5.6-alt3
- reduce the size of thumbnails in notifications

* Thu Mar 12 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1:6.5.6-alt2
- optimize notification display

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.6-alt1
- new version

* Sun Feb 22 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.5-alt6
- fix icon for PRIME menu entry

* Thu Feb 19 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.5-alt5
- detect DRI PRIME via switcheroo-control

* Fri Jan 30 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.5-alt4
- don't enchance $XDG_CURRENT_DESKTOP

* Fri Jan 30 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.5-alt3
- prefer old main menu structure for smooth dist-upgrade

* Thu Jan 22 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.5-alt2
- fix requires

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 1:6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.4-alt1
- new version

* Fri Dec 05 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.3-alt5
- hide timezone selector map

* Thu Dec 04 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.3-alt4
- set plasma menu as altertative for altlinux-menus

* Fri Nov 28 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.3-alt3
- fix using kmenuedit with new menu

* Mon Nov 24 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.3-alt2
- package own plasma menu structure

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.6-alt1
- new version

* Wed Nov 05 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.5-alt5
- fix territorial affiliation in weather applet

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.5-alt4
- fix requires (closes: 56334)

* Mon Sep 29 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.5-alt3
- update requires

* Thu Sep 25 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.5-alt2
- enable packagekit integration

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.4-alt1
- new version

* Mon Jul 28 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.3-alt2
- fix requires for timezoneselector

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.4.2-alt1
- new version

* Thu Jun 05 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.5-alt2
- disable clipboard applet by default

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.5-alt1
- new version

* Wed Apr 23 2025 Oleg Solovyov <mcpain@altlinux.org> 1:6.3.4-alt2
- freememorynotifier: fix duplicating buttons (Closes: #53011)

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.4-alt1
- new version

* Thu Mar 27 2025 Oleg Solovyov <mcpain@altlinux.org> 1:6.3.3-alt3
- update freememorynotifer:
  + fix duplicating buttons (Closes: #53011)
  + show notifications from systemd-oomd

* Wed Mar 26 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.3-alt2
- don't force $XDG_CURRENT_DESKTOP if already suitable

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.3-alt1
- new version

* Fri Mar 07 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.2-alt3
- add yandex-browser and chromium-gost for bookmarks runner (closes: 53348)

* Wed Mar 05 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.2-alt2
- package systemd service alias (altbug#53246)

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.3.0-alt1
- new version

* Tue Feb 04 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.2.5-alt3
- fix applications menu actions (closes: 52907)

* Thu Jan 23 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.2.5-alt2
- don't force default desktop wallpaper

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 1:6.2.5-alt1
- new version

* Wed Dec 11 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.4-alt6
- wait drkonqi on logout

* Mon Dec 09 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.4-alt5
- return trash on desktop by default

* Mon Dec 02 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.4-alt4
- setup SSH_ASKPASS variable

* Mon Dec 02 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.4-alt3
- check donation autorized

* Thu Nov 28 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.4-alt2
- build with kexiv2

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.4-alt1
- new version

* Thu Nov 21 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.3-alt4
- exclude comments from menu entries
- restore menu entries tooltip support

* Wed Nov 20 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.3-alt3
- add fix against kdebug#490582 (closes: 51942)

* Fri Nov 15 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1:6.2.3-alt2
- fix loading into empty session (closes: 51942)

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.2.2-alt1
- new version

* Wed Oct 09 2024 Sergey V Turchin <zerg@altlinux.org> 1:6.1.5-alt2
- don't apply background on logout screen

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

