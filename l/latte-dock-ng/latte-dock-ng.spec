%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define oname latte-dock
%set_verify_elf_method strict

Name: latte-dock-ng
Version: 1.1.12
Release: alt1
Summary: Fork of Latte Dock - a dock based on plasma frameworks

License: GPLv2+
Group: Graphical desktop/KDE
Url: https://github.com/ruizhi-lab/latte-dock-ng
Packager: Artyom Bystrov <arbars@altlinux.org>

Conflicts: %oname
Obsoletes: %oname
Provides: %oname = %EVR

# Source-url: https://download.kde.org/stable/latte-dock/latte-dock-%version.tar.xz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-kf6 rpm-build-xdg
BuildRequires: xdg-utils  libpcre2-devel libffi-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: cmake
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: libSM-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-x11extras-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ksvg-devel
BuildRequires: kf6-karchive-devel
BuildRequires: plasma6-activities-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel kf6-kdeclarative
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: qt5-base-devel
BuildRequires: plasma6-kwayland-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: plasma6-libksysguard-devel
BuildRequires: kf6-kservice-devel
# BuildRequires: kf6-plasma-framework-devel
BuildRequires: plasma-workspace-devel
BuildRequires: plasma6-lib-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel qt5-declarative-devel
BuildRequires: kde5-plasma-wayland-protocols
BuildRequires: bzlib-devel
BuildRequires: libwayland-egl-devel
BuildRequires: plasma6-activities-stats-devel

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%prep
%setup

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K6bin/%name
%_datadir/metainfo/org.kde.%oname.appdata.xml
%_datadir/metainfo/org.kde.latte.plasmoid.appdata.xml
%_datadir/metainfo/org.kde.latte.shell.appdata.xml
%_datadir/metainfo/org.kde.latte.separator.appdata.xml
%_K6xdgapp/org.kde.%oname.desktop
%_K6data/dbus-1/interfaces/org.kde.LatteDock.xml
%_K6icon/breeze/*/*/*
%_K6icon/hicolor/*/*/*
%_datadir/knotifications6/lattedock.notifyrc
%_datadir/kservicetypes6/latte-indicator.desktop
%_datadir/plasma/plasmoids/org.kde.latte.containment/
%_datadir/plasma/plasmoids/org.kde.latte.plasmoid/
%_datadir/plasma/shells/org.kde.latte.shell/
%_datadir/plasma/plasmoids/org.kde.latte.separator/contents/ui/main.qml
%_datadir/plasma/plasmoids/org.kde.latte.separator/metadata.json
%_datadir/latte
%_qt6_qmldir/org/kde/latte
%_qt6_qmldir/org/kde/plasma/private/taskmanager/.latte-fallback-module
%_qt6_qmldir/org/kde/plasma/private/taskmanager/Backend.qml
%_qt6_qmldir/org/kde/plasma/private/taskmanager/SmartLauncherItem.qml
%_qt6_qmldir/org/kde/plasma/private/taskmanager/qmldir
%_qt6_plugindir/plasma/containmentactions/org.kde.latte.contextmenu.so
%_qt6_plugindir/kpackage/packagestructure/latte_indicator.so
%_datadir/knsrcfiles/latte-layouts.knsrc
%_datadir/knsrcfiles/latte-indicators.knsrc

%changelog
* Tue Jun  2 2026 Artyom Bystrov <arbars@altlinux.org> 1.1.12-alt1
- initial build for ALT Sisyphus
