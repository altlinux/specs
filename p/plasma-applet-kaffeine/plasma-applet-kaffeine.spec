%define nameL Kaffeine

Name: plasma-applet-kaffeine
Version: 0.3
Release: alt1

Summary: caffeine kde. button to lock the screen auto lock
License: GPL-3.0-or-later
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2259520/
Vcs: https://store.kde.org/p/2259520/

Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%install
mkdir -p %buildroot%_datadir/plasma/plasmoids/
mv %nameL %buildroot%_datadir/plasma/plasmoids/

%files
%_datadir/plasma/plasmoids/%nameL/*

%changelog
* Sun Apr 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3-alt1
- Initial build for ALT Linux.
