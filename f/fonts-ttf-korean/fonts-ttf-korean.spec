Name: fonts-ttf-korean
Version: 2.1
Release: alt9

Summary: Baekmuk korean fonts
Summary (ru_RU.UTF-8): Корейские шрифты Baekmuk
License: GPL
Group: System/Fonts/True type
Url: ftp://ftp.mizi.com/pub/baekmuk

Obsoletes: korean-fonts-ttf
Provides: korean-fonts-ttf = %version

Requires: fonts-ttf-baekmuk-batang
Requires: fonts-ttf-baekmuk-dotum
Requires: fonts-ttf-baekmuk-gulim
Requires: fonts-ttf-baekmuk-hline

BuildArch: noarch

%description
Baekmuk Korean TrueType Fonts.

%description -l ru_RU.UTF-8
Корейские TrueType шрифты Baekmuk.

%prep

%install
mkdir -p %buildroot%_datadir

%files

%changelog
* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.1-alt9
- compatibility package (fonts moved to fonts-ttf-baekmuk-*)

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.1-alt8
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt7
- link to encodings.dir removed, no longer requires freetype

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt6
- link to encodings.dir fixed

* Sat Jun 26 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt5
- %postun script fix

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt4
- %postun script fix

* Wed Sep 03 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt3
- CID support fixed

* Sun Aug 24 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt2
- Changed dir
- Cleanups

* Wed May 07 2003 Stanislav Ievlev <inger@altlinux.ru> 2.1-alt1.1
- added CID support ( korean support for ghostscript )

* Wed Nov 27 2002 Vyacheslav Dikonov <slava@altlinux.ru> 2.1-alt1
- ALTLinux build
