%define fname  cyr_rfx
%define cname  iso10646-0400
%define origname iso10646-0400
%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-%fname-%cname
Version: 1.1
Release: alt10
License: distributable
Group: System/Fonts/X11 bitmap
Summary: Cyrillic bitmap fonts for the X Window System in unicode encoding
URL: http://www.inp.nsk.su/~bolkhov/files/fonts/cyr-rfx/00index.ru.html
Source: cyr-rfx-%origname-%version.bdfs.tar.bz2
Source1: Makefile.fonts-iso10646
BuildArch: noarch

PreReq: fontconfig >= 2.4.2
Provides: XFree86-%fname-fonts-%cname = %version
Obsoletes: XFree86-%fname-fonts-%cname

# Automatically added by buildreq on Wed Oct 01 2003
BuildRequires: xorg-font-utils

%description
Collection of cyrillic raster fonts for X Window System by D. Bolkhovityanov.

%prep
%setup -q -n  %origname
cd 75dpi
sed -i 's/-Adobe/-rfx/g' *.bdf
sed -i 's/\"Adobe/\"rfx/g' *.bdf
sed -i 's/\"-adobe-/\"-rfx-/g' fonts.alias
sed -i 's/ -b\&h-lucida-/ -rfx-serene-/g' fonts.alias
sed -i 's/ -b\&h-lucidatypewriter-/ -rfx-serenetypewriter-/g' fonts.alias
cd -
cd misc
sed -i 's/-Adobe/-rfx/g' *.bdf
sed -i 's/\"Adobe/\"rfx/g' *.bdf
cd -
cp %SOURCE1 ./Makefile
# no need...
rm -f */fonts.alias

%build
make

%install
mkdir -p %buildroot%_fontsdir/%fname-%cname
make FONTDIR=%buildroot%_fontsdir/%fname-%cname install

mkfontdir %buildroot%_fontsdir/%fname-%cname/misc
mkfontdir %buildroot%_fontsdir/%fname-%cname/75dpi

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir/%fname-%cname/misc \
	%buildroot%_sysconfdir/X11/fontpath.d/bitmap-%fname-%cname-misc:unscaled:pri=20
ln -s ../../..%_fontsdir/%fname-%cname/75dpi \
	%buildroot%_sysconfdir/X11/fontpath.d/bitmap-%fname-%cname-75dpi:unscaled:pri=20

%files
%doc doc/*
%_sysconfdir/X11/fontpath.d/*
%dir %_fontsdir/%fname-%cname
%_fontsdir/%fname-%cname/misc
%_fontsdir/%fname-%cname/75dpi

%changelog
* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt10
- dropped %%post/un according to Fonts Policy

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt9
- fixed bugs in default fonts.alias, just in case

* Mon May 30 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt8
- added URL, cleaned up spec

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt7
- lower priority

* Mon Sep 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt6
- fixed %%post
- added update fonconfig cache in %%postun

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt5
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Wed Nov 03 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.1-alt4.1
- Fixed build with new mkfontdir.

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 1.1-alt4
- remove old requires

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt3
- fix building in hasher

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt2
- rebuild

* Wed Sep 18 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.1-alt1
- first version
- copy spec from cyr_rfx koi8-r package
