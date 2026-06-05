%define _unpackaged_files_terminate_build 1

Name: qrca
Version: 26.04.2
Release: alt1

Summary: QR code scanner for Plasma and Plasma Mobile
License: CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Group: Graphical desktop/KDE
Url: https://apps.kde.org/qrca
VCS: https://invent.kde.org/utilities/qrca

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcontacts-devel
BuildRequires: kf6-kcodecs-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-prison-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-networkmanager-qt-devel

Requires: kf6-kconfig
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: libkf6prison
Requires: libqt6-qmlcore
Requires: libqt6-multimediaquick
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quickdialogs2
Requires: libqt6-quicklayouts
Requires: kf6-qqc2-desktop-style
Requires: libkf6sonnetui
Requires: plasma6-breeze

%description
Scan QR-Codes with your camera on phones and laptops, and create your
own for easily sharing data between devices.

%prep
%setup
sed -i "s|Categories=.*|Categories=Qt;KDE;Graphics;OCR;Scanning;|" org.kde.qrca.desktop

%build
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README.md
%_bindir/qrca
%_desktopdir/org.kde.qrca.desktop
%_desktopdir/org.kde.qrca.wifi.desktop
%_iconsdir/hicolor/scalable/apps/org.kde.qrca.svg
%_datadir/metainfo/org.kde.qrca.appdata.xml

%changelog
* Fri Jun 05 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- New version 26.04.2.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.1-alt1
- New version 26.04.1.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- New version 25.12.2.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.1-alt1
- Initial build for Sisyphus
