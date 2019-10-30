Name: zeal
Version: 0.6.1
Release: alt1
Summary: Offline documentation browser for software developers
License: GPLv3+
Group: Text tools
Url: https://zealdocs.org/
Source: %name-%version.tar.xz

# Automatically added by buildreq on Wed Oct 30 2019
# optimized out: cmake cmake-modules fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libfreetype-devel libglvnd-devel libqt5-concurrent libqt5-core libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libsasl2-3 libstdc++-devel libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel pkg-config python-base python-modules qt5-base-devel sh4 xorg-proto-devel xorg-xf86miscproto-devel
BuildRequires: extra-cmake-modules libarchive-devel libsqlite3-devel qt5-virtualkeyboard-devel qt5-wayland-devel qt5-webkit-devel qt5-x11extras-devel

%description
Zeal is a simple offline documentation browser inspired by Dash. After
installing Zeal, go to Tools->Docsets, select the ones you want, and
click the Download button.

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/*
%_desktopdir/*
%_datadir/metainfo/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Wed Oct 30 2019 Fr. Br. George <george@altlinux.ru> 0.6.1-alt1
- Autobuild version bump to 0.6.1

* Wed Oct 30 2019 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Initial build for ALT

