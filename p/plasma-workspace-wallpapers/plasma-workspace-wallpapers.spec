%define rname plasma-workspace-wallpapers

Name: %rname
Version: 6.2.1
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace Wallpapers
Url: http://www.kde.org
License: GPL-2.0-or-later

BuildArch: noarch

Provides: plasma5-workspace-wallpapers = %EVR
Obsoletes: plasma5-workspace-wallpapers < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%files
%doc COPYING*
%_datadir/wallpapers/*

%changelog
* Wed Oct 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- new version

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.3-alt1
- initial build
