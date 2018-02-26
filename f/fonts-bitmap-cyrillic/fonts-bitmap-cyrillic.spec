%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-cyrillic
Version: 2.3.1
Release: alt7
License: distributable
Source: xrus-2.3.1-src.tgz

Group: System/Fonts/X11 bitmap
Summary: Cyrillic bitmap fonts for the X Window System in koi8-r encoding

Packager: Valery V. Inozemtsev <shrek@altlinux.ru>

PreReq: mkfontdir fontconfig >= 2.4.2
Obsoletes: xorg-x11-cyrillic-fonts
Provides: xorg-x11-cyrillic-fonts = %version-%release

BuildArch: noarch
BuildRequires: xorg-x11-font-utils

%description
Collection of cyrillic raster fonts for X Window System by Andrey A. Chernov.

%prep
%setup -q -n xrus-2.3.1-src

%build
%make X11R6

%install
%make instX11R6 USERDIR=%buildroot%_fontsdir/cyrillic
rm -f %buildroot%_fontsdir/cyrillic/xrus.info

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir/cyrillic/misc %buildroot%_sysconfdir/X11/fontpath.d/bitmap-cyrillic-misc:unscaled:pri=10
ln -s ../../..%_fontsdir/cyrillic/100dpi %buildroot%_sysconfdir/X11/fontpath.d/bitmap-cyrillic-100dpi:unscaled:pri=10
ln -s ../../..%_fontsdir/cyrillic/75dpi %buildroot%_sysconfdir/X11/fontpath.d/bitmap-cyrillic-75dpi:unscaled:pri=10

%triggerin -- %name <= 2.3.1-alt4
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r  %_fontsdir/cyrillic/misc:unscaled
	%_sbindir/chkfontpath -q -r  %_fontsdir/cyrillic/75dpi:unscaled
	%_sbindir/chkfontpath -q -r  %_fontsdir/cyrillic/100dpi:unscaled
fi

%post
mkfontdir %_fontsdir/cyrillic/misc
mkfontdir %_fontsdir/cyrillic/100dpi
mkfontdir %_fontsdir/cyrillic/75dpi

%postun
%_bindir/fc-cache --system-only ||:

%files
%doc README.Winitzki xrus.info
%_sysconfdir/X11/fontpath.d/*
%_fontsdir/cyrillic

%changelog
* Thu Nov 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt7
- added "PreReq: mkfontdir" (close #13509)

* Mon Sep 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt6
- fixed %%post
- added update fonconfig cache in %%postun

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt5
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt4
- removed rpath for mkfontdir

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt3
- rebuild with new policy

* Sun Oct 17 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt2
- fixed requires for xorg-x11-6.8.1-alt8

* Sun Sep 26 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt1
- initial release

