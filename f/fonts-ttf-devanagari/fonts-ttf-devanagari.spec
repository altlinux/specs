%define _fontsdir %_datadir/fonts/ttf/devanagari

Name: fonts-ttf-devanagari
Version: 0.99
Release: alt6

Summary: Free Devanagari TrueType font
Summary (ru_RU.UTF-8): Деванагари TrueType шрифт
License: GPL
Group: System/Fonts/True type
Url: http://savannah.nongnu.org/download/smc/free-mal-fonts.pkg/1.0
Source: raghu.tar.bz2

BuildArch: noarch

PreReq: fontconfig >= 2.4.2
Obsoletes: devanagari-fonts-ttf
Provides: devanagari-fonts-ttf = %version

BuildRequires: mkfontscale

%description
This Package provides a free TrueType font suitable
for displaying Hindi, Marathi and non-vedic Sanscrit.

%description -l ru_RU.UTF-8
В этом пакете находятся TrueType шрифт пригодный
для отображения текстов на хинди, маратхи и санскрите.

%prep
%setup -q -n raghu

%install
mkdir -p %buildroot%_fontsdir
install -m644 *.ttf %buildroot%_fontsdir

mkfontscale %buildroot%_fontsdir
ln -s fonts.scale %buildroot%_fontsdir/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_fontsdir %buildroot%_sysconfdir/X11/fontpath.d/ttf-devanagari:pri=50

%post
%_bindir/fc-cache %_fontsdir ||:

%files
%doc *txt
%_sysconfdir/X11/fontpath.d/ttf-devanagari:pri=50
%_fontsdir

%changelog
* Thu Aug 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt6
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.99-alt5
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.99-alt4
- link to encodings.dir fixed

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.99-alt3
- %postun script fix

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.99-alt2
- Changed dir
- Cleanups

* Fri Nov 29 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.99-alt1
- ALTLinux build
