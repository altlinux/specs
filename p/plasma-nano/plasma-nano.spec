%define rname plasma-nano

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 minimal shell
Url: http://www.kde.org
License: GPL-2.0-or-later AND LGPL-2.1-or-later

Provides: plasma5-nano = %EVR
Obsoletes: plasma5-nano < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: qt6-svg-devel qt6-wayland-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-ki18n-devel kf6-kpackage-devel kf6-kservice-devel kf6-kwindowsystem-devel kf6-kitemmodels-devel
BuildRequires: plasma6-lib-devel plasma6-kwayland-devel

%description
A minimal plasma shell package intended for embedded devices.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6qml/org/kde/plasma/private/nanoshell/
%_K6data/plasma/packages/org.kde.plasma.nano.desktoptoolbox/
%_K6data/plasma/shells/org.kde.plasma.nano/
%_datadir/metainfo/*.xml

%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

