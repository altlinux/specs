%define rname qrca

Name: %rname
Version: 26.04.2
Release: alt2
%K6init

Summary: QR code scanner for Plasma and Plasma Mobile
License: CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Group: Graphical desktop/KDE
Url: https://apps.kde.org/qrca
VCS: https://invent.kde.org/utilities/qrca

Requires: qt6-declarative
Requires: libkf6sonnetui
Requires: libkf6prison
Requires: kf6-kconfig
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: kf6-qqc2-desktop-style
Requires: plasma6-breeze

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
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

%description
Scan QR-Codes with your camera on phones and laptops, and create your
own for easily sharing data between devices.

%prep
%setup

%build
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README.md
%_K6bin/*qrca*
%_K6xdgapp/*qrca*.desktop
%_K6icon/hicolor/*/apps/org.kde.qrca.svg
%_datadir/metainfo/*qrca*.xml

%changelog
* Mon Jun 15 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt2
- update packaging

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
