%define _unpackaged_files_terminate_build 1
# currently libleechcraft-xsd.so should be linked against ibleechcraft-util.so
# and contrariwise
#%%set_verify_elf_method unresolved=relaxed

Name: leechcraft
Version: 0.6.70
Release: alt1

Summary: LeechCraft DE
License: Boost Software License
Group: Graphical desktop/Other
URL: http://%name.org

# b0cbaa4f
Source: %name-%version.tar

Patch: %name-0.6.60-alt-link.patch

Requires: %name-data = %version-%release
# for session mode
Requires: openbox-base dbus-tools-gui

%define qxmpp_ver 0.7.6
%define qwt_ver 6.1.0

%add_findreq_skiplist %_datadir/%name/fenet/wms/*.sh
%add_findreq_skiplist %_datadir/%name/azoth/lc_azoth_modnok_latexconvert.sh

BuildRequires: gcc-c++
BuildRequires: cmake libqt4-devel qt4-mobility-devel libqtermwidget-devel libqwt6-devel >= %qwt_ver
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel boost-locale-devel
BuildRequires: qjson-devel libxml2-devel libpcre-devel
BuildRequires: gst-plugins-devel libtag-devel libguess-devel
BuildRequires: libqca2-devel libkqoauth-devel libhunspell-devel libtorrent-rasterbar-devel
BuildRequires: libspeex-devel libqxmpp-devel >= %qxmpp_ver
BuildRequires: libXcomposite-devel libXdamage-devel libxkbfile-devel
BuildRequires: libmagic-devel liblastfm-devel libudev-devel libpoppler-qt4-devel libpoppler-cpp-devel libdjvu-devel
BuildRequires: libvlc-devel libspectre-devel libnl-devel libsensors3-devel libudisks2-devel
BuildRequires: libtidy-devel
#BuildRequires: libavformat-devel libswscale-devel libpostproc-devel libswresample-devel

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
#%patch

%build
%cmake ../src \
	-DCMAKE_BUILD_TYPE=Release \
	-DHUNSPELL_LIBRARIES:FILEPATH=%_libdir/libhunspell.so \
	-DENABLE_VROOBY_UDISKS2=ON \
	-DENABLE_VROOBY_UDISKS=OFF \
	-DENABLE_MUSICZOMBIE:BOOL=OFF \
	-DENABLE_SYNCER:BOOL=OFF \
	-DENABLE_OTLOZHU_SYNC:BOOL=OFF \
	-DENABLE_TORRENT:BOOL=OFF \
	-DENABLE_XPROXY:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

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
* Sat Apr 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.70-alt1
- 0.6.70_b0cbaa4f

* Mon Feb 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.60-alt0.1
- first preview for Sisyphus



