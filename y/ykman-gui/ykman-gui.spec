%define _unpackaged_files_terminate_build 1

Name: ykman-gui
Version: 1.2.4
Release: alt1

Summary: Application for configuring any YubiKey over all USB interfaces
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://github.com/Yubico/yubikey-manager-qt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: python3-dev
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: libpcsclite-devel
BuildRequires: desktop-file-utils

Requires: libyubikey
Requires: python3(ykman)
Requires: pyotherside
Requires: ykman

%description
%summary

%prep
%setup

%build
# rename python to python3
sed -i $(echo $(find . -name '*.pro')) -e 's/python[^3]/python3 /g'

%qmake_qt5 CONFIG+=nostrip
%make_build

%install
%install_qt5

# install icons
install -pD -m0644 resources/icons/ykman.png %buildroot%_iconsdir/hicolor/128x128/apps/ykman.png
install -pD -m0644 resources/icons/ykman.svg %buildroot%_iconsdir/hicolor/scalable/apps/ykman.svg

# install .desktop file
desktop-file-install --dir %buildroot%_desktopdir resources/ykman-gui.desktop

%files
%doc COPYING NEWS
%_bindir/*
%_desktopdir/*
%attr(644,root,root) %_iconsdir/hicolor/*/apps/*

%changelog
* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.4-alt1
- initial build for Sisyphus
