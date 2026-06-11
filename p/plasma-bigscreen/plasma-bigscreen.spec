%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _udevrulesdir /lib/udev/rules.d

Name: plasma-bigscreen
Version: 6.6.91
Release: alt2

Summary: Plasma shell for TVs
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/plasma/plasma-bigscreen

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(libcec)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(wayland-cursor)

BuildRequires: kf6-bluez-qt-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kglobalaccel-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-ksvg-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: plasma6-libkscreen-devel
BuildRequires: plasma6-lib-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: plasma6-activities-devel
BuildRequires: plasma6-activities-stats-devel
BuildRequires: plasma-workspace-devel
BuildRequires: qcoro6-devel
BuildRequires: qqc2-breeze-style-devel

BuildRequires: kde5-plasma-wayland-protocols

# make sure that all Qml imports will be satisfied
Requires: qml6(org.kde.bluezqt)
Requires: plasma-workspace-qml
Requires: libkf6coreaddons
Requires: qml6(org.kde.kcmutils)
Requires: kdeconnect
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: libkf6itemmodels
Requires: kf6-kdeclarative
Requires: libkf6svg
Requires: plasma6-layer-shell-qt
Requires: milou
Requires: qml6(org.kde.plasma.core)
Requires: plasma-nm
Requires: plasma6-plasma5support
Requires: plasma-nano
Requires: powerdevil
Requires: plasma-pa
Requires: plasma-workspace
Requires: qt6-5compat
Requires: qt6-multimedia
Requires: qt6-declarative
Requires: qt6-webengine
Requires: qqc2-breeze-style

Requires: kwayland-integration
Requires: plasma6-breeze
Requires: plasma-desktop
Requires: plasma6-integration
Requires: xdg-desktop-portal-kde
Requires: kscreen
Requires: kde-volume-control-pipewire

Requires: lib%{name}libs = %{version}-%{release}

ExcludeArch: %ix86 riscv64

%description
Plasma Bigscreen is an open-source user interface for TVs. Running on
top of a Linux distribution, Plasma Bigscreen turns your TV or set-top
box into a fully hackable device. A big launcher giving you easy access
to any installed apps and skills. Controllable via voice or TV remote.

%package -n lib%{name}libs
Group: System/Libraries
Summary: libraries for %name

%description -n lib%{name}libs
This package contains libraries for %name.

%prep
%setup
sed -i "s|Categories=.*|Categories=KDE;Qt;Video;AudioVideo;Recorder;|" uvcviewer/org.kde.plasma.bigscreen.uvcviewer.desktop
sed -i "s|Categories=.*|Categories=KDE;Qt;AudioVideo;Video;Audio;TV;|" bin/plasma-bigscreen-swap-session.desktop.cmake
sed -i "s|6.6.91|6.6.5|g" CMakeLists.txt

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

# move udev-rule file to the correct location
mkdir -pv %buildroot%_udevrulesdir/
mv -v %buildroot%_libdir/udev/rules.d/40-uinput.rules %buildroot%_udevrulesdir/

%files -f %name.lang
%doc README.md
%_K6bin/plasma-bigscreen-*
%dir %_K6qml/org/kde/bigscreen
%_K6qml/org/kde/bigscreen/*
%_K6xdgapp/*.desktop
%_K6data/metainfo/*.xml
%dir %_K6data/plasma/look-and-feel/org.kde.plasma.bigscreen
%_K6data/plasma/look-and-feel/org.kde.plasma.bigscreen/*
%dir %_K6data/plasma/plasmoids/org.kde.bigscreen.homescreen
%_K6data/plasma/plasmoids/org.kde.bigscreen.homescreen/*
%dir %_K6data/plasma/shells/org.kde.plasma.bigscreen
%_K6data/plasma/shells/org.kde.plasma.bigscreen/*
%dir %_K6data/sounds/plasma-bigscreen
%_K6data/sounds/plasma-bigscreen/*
%_K6data/wayland-sessions/plasma-bigscreen-wayland.desktop
%_K6data/dbus-1/interfaces/org.kde.biglauncher.xml
%_udevrulesdir/40-uinput.rules

%files -n lib%{name}libs
%_K6plug/plasma/applets/org.kde.bigscreen.homescreen.so
%_K6plug/plasma/kcms/systemsettings/kcm_mediacenter_*.so
%_K6lib/qt6/plugins/kf6/kded/kded_plasma_bigscreen_start.so

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 6.6.91-alt2
- Moved libraries to libplasma-bigscreenlibs package.

* Sat Jun 06 2026 Nikolay Strelkov <snk@altlinux.org> 6.6.91-alt1
- New version 6.6.91.

* Thu May 28 2026 Nikolay Strelkov <snk@altlinux.org> 6.6.90-alt2
- Applied repocop fix for sisyphus_check.

* Tue May 26 2026 Nikolay Strelkov <snk@altlinux.org> 6.6.90-alt1
- New version 6.6.90.

* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 6.5.80-alt3.git.989ac8b2
- Depend on renamed style package - qqc2-breeze-style.

* Fri Apr 03 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.80-alt2.git.989ac8b2
- NMU: fix requires

* Fri Feb 14 2026 Nikolay Strelkov <snk@altlinux.org> 6.5.80-alt1.git.989ac8b2
- Updated to newer commit to get gamepad support (closes: #57842).

* Fri Feb 06 2026 Nikolay Strelkov <snk@altlinux.org> 6.4.80-alt1.git.6a767b37
- Initial build for Sisyphus
