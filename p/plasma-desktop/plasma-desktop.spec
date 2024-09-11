%define rname plasma-desktop
%def_disable scim
%def_disable accounts

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma 6 desktop view furniture
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: plasma-workspace
Requires: polkit-kde-plasma-desktop
# for ibus-ui-emojier-plasma
Requires: ibus-dicts
Requires: fonts-ttf-google-noto-emoji-color
Requires: /usr/bin/xdg-user-dir
Requires: kf6-kirigami kf6-kirigami-addons kf6-qqc2-desktop-style plasma6-kpipewire
Requires: switcheroo-control

Provides: plasma5-desktop = %EVR
Obsoletes: plasma5-desktop < %EVR
Provides: plasma5-desktop-maxi = %EVR
Obsoletes: plasma5-desktop-maxi < %EVR

Source: %rname-%version.tar
Source11: kcm_touchpad-ru-add.po
Patch1: alt-def-color-scheme.patch
Patch2: alt-menu-icon.patch
Patch3: alt-def-apps-menu.patch
Patch4: alt-def-kicker.patch
#
Patch6: alt-def-panel.patch
Patch7: alt-singleclick.patch
#
Patch9: alt-dont-indicate-audio-on-taskbar.patch
Patch10: alt-def-session.patch
Patch11: alt-def-key-numlock.patch
Patch12: alt-def-layout-indicator.patch
Patch13: alt-def-taskman.patch
Patch14: alt-def-desktop-icons.patch
Patch15: alt-menu-add-tooltip.patch
Patch16: alt-kicker-custom-btn-img-size.patch
#
Patch18: alt-keyboard-indicator-uppercase.patch
Patch19: alt-def-screenreader.patch
Patch20: alt-knetattach-test-unlock-ui.patch
# Fix bug #42348
Patch21: alt-re-set-xkb-mappings.patch
Patch22: alt-kscreenlocker.patch
Patch23: alt-screenlocker-prompt-in-placeholder.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-python3
BuildRequires: boost-devel extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-phonon-devel qt6-svg-devel qt6-5compat-devel
%if_enabled scim
BuildRequires: scim-devel
%endif
BuildRequires: libibus-devel libgio-devel glib2-devel
BuildRequires: packagekit-qt6-devel
BuildRequires: libudev-devel libSDL2-devel
BuildRequires: libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel
BuildRequires: libxkbcommon-devel libxkbfile-devel
BuildRequires: libXi-devel libXcursor-devel libXrender-devel libXft-devel
BuildRequires: libxcbutil-devel libxcbutil-image-devel libxcbutil-keysyms-devel
BuildRequires: xorg-drv-synaptics-devel xorg-sdk xorg-drv-evdev-devel xkeyboard-config-devel xorg-drv-libinput-devel
BuildRequires: iceauth mkfontdir xset /usr/bin/intltool-merge
BuildRequires: wayland-devel qt6-wayland-devel wayland-protocols plasma-wayland-protocols
BuildRequires: libvulkan-devel
BuildRequires: accounts-qt6-devel
%if_enabled accounts
BuildRequires: signon-devel kaccounts-integration-devel
%endif
BuildRequires: kf6-baloo-devel kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel
BuildRequires: kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-ksvg-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kpackage-devel kf6-kparts-devel
BuildRequires: kf6-krunner-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kwin-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kdeclarative-devel kf6-kpeople-devel
BuildRequires: kf6-kded-devel
BuildRequires: plasma6-lib-devel
BuildRequires: plasma-workspace-devel kscreenlocker-devel plasma6-breeze-devel plasma6-activities-stats-devel
BuildRequires: plasma6-libksysguard-devel plasma6-activities-devel plasma6-plasma5support-devel

%description
Plasma desktop view furniture.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-desktop-common = %EVR
Obsoletes: plasma5-desktop-common < %EVR
%description common
%name common package

%package -n plasma5-desktop
Group: System/Configuration/Other
Summary: Compatibility package
Requires: plasma-desktop >= %version-%release
%description -n plasma5-desktop
Compatibility package.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n polkit-kde-plasma-desktop
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common >= %EVR
Requires: polkit-kde-plasma-workspace
%description -n polkit-kde-plasma-desktop
Common polkit files for %name

%package -n sddm-theme-breeze
Epoch: 1
Group: Graphical desktop/KDE
Summary: SDDM breeze theme
Requires: %name-common >= %version-%release
Requires: qt6-5compat kf6-kirigami plasma-workspace-qml
Buildarch: noarch
%description -n sddm-theme-breeze
SDDM breeze theme


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#
%patch6 -p1
%patch7 -p1
#
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
#
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

msgcat --use-first po/ru/kcm_touchpad.po %SOURCE11 > po/ru/kcm_touchpad.po.tmp
cat po/ru/kcm_touchpad.po.tmp >po/ru/kcm_touchpad.po
rm -f po/ru/kcm_touchpad.po.tmp

# disable krunners by default
for d in runners/*/*.json ; do
    sed -i '/EnabledByDefault/s|true|false|' $d
done
# enable some krunners by default
for d in plasma-desktop
do
    sed -i '/EnabledByDefault/s|false|true|' runners/${d}/plasma-runner-${d}.json
done

%build
%K6cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    #
%K6make

%install
%K6install

%K6install_move data color-schemes doc kcmmouse knsrcfiles kglobalaccel
%K6install_move data kcm_componentchooser kcminput kcmkeyboard kcmkeys kcm_phonon kcmsolidactions
%K6install_move data kcontrol ksmserver kconf_update solid kpackage
%K6install_move data plasma/desktoptheme plasma/plasmoids/touchpad plasma/emoji

%find_lang %name --with-kde --all-name


%files common -f %name.lang
%doc LICENSES/*
%_datadir/locale/*/LC_SCRIPTS/kfontinst/
%_K6icon/*/*/*/*.*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6dbus/system.d/*.conf
%_K6bin/*
%exclude %_K6bin/*emojier*
%_K6libexecdir/ki*
%_K6exec/kauth/*
%_K6plug/kf6/kded/*.so
%_K6plug/kf6/krunner/*.so
%_K6plug/plasma/kcminit/
%_K6plug/plasma/kcms/*/*.so
%_K6qml/org/kde/plasma/private/*/
%_K6qml/org/kde/private/*/
%_K6qml/org/kde/plasma/activityswitcher/
%_K6qml/org/kde/plasma/emoji/
%_K6xdgapp/*
%_K6start/*.desktop
%_K6cfg/*
%_K6notif/*
%_K6data/solid/devices/solid-*.desktop
%_K6data/kcm*/
%_K6data/plasma/emoji/
%_K6data/plasma/plasmoids/*
%_K6data/plasma/packages/*
%_K6data/plasma/layout-templates/*
%_K6data/plasma/shells/*/
%_K6data/kglobalaccel/*.desktop
%_K6data/knsrcfiles/*.knsrc
%_K6dbus_sys_srv/*.service
%if_enabled accounts
%_datadir/accounts/providers/kde/*.provider
%_datadir/accounts/services/kde/*.service
%endif
%_datadir/metainfo/*.xml

%files -n polkit-kde-plasma-desktop
%_datadir/polkit-1/actions/*kcmclock*.policy

%files -n sddm-theme-breeze
%_datadir/sddm/themes/breeze/

%files devel
#%_K6link/lib*.so
%_K6dbus_iface/*.xml



%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Sep 05 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt4
- screenlocker fixes:
  + do not activate multiple mouse areas
  + switch areas by following mouse pointer
  + make cursor visible on inactive mouse areas
  + restart fade timer on switching displays

* Mon Sep 02 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt3
- show PAM prompt in screenlocker theme (Closes: #50970)

* Fri Aug 30 2024 Oleg Solovyov <mcpain@altlinux.org> 6.1.4-alt2
- fix kscreenlocker theme

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

