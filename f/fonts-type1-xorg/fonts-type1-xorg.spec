%define xf86 XFree86
%define xorgold xorg-x11

%define _fontsdir %_datadir/fonts/type1

Name: fonts-type1-xorg
Version: 7.0.0
Release: alt4

Summary: Type1 fonts required by the X Window System
Group: System/Fonts/Type1
License: MIT/X11

Url: http://xorg.freedesktop.org

Source0: font-adobe-utopia-type1-1.0.1.tar.bz2
Source2: font-bitstream-type1-1.0.0.tar.bz2
Source3: font-xfree86-type1-1.0.0.tar.bz2
Source4: font-bh-type1-1.0.0.tar.bz2
Source5: font-ibm-type1-1.0.0.tar.bz2

Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

PreReq: fontconfig >= 2.4.2
Obsoletes: %xf86-type1-fonts %xorgold-type1-fonts
Provides: %xf86-type1-fonts = 4.4
Provides: %xorgold-type1-fonts = %version-%release

BuildArch: noarch
BuildRequires: mkfontdir mkfontscale

%description
This package provides the type1 fonts that are required by the X Window System.

%prep
%setup -q -c -a2 -a3 -a4 -a5

%install
%__mkdir_p %buildroot%_fontsdir/Type1
find -name \*.pfa -print -exec cp -t %buildroot%_fontsdir/Type1 {} \;
find -name \*.pfb -print -exec cp -t %buildroot%_fontsdir/Type1 {} \;
find -name \*.afm -print -exec cp -t %buildroot%_fontsdir/Type1 {} \;
mkfontscale %buildroot%_fontsdir/Type1
ln -s fonts.scale %buildroot%_fontsdir/Type1/fonts.dir

%__mkdir_p %buildroot%_sysconfdir/X11/fontpath.d
%__ln_s ../../..%_fontsdir/Type1 %buildroot%_sysconfdir/X11/fontpath.d/type1-Type1:pri=40

%triggerun -- %name <= 7.0.0-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/Type1 ||:
fi

%post
%_bindir/fc-cache %_fontsdir/Type1 ||:

%files
%_sysconfdir/X11/fontpath.d/*
%_fontsdir/Type1

%changelog
* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt4
- added lost pfa, pfb files

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt3
- fixed trigger logic

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt2
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 7.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt1
- Xorg-7.0RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.0-alt0.1
- initial release

