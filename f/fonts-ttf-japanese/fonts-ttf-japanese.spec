%define fname japanese
%define _fontsdir %_datadir/fonts/ttf/%fname

Name: fonts-ttf-japanese
Version: 1.0
Release: alt10

Summary: Free Japanese TrueType fonts
Summary (ru_RU.UTF-8): Японские TrueType шрифты
License: Distributable
Group: System/Fonts/True type
Url: http://www.on.cs.keio.ac.jp/~yasu/linux/fonts/

Source: xtt-fonts_0.19990222-3.tar.bz2

Requires: fonts-ttf-sazanami-gothic
Requires: fonts-ttf-sazanami-mincho

PreReq: fontconfig >= 2.4.2
Obsoletes: japanese-fonts-ttf
Provides: japanese-fonts-ttf = %version

BuildArch: noarch
BuildRequires: rpm-build-fonts

%description
This Package provides free Japanese TrueType fonts.

%description -l ru_RU.UTF-8
Пакет предоставляет японские TrueType шрифты. 

%prep
%setup -n xtt-fonts-0.19990222

%install
#%%ttf_fonts_install %fname
mkdir -p %buildroot

%files
#%_sysconfdir/X11/fontpath.d/*
#%_fontsdir

%changelog
* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt10
- dropped original Wadalab font kit as Sazanami fonts succeed it.
- made a virtual compat package

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt9
- replaced Kochi fonts with Sazanami fonts

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt8
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt7
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt6
- link to encodings.dir fixed

* Sat Jun 26 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt5
- %postun script fix

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt4
- %postun script fix

* Wed Sep 03 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- CID support fixed

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- Changed dir
- Cleanups

* Wed May 07 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt1.1
- added CID support (japanese support for ghostscript )

* Wed Nov 27 2002 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- ALTLinux build
