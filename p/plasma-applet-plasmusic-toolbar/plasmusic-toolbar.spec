%define nameL plasmusic-toolbar

Name: plasma-applet-%nameL
Version: 3.0.0
Release: alt1

Summary: Plasma widget that shows playing song information and provide controls
License: GPL-3.0-only
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2128143
Vcs: https://github.com/ccatterina/plasmusic-toolbar

Source: %name-%version.tar

BuildArch: noarch

%description
PlasMusic Toolbar is a widget for KDE Plasma 6 that shows currently playing song
information and provide playback controls.

%prep
%setup

%build
%install
install -d %buildroot%_datadir/plasma/plasmoids/%nameL
cp -r src/* %buildroot%_datadir/plasma/plasmoids/%nameL/

%files
%doc LICENSE *.md
%_datadir/plasma/plasmoids/%nameL

%changelog
* Sun Jun 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt1
- 2.7.0 -> 3.0.0

* Fri Jun 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.0-alt1
- 2.6.0 -> 2.7.0

* Sun Jun 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.6.0-alt1
- 2.5.0 -> 2.6.0

* Wed May 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.5.0-alt1
- Initial build for ALT Linux.
