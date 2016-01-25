Name: klatexformula
Version: 3.2.11
Release: alt2
License: GPLv2
Group: Publishing
Summary: Generating images from LaTeX equations
Source: %name-%version.tar.gz
Patch: klatexformula-3.2.9-setlocale.patch
Url: http://klatexformula.sourceforge.net/

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: automoc cmake cmake-modules fontconfig fontconfig-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
BuildRequires: doxygen fonts-ttf-xorg gcc-c++ graphviz kde4libs-devel qt4-designer

Requires: libqt4-sql-sqlite

%description
KLatexFormula is an easy-to-use graphical application for generating
images (that you can drag and drop, copy and paste or save to disk) from
LaTeX equations.

%package devel
Group: Development/KDE and QT
Summary: Development environment for %name
%description devel
%summary
TODO: make shared version of %name-devel.

%prep
%setup
sed -i 's/target_link_libraries(\([^ ]*\)/target_link_libraries(\1 -lX11/' src/CMakeLists.txt
%patch -p1
sed -i '/Uninstall target/,$s/^/#/' cmake/klfinstallpaths.cmake

%build
%cmake -D QT_QMAKE_EXECUTABLE_FINDQT:path=/usr/bin/qmake-qt4 \
       -D QT_QMAKE_EXECUTABLE:path=/usr/bin/qmake-qt4 \
       -D KLF_LIBKLFBACKEND_STATIC=False \
       -D KLF_LIBKLFTOOLS_STATIC=False \
       -D KLF_LIBKLFAPP_STATIC=False \
       ..
# -D KLF_DEBUG=True ..
%cmake_build all doc

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/kde4/*
%_libdir/lib*.so.*
%_iconsdir/hicolor/*/apps/*.png
%_pixmapsdir/*.png
%_desktopdir/*
%_xdgmimedir/*
%_Kapps/*
%_K4srv/*
%_datadir/%name

%files devel
%_includedir/*
%_libdir/lib*.so

%changelog
* Mon Jan 25 2016 Fr. Br. George <george@altlinux.ru> 3.2.11-alt2
- Fix build

* Wed Aug 20 2014 Fr. Br. George <george@altlinux.ru> 3.2.11-alt1
- Autobuild version bump to 3.2.11
- Fix build and patch

* Tue May 13 2014 Fr. Br. George <george@altlinux.ru> 3.2.9-alt1
- Autobuild version bump to 3.2.9
- Devel now uses shared libraries

* Thu Feb 27 2014 Fr. Br. George <george@altlinux.ru> 3.2.8-alt1
- Autobuild version bump to 3.2.8
- Fix good old RU_ru LC_NUMERIC in postscript files

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 3.2.7-alt1
- Autobuild version bump to 3.2.7
- Fix requires

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 3.2.6-alt1
- Autobuild version bump to 3.2.6
- DSO list completion

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 3.2.5-alt1
- Autobuild version bump to 3.2.5

* Thu Oct 13 2011 Fr. Br. George <george@altlinux.ru> 3.2.4-alt1
- Initial build from scratch

