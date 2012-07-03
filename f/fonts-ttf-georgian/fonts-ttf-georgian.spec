%define _fontsdir %_datadir/fonts/ttf/georgian

Name: fonts-ttf-georgian
Version: 1.0
Release: alt8

Summary: Free Georgian TrueType fonts
Summary (ru_RU.UTF-8): Грузинские TrueType шрифты
License: Distributable
Group: System/Fonts/True type
Url: http://www.main.osgf.ge/eng/dounen.htm
Source: Georgian_Fonts.zip
Packager: Ilya Mashkin <oddity@altlinux.ru>

PreReq: fontconfig >= 2.4.2
Obsoletes: georgian-fonts-ttf
Provides: georgian-fonts-ttf

BuildArch: noarch
BuildRequires: mkfontscale unzip

%description
This Package provides free Georgian TrueType fonts.

%description -l ru_RU.UTF-8
В пакете находятся грузинские TrueType шрифты.

%prep
%setup -q -n KA_FONTS

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-georgian:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
%_sysconfdir/X11/fontpath.d/*
%_fontsdir

%changelog
* Sun Jan 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0-alt8
- fix build

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt7
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt6
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt5
- link to encodings.dir fixed

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt4
- %postun script fix

* Tue Jan 27 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- Build fix

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- Changed dir
- Cleanups

* Fri Nov 29 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
