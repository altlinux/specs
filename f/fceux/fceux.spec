Name: fceux
Version: 2.1.4a
Release: alt3.1

Summary: FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom Disk System (FDS) emulator
Summary(ru_RU.UTF-8): FCEUX - это эмулятор Nintendo Entertainment System ("Денди"), Famicom и Famicom Disk System (FDS)

License: GPLv2
Group: Emulators
Url: http://fceux.com/web/home.html

Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.src.tar.bz2

# Fixed desktop file and icons from previous version
Source1: fceux.desktop
Source2: fceux.png
Source3: fceux_big.png 


# fix directory and options to build and install
Patch0: %name-%version-alt-fix_install.patch

# patch from openSUSE Build Service to fix build process
Patch1: %name-%version-opensuse-overflow.patch
Patch2: %name-2.1.4a-alt-DSO.patch

BuildRequires: gcc-c++ libgtk+2-devel libSDL-devel python-modules-email scons zlib-devel

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
%patch0
%patch1
%patch2 -p2

%build
CFLAGS="%optflags" scons

%install
# install binaries
install -D -m 755 bin/%name %buildroot/%_bindir/%name
install -D -m 755 bin/%name.chm %buildroot/%_bindir/%name.chm

# fix rights for docs
find documentation/ -type f -exec chmod -x {} \;
for i in Authors.txt changelog.txt NewPPUtests.txt README-SDL TODO-PROJECT TODO-SDL ; do
    chmod -x $i 
done

# install desktop and icons files
install -D -m 644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -D -m 644 %SOURCE2 %buildroot/%_iconsdir/%name.png
install -D -m 644 %SOURCE3 %buildroot/%_pixmapsdir/%name-big.png

%files
%_bindir/*
%doc Authors.txt changelog.txt NewPPUtests.txt README-SDL TODO-PROJECT TODO-SDL documentation/*
%_iconsdir/*
%_desktopdir/*
%_pixmapsdir/*

%changelog
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
