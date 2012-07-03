Name: wmfire
Version: 1.2.4
Release: alt2

Summary: WindowMaker dock-app showing CPU load as a flame
License: GPL
Group: Graphical desktop/Window Maker

Url: http://www.swanson.ukfsn.org
Source0: %url/%name/%name-%version.tar.gz
Source1: %name-icons.tar.bz2
Source2: %name.desktop
Source100: %name.watch
Patch0: wmfire-1.2.3-stringh.patch
Patch1: wmfire-1.2.4-no_display.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Аплет WindowMaker, отображающий загрузку в виде пламени
Summary(uk_UA.KOI8-U): Аплет WindowMaker, який зобража╓ завантаження як полум'я

# Automatically added by buildreq on Sun Dec 10 2006 (-bi)
BuildRequires: imake libSM-devel libXext-devel libgtk+2-devel libgtop-devel xorg-cf-files

# buildreqs MUST NOT get gtk1 in!

%description
wmfire is an eye-candy dock applet for Window Maker that displays
generated fire, possibly according to how much load the system is
experiencing, or from a number somewhere in a file. wmfire
requires very little CPU.  It has options for cyanish or
orange/red flames, you can even set it to display your
motherboard temperature through lm_sensors.

This is an update of the original wmfire dock applet. Like the
wmufo program it uses the GDK library to improve its speed -
using less than half the cpu of the original program.

%description -l ru_RU.KOI8-R
wmfire - занятный аплет для WindowMaker, отображающий загрузку
системы (или числовые данные из заданного файла) в виде пламени,
при этом сам ее практически не увеличивает.

Это обновленная версия, которая использует GDK для понижения
использования процессора при отрисовке (примерно вдвое).

%description -l uk_UA.KOI8-U
wmfire - ц╕кавий аплет для WindowMaker, який в╕дображу╓
завантаження системи (чи числов╕ дан╕ з файлу) у вигляд╕ полум'я;
при цьому сам в╕н майже не дода╓ до нього.

Це поновлена верс╕я, котра використову╓ GDK для зниження
використання процесору при малюванн╕ (приблизно вдв╕ч╕).

%prep
%setup -a1
%patch0 -p1
%patch1 -p0

%build
export LDFLAGS="$LDFLAGS -lgdk-x11-2.0"
export CFLAGS="$CFLAGS %optflags \
	-funroll-loops \
	-fexpensive-optimizations \
	-fomit-frame-pointer \
	-I%_includedir/libgtop-2.0"
%autoreconf
%configure --enable-session
%make_build

%install
%makeinstall
install -pDm644 16x16.png %buildroot%_miconsdir/%name.png
install -pDm644 32x32.png %buildroot%_niconsdir/%name.png
install -pDm644 48x48.png %buildroot%_liconsdir/%name.png
install -pDm644 %SOURCE2  %buildroot%_desktopdir/%name.desktop

%files
%doc AUTHORS ALL_I_GET_IS_A_GREY_BOX README ChangeLog NEWS
%_man1dir/*
%_bindir/*
%_desktopdir/*
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt2
- added watch file

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4, yay!
- fixed desktop file contents/permissions (thx repocop)
- applied gentoo patches (mainly libgtk+2 >= 2.18 fix)

* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 1.2.3-alt4.5.6
- applied repocop patch
- moved desktop file to a, well, file while fixin' it up
- adjusted description text width

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 1.2.3-alt4.5
- replaced debian menufile with desktop one

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.2.3-alt4
- applied repocop patch
- minor spec cleanup

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 1.2.3-alt3
- updated Url:
- buildreq

* Tue Feb 28 2006 Michael Shigorin <mike@altlinux.org> 1.2.3-alt2
- rebuild (libgtop2)

* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3
- updated package Url

* Tue Jun 29 2004 Michael Shigorin <mike@altlinux.ru> 1.2.2-alt1
- 1.2.2
- patch merged upstream

* Thu Jun 17 2004 Michael Shigorin <mike@altlinux.ru> 1.2.1-alt1
- 1.2.1
- added workaround by Sergey Pinaev (dfo@)

* Wed Apr 07 2004 Michael Shigorin <mike@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Jan 31 2004 Michael Shigorin <mike@altlinux.ru> 1.1.99-alt3
- *fixed* build (was linking both gtk1/2, glib1/2 in)
- added a few optimization flags

* Tue Jan 27 2004 Michael Shigorin <mike@altlinux.ru> 1.1.99-alt2
- strange workaround for broken build (LDFLAGS)

* Thu Sep 04 2003 Michael Shigorin <mike@altlinux.ru> 1.1.99-alt1
- switched to version from http://www.swanson.uklinux.net/#wmfire
  (link found in http://newrpms.sunsite.dk package)
- gtk2/libgtop2 version
- minor prettyspec'ing :)

* Fri Oct 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.0.3.9pre4-alt2
- rebuild with gcc3

* Tue May 07 2002 Michael Shigorin <mike@altlinux.ru> 0.0.3.9pre4-alt1
- built for ALT Linux

* Sat May 04 2002 Michael Shigorin <mike@altlinux.ru> 0.0.3.9pre4-alt1
- updated version
- translated package info
- lazily borrowed icons from Cooker

* Fri May 03 2002 Michael Shigorin <mike@altlinux.ru> 0.0.3.8-alt1
- built for ALT Linux

