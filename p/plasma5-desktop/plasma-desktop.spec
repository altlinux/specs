%define rname plasma-desktop
%def_disable scim

Name: plasma5-desktop
Version: 5.27.3
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 plasma desktop view furniture
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: plasma5-workspace
Requires: polkit-kde-plasma-desktop
# for ibus-ui-emojier-plasma
Requires: ibus-dicts

Source: %rname-%version.tar
Source10: kcm_multicomponentchooser-ru-add.po
Source11: kcm_touchpad-ru-add.po
Source1: multicomponentchooser.tar
Patch2: alt-menu-icon.patch
Patch3: alt-def-apps-menu.patch
Patch4: alt-def-kicker.patch
Patch5: alt-multimedia-player-chooser.patch
Patch6: alt-def-panel.patch
Patch7: alt-def-desktop-containment.patch
Patch8: alt-def-desktop-widgets.patch
Patch10: alt-def-session.patch
Patch11: alt-def-key-numlock.patch
Patch12: alt-def-layout-indicator.patch
Patch13: alt-def-taskman.patch
Patch14: alt-def-desktop-icons.patch
Patch15: alt-menu-add-tooltip.patch
Patch16: alt-kicker-custom-btn-img-size.patch
Patch17: alt-users-use-gost-yescrypt.patch
Patch18: alt-kxkb-indicator-uppercase.patch
#
Patch20: alt-knetattach-test-unlock-ui.patch
# Fix bug #42348
Patch21: alt-re-set-xkb-mappings.patch
Patch22: alt-i18n.patch
Patch23: alt-handle-etc-x11-xinit-xkbmap.patch

# Automatically added by buildreq on Mon Mar 23 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libdbusmenu-qt52 libfreetype-devel libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libusb-compat libxcb-devel libxcbutil-image libxcbutil-keysyms libxkbfile-devel mkfontscale pkg-config python-base qt5-base-devel rpm-build-gir ruby ruby-stdlibs xml-common xml-utils xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ iceauth kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libksysguard-devel kf5-plasma-framework-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel libxcbutil-image-devel mkfontdir python-module-google qt5-declarative-devel qt5-phonon-devel qt5-svg-devel qt5-x11extras-devel rpm-build-ruby xset
BuildRequires(pre): rpm-build-kf5
BuildRequires: rpm-build-python3
BuildRequires: boost-devel extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel qt5-phonon-devel qt5-svg-devel qt5-x11extras-devel
%if_enabled scim
BuildRequires: scim-devel
%endif
BuildRequires: libibus-devel libgio-devel glib2-devel
BuildRequires: packagekit-qt-devel
BuildRequires: libudev-devel
BuildRequires: libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel
BuildRequires: libxcbutil-devel libxcbutil-image-devel libxkbcommon-devel
BuildRequires: xorg-drv-synaptics-devel xorg-sdk xorg-drv-evdev-devel xkeyboard-config-devel xorg-drv-libinput-devel
BuildRequires: iceauth mkfontdir xset /usr/bin/intltool-merge
BuildRequires: wayland-devel qt5-wayland-devel wayland-protocols kde5-plasma-wayland-protocols
BuildRequires: accounts-qt5-devel kde5-kaccounts-integration-devel signon-devel
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel
BuildRequires: kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel plasma5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel plasma5-libksysguard-devel
BuildRequires: kf5-plasma-framework-devel plasma5-workspace-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kdeclarative-devel kf5-kpeople-devel kf5-kactivities-stats-devel
BuildRequires: kf5-kded kf5-kded-devel plasma5-kscreenlocker-devel plasma5-breeze-devel

Provides: kf5-plasma-desktop = %EVR
Obsoletes: kf5-plasma-desktop < %EVR

%description
Plasma desktop view furniture.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-plasma-desktop-common = %EVR
Obsoletes: kf5-plasma-desktop-common < %EVR
%description common
%name common package

%package maxi
Summary: %name maximum package
Group: System/Configuration/Packaging
Requires: %name
%description maxi
%name maximum package.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Provides: kf5-plasma-desktop-devel = %EVR
Obsoletes: kf5-plasma-desktop-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n polkit-kde-plasma-desktop
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common
Requires: polkit-kde-plasma-workspace
Provides: polkit-kde-kcmclock
%description -n polkit-kde-plasma-desktop
Common polkit files for %name


%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
# use-gost-yescrypt
#%patch17 -p1
%patch18 -p1
#
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

msgcat --use-first po/ru/kcm_componentchooser.po %SOURCE10 > po/ru/kcm_multicomponentchooser.po
cat po/ru/kcm_multicomponentchooser.po > po/ru/kcm_componentchooser.po
msgcat --use-first po/ru/kcm_touchpad.po %SOURCE11 > po/ru/kcm_touchpad.po.tmp
cat po/ru/kcm_touchpad.po.tmp >po/ru/kcm_touchpad.po
rm -f po/ru/kcm_touchpad.po.tmp

pushd kcms
    tar xvf %SOURCE1
popd

# disable krunners by default
for d in runners/*/*.json ; do
    sed -i '/EnabledByDefault/s|true|false|' $d
done
# enable some krunners by default
for d in plasma-desktop
do
    sed -i '/EnabledByDefault/s|false|true|' runners/${d}/plasma-runner-${d}.json
done

#Fix translate in Input Method Panel (kimpanel) widget.
#If the po-file is called differently than "plasma_applet_org.kde.plasma.kimpanel.po", the kimpanel widget menu will be in English only.
#find po/ -maxdepth 2 -name plasma_applet_org.kde.kimpanel.po -type f -exec rename plasma_applet_org.kde.kimpanel.po plasma_applet_org.kde.plasma.kimpanel.po '{}' \;

%build
%K5cmake \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    #
%K5make

%install
%K5install

%K5install_move data color-schemes doc kcmmouse knsrcfiles kglobalaccel
%K5install_move data kcm_componentchooser kcminput kcmkeyboard kcmkeys kcm_phonon kcmsolidactions
%K5install_move data kcontrol ksmserver kconf_update solid kpackage
%K5install_move data plasma/desktoptheme plasma/plasmoids/touchpad plasma/emoji

%find_lang %name --with-kde --all-name


%files common -f %name.lang
%doc LICENSES/*
%_datadir/locale/*/LC_SCRIPTS/kfontinst/
%_K5icon/*/*/*/*.*
%_datadir/qlogging-categories5/*.*categories

%files
%_K5dbus/system.d/*.conf
%_K5bin/*
%exclude %_K5bin/*emojier*
%_K5exec/*
%_K5libexecdir/kauth/*
%_K5plug/*.so
%_K5plug/kcms/*.so
%_K5plug/kf5/kded/*.so
%_K5plug/kf5/krunner/*.so
%_K5plug/plasma/dataengine/*.so
%_K5plug/plasma/kcminit/
%_K5plug/plasma/kcms/*/*.so
%_K5qml/org/kde/activities/settings/
%_K5qml/org/kde/plasma/private/*/
%_K5qml/org/kde/private/*/
%_K5qml/org/kde/plasma/activityswitcher/
%_K5qml/org/kde/plasma/emoji/
%_K5xdgapp/*
%exclude %_K5xdgapp/*emojier*
%_K5start/*.desktop
%_K5cfg/*
%_K5conf_up/*
%_K5srv/*.desktop
%_K5srvtyp/*.desktop
%_K5notif/*
%_K5data/solid/devices/solid-*.desktop
%_K5data/kcm*/
%_K5data/kactivitymanagerd/
%_K5data/kpackage/kcms/*
%_K5data/plasma/emoji/
%_K5data/plasma/plasmoids/*
%_K5data/plasma/packages/*
%_K5data/plasma/layout-templates/*
%_K5data/plasma/shells/*/
%_K5data/plasma/services/*
%_K5data/plasma/desktoptheme/default/icons/*
%_K5data/kglobalaccel/*.desktop
%exclude %_K5data/kglobalaccel/*emojier*.desktop
%_K5data/knsrcfiles/*.knsrc
%_K5dbus_sys_srv/*.service
%_datadir/accounts/providers/kde/*.provider
%_datadir/accounts/services/kde/*.service

%files maxi
%_K5bin/*emojier*
%_K5xdgapp/*emojier*
%_K5data/kglobalaccel/*emojier*.desktop

%files -n polkit-kde-plasma-desktop
%_datadir/polkit-1/actions/*kcmclock*.policy

%files devel
#%_K5link/lib*.so
%_K5dbus_iface/*.xml

%changelog
* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Tue Feb 21 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt3
- show tooltips when hovering task buttons by default

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt2
- build without scim

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Thu Dec 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt2
- don't show tooltips when hovering task buttons by default

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Oct 26 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt2
- disable knetattach connection test because dialogs blocks ui with new KIO

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Fri Jul 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt4
- rebuild

* Mon Jul 25 2022 Slava Aseev <ptrnine@altlinux.org> 5.24.6-alt3
- Handle /etc/X11/xinit/Xkbmap (closes: 42348, 41709, 42790)

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt2
- fix translation of "No touchpad was found"

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed Jul 06 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt3
- fix translation of "No touchpad found"

* Mon Jul 04 2022 Slava Aseev <ptrnine@altlinux.org> 5.24.5-alt2
- re-set xkb mappings after attaching any input device (closes: 42348)

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Wed Feb 16 2022 Oleg Solovyov <mcpain@altlinux.org> 5.23.5-alt5
- apply screen mapper fix from upstream (Closes: #41914)

* Wed Feb 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt4
- don't add tablet mode button to default panel

* Wed Feb 02 2022 Oleg Solovyov <mcpain@altlinux.org> 5.23.5-alt3
- Fix patch against bug 41564

* Thu Jan 13 2022 Oleg Solovyov <mcpain@altlinux.org> 5.23.5-alt2
- Apply QKeySequence patch against KF 5.90

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 29 2021 Oleg Solovyov <mcpain@altlinux.org> 5.23.4-alt3
- Fix swapping icons when choosing kicker alternatives (Closes: #41564)

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt2
- fix package icons

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Fri Nov 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt5
- add tablet mode button to default panel

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt4
- reserve more space for desktop icons text by default

* Thu Nov 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt3
- fix mediaplayers chooser translation

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt2
- translate mediaplayers chooser into russian

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Aug 31 2021 Oleg Solovyov <mcpain@altlinux.org> 5.22.4-alt2
- make "Show Desktop" widget opaque

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Wed Jun 02 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt3
- arrange desktop icons by columns by default

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt2
- split ibus emojier into separate subpackage

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Wed Apr 28 2021 Oleg Solovyov <mcpain@altlinux.org> 5.21.4-alt6
- Calculate cursor position relative to top-left corner of current screen

* Mon Apr 26 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt5
- don't arrange desktop icons by columns by default

* Wed Apr 14 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt4
- fix crash in media players chooser

* Wed Apr 14 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt3
- fix to show selected media players

* Tue Apr 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt2
- readd default media players chooser

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Thu Apr 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt2
- update improved performance of task groups patch (thanks darktemplar@alt)

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version
- improved performance of task groups (thanks darktemplar@alt)

* Thu Mar 18 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt4
- fix default desktop mouse middle-button action

* Thu Mar 04 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt3
- set default main menu button icon

* Tue Feb 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt2
- fix taskmanager group mouseclick action to show apps list

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- new version

* Fri Nov 20 2020 Slava Aseev <ptrnine@altlinux.org> 5.20.2-alt3
- Use gost-yescrypt password hashing instead of SHA-512

* Tue Nov 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt2
- don't increase kicker button size when custom icon selected

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt1
- new version

* Mon Oct 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt3
- show apps from all desktops on tasks panel by default (closes: 39092)

* Fri Sep 25 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt2
- fix defalut multimedia players chooser

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.4-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt2
- support chromium-gost in favorites menu

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Tue Apr 21 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt2
- fix requires

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Apr 01 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt3
- disable plasma krunner plugin by default

* Fri Mar 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt2
- improve taskmanager defaults

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 20 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt2
- add main menu items tooltip

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Tue Jul 02 2019 Ivan Razzhivin <underwit@altlinux.org> 5.16.2-alt2
- fix patch alt-menu-add-tooltip.patch

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Wed Apr 10 2019 Pavel Moseev <mars@altlinux.org> 5.12.8-alt3
- fix translate in Input Method Panel (kimpanel) widget

* Tue Apr 02 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- fix menu settings russian translation

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Wed Feb 13 2019 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt7
- plasmashell: filter out items from disabled folderviews

* Mon Jan 14 2019 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt6
- use better patch from upstream

* Thu Dec 27 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt5
- plasmashell: fix moving icons when we're overlapping with existing ones

* Thu Dec 20 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt4
- plasmashell: no more phantom icons after creating something on a fresh desktop
- plasmashell: create new icons in place

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt3
- disable kwin runner by default

* Tue Oct 02 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt2
- plasmashell: fix moving icons between separate desktops on different monitors
- plasmashell: fix incorrect behavior after creating folders

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Tue Sep 11 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.6-alt4
- systemsettings: fix locales preview

* Tue Sep 4 2018 Ivan Razzhivin <underwit@altlinux.org> 5.12.6-alt3
- fix tooltip for appentry

* Fri Aug 31 2018 Ivan Razzhivin <underwit@altlinux.org> 5.12.6-alt2
- add tooltip for appentry

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon May 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- add fix against KDEBUG-394013

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2
- add Falkon to favorite menu apps

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt2
- exclude krb5-ticket-watcher from saved session by default

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2
- renamed kf5-plasma-desktop -> plasma5-desktop

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt2
- apply fix against KDEBUG-378262 (ALT#33663)

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1
- new version

* Fri Jun 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2
- add application generic name to kikoff menu search results

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt2
- fix taskmanager for Qt 5.6

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt4.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt5
- show name and generic name in main menu by default

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2.M80P.1
- build for M80P

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt3
- add Places widget to panel by default

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1.M80P.1
- build for M80P

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2
- fix default panel with absent widget

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Sep 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt4
- fix kicker menu width

* Wed Sep 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt3
- fix kicker menu width

* Tue Sep 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt2
- set kicker main menu by default

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt2
- update menu default favorites

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Tue Apr 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt2
- set default keyboard layout swithcing policy

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt3
- update menu favorites defaults

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt2
- update requires

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- update kbd defaults

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt3
- return set of available languages list by systemsettings translations

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt2
- start empty session by default

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Mon Dec 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt3
- fix menu default apps

* Wed Dec 23 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- simplify menu favorites apps patch

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Tue Oct 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt3
- set desktop defaults

* Fri Oct 23 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- set panel defaults

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Sep 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt4
- add default multimedia players chooser

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt3
- fix languages list in translations settings

* Fri Sep 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt2
- set default favorites menu apps

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt4
- rebuild with new baloo

* Mon Jul 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt3
- return default menu icon

* Fri Jul 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- set default menu icon

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Fri May 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- update from Plasma/5.3 branch

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
