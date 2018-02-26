%define xf86 XFree86
%define xorgold xorg-x11

%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-100dpi
Version: 7.0.0
Release: alt3

Summary: X Window System 100dpi fonts
Group: System/Fonts/X11 bitmap
License: MIT/X11

Url: http://xorg.freedesktop.org

Source0: font-alias-1.0.1.tar.bz2
Source1: font-adobe-100dpi-1.0.0.tar.bz2
Source2: font-bh-lucidatypewriter-100dpi-1.0.0.tar.bz2
Source3: font-adobe-utopia-100dpi-1.0.1.tar.bz2
Source4: font-bitstream-100dpi-1.0.0.tar.bz2
Source5: font-bh-100dpi-1.0.0.tar.bz2

Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

PreReq: mkfontdir mkfontscale fontconfig >= 2.4.2
Obsoletes: %xf86-100dpi-fonts %xorgold-100dpi-fonts
Obsoletes: %xf86-100dpi-fonts-unicode %xorgold-100dpi-fonts-unicode
Provides: %xf86-100dpi-fonts = 4.4 %xf86-100dpi-fonts-unicode = 4.4
Provides: %xorgold-100dpi-fonts = %version-%release
Provides: %xorgold-100dpi-fonts-unicode = %version-%release

BuildArch: noarch
BuildRequires: bdftopcf xorg-x11-font-utils mkfontdir mkfontscale pkg-config

%description
If you're going to use the X Window System and you have a
high resolution monitor capable of 100 dpi, you should install
%name. This package contains a set of 100 dpi fonts used on
most Linux systems.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5

%build
cd font-alias-*
%configure \
	--with-top-fontdir=%_fontsdir
%make
cd ..
for d in `ls | grep -v alias`; do
    cd $d
    %configure \
	--with-fontdir=%_fontsdir/100dpi
    %make_build
    cd ..
done

%install
for d in *; do
    cd $d
    %make DESTDIR=%buildroot install
    cd ..
done

%__mkdir_p %buildroot%_sysconfdir/X11/fontpath.d
%__ln_s ../../..%_fontsdir/100dpi %buildroot%_sysconfdir/X11/fontpath.d/bitmap-100dpi:unscaled:pri=20

%triggerun -- %name <= 7.0.0-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/100dpi:unscaled ||:
fi

%post
%_bindir/mkfontdir %_fontsdir/100dpi
%_bindir/fc-cache %_fontsdir/100dpi

%files
%_sysconfdir/X11/fontpath.d/*
%ghost %_fontsdir/100dpi/fonts.scale
%_fontsdir/100dpi

%changelog
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

