%global appname io.github.antimicrox.antimicrox

Name: antimicrox
Version: 3.4.1
Release: alt1

Summary: Graphical program used to map keyboard buttons and mouse controls to a gamepad

License: GPL-3.0-or-later AND Zlib AND LGPL-3.0-or-later AND LGPL-2.1-or-later
Group: System/Configuration/Hardware
Url: https://github.com/AntiMicroX/antimicrox

# Source-url: https://github.com/AntiMicroX/antimicrox/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libSDL2-devel
BuildRequires: itstool
BuildRequires: gettext-tools
# For desktop file & AppData
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

%description
AntiMicroX is a graphical program used to map keyboard keys and mouse controls
to a gamepad. This program is useful for playing PC games using a gamepad that
do not have any form of built-in gamepad support. AntiMicroX is a fork of
AntiMicro which was inspired by QJoyPad but has additional features.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %name --with-qt

mkdir -p  %buildroot/lib/udev/rules.d/
mv -v %buildroot%_libexecdir/udev/rules.d/60-antimicrox-uinput.rules %buildroot/lib/udev/rules.d/
rm -rv %buildroot%_iconsdir/breeze

%files
%dir %_docdir/%name/
%_docdir/%name/*.md
%_bindir/%name
%dir %_datadir/%name/
%_datadir/%name/*
%_desktopdir/%appname.desktop
%_iconsdir/*/*/apps/*
%_datadir/metainfo/%appname.appdata.xml
%_datadir/mime/packages/%appname.xml
%_man1dir/%name.1*
/lib/udev/rules.d/60-antimicrox-uinput.rules

%check
%_bindir/desktop-file-validate %buildroot/%_desktopdir/%appname.desktop
%_bindir/appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%appname.appdata.xml

%changelog
* Mon Aug 19 2024 Mikhail Tergoev <fidel@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 11 2024 Mikhail Tergoev <fidel@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Jul 12 2023 Mikhail Tergoev <fidel@altlinux.org> 3.3.4-alt1
- initial build for ALT Sisyphus


