%define xf86 XFree86
%define xorgold xorg-x11

%define _fontsdir %_datadir/fonts/ttf

Name: fonts-ttf-xorg
Version: 1.0.0
Release: alt3
Serial: 1
Summary: TrueType fonts provided by the X Window System
Group: System/Fonts/Type1
License: MIT/X11

Url: http://xorg.freedesktop.org

Source0: font-bh-ttf-%version.tar.bz2

Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

PreReq: fontconfig >= 2.4.2
Obsoletes: %xf86-ttf-fonts %xorgold-ttf-fonts
Provides: %xf86-ttf-fonts = 4.4
Provides: %xorgold-ttf-fonts = 7.0.0-%release

BuildArch: noarch
BuildRequires: mkfontdir mkfontscale

%description
A collection of truetype fonts which are part of the core X Window System
distribution.

%prep
%setup -q -n font-bh-ttf-%version

%install
%__mkdir_p %buildroot%_fontsdir/TTF
%__install -m644 *.ttf %buildroot%_fontsdir/TTF/
mkfontscale %buildroot%_fontsdir/TTF
mkfontdir %buildroot%_fontsdir/TTF

%__mkdir_p %buildroot%_sysconfdir/X11/fontpath.d
%__ln_s ../../..%_fontsdir/TTF %buildroot%_sysconfdir/X11/fontpath.d/ttf-TTF:pri=50

%triggerun -- %name <= 1:1.0.0-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/TTF ||:
fi

%post
%_bindir/fc-cache %_fontsdir/TTF ||:

%files
%_sysconfdir/X11/fontpath.d/*
%_fontsdir/TTF

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt3
- fixed trigger logic

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt2
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt1
- Xorg-7.0RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.0-alt0.1
- initial release

