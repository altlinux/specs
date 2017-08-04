Name: bk
Version: 20050826
Release: alt3

Summary: BK0010, BK0011M and Terak Emulator
License: BSD
Group: Emulators

Url: http://www.mailcom.com/bk0010
#URL: http://sourceforge.net/projects/bk-terak-emu
Source0: bk-terak-emu.2005.08.26.tar.gz
Source1: bk.png
Source2: bk.sh
Source3: User.txt
Source4: System.txt
Source5: bk.desktop
Patch: bk-terak-emu.2005.08.26-linuxsound.diff

BuildRequires: esound libSDL-devel
BuildRequires: gcc >= 3.2
Requires: alsa-oss

Summary(ru_RU.UTF-8): Эмулятор БК0010, БК0011М и Terak

%description
BK0010, BK0011M and Terak Emulator by Leonid Broukhis.

%description -l ru_RU.UTF-8
Эмулятор БК0010, БК0011М и Terak. Написан Леонидом Брухисом.

%prep
%setup -n bk-terak-emu.2005.08.26
%patch -p1
sed -i 's,/usr/lib,`getconf LIBDIR`,' Makefile
cat %SOURCE3 > User.txt
cat %SOURCE4 > System.txt

%build
%make

%install
install -m755 -D bk %buildroot%_bindir/bk.bin
install -m755 -D maketape %buildroot%_bindir/maketape
install -m755 -D readtape %buildroot%_bindir/readtape
install -m755 -d %buildroot%_datadir/bk
install -m644 Rom/*.ROM %buildroot%_datadir/bk
install -m644 -D %SOURCE1 %buildroot%_datadir/pixmaps/bk.png
install -m755 -D %SOURCE2 %buildroot%_bindir/bk
install -m644 -D po/messages.mo %buildroot%_datadir/locale/ru/LC_MESSAGES/%name.mo
#install -m755 -d %buildroot%_datadir/applications
install -m644 -D %SOURCE5 %buildroot%_datadir/applications/bk.desktop

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/bk
%_datadir/pixmaps/bk.png
%_desktopdir/bk.desktop
%doc README* System.txt User.txt

%changelog
* Fri Aug 04 2017 Michael Shigorin <mike@altlinux.org> 20050826-alt3
- allow build on 64-bit platforms
- minor spec cleanup
- aoss out-of-box

* Sun Nov 19 2006 Vyacheslav Dikonov <slava@altlinux.ru> 20050826-alt2
- returned older but better linux-only sound.c

* Sun Nov 19 2006 Vyacheslav Dikonov <slava@altlinux.ru> 20050826-alt1
- 2005.08.26, ru.po updated, freedesktop menu

* Wed Nov 17 2004 Vyacheslav Dikonov <slava@altlinux.ru> 20041117-alt1
- 2004.11.17

* Sat Aug 23 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.1-0
- ALTLInux build
bk-terak-emu.2005.08.26-linuxsound.diff
