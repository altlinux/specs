%define rname plasma-workspace-wallpapers

Name: %rname
Version: 6.5.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Workspace Wallpapers
Url: http://www.kde.org
License: GPL-2.0-or-later

BuildArch: noarch

Provides: plasma5-workspace-wallpapers = %EVR
Obsoletes: plasma5-workspace-wallpapers < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build \
     -DBUILD_WITH_QT6=ON \
     #

%install
%K6install

%files
%doc COPYING*
%_datadir/wallpapers/*

%changelog
* Sat Nov 01 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.1-alt1
- new version

* Wed Jul 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Oct 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- new version

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.3-alt1
- initial build
