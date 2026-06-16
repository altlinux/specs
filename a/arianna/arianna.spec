%define rname arianna
Name: %rname
Version: 26.04.2
Release: alt2

Group: Graphical desktop/KDE
Summary: Epub Reader for Plasma and Plasma Mobile
License: (BSD-2-Clause OR BSD-3-Clause) AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.0-or-later OR LGPL-2.1-or-later OR LGPL-3.0-or-later)
Url: https://apps.kde.org/arianna
VCS: https://invent.kde.org/graphics/arianna

ExcludeArch: %not_qt6_qtwebengine_arches

Requires: qt6-declarative
Requires: qml6(QtWebChannel)
Requires: qml6(QtWebEngine)
Requires: libkf6itemmodels
Requires: libkf6sonnetui
Requires: kf6-kconfig
Requires: kf6-kirigami
Requires: kf6-kquickcharts
Requires: kf6-kirigami-addons

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6WebEngineQuick)
BuildRequires: pkgconfig(Qt6WebSockets)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6HttpServer)
BuildRequires: qt6-webchannel-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kfilemetadata-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kquickcharts-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-qqc2-desktop-style-devel
BuildRequires: kf6-baloo-devel

%description
An ebook reader and library management app supporting ".epub" files.
Arianna discovers your books automatically, and sorts them by categories,
genres and authors.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README.md
%_K6bin/arianna
%_K6xdgapp/*arianna*.desktop
%_K6icon/hicolor/*/apps/*arianna*
%_datadir/metainfo/*arianna*
%_datadir/qlogging-categories6/*arianna*.categories

%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt2
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
