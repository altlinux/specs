%define _fontsdir %_datadir/fonts/ttf/kannada

Name: fonts-ttf-kannada
Version: 1.0
Release: alt6

Summary: Free Kannada TrueType font
Summary (ru_RU.UTF-8): TrueType шрифт для языка каннада
License: GPL
Group: System/Fonts/True type
Url: http://brahmi.sourceforge.net

Source: sampige.tar.bz2

PreReq: fontconfig >= 2.4.2
Obsoletes: kannada-fonts-ttf
Provides: kannada-fonts-ttf = %version

BuildArch: noarch
BuildRequires: mkfontscale

%description
This Package provides a free Kannada TrueType font.

%description -l ru_RU.UTF-8
В этом пакете находится TrueType шрифт для языка каннада (Индия).

%prep
%setup -q -n sampige

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-kannada:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
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

* Tue Dec 03 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
