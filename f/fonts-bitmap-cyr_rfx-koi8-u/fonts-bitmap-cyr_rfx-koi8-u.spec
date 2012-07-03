%define fname  cyr_rfx
%define cname  koi8-u
%define origname koi8-ub
%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-%fname-%cname
Version: 1.1
Release: alt13
License: distributable
Group: System/Fonts/X11 bitmap
URL: http://www.inp.nsk.su/~bolkhov/files/fonts/cyr-rfx/00index.ru.html
Summary: Cyrillic bitmap fonts for the X Window System in koi8-ub encoding

Source: cyr-rfx-%origname-%version.bdfs.tar.bz2
Source1: Makefile.fonts-koi8-u
Source3: fonts.alias.75dpi-koi8-u
Source4: fonts.alias.misc-koi8-u
BuildArch: noarch

Obsoletes: cyr_rfx-koi8-ub XFree86-cyr_rfx-fonts-koi8-ub XFree86-%fname-fonts-%cname
Provides: XFree86-cyr_rfx-fonts-koi8-ub XFree86-%fname-fonts-%cname = %version
PreReq: fontconfig >= 2.4.2

# Automatically added by buildreq on Wed Oct 01 2003
BuildRequires: xorg-x11-font-utils

%description
Collection of cyrillic raster fonts for X Window System by D. Bolkhovityanov.

%prep
%setup -q -n  %origname
cd 75dpi
sed -i 's/-Adobe/-rfx/g' *.bdf
sed -i 's/\"Adobe/\"rfx/g' *.bdf
sed -i 's/koi8-ub/koi8-u/g' *.bdf
echo 'variable     -*-helvetica-bold-r-normal-*-*-120-*-*-*-*-koi8-u' >> fonts.alias
cd -
cd misc
sed -i 's/-Adobe/-rfx/g' *.bdf
sed -i 's/\"Adobe/\"rfx/g' *.bdf
sed -i 's/koi8-ub/koi8-u/g' *.bdf
grep -v helvetica-bold-r-normal fonts.alias > fonts.alias.0
mv fonts.alias.0 fonts.alias
cd -
cp %SOURCE1 ./Makefile
cp %SOURCE3 75dpi/fonts.alias
subst 's,koi8-ub,koi8-u,g' misc/fonts.alias

%build
make

%install
mkdir -p %buildroot%_fontsdir/%fname-%cname
make FONTDIR=%buildroot%_fontsdir/%fname-%cname install
for n in 75dpi misc; do mkfontdir %buildroot%_fontsdir/%fname-%cname/$n; done

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir/%fname-%cname/misc \
	%buildroot%_sysconfdir/X11/fontpath.d/bitmap-%fname-%cname-misc:unscaled:pri=10
ln -s ../../..%_fontsdir/%fname-%cname/75dpi \
	%buildroot%_sysconfdir/X11/fontpath.d/bitmap-%fname-%cname-75dpi:unscaled:pri=10

%files
%doc doc/*
%_sysconfdir/X11/fontpath.d/*
%dir %_fontsdir/%fname-%cname
%_fontsdir/%fname-%cname/misc
%_fontsdir/%fname-%cname/75dpi

%changelog
* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt13
- dropped %%post/un according to Fonts Policy

* Mon May 30 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt12
- added URL:, fixed font aliases, cleaned up spec.

* Mon Sep 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt11
- fixed %%post
- added update fonconfig cache in %%postun

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt10
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Wed Nov 03 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.1-alt9.1
- Fixed build with new mkfontdir.

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 1.1-alt9
- removed old requires

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt8
- fix building in hasher

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt7
- rebuild

* Tue Jun 11 2002 AEN <aen@altlinux.ru> 1.1-alt6
- %post fixed

* Wed Apr 17 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt5
- fixed sources names

* Tue Apr 16 2002 AEN <aen@logic.ru> 1.1-alt4
- back to alt2

* Tue Apr 16 2002 AEN <aen@logic.ru> 1.1-alt3
- CHARSET_ENCODING changed to "u"

* Tue Apr 16 2002 AEN <aen@logic.ru> 1.1-alt2
- "unscaled" added to font path

* Mon Nov 19 2001 AEN <aen@logic.ru> 1.1-alt1
- new name
- s/koi8-ub/koi8-u/

* Sun Feb 18 2001 AEN <aen@logic.ru>
- source global i18n in %post

* Mon Nov 28 2000 AEN <aen@logic.ru>
- 1.1
- build for RE
- name changed

* Mon Dec 27 1999 AEN <aen@logic.ru>
- new aliases

* Tue Dec 21 1999 AEN <aen@logic.ru>
- new version
- build from bdf's

* Fri Dec 10 1999 AEN <aen@logic.ru>
- first spec
