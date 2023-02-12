Name: fceux
Version: 2.6.5
Release: alt1

Summary: FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom Disk System (FDS) emulator
Summary(ru_RU.UTF-8): FCEUX - это эмулятор Nintendo Entertainment System ("Денди"), Famicom и Famicom Disk System (FDS)

License: GPLv2
Group: Emulators
Url: http://fceux.com/web/home.html

Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.gz

# Fixed desktop file and icons from previous version
Source1: fceux.desktop
Source2: fceux.png
Source3: fceux_big.png 


# fix directory and options to build and install
Patch0: %name-2.1.4a-alt-fix_install.patch

# patch from openSUSE Build Service to fix build process
Patch1: %name-2.1.4a-opensuse-overflow.patch
Patch2: %name-2.1.4a-alt-DSO.patch
Patch3: %name-2.1.4a-alt-glibc-2.16.patch
Patch4: %name-2.1.4a-alt-zlib-1.2.7.patch
#Patch5: %name-2.2.3-alt-gcc8-fix.patch
# patch for SConstruct files (https://stackoverflow.com/questions/8427352/how-to-solve-attributeerror-environ-object-has-no-attribute-has-key#8427495)
Patch6: %name-2.2.3-SConstruct.patch

#BuildRequires: libgtk+2-devel
#BuildRequires: liblua5.3-devel
BuildRequires: gcc-c++ libSDL2-devel python-modules-email scons zlib-devel  libminizip-devel qt5-base-devel cmake
# liblua5.1-compat-devel

Excludearch: armh


%description
FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom Disk System
FDS) emulator. It supports both PAL (European) and NTSC (USA/JPN) modes. 
It supports both Windows and SDL versions for cross compatibility.
The FCEUX concept is that of an "all in one" emulator that offers accurate 
emulation and the best options for both casual play and a variety of more 
advanced emulator functions. For pro users, FCEUX offers tools for debugging, 
rom-hacking, map making, Tool-assisted movies, and Lua scripting

FCEUX is an evolution of the original FCE Ultra emulator. Over time FCE Ultra
had separated into many distinct branches. The concept behind FCEUX is to merge 
elements from FCEU Ultra, FCEU rerecording, FCEUXD, FCEUXDSP, FCEUXDSP CE, 
and FCEU-mm into a single branch of FCEU.

%description -l ru_RU.UTF-8
FCEUX - это эмулятор Nintendo Entertainment System ("Денди"), Famicom и Famicom Disk 
System (FDS). Он обеспечивает поддержку видеорежимов PAL (Европа) и NTSC (США/Япония) и
существует в двух версиях - Windows и SDL (UNIX-совместимые системы).

Основная идея FCEUX - это эмулятор "все-в-одном": хорошая эмуляция и прекрасный набор опций
и для игр и для использования дополнительных функций. Так, например, для опытных пользователей
FCEUX предоставляет набор утилит для отладки и исследования ROM, создания карт, записи видео,
поддержку скриптов Lua.

FCEUX - это развитие эмулятора FCE Ultra. В какое-то время данный проект раскололся на
несколько независимых ветвей. Задача FCEUX собрать их все в один проект FCEU.

%prep

%setup

# Remove attic directories
find . -name 'attic' -type d -prune -exec rm -rf {} \;

# Remove Visual Studio directory
rm -rf vc

# Remove bundled LUA library
#rm -rf src/lua

# Remove bundled minizip library
rm -rf src/utils/unzip.*

# Fix end-of-line-encoding
sed -i 's/\r//' changelog.txt NewPPUtests.txt \
  documentation/Videolog.txt

# Fix desktop file
sed -i 's/\/usr\/share\/pixmaps\/fceux1.png/fceux/' fceux.desktop
sed -i '/MimeType=*/s/$/;/' fceux.desktop
sed -i '/OnlyShowIn=*/s/$/;/' fceux.desktop

# Public release
sed -i 's!//#define PUBLIC_RELEASE!#define PUBLIC_RELEASE!' src/version.h

# Set git data
sed -i -r 's!(GIT_URL=).+!\1"%{giturl}"!' scripts/genGitHdr.sh
sed -i -r 's!(GIT_REV=).+!\1"%{commit}"!' scripts/genGitHdr.sh

#setup
#patch0
#patch1
#patch2 -p2
#patch3 -p2
#patch4 -p2
#patch5 -p2
#patch6 -p2
#build
#add_optflags -fpermissive
#CFLAGS="%optflags" scons

%build
%cmake
%cmake_build


%install
%cmake_install

# install binaries
#install -D -m 755 %_cmake__builddir/src/%name %buildroot/%_bindir/%name
#install -D -m 755 bin/%name.chm %buildroot/%_bindir/%name.chm

# fix rights for docs
#find documentation/ -type f -exec chmod -x {} \;
#for i in Authors changelog.txt NewPPUtests.txt README-SDL TODO-SDL ; do
#    chmod -x $i 
#done

# install desktop and icons files
install -D -m 644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -D -m 644 %SOURCE2 %buildroot/%_iconsdir/%name.png
install -D -m 644 %SOURCE3 %buildroot/%_pixmapsdir/%name-big.png

%files
%_bindir/*
%doc ChangeLog NewPPUtests.txt README NEWS TODO-SDL documentation/*
%_iconsdir/*
%_desktopdir/*
%_pixmapsdir/*
%_man6dir/*
%_datadir/%name/*
%dir %_datadir/%name/palettes
%dir %_datadir/%name/luaScripts
%dir %_datadir/%name/tools



%changelog
* Sun Feb 12 2023 Ilya Mashkin <oddity@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Fri Mar 25 2022 Ilya Mashkin <oddity@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Tue Mar 08 2022 Ilya Mashkin <oddity@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Sat Feb 05 2022 Ilya Mashkin <oddity@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Thu Jan 20 2022 Ilya Mashkin <oddity@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Jan 14 2022 Ilya Mashkin <oddity@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Sat Oct 23 2021 Ilya Mashkin <oddity@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Jun 27 2021 Ilya Mashkin <oddity@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Apr 13 2021 Arseny Maslennikov <arseny@altlinux.org> 2.3.0-alt2
- NMU: adapted to altlinux.org/CMakeMigration2021.

* Sun Jan 31 2021 Ilya Mashkin <oddity@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Fri Jan 29 2021 Ilya Mashkin <oddity@altlinux.ru> 2.2.3-alt4
- rebuild

* Sat Mar 28 2020 Artyom Bystrov <arbars@altlinux.org> 2.2.3-alt3
- Fixed build

* Mon Feb 11 2019 Ivan Razzhivin <underwit@altlinux.org> 2.2.3-alt2
- GCC8 fix

* Thu Aug 04 2016 Ilya Mashkin <oddity@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Sun Sep 29 2013 Ilya Mashkin <oddity@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Apr 25 2013 Ilya Mashkin <oddity@altlinux.ru> 2.2.1.1-alt1
- 2.2.1.1

* Wed Nov 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4a-alt3.2
- Fixed build

* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4a-alt3.1
- Fixed build

* Sat Feb 18 2012 Ilya Mashkin <oddity@altlinux.ru> 2.1.4a-alt3
- rebuild

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.4a-alt2
- fix build

* Wed Nov 10 2010 Anton Chernyshov <ach@altlinux.org> 2.1.4a-alt1
- create (more or less) generic spec file and initial build...
- add desktop and icons from previous version
- add openSUSE Build Service patch to fix build process
