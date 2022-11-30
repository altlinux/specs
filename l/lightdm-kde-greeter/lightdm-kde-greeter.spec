%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: lightdm-kde-greeter
Version: 0.3.2.1
Release: alt8
Group: Graphical desktop/Other
Summary: LightDM KDE5 Greeter
License: GPL-3.0+
Url: http://git.altlinux.org/gears/l/lightdm-kde-greeter.git

Source: %name-%version.tar

Patch1: %name-%version-alt.patch

%K5init altplace

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-qml
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: lightdm-devel
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-declarative-devel qt5-tools-devel qt5-tools-devel-static
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kdeclarative-devel kf5-kiconthemes-devel kf5-plasma-framework-devel kf5-kconfig-devel kf5-ki18n-devel kf5-kauth-devel kf5-kconfigwidgets-devel
# deps of used stuff
BuildRequires: kf5-kcoreaddons-devel kf5-kpackage-devel kf5-kservice-devel

Requires: lightdm
Provides: lightdm-greeter

%qml_req_skipall 0
# QtQuick is not provided yet
%qml_add_req_skip QtQuick

%description
This package provides a KDE-based LightDM greeter engine.

This is a fork of KDE4-based LightDM greeter engine for KDE5.

%prep
%setup
%patch1 -p1

%build
%K5build

%install
%K5install

%find_lang --with-kde %name
%find_lang --with-kde --append --output=%name.lang kcm_lightdm
%find_lang --with-kde --append --output=%name.lang lightdm_theme_classic
%find_lang --with-kde --append --output=%name.lang lightdm_theme_userbar
%find_lang --with-kde --append --output=%name.lang desktop_playground-base_lightdm

# Add alternatives for xgreeters
mkdir -p %buildroot%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-kde-greeter.desktop\t300\n' > %buildroot%_altdir/lightdm-kde-greeter

%files -f %name.lang
%_altdir/lightdm-kde-greeter
%_sbindir/lightdm-kde-greeter
%_datadir/xgreeters/lightdm-kde-greeter.desktop
%_datadir/dbus-1/system.d/org.kde.kcontrol.kcmlightdm.conf
%_K5plug/kcm_lightdm.so
%_K5libexecdir/kauth/kcmlightdmhelper
%_K5libexecdir/lightdm-kde-greeter-rootimage
%_K5dbus_sys_srv/org.kde.kcontrol.kcmlightdm.service
%_datadir/lightdm-kde-greeter/
%_K5srv/kcm_lightdm.desktop
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmlightdm.policy

%changelog
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
