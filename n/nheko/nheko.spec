Name: nheko
Version: 0.6.2
Release: alt2

Summary: Desktop client (QT) for the Matrix protocol

Group: Development/Other
License: GPLv3
Url: https://github.com/mujx/nheko

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: qt5-tools-devel qt5-multimedia-devel qt5-svg-devel
BuildRequires: boost-asio-devel boost-devel-headers boost-signals-devel
BuildRequires: libssl-devel zlib-devel libtweeny-devel liblmdbxx-devel
BuildRequires: libmtxclient-devel liblmdb-devel cmark-devel json-cpp
BuildRequires: libolm-devel libsodium-devel libspdlog-devel

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app (Riot, Telegram etc)
and less like an IRC client.

%prep
%setup

%build
%cmake -DUSE_BUNDLED_BOOST=OFF  \
       -DUSE_BUNDLED_SPDLOG=OFF \
       -DUSE_BUNDLED_OLM=OFF    \
       -DUSE_BUNDLED_CMARK=OFF  \
       -DUSE_BUNDLED_LMDBXX=OFF \
       -DUSE_BUNDLED_TWEENY=OFF \
       -DUSE_BUNDLED_MATRIX_CLIENT=OFF
# Adjust nprocs for git.alt
[ ${NPROCS:-%__nprocs} -le 16 ] || NPROCS=16
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md LICENSE
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_datadir/metainfo/*.appdata.xml

%changelog
* Wed Dec 05 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt2
- Adjust nprocs for git.alt (<= 16).

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Initial release.
