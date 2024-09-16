%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: latte-dock
Version: 0.10.9
Release: alt3
Summary: Latte is a dock based on plasma frameworks

License: GPLv2+
Group: Graphical desktop/KDE
Url: https://download.kde.org/stable/%name
Packager: Artyom Bystrov <arbars@altlinux.org>

# Source-url: https://download.kde.org/stable/latte-dock/latte-dock-%version.tar.xz
Source: %name-%version.tar
Patch: K5bin.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-kf5 rpm-build-xdg
BuildRequires: xdg-utils
BuildRequires: libxdg-basedir-devel
BuildRequires: cmake
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: libSM-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-x11extras-devel
BuildRequires: kf5-kirigami-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: qt5-base-devel
BuildRequires: kf5-kwayland-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: plasma6-libksysguard-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-plasma-framework-devel

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%prep
%setup
%patch -p2

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/%name
%_datadir/metainfo/org.kde.%name.appdata.xml
%_datadir/metainfo/org.kde.latte.plasmoid.appdata.xml
%_datadir/metainfo/org.kde.latte.shell.appdata.xml
%_K5xdgapp/org.kde.%name.desktop
%_K5data/dbus-1/interfaces/org.kde.LatteDock.xml
%_K5icon/breeze/*/*/*
%_K5icon/hicolor/*/*/*
%_datadir/knotifications5/lattedock.notifyrc
%_K5srv/plasma-containmentactions-lattecontextmenu.desktop
%_datadir/kservicetypes5/latte-indicator.desktop
%_kf5_data/plasma/plasmoids/org.kde.latte.containment/
%_kf5_data/plasma/plasmoids/org.kde.latte.plasmoid/
%_kf5_data/plasma/shells/org.kde.latte.shell/
%_datadir/latte
%_qt5_qmldir/org/kde/latte
%_qt5_plugindir/plasma_containmentactions_lattecontextmenu.so
%_qt5_plugindir/kpackage/packagestructure/latte_packagestructure_indicator.so
%_datadir/knsrcfiles/latte-layouts.knsrc
%_datadir/knsrcfiles/latte-indicators.knsrc
%_K5srv/plasma-applet-org.kde.latte.containment.desktop
%_K5srv/plasma-applet-org.kde.latte.plasmoid.desktop
%_K5srv/plasma-shell-org.kde.latte.shell.desktop

%changelog
* Mon Sep 16 2024 Artyom Bystrov <arbars@altlinux.org> 0.10.9-alt3
- NMU: Fixed build with plasma6-libksysguard-devel

* Tue Nov 14 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.9-alt2
- NMU: Fixed build with new rpm-build-kf5.

* Thu Aug 17 2023 Mikhail Tergoev <fidel@altlinux.org> 0.10.9-alt1
- NMU: new version (0.10.9) with rpmgs script (ALT bug 47233)

* Mon Jan 31 2022 Konstantin Rybakov <kastet@altlinux.org> 0.10.8-alt1
- Updated to upstream version 0.10.8

* Tue Jan 18 2022 Konstantin Rybakov <kastet@altlinux.org> 0.10.7-alt1
- Updated to upstream version 0.10.7

* Wed Dec 29 2021 Konstantin Rybakov <kastet@altlinux.org> 0.10.6-alt1
- Updated to upstream version 0.10.6
- Restore package service files

* Fri Dec 17 2021 Konstantin Rybakov <kastet@altlinux.org> 0.10.5-alt1
- Updated to upstream version 0.10.5

* Mon Dec 06 2021 Konstantin Rybakov <kastet@altlinux.org> 0.10.4-alt1
- Updated to upstream version 0.10.4

* Mon Nov 15 2021 Konstantin Rybakov <kastet@altlinux.org> 0.10.3-alt1
- Updated to upstream version 0.10.3

* Tue Oct 12 2021 Konstantin Rybakov <kastet@altlinux.org> 0.10.2-alt1
- Updated to upstream version 0.10.2

* Mon Aug 09 2021 Artyom Bystrov <arbars@altlinux.org> 0.10.0-alt1
- Updated to upstream version 0.10.0

* Fri Jul 16 2021 Konstantin Rybakov <kastet@altlinux.org> 0.9.12-alt1
- Updated to upstream version v0.9.12
- Fix package service files

* Tue Apr 06 2021 Konstantin Rybakov <kastet@altlinux.org> 0.9.11-alt3
- Add translation files.
- Change source URL.

* Wed Mar 24 2021 Konstantin Rybakov <kastet@altlinux.org> 0.9.11-alt2
- Fix desktop file

* Sat Mar 13 2021 Konstantin Rybakov <kastet@altlinux.org> 0.9.11-alt1
- Updated to upstream version v0.9.11

* Sun Mar 01 2020 Artyom Bystrov <arbars@altlinux.org> 0.9.9-alt1
- initial build for ALT Sisyphus
