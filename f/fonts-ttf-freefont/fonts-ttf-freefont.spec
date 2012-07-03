Name: fonts-ttf-freefont
Version: 20100919
Release: alt1

Summary: Free unicode True Type fonts based on URW/Valek fonts
Summary (ru_RU.UTF-8): Свободные True Type шрифты основанные на шрифтах URW/Valek
License: GPL
Group: System/Fonts/True type
Url: http://savannah.nongnu.org/projects/freefont

Obsoletes: freefont-ttf freefont-fonts-ttf braille-fonts-ttf
Provides: freefont-ttf freefont-fonts-ttf = %version

Requires: fonts-ttf-gnu-freefont-mono fonts-ttf-gnu-freefont-sans fonts-ttf-gnu-freefont-serif
BuildRequires: fonts-ttf-gnu-freefont-mono fonts-ttf-gnu-freefont-sans fonts-ttf-gnu-freefont-serif

BuildArch: noarch

%description
A set of  Free unicode True Type fonts based on URW/Valek fonts

%description -l ru_RU.UTF-8
Свободные Unicode шрифты в формате True Type, основанные на шрифтах URW с дополнениями Валентина Филиппова.

%prep

%install
mkdir -p %buildroot%_datadir/fonts/ttf/freefont
for i in %_datadir/fonts/ttf/gnu-free/*.ttf; do
    ln -s ../gnu-free/`basename $i` %buildroot%_datadir/fonts/ttf/freefont/`basename $i`
done

%files
%_datadir/fonts/ttf/freefont

%changelog
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 20100919-alt1
- fonts moved to fonts-ttf-gnu-freefont-* packages;
- fonts-ttf-freefont is turned into compatibility package.

* Mon Sep 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.060126-alt2
- fixed Obsoletes/Requires

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.060126-alt1
- new version
- rebuild with fonts policy
- used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Mon Jul 11 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.050704-alt8
- link to encodings.dir removed, no longer requires freetype
- update from the 7th of April 2005

* Thu Dec 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.030422-alt7
- link to encodings.dir fixed

* Tue Jul 06 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.030422-alt6
- spec fix (buf #4582)

* Sat May 15 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.030422-alt5
- macros fix (bug #4141)

* Wed Feb 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.030422-alt4
- %postun script fix

* Thu Aug 28 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.030422-alt3
- Renamed to freefont-fonts-ttf for uniformity
- Obsoletes braille-fonts-ttf (Braille font is now part of freefont)

* Wed Aug 27 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.021011-alt2
- New version
- Changed dir
- Cleanups
- Translation
- Wrong URL fixed

* Wed Oct 16 2002 AEN <aen@altlinux.ru> 0.021011-alt1
- new package in Sisyphus
