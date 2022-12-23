Name: kde5-plasma-mmcklauncher
Version: 0.6
Release: alt1
Summary: A Launcher for KDE Plasma based on a design by Max McKinney
License: GPL-2.0
Group: Graphical desktop/KDE
Url: https://github.com/SnoutBug/mmcklauncher
Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/kf5/plasma/plasmoids/com.github.SnoutBug.mmckLauncher
cp -pr contents metadata.desktop %buildroot%_datadir/kf5/plasma/plasmoids/com.github.SnoutBug.mmckLauncher

%files
%_datadir/kf5/plasma/plasmoids/com.github.SnoutBug.mmckLauncher

%changelog
* Sat Dec 24 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.6-alt1
- Initial build for ALT

