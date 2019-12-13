Name: vcmi
Version: 0.99
Release: alt5

Summary: Open-source project aiming to reimplement HMM3:WoG game engine
Summary(ru_RU.UTF-8): Open-source движок для игры HMM3:WoG
License: GPLv2+
Group: Games/Strategy
URL: http://wiki.vcmi.eu/index.php?title=Main_Page
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch1: vcmi-boost-1.66.patch
Patch2: vcmi-boost-1.66-2.patch
# https://github.com/vcmi/vcmi/pull/615
Patch3: vcmi-boost-1.66-3.patch
Patch4: vcmi-boost-1.66-4.patch
Patch5: vcmi-boost-1.66-5.patch
Patch6: vcmi-boost-1.66-6.patch
Patch7: vcmi-boost-1.66-7.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: doxygen
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-asio-devel
BuildRequires: boost-interprocess-devel
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libavresample)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(fuzzylite)
BuildRequires: pkgconfig(minizip)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(SDL2_ttf)
BuildRequires: pkgconfig(zlib)

Requires: ffmpeg

%description
The purpose of VCMI project is to rewrite entire HOMM 3: WoG engine from
scratch, giving it new and extended possibilities. We hope to support 
mods and new towns already made by fans but abandoned because of game
code limitations.

VCMI is fan-made open-source project in progress. We already allow
support for maps of any sizes, higher resolutions and extended engine
limits. However, although working, the game is not finished. There are
still many features and functionalities to add, both old and brand new.

As yet VCMI is not standalone program, it uses Wake of Gods files and
graphics. You need to install WoG before running VCMI.

%description -l ru_RU.UTF8
Цель проекта VCMI состоит в том, чтобы переписать полностью движок
HoMM 3: WoG, и тем самым дать ему новые и расширенные возможности.
Мы надеемся реализовать поддержку модов и новых городов, которые уже
сделаны фанатами, но от которых отказались из-за ограничений кода игры.

VCMI это фанатский проект с открытым исходным кодом. Мы уже реализовали
поддержку карт любых размеров, более высокое разрешение и расширенные
возможности движка. Тем не менее хотя игра и работает, она ещё не
закончена. Есть еще много особенностей которые нужно добавить, как 
старых так и новых.

Пока VCMI не отдельная программа, она использует файлы от Wake of Gods.
Вам нужно установить WoG перед запуском VCMI.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
    
%cmake -DLIB_DIR=%_lib/%name \
       -DCMAKE_INSTALL_LIBDIR=%_lib \
       -DCMAKE_SKIP_RPATH=OFF \
       -DENABLE_SDL2=ON

%cmake_build

%install
%cmakeinstall_std
mv %buildroot/%_libdir/%name/libvcmi.so %buildroot/%_libdir/libvcmi.so
rm -f %buildroot%_libdir/*.a

%files
%doc README.md README.linux AUTHORS ChangeLog
%_bindir/%{name}*
%_datadir/%name/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_libdir/lib%name.so
%_libdir/%name/

%changelog
* Wed Dec 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.99-alt5
- Rebuilt with boost-1.71.0.

* Fri Jun 22 2018 Anton Midyukov <antohami@altlinux.org> 0.99-alt4
- Rebuilt with ffmpeg 4.0

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.99-alt3.1
- NMU: rebuilt with boost-1.67.0

* Tue May 01 2018 Anton Midyukov <antohami@altlinux.org> 0.99-alt3
- Rebuilt with boost 1.66
- Update buildrequires

* Wed Jun 07 2017 Anton Midyukov <antohami@altlinux.org> 0.99-alt2
- Rebuild with ffmpeg.

* Wed Nov 02 2016 Anton Midyukov <antohami@altlinux.org> 0.99-alt1
- New version 0.99

* Thu Mar 03 2016 Anton Midyukov <antohami@altlinux.org> 0.98h-alt1
- New version.

* Sun Aug 23 2015 Anton Midyukov <antohami@altlinux.org> 0.98-alt1
- New version (Closes: 31364);
- Fix build with boost-1.58.

* Fri Oct 11 2013 Igor Zubkov <icesik@altlinux.org> 0.94-alt3
- rebuild with -O3 optimization

* Thu Oct 10 2013 Igor Zubkov <icesik@altlinux.org> 0.94-alt2
- rebuild with gcc 4.7

* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.94-alt1
- 0.93 -> 0.94

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.93-alt1
- build for Sisyphus (closes #28586)

* Sun Oct 21 2012 VCMI - 0.9-2
- Second release of 0.9, Fixed battles crash

* Sat Oct 06 2012 VCMI - 0.9-1
- New upstream release

* Sun Jun 08 2012 VCMI - 0.89-1
- Initial version
