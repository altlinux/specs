%define rname aurorae

Name: kwin-%rname
Version: 6.4.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Themeable window decoration for KWin
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-common >= %EVR
Conflicts: kwin < 6.4

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-ki18n-devel kf6-kcolorscheme-devel kf6-kcoreaddons-devel kf6-kcmutils-devel kf6-knewstuff-devel kf6-kpackage-devel
BuildRequires: kf6-kconfig-devel kf6-attica-devel kf6-kconfigwidgets-devel
BuildRequires: plasma6-kdecoration-devel

%description
Aurorae is a themeable window decoration for KWin.

It supports theme files consisting of several SVG files for decoration and buttons. Themes can be
installed and selected directly in the configuration module of KWin decorations.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common >= %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %rname-%version

sed -i 's|/usr/bin/bash|/bin/sh|' src/plasma-apply-aurorae.cmake

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files common  -f %name.lang
%doc LICENSES/*

%files
%_K6libexecdir/*aurorae*
%_K6plug/org.kde.kdecoration3.kcm/
%_K6plug/org.kde.kdecoration3/
%_K6qml/org/kde/kwin/decoration/
%dir %_K6qml/org/kde/kwin/decorations/
%_K6qml/org/kde/kwin/decorations/*
%_K6data/knsrcfiles/*aurorae*
%_K6data/kwin/aurorae/
%dir %_K6data/kwin/decorations/
%_K6data/kwin/decorations/kwin4_decoration_qml_plastik/

%files devel
%_libdir/cmake/Aurorae/

%changelog
* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Wed Jul 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- initial build
