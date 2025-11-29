%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: kdocker
Version: 6.2
Release: alt1

Summary: Dock most applications to the system tray
License: GPL-2.0-only
Group: Graphical desktop/Other
Url: https://github.com/user-none/KDocker

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)

%description
KDocker will help you dock any application into the system tray.
This means you can dock openoffice, xmms, firefox, thunderbird, anything!
Just point and click. Works for all NET WM compliant window managers - that
includes KDE, GNOME, Xfce, Fluxbox and many more.

%prep
%setup
sed -i "s/Categories=.*/Categories=Utility;Accessibility;/" resources/desktop/com.kdocker.KDocker.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog LICENSE README.md
%_bindir/kdocker
%_desktopdir/com.kdocker.KDocker.desktop
%_datadir/bash-completion/completions/kdocker
%exclude %_datadir/dbus-1/interfaces/com.kdocker.KDocker.xml
%_datadir/dbus-1/services/com.kdocker.KDocker.service
%_iconsdir/hicolor/128x128/apps/com.kdocker.KDocker.png
%_iconsdir/hicolor/256x256/apps/com.kdocker.KDocker.png
%_iconsdir/hicolor/32x32/apps/com.kdocker.KDocker.png
%_iconsdir/hicolor/512x512/apps/com.kdocker.KDocker.png
%_iconsdir/hicolor/64x64/apps/com.kdocker.KDocker.png
%_iconsdir/hicolor/scalable/apps/com.kdocker.KDocker.svg
%_datadir/metainfo/com.kdocker.KDocker.metainfo.xml

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 6.2-alt1
- Initial build for Sisyphus
