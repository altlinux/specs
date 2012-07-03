Name:     atari800
Version:  2.2.1
Release:  alt1

Summary:  An emulator of 8-bit Atari personal computers.
License:  GPL
URL:      http://atari800.sourceforge.net/
Group:    Emulators

Packager: Evgeny V. Shishkov <shev@altlinux.org>
Source:   %name-%version.tar.gz
Source1:  %name-16.png
Source2:  ATARI5200.ROM
Source3:  ATARIBAS.ROM
Source4:  ATARIOSA.ROM
Source5:  ATARIOSB.ROM
Source6:  ATARIXL.ROM
Source7:  %name.desktop
Source8:  %name-32.png
Source9:  %name-48.png
Patch1:   atari800.cfg.patch

Summary(ru_RU.UTF8): Эмулятор 8-bit компьютера Atari.

# Automatically added by buildreq on Thu Apr 02 2009
BuildRequires: libSDL-devel libX11-devel libpng-devel

%package -n %name-rom
BuildArch: noarch
Summary: ROM files for Atari800 emulator
Summary(ru_RU.UTF8): ROM файлы для эмулятора Atari800
License: Free for use
Group: System/Libraries
Requires: %name = %version-%release

%description
Atari800 is an emulator for the 800, 800XL, 130XE and 5200 models of
the Atari personal computer. It can be used on console, FrameBuffer or X11.
It features excellent compatibility, HIFI sound support, artifacting
emulation, precise cycle-exact ANTIC/GTIA emulation and more.

%description -l ru_RU.UTF-8
Atari800 это эмулятор персонального компьютера Atari моделей 800, 800XL, 130XE и 5200
Он имеет отличную совместимость, HIFI поддержку звука, эмуляцю артифактов,
ANTIC / GTIA эмуляцию и многое другое.

%description -n %name-rom
Notes: Darek Mihocka got the permission from Atari corp. to distribute the images of
Atari 800XL's OS and BASIC ROMs. Package that contains these ROM images
is free now so download and unpack it to get the ROM files needed for Atari800 run.

%description -l ru_RU.UTF-8 -n %name-rom
Примечания: Darek Mihocka получил разрешение от корп. Atari распространять образы Atari 800XL ОС и BASIC ROM.
Пакет, который включает эти образы ROM является бесплатным для загрузки и распаковки,
Он необходим для запуска Atari800.

%prep
%setup -n %name-%version/src
%patch1 -p1

%build
%configure --target=sdl --enable-riodevice --enable-nonlinear_mixing --disable-readline --enable-monitorprofile --enable-monitortrace
%make_build

%install
%make_install DESTDIR="%buildroot/" install

%__install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
%__install -pD -m644 %SOURCE8 %buildroot%_niconsdir/%name.png
%__install -pD -m644 %SOURCE9 %buildroot%_liconsdir/%name.png
%__install -pD -m644 %SOURCE2 %buildroot%_datadir/%name/ATARI5200.ROM
%__install -pD -m644 %SOURCE3 %buildroot%_datadir/%name/ATARIBAS.ROM
%__install -pD -m644 %SOURCE4 %buildroot%_datadir/%name/ATARIOSA.ROM
%__install -pD -m644 %SOURCE5 %buildroot%_datadir/%name/ATARIOSB.ROM
%__install -pD -m644 %SOURCE6 %buildroot%_datadir/%name/ATARIXL.ROM
%__install -pD -m644 %SOURCE7 %buildroot%_desktopdir/%name.desktop

%files -n %name-rom
%_datadir/%name/*

%files
%_bindir/%name
%_docdir/*
%_man1dir/%name.1.bz2
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Mon May 30 2011 Evgeny V. Shishkov <shev@altlinux.org> 2.2.1-alt1
- version 2.2.1 

* Thu Apr 02 2009 Evgeny V. Shishkov <shev@altlinux.org> 2.1.0-alt1
- version 2.1.0

* Mon Mar 16 2009 Evgeny V. Shishkov <shev@altlinux.org> 2.0.3-alt3
- update .desktop file
- add menu icons

* Mon Nov 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 2.0.3-alt2
- remove update_menus, clean_menus from spec file
    (update_menus repocop test)

* Tue May 06 2008 Evgeny V. Shishkov <shev@altlinux.org> 2.0.3-alt1
- Initial build for ALTLinux
