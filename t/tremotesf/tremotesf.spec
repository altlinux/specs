%define _unpackaged_files_terminate_build 1

%def_with check

Name: tremotesf
Version: 2.9.1
Release: alt3

Summary: Remote GUI for transmission-daemon
License: GPL-3.0-or-later
Group: Networking/File transfer
Url: https://github.com/equeim/tremotesf2

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(cxxopts)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(fmt)
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: libcpp-httplib-devel
BuildRequires: libbrotli-devel
BuildRequires: gettext
BuildRequires: qt6-tools-devel

%if_with check
BuildRequires: ctest
%endif

%description
Tremotesf is yet another, but modern (first-released in 2016)
cross-platfom GUI for Transmission daemon written in C++ and Qt.

Features include, but not necessarily limited to:

* View torrent list
* Sort torrents
* Filter torrents by name, status and trackers
* Start/stop/verify/remove torrents with multi-selection
* Add torrents from torrent files and magnet links
* Select which files to download when adding torrent
* Manage torrent files
* Add and remove torrent trackers
* View torrent peers
* Set torrent limits
* Change remote server settings
* View server statistics
* Multiple servers
* Supports HTTPS connection
* Can connect to servers with self-signed certificates (you need to add
certificate to server settings)
* Client certificate authentication

%prep
%setup
sed -i "s/0.22.5/0.21/" data/CMakeLists.txt

%build
%cmake \
       -DTREMOTESF_QT6=ON \
       -DTREMOTESF_WITH_HTTPLIB=system
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV -E tracker_test

%files
%doc CHANGELOG.md LICENSE LICENSES README.md
%_bindir/tremotesf
%_desktopdir/org.equeim.Tremotesf.desktop
%_iconsdir/hicolor/16x16/apps/org.equeim.Tremotesf.png
%_iconsdir/hicolor/22x22/apps/org.equeim.Tremotesf.png
%_iconsdir/hicolor/24x24/apps/org.equeim.Tremotesf.png
%_iconsdir/hicolor/256x256/apps/org.equeim.Tremotesf.png
%_iconsdir/hicolor/32x32/apps/org.equeim.Tremotesf.png
%_iconsdir/hicolor/48x48/apps/org.equeim.Tremotesf.png
%_iconsdir/hicolor/scalable/apps/org.equeim.Tremotesf.svg
%_datadir/metainfo/org.equeim.Tremotesf.appdata.xml

%changelog
* Sat Jun 20 2026 Nikolay Strelkov <snk@altlinux.org> 2.9.1-alt3
- Fixed FTBFS.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 2.9.1-alt2
- Fixed FTBFS by skipping tracker_test which needs network access.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 2.9.1-alt1
- New version 2.9.1.

* Sun Dec 07 2025 Nikolay Strelkov <snk@altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus
