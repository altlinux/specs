%define _fontsdir %_datadir/fonts/ttf/bengali

Name: fonts-ttf-bengali
Version: 1.0
Release: alt6

Summary: Free Bengali TrueType font
Summary (ru_RU.UTF-8): Бенгальский TrueType шрифт
License: GPL
Group: System/Fonts/True type
Url: http://www.geocities.com/mitra_anirban/hobbies
Source: ani.tar.bz2

BuildArch: noarch
PreReq: fontconfig >= 2.4.2
Obsoletes: bengali-fonts-ttf
Provides: bengali-fonts-ttf = %version

BuildRequires: mkfontscale

%description
This Package provides a free Bengali TrueType font.

%description -l ru_RU.UTF-8
В этом пакете находится бенгальский TrueType шрифт.

%prep
%setup -q -n ani

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-bengali:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
%doc ani.txt
%_sysconfdir/X11/fontpath.d/*
%_fontsdir

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt6
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
