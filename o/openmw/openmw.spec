%define _unpackaged_files_terminate_build 1
%define osg_abiversion 162
%define osg_version 3.6.5
%define ot_abiversion 21
%define ot_version 3.3.1
%filter_from_requires /lua5.4(/d

Name: openmw
Version: 0.50.0
Release: alt1

Summary: OpenMW is an open-source game engine
License: GPL-3.0-only
Group: Development/Other
Url: https://openmw.org/
Vcs: https://github.com/OpenMW/openmw

Source: %name-%version.tar

Source1: osg.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake >= 3.0
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: ctest
BuildRequires: ninja-build

BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-iostreams-devel
BuildRequires: boost-program-options-devel
BuildRequires: boost-system-devel
BuildRequires: boost-thread-devel
BuildRequires: boost-geometry-devel

BuildRequires: libSDL2-devel
BuildRequires: libbullet3-devel

BuildRequires: libcollada-dom-devel
BuildRequires: desktop-file-utils

BuildRequires: recastnavigation-devel

BuildRequires: libavcodec-devel
BuildRequires: libavdevice-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libpostproc-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel

BuildRequires: libgmock-devel
BuildRequires: libgtest-devel
BuildRequires: libXt-devel
BuildRequires: libavcodec-devel
BuildRequires: libstdc++-devel
BuildRequires: liblua-devel
BuildRequires: libluajit-devel
BuildRequires: liblz4-devel
BuildRequires: libmygui-devel
BuildRequires: libopenal-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: libsqlite3-devel
BuildRequires: tinyxml-devel
BuildRequires: unshield-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel

#OSG deps
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: boost-asio-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libgif-devel
BuildRequires: gnuplot
BuildRequires: libcurl-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libvncserver-devel
BuildRequires: libxml2-devel
BuildRequires: libXmu-devel
BuildRequires: libX11-devel
BuildRequires: libInventor-devel
BuildRequires: libcairo-devel
BuildRequires: libXrandr-devel
BuildRequires: libgtkglext-devel
BuildRequires: libpoppler-glib-devel
BuildRequires: librsvg-devel
BuildRequires: libxkbfile-devel
BuildRequires: libgta-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: libgstreamermm1.0-devel
BuildRequires: gst-plugins-bad1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libgdal-devel

%description
OpenMW is an open-source game engine focused on 3D role-playing games

%package cs
Summary: The OpenMW Construction Set
Group: Development/Other

%description cs
OpenMW-CS is a construction kit for making games in the OpenMW engine

%package tools
Summary: Utility programs for OpenMW
Group: Development/Tools

%description tools
Various utility tools for developing and debugging with OpenMW

%prep
%setup
sed -i s/system\)$/\)/ CMakeLists.txt
sed -i s/Boost::system// components/CMakeLists.txt
mkdir -p %_target_platform/extern/fetched/osg
tar -xf %{SOURCE1} -C %_target_platform/extern/fetched/osg --strip-components=1

%build
%cmake -G Ninja \
    -DBUILD_OPENMW_TESTS=ON \
    -DBUILD_OPENCS_TESTS=ON \
    -DBULLET_STATIC=OFF \
    -DOSG_STATIC=ON \
    -DMYGUI_STATIC=OFF \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    -DGLOBAL_DATA_PATH=%_datadir \
    -DOPENMW_USE_SYSTEM_BULLET=ON \
    -DOPENMW_USE_SYSTEM_GOOGLETEST=ON \
    -DOPENMW_USE_SYSTEM_OSG=OFF \
    -DOPENMW_USE_SYSTEM_RECASTNAVIGATION=ON \
    -Wno-dev \
    #
%cmake_build

%install
%cmake_install

%check
%ctest
./%_target_platform/openmw-tests

%files
%doc LICENSE
%doc README.md
%doc AUTHORS.md
%doc CHANGELOG.md
%dir %_sysconfdir/openmw
%dir %_datadir/openmw
%dir %_datadir/openmw/resources
%dir %_datadir/openmw/resources/vfs
%dir %_datadir/openmw/resources/vfs/fonts
%_bindir/openmw
%_bindir/openmw-launcher
%_bindir/openmw-bulletobjecttool
%_bindir/openmw-iniimporter
%_bindir/openmw-essimporter
%_bindir/openmw-navmeshtool
%_bindir/openmw-wizard
%_datadir/pixmaps/openmw.png
%_datadir/applications/org.openmw.launcher.desktop
%_datadir/openmw/resources/openmw.png
%_datadir/openmw/resources/defaultfilters
%_datadir/openmw/resources/version
%_datadir/openmw/resources/lua_api
%_datadir/openmw/resources/lua_libs
%_datadir/openmw/resources/shaders
%_datadir/openmw/resources/translations
%_datadir/openmw/resources/vfs-mw
%_datadir/openmw/resources/vfs/builtin.omwscripts
%_datadir/openmw/resources/vfs/animations
%_datadir/openmw/resources/vfs/l10n
%_datadir/openmw/resources/vfs/mygui
%_datadir/openmw/resources/vfs/openmw_aux
%_datadir/openmw/resources/vfs/scripts
%_datadir/openmw/resources/vfs/shaders
%_datadir/openmw/resources/vfs/textures
%_datadir/openmw/resources/vfs/fonts/DejaVuLGCSansMono.ttf
%_datadir/openmw/resources/vfs/fonts/DejaVuFontLicense.txt
%_datadir/openmw/resources/vfs/fonts/DejaVuLGCSansMono.omwfont
%_datadir/openmw/resources/vfs/fonts/DemonicLettersFontLicense.txt
%_datadir/openmw/resources/vfs/fonts/DemonicLetters.omwfont
%_datadir/openmw/resources/vfs/fonts/DemonicLetters.ttf
%_datadir/openmw/resources/vfs/fonts/MysticCardsFontLicense.txt
%_datadir/openmw/resources/vfs/fonts/MysticCards.omwfont
%_datadir/openmw/resources/vfs/fonts/MysticCards.ttf
%_datadir/metainfo/openmw.appdata.xml
%_sysconfdir/openmw/defaults.bin
%_sysconfdir/openmw/defaults-cs.bin
%_sysconfdir/openmw/gamecontrollerdb.txt
%_sysconfdir/openmw/openmw.cfg

%files cs
%_bindir/openmw-cs
%_datadir/applications/org.openmw.cs.desktop
%_datadir/pixmaps/openmw-cs.png

%files tools
%_bindir/bsatool
%_bindir/esmtool
%_bindir/niftest

%changelog
* Thu Feb 19 2026 Pavel Petrykin <silverducks@altlinux.org> 0.50.0-alt1
- Initial build for Alt Linux.
