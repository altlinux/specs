%define fname  cyr_rfx
%define cname  cp1251

%define origname windows-1251
%define oversion 1.1

%define __bitmapdir %_bitmapfontsdir/%fname-%cname

Name: fonts-bitmap-cyr_rfx-cp1251
Version: 1.1a
Release: alt6

Summary: Cyrillic bitmap fonts for the X Window System in microsoft-cp1251 encoding

License: distributable
Group: System/Fonts/X11 bitmap
Url: http://www.inp.nsk.su/~bolkhov/files/fonts/cyr-rfx/00index.en.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.inp.nsk.su/~bolkhov/files/fonts/cyr-rfx/srctgz/cyr-rfx-%origname-%oversion.bdfs.tar.bz2
Source1: Makefile.fonts
Source2: fonts.dir.75dpi
Source3: fonts.dir.misc
Source4: fonts.alias.misc.1251
Source5: fonts.alias.75dpi

BuildArch: noarch

BuildRequires: unzip mkfontdir bdftopcf xorg-font-utils rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

Provides: XFree86-%fname-fonts-%cname
Obsoletes: XFree86-%fname-fonts-%cname
Obsoletes: cyr_rfx-windows-1251

%description
Collection of cyrillic raster fonts for X Window System by D. Bolkhovityanov.

%prep
%setup -q -n %origname
for i in misc 75dpi ; do
	cd $i
	sed -i 's/-Adobe/-rfx/g' *.bdf
	sed -i 's/\"Adobe/\"rfx/g' *.bdf
	sed -i 's/windows/microsoft/g' *.bdf
	sed -i 's/-1251/-cp1251/g' *.bdf
	cd -
done
cp %SOURCE1 ./Makefile
cp %SOURCE4 ./misc/fonts.alias
cp %SOURCE5 ./75dpi/fonts.alias

%build
make

%install
mkdir -p %buildroot%__bitmapdir
make FONTDIR=%buildroot%__bitmapdir install
# due bdf in orig dir, make only pcf here
for n in 75dpi misc; do
	mkfontdir %buildroot%__bitmapdir/$n
done

mkdir -p %buildroot%_fontpathdir/
ln -s ../../..%__bitmapdir/misc \
	%buildroot%_fontpathdir/bitmap-%fname-%cname-misc:unscaled:pri=10
ln -s ../../..%__bitmapdir/75dpi \
	%buildroot%_fontpathdir/bitmap-%fname-%cname-75dpi:unscaled:pri=10

%files
%doc doc/*
%_fontpathdir/*
%dir %__bitmapdir/
%__bitmapdir/misc/
%__bitmapdir/75dpi/

%changelog
* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1a-alt6
- dropped %%post/un according to Fonts Policy

* Thu Jun 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.1a-alt5
- added xorg-font-utils to BuildRequires:

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.1a-alt4
- rearranged fonts.alias; added -b&h- and lucidasans cp1251 aliases

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1a-alt3
- rebuild with new fonts policy
- links to %_fontpathdir, remove chkfontpath
- cleanup spec

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1a-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sat May 19 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1a-alt1
- rename package, cleanup spec
- repackage according to new font policy (fix bug #11794)

* Wed Nov 03 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.1-ipl7mdk.1
- Fixed build with new mkfontdir.

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 1.1-ipl7mdk
- remove old requires

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1-ipl6mdk
- fix building in hasher

* Fri Nov 22 2002 AEN <aen@altlinux.ru> 1.1-ipl5mdk
- fonts.alias.misc restored

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-ipl4mdk
- rebuild

* Tue Apr 16 2002 AEN <aen@logic.ru> 1.1-ipl3mdk
- "unscaled" added to font path

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
