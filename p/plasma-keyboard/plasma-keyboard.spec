
Name: plasma-keyboard
Version: 6.6.5
Release: alt2
%K6init no_altplace

Group: System/Libraries
Summary: Virtual Keyboard
License: LGPL-3.0-only and BSD
Url: https://invent.kde.org/plasma/plasma-keyboard

Requires: qt6-wayland qt6-virtualkeyboard

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: wayland-protocols
BuildRequires: qt6-wayland-devel qt6-virtualkeyboard-devel qt6-virtualkeyboard
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kcmutils-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kcrash-devel

%description
The plasma-keyboard is a virtual keyboard based on Qt Virtual Keyboard designed for Plasma integration.

%prep
%setup -n %name-%version

%build
%K6build

%install
make -C BUILD DESTDIR=%buildroot install
%find_lang --with-kde --all-name %name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/plasma-keyboard*
%_K6plug/plasma/kcms/systemsettings/*keyboard*
%_K6qml/QtQuick/VirtualKeyboard/Styles/Breeze/
%_K6qml/org/kde/plasma/keyboard/
%_K6xdgapp/*keyboard*.desktop
%_datadir/plasma/keyboard/
%_datadir/metainfo/*keyboard*.xml

%changelog
* Thu Jun 18 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt2
- add russian translation

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Apr 06 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Tue Nov 25 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
