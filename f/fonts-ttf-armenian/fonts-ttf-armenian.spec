%define _fontsdir %_datadir/fonts/ttf/armenian

Name: fonts-ttf-armenian
Version: 1.1
Release: alt7

Summary: Free Armenian TrueType fonts
Summary (ru_RU.UTF-8): Армянские TrueType шрифты
License: Distributable
Group: System/Fonts/True type
Url: http://www.freenet.am/armnls/

Source: fonts-ttf-armenian-%version.tar.bz2

BuildArch: noarch
PreReq: fontconfig >= 2.4.2
Obsoletes: armenian-fonts-ttf
Provides: armenian-fonts-ttf = %version

BuildRequires: mkfontscale

%description
This Package provides free Armenian TrueType fonts.

%description -l ru_RU.UTF-8
В пакете находятся армянские TrueType шрифты.

%prep
%setup -q -n fonts-ttf-armenian-%version

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-armenian:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
%_sysconfdir/X11/fontpath.d/*
%_fontsdir

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt7
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt6
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt5
- link to encodings.dir fixed

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt4
- %postun script fix

* Mon Sep 01 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt3
- Changed dir
- Cleanups

* Tue Jan 21 2003 Rider <rider@altlinux.ru> 1.1-alt2
- build requires fix (freetype)

* Wed Nov 27 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt1
- ALTLinux build
