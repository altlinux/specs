%define xf86 XFree86
%define xorgold xorg-x11

%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-75dpi
Version: 7.0.0
Release: alt4

Summary: X Window System 75dpi fonts
Group: System/Fonts/X11 bitmap
License: MIT/X11

Url: http://xorg.freedesktop.org

Source0: font-alias-1.0.1.tar.bz2
Source1: font-adobe-75dpi-1.0.0.tar.bz2
Source2: font-bh-75dpi-1.0.0.tar.bz2
Source3: font-bitstream-75dpi-1.0.0.tar.bz2
Source4: font-adobe-utopia-75dpi-1.0.1.tar.bz2
Source5: font-bh-lucidatypewriter-75dpi-1.0.0.tar.bz2

Patch1: font-adobe-75dpi-1.0.0-alt-iso10646cyr.patch.bz2
Patch2: font-bh-75dpi-1.0.0-alt-iso10646cyr.patch.bz2

Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

PreReq: mkfontdir mkfontscale fontconfig >= 2.4.2
Obsoletes: %xf86-75dpi-fonts %xorgold-75dpi-fonts
Obsoletes: %xf86-75dpi-fonts-unicode %xorgold-75dpi-fonts-unicode
Provides: %xf86-75dpi-fonts = 4.4 %xf86-75dpi-fonts-unicode = 4.4
Provides: %xorgold-75dpi-fonts = %version-%release
Provides: %xorgold-75dpi-fonts-unicode = %version-%release

BuildArch: noarch
BuildRequires: bdftopcf xorg-x11-font-utils mkfontdir mkfontscale pkg-config

%description
If you're going to use the X Window System and you have a
high resolution monitor capable of 75 dpi, you should install
%name. This package contains a set of
75 dpi fonts used on most Linux systems.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5

%patch1 -p0
%patch2 -p0

%build
cd font-alias-*
%configure \
	--with-top-fontdir=%_fontsdir
%make
cd ..
for d in `ls | grep -v alias`; do
    cd $d
    %configure \
	--with-fontdir=%_fontsdir/75dpi
    %make_build
    cd ..
done

%install
for d in font-*; do
    cd $d
    %make DESTDIR=%buildroot install
    cd ..
done

%__mkdir_p %buildroot%_sysconfdir/X11/fontpath.d
%__ln_s ../../..%_fontsdir/75dpi %buildroot%_sysconfdir/X11/fontpath.d/bitmap-75dpi:unscaled:pri=20

%triggerun -- %name <= 7.0.0-alt2
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/75dpi:unscaled ||:
fi

%post
%_bindir/mkfontdir %_fontsdir/75dpi ||:
%_bindir/fc-cache %_fontsdir/75dpi ||:

%files
%_sysconfdir/X11/fontpath.d/*
%ghost %_fontsdir/75dpi/fonts.scale
%_fontsdir/75dpi

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt4
- fixed trigger logic

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt3
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jan 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt2
- added alt-iso10646cyr patches

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

