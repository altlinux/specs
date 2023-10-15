%define _unpackaged_files_terminate_build 1

Name: nheko
Version: 0.9.3
Release: alt1.1

Summary: Desktop client (QT) for the Matrix protocol

Group: Development/Other
License: GPLv3
Url: https://nheko.im/nheko-reborn/nheko

Source: %name-%version.tar
Patch: %name-fmt10-fix.patch

BuildRequires: cmake gcc-c++
BuildRequires: qt5-tools-devel qt5-multimedia-devel qt5-svg-devel
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: boost-asio-devel boost-devel-headers boost-signals-devel
BuildRequires: libssl-devel zlib-devel libtweeny-devel liblmdbxx-devel
BuildRequires: libmtxclient-devel liblmdb-devel cmark-devel
BuildRequires: nlohmann-json-devel libfmt-devel
BuildRequires: libolm-devel libsodium-devel libspdlog-devel
BuildRequires: gst-plugins-bad-devel gst-plugins-devel
BuildRequires: libpcre-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
BuildRequires: libselinux-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: asciidoc-a2x

# Additional (runtime) dependencies
Requires: qt5-graphicaleffects qt5-quickcontrols2 qt5-multimedia

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app (Riot, Telegram etc)
and less like an IRC client.

%prep
%setup
%patch0 -p1

%build
%cmake -DUSE_BUNDLED_SPDLOG=OFF    \
       -DUSE_BUNDLED_OLM=OFF       \
       -DUSE_BUNDLED_GTEST=OFF     \
       -DUSE_BUNDLED_CMARK=OFF     \
       -DUSE_BUNDLED_JSON=OFF      \
       -DUSE_BUNDLED_OPENSSL=OFF   \
       -DUSE_BUNDLED_MTXCLIENT=OFF \
       -DUSE_BUNDLED_LMDB=OFF      \
       -DUSE_BUNDLED_LMDBXX=OFF    \
       -DUSE_BUNDLED_COEURL=OFF    \
       -DUSE_BUNDLED_LIBCURL=OFF   \
       -DUSE_BUNDLED_LIBEVENT=OFF  \
       -DCMAKE_BUILD_TYPE=Release

# Adjust nprocs for git.alt
[ ${NPROCS:-%__nprocs} -le 16 ] || NPROCS=16
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md COPYING
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/*.appdata.xml
%_man1dir/nheko*

%changelog
* Sun Oct 15 2023 Nazarov Denis <nenderus@altlinux.org> 0.9.3-alt1.1
- NMU: Fix build with fmt 10

* Tue Jul 19 2022 Vladimir Didenko <cow@altlinux.org> 0.9.3-alt1
- Updated to v0.9.3.

* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt1
- Switch to https://nheko.im/nheko-reborn/nheko.git.
- Updated to v0.9.1.

* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.8.2-alt1
- Updated to v0.8.2.

* Sun Feb 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.8.1-alt1
- Fixed build requirements for new version.
- Fresh up to v0.8.1.

* Fri Jul 10 2020 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt2
- Fix: Additional (runtime) QT dependencies.

* Wed Jul 08 2020 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt1
- Fresh up to v0.7.2.
- Package the SVG icon.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.4-alt1
- New upstream: https://github.com/Nheko-Reborn/nheko.git
- Added -DCMAKE_BUILD_TYPE=Release
- New upstream version 0.6.4.

* Wed Dec 05 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt2
- Adjust nprocs for git.alt (<= 16).

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Initial release.
