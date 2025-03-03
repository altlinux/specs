# wx-config
%global wxversion 3.2

Name: guayadeque
Version: 0.7.0
Release: alt1
Summary: Music player
License: GPL-3.0-or-later and BSD and LGPL-2.0-or-later and wxWidgets
URL: https://guayadeque.org/
VCS: https://github.com/thothix/guayadeque.git
Group: Sound
# Source-url: https://github.com/thothix/guayadeque/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: libtag-devel
BuildRequires: libcurl-devel
BuildRequires: libgpod-devel
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libwxGTK3.2-devel
BuildRequires: libwxsqlite3-devel
BuildRequires: libdbus-devel
BuildRequires: libicu-devel

%description
Guayadeque is a music management program designed for all music enthusiasts. It
is Full Featured Linux media player that can easily manage large collections
and uses the Gstreamer media framework.

%prep
%setup

%build
%cmake \
 -DCMAKE_BUILD_TYPE='Release' \
 -DCMAKE_EXE_LINKER_FLAGS:STRING=-lwx_gtk3u_aui-%wxversion \
 -DCMAKE_CXX_FLAGS="%optflags"
 
%cmake_build

%install
%cmake_install

%find_lang %name

%check
desktop-file-validate %buildroot%_datadir/applications/*.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.metainfo.xml

%files -f %name.lang
%doc LICENSE RADIOS.md README.md
%_bindir/guayadeque
%_datadir/guayadeque/*.conf
%_datadir/guayadeque/*.xml
%dir %_datadir/guayadeque
%_iconsdir/hicolor/*/apps/guayadeque.png
%_desktopdir/org.guayadeque.guayadeque.desktop
%_datadir/metainfo/org.guayadeque.guayadeque.metainfo.xml

%changelog
* Mon Mar 03 2025 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- new version (0.7.0) with rpmgs script
- add VCS tag

* Fri Oct 11 2024 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1
- New version 0.5.3

* Fri Mar 17 2023 Anton Midyukov <antohami@altlinux.org> 0.4.7-alt1
- Initial build
