%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%def_with check

Name: fancontrol-gui
Version: 0.8
Release: alt1.git.c752e3b

Summary: GUI for the fancontrol script and systemd service
License: GPL-2.0-or-later
Group: Monitoring
Url: https://github.com/Maldela/fancontrol-gui

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-macros-qt5

BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kirigami
BuildRequires: qt5-quickcontrols
BuildRequires: qt5-quickcontrols2
BuildRequires: libqt5-qml
BuildRequires: libkf5plasmaquick

%if_with check
BuildRequires: ctest
%endif

Requires: lm_sensors3-utils
Requires: kf5-kirigami
Requires: qt5-quickcontrols
Requires: qt5-quickcontrols2
Requires: libqt5-qml
Requires: libkf5plasmaquick

%description
GUI for Fancontrol. It uses the KAuth module of the KDE Frameworks 5
to write the generated config file. Furthermore it communicates with
systemd via dbus to control the fancontrol service.

%prep
%setup
mv -v readMe.MD README.md
sed -i "s|Categories=.*|Categories=Qt;KDE;Monitor;System;|" fancontrol-gui/org.kde.fancontrol.gui.desktop
sed -i "s/0.7/%version/" fancontrol-gui/src/main.cpp

%build
%cmake \
      -DKDE_INSTALL_USE_QT_SYS_PATHS=On \
%if_with check
      -DBUILD_TESTING=On
%else
      -DBUILD_TESTING=Off
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --all-name --with-kde

%check
%ctest

%files -f %{name}.lang
%doc LICENSE README.md
%_bindir/fancontrol_gui
%dir %_qt5_qmldir/Fancontrol
%_qt5_qmldir/Fancontrol/*
%_libexecdir/kauth/fancontrol_gui-helper
%_desktopdir/org.kde.fancontrol.gui.desktop
%_datadir/dbus-1/system-services/org.kde.fancontrol.gui.helper.service
%_datadir/dbus-1/system.d/org.kde.fancontrol.gui.helper.conf
%_iconsdir/hicolor/scalable/apps/org.kde.fancontrol.gui.svg
%dir %_datadir/kpackage/genericqml/org.kde.fancontrol.gui
%_datadir/kpackage/genericqml/org.kde.fancontrol.gui/*
%_datadir/metainfo/org.kde.fancontrol.gui.appdata.xml
%_datadir/polkit-1/actions/org.kde.fancontrol.gui.helper.policy

%changelog
* Sun Mar 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.8-alt1.git.c752e3b
- Initial build for Sisyphus
