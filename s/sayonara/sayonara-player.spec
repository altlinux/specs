Name: sayonara
Version: 1.8.0
Release: alt0.beta1.10

Summary: A lightweight Qt Audio player
License: GPLv3+
Group: Sound
Url: http://sayonara-player.com
Vcs: https://gitlab.com/luciocarreras/sayonara-player.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): desktop-file-utils
BuildRequires: cmake gcc-c++
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libappstream-glib
BuildRequires: libnotify-devel
BuildRequires: libgio-devel
BuildRequires: libtag-devel
BuildRequires: libpcre2-devel libtag-devel liblame-devel zlib-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-base-1.0)
%if_with check
BuildRequires: ctest
%endif

Requires: icon-theme-hicolor python3-module-pydbus
Requires: gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-base1.0
Requires: lame vorbis-tools

%description
%name is a small, clear, not yet platform-independent music player. Low
CPU usage, low memory consumption and no long loading times are only three
benefits of this player. Sayonara should be easy and intuitive to use and
therefore it should be able to compete with the most popular music players.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %name --all-name --with-qt

%check
desktop-file-validate %buildroot%_datadir/applications/*.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.appdata.xml

%files -f %name.lang
%doc COPYING LICENSE *.md
%_bindir/*
%_man1dir/*
%_desktopdir/*.desktop
%_datadir/metainfo/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Nov 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.8.0-alt0.beta1.10
- Initial build for ALT.

