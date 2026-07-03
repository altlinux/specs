%define _stripped_files_terminate_build 1

%ifndef _udev_rulesdir
%define _udev_rulesdir /lib/udev/rules.d
%endif

Name: plasma-bigscreen
Version: 6.7.2
Release: alt2

Summary: Plasma shell for TVs
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/plasma/plasma-bigscreen

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: libplasma-bigscreenlibs = %EVR
Obsoletes: libplasma-bigscreenlibs < %EVR

Requires: qt6-declarative qt6-multimedia qt6-webengine qt6-5compat
#
Requires: qml6(org.kde.kcmutils)
Requires: qml6(org.kde.bluezqt)
Requires: libkf6coreaddons libkf6itemmodels libkf6svg libkf6itemmodels
Requires: kf6-kirigami kf6-kirigami-addons kf6-kdeclarative
#
Requires: qml6(org.kde.plasma.core)
Requires: qqc2-breeze-style
Requires: plasma-nm plasma6-plasma5support powerdevil plasma-pa plasma-workspace
Requires: plasma6-layer-shell-qt plasma6-breeze plasma6-integration xdg-desktop-portal-kde
Requires: kscreen milou
#
Requires: kdeconnect
#
Requires: kde-volume-control

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: cmake extra-cmake-modules
BuildRequires: pkgconfig(libcec)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(vulkan)
BuildRequires: qcoro6-devel
BuildRequires: pkgconfig(Qt6) pkgconfig(Qt6Qml) pkgconfig(Qt6Multimedia) pkgconfig(Qt6WebEngineCore)
BuildRequires: kf6-bluez-qt-devel kf6-ki18n-devel kf6-kirigami-devel kf6-kcmutils-devel kf6-kglobalaccel-devel
BuildRequires: kf6-knotifications-devel kf6-kio-devel kf6-kwindowsystem-devel kf6-ksvg-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kiconthemes-devel kf6-kpackage-devel kf6-kitemmodels-devel
BuildRequires: plasma-wayland-protocols
BuildRequires: plasma6-libkscreen-devel plasma6-lib-devel plasma6-activities-devel plasma6-activities-stats-devel
BuildRequires: plasma-workspace-devel qqc2-breeze-style-devel

%description
Plasma Bigscreen is an open-source user interface for TVs. Running on
top of a Linux distribution, Plasma Bigscreen turns your TV or set-top
box into a fully hackable device. A big launcher giving you easy access
to any installed apps and skills. Controllable via voice or TV remote.

%prep
%setup

%build
%K6build

%install
%K6install

# move udev-rule file to the correct location
if ! [ -d "%buildroot/%_udev_rulesdir" ] ; then
    mkdir -p %buildroot/%_udev_rulesdir/
    mv %buildroot/%_libdir/udev/rules.d/*.rules %buildroot/%_udev_rulesdir/
fi

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README.md
%_K6bin/*bigscreen*
%_K6qml/org/kde/bigscreen/
%_K6xdgapp/*.desktop
%_K6data/metainfo/*.xml
%_K6data/plasma/look-and-feel/org.kde.plasma.bigscreen/
%_K6data/plasma/plasmoids/org.kde.bigscreen.homescreen/
%_K6data/plasma/shells/org.kde.plasma.bigscreen/
%_K6data/sounds/plasma-bigscreen/
%_K6data/wayland-sessions/plasma-bigscreen-wayland.desktop
%_K6plug/plasma/applets/org.kde.bigscreen.homescreen.so
%_K6plug/plasma/kcms/systemsettings/kcm_mediacenter_*.so
%_K6lib/qt6/plugins/kf6/kded/kded_plasma_bigscreen_start.so
%_udev_rulesdir/40-uinput.rules

%changelog
* Thu Jul 02 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt2
- fix packaging

* Tue Jun 30 2026 Nikolay Strelkov <snk@altlinux.org> 6.7.2-alt1
- New version 6.7.2.

* Fri Jun 26 2026 Nikolay Strelkov <snk@altlinux.org> 6.7.1-alt1
- New version 6.7.1.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 6.7.0-alt1
- New version 6.7.0.

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
