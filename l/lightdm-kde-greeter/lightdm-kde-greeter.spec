%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lightdm-kde-greeter
Version: 0.4.23
Release: alt11
Group: Graphical desktop/Other
Summary: LightDM KDE6 Greeter
License: GPL-3.0+
Url: https://invent.kde.org/plasma/lightdm-kde-greeter.git

Source: %name-%version.tar

Patch1: port-build-files-to-kde6.patch
Patch2: embed-liblightdm.patch
Patch3: port-to-kde6.patch
Patch4: move-kcm-module-qml-files.patch
Patch5: port-kcm-to-qt-6.patch
Patch6: remove-the-binding-loop-in-the-userslist-component.patch
Patch7: make-non-existent-default-index-in-listbutton.patch
Patch8: fix-networkmanager-widget-in-the-userbar-theme.patch
Patch9: bring-back-the-password-preview-button.patch
Patch10: provide-some-time-to-read-messages-from-pam.patch
Patch11: show-caps-lock-or-num-lock-enabled.patch

%K6init

BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-build-qml6
BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: lightdm-devel
BuildRequires: libgtk+2-devel
BuildRequires: libXrandr-devel
BuildRequires: qt6-base-devel qt6-declarative-devel qt6-tools-devel qt6-tools-devel qt6-5compat-devel qt6-shadertools-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kdeclarative-devel kf6-kiconthemes-devel plasma6-lib-devel kf6-kconfig-devel kf6-ki18n-devel kf6-kauth-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcmutils-devel
# deps of used stuff
BuildRequires: kf6-kcoreaddons-devel kf6-kpackage-devel kf6-kservice-devel
BuildRequires: kf6-networkmanager-qt-devel

Requires: lightdm
Requires: plasma-workspace-qml
Requires: polkit

Provides: lightdm-greeter

%description
This package provides a KDE-based LightDM greeter engine.

This is a fork of KDE4-based LightDM greeter engine for KDE6.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%K6build \
%_K6if_ver_gteq %ubt_id M110
        -DGREETER_WAYLAND_SESSIONS_FIRST=ON \
%endif
        -DGREETER_IMAGES_DIR=%_var/lib/ldm/%name/images

%install
%K6install
%K6install_move data kcm_lightdm kpackage

%find_lang --with-kde %name
%find_lang --with-kde --append --output=%name.lang kcm_lightdm
%find_lang --with-kde --append --output=%name.lang lightdm_kde_greeter
%find_lang --with-kde --append --output=%name.lang lightdm_theme_userbar

# Add alternatives for xgreeters
mkdir -p %buildroot%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-kde-greeter.desktop\t300\n' > %buildroot%_altdir/lightdm-kde-greeter

%files -f %name.lang
%config(noreplace) %_sysconfdir/lightdm/lightdm-kde-greeter.conf
%_altdir/lightdm-kde-greeter
%_sbindir/lightdm-kde-greeter
%_datadir/xgreeters/lightdm-kde-greeter.desktop
%_datadir/dbus-1/system.d/org.kde.kcontrol.kcmlightdm.conf
%_K6libexecdir/kf6/kauth/kcmlightdmhelper
%_K6libexecdir/lightdm-kde-greeter-rootimage
%_K6libexecdir/lightdm-kde-greeter-wifikeeper
%_K6dbus_sys_srv/org.kde.kcontrol.kcmlightdm.service
%_libexecdir/systemd/user/lightdm-kde-greeter-wifikeeper.service
%_datadir/lightdm-kde-greeter/
%_K6xdgapp/kcm_lightdm.desktop
%_K6plug/plasma/kcms/systemsettings/kcm_lightdm.so
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmlightdm.policy


%changelog
* Mon Oct 21 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt11
- show Caps Lock or Num Lock enabled

* Fri Oct 18 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt10
- provide some time to read messages from PAM (Closes: 51493)

* Thu Oct 10 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt9
- bring back the password preview button

* Mon Sep 30 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt8
- fix NetworkManager widget in the userbar theme

* Tue Sep 24 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt7
- fix that the last logged in user is not selected automatically
- fix empty session title

* Fri Sep 20 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt6
- set a nicer icon for the "log in" button
- better debug info
- port KCM to Qt 6 (Closes: 51186)

* Wed Sep 04 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt5
- fix FTBFS due to qml_req_skipall macro

* Thu Aug 15 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt4
- remove the link to the debug file
- fix PAM messages

* Tue Aug 13 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt3
- fix the main problems of the greeter after porting
- move embedding liblightdm into a separate patch

* Fri Jul 26 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt2
- port to kde6

* Wed May 29 2024 Anton Golubev <golubevan@altlinux.org> 0.4.23-alt1
- consider permissions and device availability in the NetworkManager
  widget
- add an option in the config to hide network widget
- show hostname in the upper left corner

* Tue May 28 2024 Anton Golubev <golubevan@altlinux.org> 0.4.22-alt2
- remerge upstream, further development will be on invent.kde.org

* Wed Apr 24 2024 Anton Golubev <golubevan@altlinux.org> 0.4.22-alt1
- use build-time set default background everywhere
- add default configuration file (Closes: 49221)
- remove altplace

* Fri Apr 19 2024 Anton Golubev <golubevan@altlinux.org> 0.4.21-alt1
- close menu when pressing side arrow (Closes: 48929)

* Thu Apr 18 2024 Anton Golubev <golubevan@altlinux.org> 0.4.20-alt1
- return to menu when pressing Enter (Closes: 48929)
- show Wayland sessions first in the session list, for p11+ (Closes: 49969)

* Mon Apr 15 2024 Anton Golubev <golubevan@altlinux.org> 0.4.19-alt1
- navigate buttons with arrows and activate by enter (Closes: 48929)

* Thu Jan 25 2024 Anton Golubev <golubevan@altlinux.org> 0.4.18-alt1
- re-layout PSK input dialog (Closes: 48123)
- make avatars more like locker in the breeze theme (Closes: 47950)
- add battery indicator to userbar theme
- move the "Log in as another user" to the center
- support "hide-users" hint

* Thu Sep 28 2023 Anton Golubev <golubevan@altlinux.org> 0.4.17-alt1
- Show tooltips for keyboard and session buttons (Closes: 46496)
- Cancel auth when click 'Log in as another user' (Closes: 47760)

* Fri Sep 01 2023 Anton Golubev <golubevan@altlinux.org> 0.4.16-alt1
- fix bug when changing background in KCM module

* Thu Aug 31 2023 Anton Golubev <golubevan@altlinux.org> 0.4.15-alt1
- create a prompt queue (Closes: 47377)
- update thumbnail
- small fixes

* Wed Aug 09 2023 Anton Golubev <golubevan@altlinux.org> 0.4.14-alt1
- always show the last logged in user on the userbar

* Tue Aug 01 2023 Anton Golubev <golubevan@altlinux.org> 0.4.13-alt1
- add basic wireless 802.1x support
- add a service to prolong wifi connection

* Mon Jun 26 2023 Anton Golubev <golubevan@altlinux.org> 0.4.12-alt1
- fix focus loss when typing PSK from virt. keyboard (Closes: 46499)
- activate new connection automatically (Closes: 46518)
- show hint for private connection (Closes: 46502)
- add a password re-entry dialog (Closes: 46514)
- handle deferred autologin (Closes: 46530)
- show error messages more correctly (Closes: 46525)
- fix letters creeping over the keyboard icon (Closes: 46500)
- show displayName in user's icon label (Closes: 46524)
- remove "classic" theme (Closes: 46533, 46534)
- use extra config file (Closes: 46606)

* Wed Jun 07 2023 Anton Golubev <golubevan@altlinux.org> 0.4.11-alt1
- add a widget to configure the network
- write the name of the last logged in user in the input field
  when clicking "log in as another user" (Closes: 46353)

* Fri Apr 28 2023 Anton Golubev <golubevan@altlinux.org> 0.4.10-alt1
- explicitly specify output names for screen scales

* Tue Apr 25 2023 Anton Golubev <golubevan@altlinux.org> 0.4.9-alt1
- apply scales to screens

* Wed Mar 29 2023 Anton Golubev <golubevan@altlinux.org> 0.4.8-alt1
- improve config handling
- bring the userbar theme closer visually to the design of the breeze theme

* Mon Mar 20 2023 Anton Golubev <golubevan@altlinux.org> 0.4.7-alt1
- bugfixes, update dependencies

* Tue Feb 21 2023 Anton Golubev <golubevan@altlinux.org> 0.4.6-alt1
- use Plasma's background selection dialog

* Mon Feb 13 2023 Anton Golubev <golubevan@altlinux.org> 0.4.5-alt1
- minor tweaks

* Mon Feb 06 2023 Anton Golubev <golubevan@altlinux.org> 0.4.4-alt1
- some improvements in the configuration module

* Thu Jan 26 2023 Anton Golubev <golubevan@altlinux.org> 0.4.3-alt1
- Rewrite configuration module to QML

* Tue Jan 17 2023 Anton Golubev <golubevan@altlinux.org> 0.4.2-alt1
- fix some minor bugs in 'userbar' theme

* Wed Jan 11 2023 Anton Golubev <golubevan@altlinux.org> 0.4.1-alt1
- improve behavior for multiple screens

* Mon Dec 12 2022 Anton Golubev <golubevan@altlinux.org> 0.4.0-alt1
- improve layout of the main theme 'userbar'
- simplify gear rules

* Wed Nov 30 2022 Sergey V Turchin <zerg@altlinux.org> 0.3.2.1-alt8
- fix to build with KF-5.100

* Mon Sep 19 2022 Sergey V Turchin <zerg@altlinux.org> 0.3.2.1-alt7
- fix to build with KF-5.98

* Mon Apr 04 2022 Slava Aseev <ptrnine@altlinux.org> 0.3.2.1-alt6
- Introduce virtual keyboard
- Fix FTBFS due to deprecated includes

* Tue Jan 11 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2.1-alt5
- Updated userbar theme to allow logging in even if username is not listed.

* Tue Jul 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2.1-alt4
- Ported to Qt5/KDE5.

* Mon Mar 31 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.2.1-alt3
- rebuild with liblightdm-qt-3.pc

* Wed Jun 05 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.2.1-alt2
- fix requires (ALT#29053)

* Thu May 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.2.1-alt1
- new version

* Fri Feb 01 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt2
- fix requires

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Wed Jul 25 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- initial build
