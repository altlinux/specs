%define xf86 XFree86
%define xorgold xorg-x11

%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-misc
Version: 7.0.0
Release: alt6

Summary: Misc fonts required by the X Window System
Group: System/Fonts/X11 bitmap
License: MIT/X11

Url: http://xorg.freedesktop.org

Source0: font-alias-1.0.1.tar.bz2
Source1: font-arabic-misc-1.0.0.tar.bz2
Source2: font-jis-misc-1.0.0.tar.bz2
Source3: font-misc-misc-1.0.0.tar.bz2
Source4: font-cursor-misc-1.0.0.tar.bz2
Source5: font-micro-misc-1.0.0.tar.bz2
Source6: font-mutt-misc-1.0.0.tar.bz2
Source7: font-daewoo-misc-1.0.0.tar.bz2
Source8: font-schumacher-misc-1.0.0.tar.bz2
Source9: font-dec-misc-1.0.0.tar.bz2
Source10: font-sony-misc-1.0.0.tar.bz2
Source11: font-isas-misc-1.0.0.tar.bz2
Source12: font-sun-misc-1.0.0.tar.bz2

Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: mkfontdir mkfontscale fontconfig >= 2.4.2
Obsoletes: %xf86-misc-fonts %xorgold-misc-fonts
Provides: %xf86-misc-fonts = 4.4 %xorgold-misc-fonts = %version-%release

BuildArch: noarch
BuildRequires: bdftopcf xorg-font-utils mkfontdir mkfontscale xorg-util-macros

%description
This package provides the misc fonts that are required by the X Window System.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12

%build
for d in *; do
	cd $d
	%autoreconf
	%configure \
		--with-fontdir=%_fontsdir/misc \
		--with-top-fontdir=%_fontsdir
	%make_build
	cd ..
done

%install
for d in *; do
	cd $d
	%make DESTDIR=%buildroot install
	cd ..
done

mkfontdir %buildroot%_fontsdir/misc/

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir/misc %buildroot%_sysconfdir/X11/fontpath.d/bitmap-misc:unscaled:pri=20

%post
%_bindir/mkfontdir %_fontsdir/misc ||:
%_bindir/fc-cache %_fontsdir/misc ||:

%triggerun -- %name <= 7.0.0-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/misc:unscaled ||:
fi

%triggerpostun -- %name <= 7.0.0-alt3
%_bindir/mkfontdir %_fontsdir/misc ||:
%_bindir/fc-cache %_fontsdir/misc ||:

%files
%_sysconfdir/X11/fontpath.d/*
%ghost %_fontsdir/misc/fonts.scale
%_fontsdir/misc

%changelog
* Wed Apr 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt6
- all misc fonts

* Thu Aug 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt5
- fixed update fonts.dir

* Tue Aug 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt4
- fonts cleanup

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt3
- fixed trigger logic

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt2
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

