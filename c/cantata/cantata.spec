%define _unpackaged_files_terminate_build 1
%define rdn_name dog.unix.cantata.Cantata

Name: cantata
Version: 3.2.1
Release: alt1
Summary: Qt Graphical MPD Client
License: GPL-3.0
Group: Sound
Url: https://github.com/nullobsi/cantata

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-common gcc-c++
BuildRequires: qt6-base-devel qt6-svg-devel qt6-multimedia-devel
BuildRequires: zlib-devel

%description
A client for the Music Player Daemon (MPD).

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/cantata
%_desktopdir/%rdn_name.desktop
%_datadir/Cantata/icons/*.png
%_datadir/Cantata/scripts/cantata-dynamic
%_datadir/Cantata/scripts/cantata-remote
%_iconsdir/hicolor/*/apps/%{rdn_name}.png
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri Jan 24 2025 Andrey Kovalev <ded@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus.
