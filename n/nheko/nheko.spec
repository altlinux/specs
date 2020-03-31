%define _unpackaged_files_terminate_build 1

Name: nheko
Version: 0.6.4
Release: alt1

Summary: Desktop client (QT) for the Matrix protocol

Group: Development/Other
License: GPLv3
Url: https://github.com/Nheko-Reborn/nheko.git

Source: %name-%version.tar

Patch0: nheko-fix-missing-libfmt.patch

BuildRequires: cmake gcc-c++
BuildRequires: qt5-tools-devel qt5-multimedia-devel qt5-svg-devel
BuildRequires: boost-asio-devel boost-devel-headers boost-signals-devel
BuildRequires: libssl-devel zlib-devel libtweeny-devel liblmdbxx-devel
BuildRequires: libmtxclient-devel liblmdb-devel cmark-devel
BuildRequires: nlohmann-json-devel libfmt-devel
BuildRequires: libolm-devel libsodium-devel libspdlog-devel

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app (Riot, Telegram etc)
and less like an IRC client.

%prep
%setup
%patch -p2

%build
%cmake -DUSE_BUNDLED_BOOST=OFF  \
       -DUSE_BUNDLED_SPDLOG=OFF \
       -DUSE_BUNDLED_OLM=OFF    \
       -DUSE_BUNDLED_CMARK=OFF  \
       -DUSE_BUNDLED_LMDBXX=OFF \
       -DUSE_BUNDLED_TWEENY=OFF \
       -DUSE_BUNDLED_MATRIX_CLIENT=OFF \
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
%_datadir/metainfo/*.appdata.xml

%changelog
* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.4-alt1
- New upstream: https://github.com/Nheko-Reborn/nheko.git
- Added -DCMAKE_BUILD_TYPE=Release
- New upstream version 0.6.4.

* Wed Dec 05 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt2
- Adjust nprocs for git.alt (<= 16).

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Initial release.
