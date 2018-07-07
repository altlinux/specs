%def_with xfs
%define fname  cyr_rfx
%define cname  iso8859-5
%define origname iso8859-5
%define _fontsdir %_datadir/fonts/bitmap

Name: fonts-bitmap-%fname-%cname
Version: 1.1
Release: alt6
License: distributable
URL: http://www.inp.nsk.su/~bolkhov/files/fonts/cyr-rfx/00index.ru.html
Group: System/Fonts/X11 bitmap
Summary: Cyrillic bitmap fonts for the X Window System in iso859-5 encoding
Source: cyr-rfx-%origname-%version.bdfs.tar.bz2
Source1: Makefile.fonts

BuildArch: noarch
PreReq: fontconfig >= 2.4.2

Obsoletes: cyr_rfx-iso8859-5 XFree86-%fname-fonts-%cname
Requires: fonts-bitmap-%fname-%cname-misc = %EVR
Requires: fonts-bitmap-%fname-%cname-75dpi = %EVR

# Automatically added by buildreq on Wed Oct 01 2003
BuildRequires: xorg-x11-font-utils

%description
Collection of cyrillic raster fonts for X Window System by D. Bolkhovityanov.

%package -n fonts-bitmap-%fname-%cname-misc
Group: System/Fonts/X11 bitmap
Summary: Cyrillic bitmap fonts in iso859-5 encoding - misc part
Conflicts: fonts-bitmap-%fname-%cname < 1.1-alt5

%description -n fonts-bitmap-%fname-%cname-misc
Collection of cyrillic raster fonts for X Window System  in iso859-5 encoding
by D. Bolkhovityanov, misc part.

%package -n fonts-bitmap-%fname-%cname-75dpi
Group: System/Fonts/X11 bitmap
Summary: Cyrillic bitmap fonts in iso859-5 encoding - 75dpi part
Conflicts: fonts-bitmap-%fname-%cname < 1.1-alt5

%description -n fonts-bitmap-%fname-%cname-75dpi
Collection of cyrillic raster fonts for X Window System  in iso859-5 encoding
by D. Bolkhovityanov, 75dpi part.

%prep
%setup -q -n  %origname
cd 75dpi
sed -i 's/-Adobe/-rfx/g' *.bdf
sed -i 's/\"Adobe/\"rfx/g' *.bdf
sed -i 's/-b\&h-lucida-/-rfx-serene-/g' fonts.alias
sed -i 's/-b\&h-lucidatypewriter-/-rfx-serenetypewriter-/g' fonts.alias
echo 'variable     -*-helvetica-bold-r-normal-*-*-120-*-*-*-*-iso8859-5' >> fonts.alias
cd -
cd misc
sed -i 's/-Adobe/-rfx/g' *.bdf
sed -i 's/\"Adobe/\"rfx/g' *.bdf
grep -v helvetica-bold-r-normal fonts.alias > fonts.alias.0
mv fonts.alias.0 fonts.alias
cd -
cp %SOURCE1 ./Makefile

%build
make

%install
mkdir -p %buildroot%_fontsdir/%fname-%cname
make FONTDIR=%buildroot%_fontsdir/%fname-%cname install

%if_with xfs
mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir/%fname-%cname/misc \
	%buildroot%_sysconfdir/X11/fontpath.d/bitmap-%fname-%cname-misc:unscaled:pri=10
ln -s ../../..%_fontsdir/%fname-%cname/75dpi \
	%buildroot%_sysconfdir/X11/fontpath.d/bitmap-%fname-%cname-75dpi:unscaled:pri=10
%endif

%files
%doc doc/*

%files -n fonts-bitmap-%fname-%cname-misc
%if_with xfs
%_sysconfdir/X11/fontpath.d/*misc*
%endif
%dir %_fontsdir/%fname-%cname
%_fontsdir/%fname-%cname/misc

%files -n fonts-bitmap-%fname-%cname-75dpi
%if_with xfs
%_sysconfdir/X11/fontpath.d/*75dpi*
%endif
%dir %_fontsdir/%fname-%cname
%_fontsdir/%fname-%cname/75dpi

%changelog
* Sat Jul 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt6
- restored X fontpath.d support

* Tue Jul 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5
- split on misc and 75dpi subpackages
  to avoid fonconfig conflict for times and helvetica

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4
- dropped %%post/un according to Fonts Policy

* Mon May 30 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3
- fixed font aliases; added URL; cleaned up spec.

* Mon Sep 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt2
- fixed %%post
- added update fonconfig cache in %%postun

* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Wed Nov 03 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.1-ipl4mdk.1
- Fixed build with new mkfontdir.

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 1.1-ipl4mdk
- remove old requires

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1-ipl3mdk
- fix building in hasher

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-ipl2mdk
- rebuild

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
