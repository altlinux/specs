%define _unpackaged_files_terminate_build 1
%define rdn_name dog.unix.cantata.Cantata

Name: cantata
Version: 3.3.0
Release: alt1
Summary: Qt Graphical MPD Client
License: GPL-3.0
Group: Sound
Url: https://github.com/nullobsi/cantata
Vcs: https://github.com/nullobsi/cantata.git

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-qt6

BuildRequires: cmake
BuildRequires: gcc-common gcc-c++
BuildRequires: qt6-base-devel qt6-svg-devel qt6-multimedia-devel qt6-tools-devel
BuildRequires: zlib-devel

%description
A client for the Music Player Daemon (MPD).

%prep
%setup
%patch -p1

%build
export PATH="%_qt6_bindir:$PATH"
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/cantata
%_datadir/Cantata
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}.png
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Tue Jan 28 2025 Andrey Kovalev <ded@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.
- Added Vcs tag and other minor improvements.
- Added localization.

* Fri Jan 24 2025 Andrey Kovalev <ded@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus.
