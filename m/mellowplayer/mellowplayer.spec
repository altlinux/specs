%define _unpackaged_files_terminate_build 1

# no qtwebengine (bug#41476)
ExcludeArch: ppc64le

Name: mellowplayer
Version: 3.6.7
Release: alt2
Summary: Cloud music integration for your desktop
License: GPL-2.0
Group: Sound
Url: https://gitlab.com/ColinDuquesnoy/MellowPlayer
Source: %name-%version.tar
Patch1: %name-3.5.5-desktop-additional-categories-fix.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-tools-devel
BuildRequires: libnotify-devel

%description
MellowPlayer is a free, open source and cross-platform desktop application
that runs web-based music streaming services in its own window and
provides integration with your desktop (hotkeys, multimedia keys, system tray,
notifications and more).

%prep
%setup
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
ln -svr %buildroot%_bindir/MellowPlayer %buildroot%_bindir/%name

%files
%_bindir/MellowPlayer
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/com.gitlab.ColinDuquesnoy.MellowPlayer.metainfo.xml
%doc LICENSE

%changelog
* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 3.6.7-alt2
- exclude ppc64le from build

* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.7-alt1
- Updated to version 3.6.7

* Tue Jun 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.4-alt1
- Updated to version 3.6.4

* Wed Jun 10 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.3-alt1
- Updated to version 3.6.3

* Sat May 09 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.2-alt1
- Updated to version 3.6.2
- Fix license

* Sun Feb 02 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.9-alt1
- New version

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.5-alt2
- Add additional category in desktop file

* Sat Aug 10 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.5-alt1
- Initial build for ALT

