%define _unpackaged_files_terminate_build 1
%def_enable torrent
%def_disable musiczombie

# https://bugzilla.gnome.org/show_bug.cgi?id=739767
%add_optflags -I%_libdir/gstreamer-1.0/include

Name: leechcraft
Version: 0.6.75
Release: alt0.2

Summary: LeechCraft DE
License: Boost Software License
Group: Graphical desktop/Other
URL: http://%name.org

# 37f7ed557
Source: %name-%version.tar

%define qxmpp_ver 0.7.6
%define qwt_ver 6.1.0
%define torrent_ver 0.16.19
%define gst_api_ver 1.0

Requires: %name-data = %version-%release
Requires: polkit udisks2
Requires: libqt4-sql-sqlite
%if "%gst_api_ver" == "0.10"
Requires: gst-plugins-base
Requires: gst-plugins-good
Requires: gst-plugins-bad
%else
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
%endif
# for session mode
Requires: openbox-base dbus-tools-gui

%add_findreq_skiplist %_datadir/%name/fenet/wms/*.sh
%add_findreq_skiplist %_datadir/%name/azoth/lc_azoth_modnok_latexconvert.sh

BuildRequires: gcc-c++
BuildRequires: cmake libqt4-devel qt4-mobility-devel libqtermwidget-devel libqwt6-devel >= %qwt_ver
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: boost-asio-devel boost-locale-devel
BuildRequires: qjson-devel libxml2-devel libpcre-devel
%if "%gst_api_ver" == "0.10"
BuildRequires: gst-plugins-devel
%else
BuildRequires: gst-plugins%gst_api_ver-devel
%endif
BuildRequires: libtag-devel libguess-devel
BuildRequires: libqca2-devel libkqoauth-devel libhunspell-devel
%{?_enable_torrent:BuildRequires: libtorrent-rasterbar-devel >= %torrent_ver}
BuildRequires: libspeex-devel libqxmpp-devel >= %qxmpp_ver
BuildRequires: libXcomposite-devel libXdamage-devel libxkbfile-devel
BuildRequires: libmagic-devel liblastfm-devel libudev-devel libpoppler-qt4-devel libpoppler-cpp-devel libdjvu-devel
BuildRequires: libvlc-devel libspectre-devel libnl-devel libsensors3-devel libudisks2-devel
BuildRequires: libtidy-devel libGeoIP-devel
%{?_enable_musiczombie:BuildRequires: libavformat-devel libswscale-devel libpostproc-devel libswresample-devel}

%description
LeechCraft is a free open source cross-platform modular live environment.

%package data
Summary: Arch independent files for LeechCraft
Group: Graphical desktop/Other
BuildArch: noarch

%description data
This package provides noarch data needed for LeechCraft to work.

%package devel
Summary: Development headers for LeechCraft
Group: Development/C
Requires: %name = %version-%release

%description devel
Development headers for LeechCraft.

%prep
%setup

%build
%cmake ../src \
	-DCMAKE_BUILD_TYPE=Release \
	-DHUNSPELL_LIBRARIES:FILEPATH=%_libdir/libhunspell.so \
	-DENABLE_VROOBY_UDISKS2=ON \
	-DENABLE_VROOBY_UDISKS=OFF \
	-DENABLE_SYNCER:BOOL=OFF \
	-DENABLE_OTLOZHU_SYNC:BOOL=OFF \
	-DENABLE_XPROXY:BOOL=OFF \
	-DUSE_GSTREAMER_10:BOOL=ON \
	%{?_disable_musiczombie:-DENABLE_MUSICZOMBIE:BOOL=OFF} \
	%{?_disable_torrent:-DENABLE_TORRENT:BOOL=OFF}

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/03LCDE
NAME=LeechCraft DE
ICON=%_iconsdir/hicolor/48x48/apps/%{name}_main.png
EXEC=%_bindir/%name-session
DESC=LeechCraft desktop environment
SCRIPT:
exec %_bindir/%name-session
__EOF__

%find_lang --all-name --with-qt %name

%files
%_bindir/*
%_libdir/lib%name-util.so.*
%_libdir/lib%name-xsd.so.*
%_libdir/lib%name-util-db.so.*
%_libdir/lib%name-util-gui.so.*
%_libdir/lib%name-util-models.so.*
%_libdir/lib%name-util-network.so.*
%_libdir/lib%name-util-qml.so.*
%_libdir/lib%name-util-shortcuts.so.*
%_libdir/lib%name-util-sll.so.*
%_libdir/lib%name-util-svcauth.so.*
%_libdir/lib%name-util-sys.so.*
%_libdir/lib%name-util-tags.so.*
%_libdir/lib%name-util-x11.so.*
%_libdir/lib%name-util-xdg.so.*
%_libdir/lib%name-util-xpc.so.*
%_libdir/lib%name-util-xsd.so.*
%_libdir/%name/
%doc README

%files data -f %name.lang
%_sysconfdir/X11/wmsession.d/03LCDE
%_desktopdir/*.desktop
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/%name/azoth/
%_datadir/%name/fenet/
%_datadir/%name/global_icons/
%_datadir/%name/installed/
%_datadir/%name/kinotify/
%_datadir/%name/knowhow/
%_datadir/%name/qml/
%_datadir/%name/qml5/
%_datadir/%name/scripts/
%_datadir/%name/settings/
%_datadir/%name/sounds/
%_datadir/%name/themes/
%_iconsdir/hicolor/*x*/apps/*.png
%_datadir/xsessions/LCDE.desktop
%_man1dir/*

%files devel
%_includedir/%name/
%_libdir/*.so
%_datadir/cmake/Modules/InitLCPlugin.cmake
%_datadir/%name/cmake/

%changelog
* Wed Jun 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.75-alt0.2
- 0.6.75_37f7ed55

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.75-alt0.1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue May 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.75-alt0.1
- 0.6.75_00a4cac2
- built against gstreamer-1.0 using gcc-4.9

* Thu May 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.70-alt4
- updated to 0.6.70_e4303f5d
- enabled torrent plugin

* Fri May 01 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.70-alt3
- added /etc/X11/wmsession.d/03LCDE

* Fri Apr 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.70-alt2
- 0.6.70_5621455b
- requires: polkit, udisks2, libqt4-sql-sqlite

* Sat Apr 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.70-alt1
- 0.6.70_b0cbaa4f

* Mon Feb 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.60-alt0.1
- first preview for Sisyphus



