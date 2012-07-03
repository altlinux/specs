%define origversion r08832
%define gameversion %name-%origversion-alpha

Name:    	0ad
Version:        0.%origversion
Release:        alt2.4

Summary:        Free, Open-Source, Cross-Platform RTS Game of Ancient Warfare
Summary(ru_RU.UTF-8): Свободная, кроссплатформенная игра в жанре исторической стратегии реального времени с открытым исходным кодом

License:        GPLv2
Group:          Games/Strategy
Url:            http://wildfiregames.com/0ad/

Packager: 	Anton Chernyshov <ach@altlinux.org>
Source0:        %gameversion-unix-build.tar
Patch0: 0ad-alt-boost1.47.0.patch

Requires: %name-data = %version

BuildPreReq: binutils
BuildPreReq: gcc-c++
BuildPreReq: imake
BuildPreReq: desktop-file-utils
BuildPreReq: subversion
BuildPreReq: pkg-config
BuildPreReq: cmake
BuildPreReq: nasm 
BuildPreReq: unzip 
BuildPreReq: zip
BuildPreReq: boost-devel
BuildPreReq: boost-filesystem-devel
BuildPreReq: boost-signals-devel
BuildPreReq: libalut-devel
BuildPreReq: libdevil-devel 
BuildPreReq: libenet-devel
BuildPreReq: libfreeglut-devel
BuildPreReq: libgamin-devel 
BuildPreReq: libjpeg-devel 
BuildPreReq: libogg-devel
BuildPreReq: libopenal-devel 
BuildPreReq: libpng-devel 
BuildPreReq: libvorbis-devel 
BuildPreReq: libwxGTK-devel 
BuildPreReq: libxml2-devel 
BuildPreReq: libGL-devel 
BuildPreReq: libSDL-devel 
BuildPreReq: libX11-devel
BuildPreReq: libXext-devel
BuildPreReq: libXft-devel
BuildPreReq: libXi-devel 
BuildPreReq: libXmu-devel 
BuildPreReq: libXrandr-devel 
BuildPreReq: python-devel
BuildPreReq: zlib-devel

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform real-time 
strategy (RTS) game of ancient warfare. In short, it is a historically-based 
war/economy game that allows players to relive or rewrite the history of Western 
civilizations, focusing on the years between 500 B.C. and 500 A.D. The project is 
highly ambitious, involving state-of-the-art 3D graphics, detailed artwork, sound, 
and a flexible and powerful custom-built game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer, 
hobbyist game developers, since 2001. The code and data are available under the GPL 
license, and the art, sound and documentation are available under CC-BY-SA.

NOTE! This game is still alpha version!

%description -l ru_RU.UTF-8
0 A.D. (произносится как "зеро эй-ди") - свободная, кроссплатформенная игра в жанре
исторической стратегии реального времени с открытым исходным кодом. Это одновременно
экономическая и военная игра, которая позволяет игрокам пережить и даже переписать
историю западных цивилизаций в период времени между 500 г. до н.э. и 500 г. н.э. 
Проект, развивающий эту игру, имеет далеко идущие цели, современную 3D графику,
проработанное оформление и звук, гибкий и мощный собственный движок игры.

Разработка игры развивается компанией Wildfire Games (WFG), группой добровольцев,
занимающихся этим ради хобби. Код игры и ее ресурсы доступны под лицензией GPL,
оформление, звук и документация - под лицензией CC-BY-SA.

ВНИМАНИЕ! Эта игра еще находится в альфа-версии! Но более-менее стабильна.

%prep
%setup -n %gameversion
%patch0 -p2

%build
export CFLAGS="%optflags -DHAVE_C99_MATH"
export CPPFLAGS="%optflags -DHAVE_C99_MATH"
cd build/workspaces/
./update-workspaces.sh 	\
		       --verbose \
		       --bindir %_bindir \
		       --datadir %_gamesdatadir/%name \
		       --libdir %_libdir/%name
cd gcc
%make_build CONFIG=Release

%install

# install game executables 
install -Dm 0755 binaries/system/pyrogenesis %buildroot/%_bindir/pyrogenesis
install -Dm 0755 build/resources/%name.sh %buildroot/%_bindir/%name

# install game libs:
# - base libs
install -Dm 0644 binaries/system/libCollada.so %buildroot/%_libdir/%name/libCollada.so
install -Dm 0644 binaries/system/libAtlasUI.so %buildroot/%_libdir/%name/libAtlasUI.so

# - spidermonkey libs
install -Dm 0644 binaries/system/libmozjs-ps-release.so %buildroot/%_libdir/%name/libmozjs-ps-release.so

# - NVIDIA texture tool libs
install -Dm 0644 binaries/system/libnvcore.so %buildroot/%_libdir/%name/libnvcore.so
install -Dm 0644 binaries/system/libnvimage.so %buildroot/%_libdir/%name/libnvimage.so
install -Dm 0644 binaries/system/libnvmath.so %buildroot/%_libdir/%name/libnvmath.so
install -Dm 0644 binaries/system/libnvtt.so %buildroot/%_libdir/%name/libnvtt.so

# install additional executables (upstream do not pack it)
# install -Dm 0755 binaries/system/ActorEditor %buildroot/%_libexecdir/%name/bin/ActorEditor
# install -Dm 0755 binaries/system/ColourTester %buildroot/%_libexecdir/%name/bin/ColourTester

# install game desktop and icon files
install -Dm 0644 build/resources/%name.desktop %buildroot/%_desktopdir/%name.desktop
install -Dm 0644 build/resources/%name.png %buildroot/%_iconsdir/%name.png

# copy game command line options file to source dir
install -Dm 0644 binaries/system/readme.txt ./command-line-options.txt

%files
%doc README.txt LICENSE.txt command-line-options.txt
%_bindir/*
%_libdir/%name/*
%_desktopdir/*
%_iconsdir/*

# Additional executables that we do not pack (see above)
# _libexecdir/%name/*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.r08832-alt2.4
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.r08832-alt2.3
- Rebuilt with Boost 1.48.0

* Thu Jul 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.r08832-alt2.2
- Rebuilt with Boost 1.47.0

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.r08832-alt2.1
- Rebuilt with Boost 1.46.1

* Wed Dec 15 2010 Kirill A. Shutemov <kas@altlinux.org> 0.r08832-alt2
- drop libbfd-devel and libiberty-devel BuildReqReq'es

* Mon Dec 12 2010 Anton Chernyshov <ach@altlinux.org> 0.r08832-alt1
- new upstream release - r08832
- clean up spec file frome some stuff
- minor spec file changes

* Wed Nov 3 2010 Anton Chernyshov <ach@altlinux.org> 0.r08413-alt1
- add new build dependencies
- fix build on i586
- fix game version
- fix changelog according to distribution rules

* Tue Oct 26 2010 Anton Chernyshov <ach@altlinux.org> r08413-alt1.1
- add new upstream documentation to package

* Tue Oct 19 2010 Anton Chernyshov <ach@altlinux.org> r08413-alt1
- new upstream release
- new build deps
- fix and clean up .spec file

* Tue Oct 19 2010 Anton Chernyshov <ach@altlinux.org> r07970-alt1
- create spec file and first build
- add buildreq dependencies
