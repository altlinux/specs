%define rname plasma-workspace-wallpapers

Name: %rname
Version: 6.1.3
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace Wallpapers
Url: http://www.kde.org
License: GPL-2.0-or-later

BuildArch: noarch

Provides: kf5-plasma-workspace-wallpapers = %EVR
Obsoletes: kf5-plasma-workspace-wallpapers < %EVR
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
* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.3-alt1
- initial build
