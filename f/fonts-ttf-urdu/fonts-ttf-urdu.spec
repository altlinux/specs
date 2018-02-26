%define _fontsdir %_datadir/fonts/ttf/urdu

Name: fonts-ttf-urdu
Version: 1.0
Release: alt6

Summary: Free Urdu TrueType font
Summary (ru_RU.UTF-8): Урду TrueType шрифт
License: GPL
Group: System/Fonts/True type
Url: http://www.yudit.org/download/fonts

Source: nastaliq.tar.bz2

PreReq: fontconfig >= 2.4.2
Obsoletes: urdu-fonts-ttf
Provides: urdu-fonts-ttf = %version

BuildArch: noarch
BuildRequires: mkfontscale

%description
This Package provides a free Urdu nastaliq style TrueType font.

%description -l ru_RU.UTF-8
В этом пакете находится TrueType шрифт Урду в стиле nastaliq.

%prep
%setup -q -n nastaliq

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-urdu:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
%doc nastaliq.txt
%_sysconfdir/X11/fontpath.d/*
%_fontsdir

%changelog
* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt6
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt5
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt4
- link to encodings.dir fixed

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- %postun script fix

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- Changed dir
- Cleanups

* Fri Nov 29 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
