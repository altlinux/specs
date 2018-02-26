Name: vice
Version: 2.1
Release: alt7.1

Summary: Versatile Commodore Emulator
License: GPL v2+
Group: Emulators

Url: http://www.viceteam.org
Source0: http://www.zimmers.net/anonftp/pub/cbm/crossplatform/emulators/VICE/%name-%version.tar.gz
Source1: vice-c128.desktop
Source2: vice-c64.desktop
Source3: vice-cbm2.desktop
Source4: vice-pet.desktop
Source5: vice-plus4.desktop
Source6: vice-vic20.desktop
Source7: vice-vsid.desktop
Source8: vice-c1541.desktop
Source11: vice-normalicons.tar.bz2
Source12: vice-largeicons.tar.bz2
Source13: vice-miniicons.tar.bz2
Patch0: vice-info.patch
Patch1: vice-gettext.patch
Patch2: vice-home_etc.patch
Patch3: vice-2.1-fix-str-fmt.patch
Patch4: vice-2.1-fix-alsa-fragment.patch
Patch5: vice-2.1-gcc44.patch
Patch6: vice-2.1-alt-DSO.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Mar 16 2009
BuildRequires: flex gcc-c++ libGL-devel libSDL-devel libXrandr-devel libesd-devel libgtk+2-devel libjpeg-devel liblame-devel libreadline-devel libungif-devel
BuildRequires: libpng-devel zlib-devel libX11-devel libXxf86vm-devel libalsa-devel

Summary(pl.UTF-8):	Uniwersalny emulator Commodore

%description
VICE is a Versatile Commodore Emulator, i.e. a program that runs on a
Unix, MS-DOS, Win95/NT, OS/2, RiscOS or BeOS machine and executes
programs intended for the old 8-bit Commodore computers. The current
version emulates the C64, the C128 (80 column screen is included now),
the VIC20, all the PET models (except the SuperPET 9000, which is out
of line anyway), CBM-II (aka C610) and the Plus4.

%description -l pl.UTF-8
VICE jest wszechstronnym emulatorem 8-bitowego komputera Commodore.
Aktualna wersja emuluje C64, C128 (wraz z trybem pracy 80 kolumnowym),
VIC20, wszystkie modele PET (poza SuperPET 9000, który zresztą nie
pasował do tej linii), CBM-II (C610) oraz Plus4.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p2
%patch5 -p0
%patch6 -p2

%build
touch ABOUT-NLS config.rpath
%autoreconf
%configure \
	--enable-autobpp \
	--with-sdl \
	--enable-fullscreen \
	--enable-gnomeui \
	--enable-nls \
	--without-xaw3d \
	--without-included-gettext \
	--with-x
%make

%install
install -d %buildroot{%_desktopdir,%_pixmapsdir}

perl -i -pe 's/SUBDIRS = html\n//' doc/Makefile
%make_install install DESTDIR=%buildroot 

rm -f doc/html/{Makefile*,texi2html}
rm -rf %buildroot%_datadir/vice/doc

install -pm644 \
	%SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 \
	%SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 \
	%buildroot%_desktopdir

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
tar xjf %SOURCE11 -C %buildroot%_iconsdir/hicolor/32x32/apps
tar xjf %SOURCE12 -C %buildroot%_iconsdir/hicolor/48x48/apps
tar xjf %SOURCE13 -C %buildroot%_iconsdir/hicolor/16x16/apps

pushd src/arch/unix/x11
for i in *icon.c; do
	install -pm644 $i %buildroot%_pixmapsdir/${i%%.c}.xpm
done
popd

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog FEEDBACK NEWS README
%doc doc/iec-bus.txt doc/mon.txt doc/html
%_bindir/*
%_usr/lib/%name/
%_mandir/man?/*
%_infodir/*.info*
%_desktopdir/*.desktop
%_pixmapsdir/*
%_iconsdir/hicolor/*/*/*.png

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt7.1
- Fixed build

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 2.1-alt7
- more missing BR: back

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 2.1-alt6
- re-added lost BRs, thx at@

* Thu May 28 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt5
- fixed the last problem with deeply broken mandriva desktop files
  (thanks viy@ who did better than desktop-file-validate)

* Tue May 26 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt4
- fixed a couple of broken desktop files

* Sun May 24 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt3
- rebuilt with libalsa-1.0.20-alt2

* Fri May 15 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt2
- applied gentoo patch to fix FTBFS with gcc-4.4

* Tue Mar 17 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- built for ALT Linux (folks from Virtual Sky Solutions asked for it)
  + somewhat based on PLD 2.1-1, Mandriva 2.1-2mdk and DAG's
    specs, resources and patches
  + heavy cleanup/merge/adaptation
  + VICEDIR=/usr/lib/vice
- NB: no C64, no ROMs, so you guessed no maintainer ;-)
