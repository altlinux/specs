# this is not a relocatable package.
Name: einstein
Version: 2.0
Release: alt7
License: GPL
Group: Games/Puzzles
URL: http://www.babichev.info/ru/projects/einstein/
Source: http://www.babichev.info/files/einstein/%name-%version-src.tar.gz
Source1: %name-1.0-html-pages.tgz
Source2: %name-wrapper
Source3: icon.bmp
Source4: einstein.desktop
Source5: einstein.png
# how to get Source1
# wget -r -l1 -np -nH http://www.babichev.info/en/projects/einstein/index.html --cut-dirs=2
# wget http://www.babichev.info/ru/projects/einstein/index.html -O einstein/index.ru.html
# Ugh-ogh, upstream is dead (was moved here and vanished):
# http://games.flowix.com

#Patch: einstein-optimize.patch
Patch1: einstein-math_h.patch
Patch2: einstein-Makefile.patch
Patch3: einstein-formatter_cpp.patch
Patch4: einstein-2.0-deb-icon_change.patch
Patch5: einstein-2.0-deb-font_change.patch
Patch6: einstein-2.0-deb-random_init.patch
Patch7: einstein-2.0-alt-rules_clarification.patch
Patch8: einstein-2.0-alt-fix_mkres_link.patch
Patch9: einstein-2.0-alt-translation_fix.patch
Patch10: einstein-2.0-gcc43.patch
Packager: Fr. Br. George <george@altlinux.ru>
Summary: Open source remake of old DOS game Sherlock which was inspired by Albert Einstein's puzzle.

Summary(ru_RU.KOI8-R): Логическая головоломка, написанная по мотивам старой игры Sherlock, которая в свою очередь была написана по мотивам задачи Эйнштейна

# Automatically added by buildreq on Tue Apr 05 2011
# optimized out: libSDL-devel libstdc++-devel
BuildRequires: fonts-ttf-dejavu gcc-c++ libSDL_mixer-devel libSDL_ttf-devel libfreetype-devel makedepend zlib-devel

%description
Einstein puzzle is cross-platform open source remake of old DOS game Sherlock
which was inspired by Albert Einstein's puzzle. Einstein said that only those
with an intelligence quotient of 97 percentile and higher should be able to
solve it.

The game goal is to open all cards in square of 6x6 cards.
Every row of square contains cards of one type only. For example, first row
contains arabic digits, second - letters, third - rome digits, fouths - dices,
fifth - geometric figures, sixs - mathematic symbols.

%description -l ru_RU.KOI8-R
Einstein - это логическая головоломка, написанная по мотивам старой игры
Sherlock, которая в свою очередь была написана по мотивам задачи Эйнштейна.
Эйнштейн утверждал, что для её решения необходимо обладать IQ не менее 97
процентов.

Правила игры очень простые: надо открыть все фишки в квадрате 6x6 фишек.
В каждой строке квадрата находятся фишки одного типа. Например, в первой строке
квадрата находятся арабские цифры, во второй - латинские буквы, в третьей -
римские цифры, в четвертой - игральные кости, в пятой - геометрические фигуры,
в шестой - математические символы. 

%prep
%setup
%setup -q -T -D -a 1
install %SOURCE3 res/
mv %name doc
#patch
%patch1
%patch2
%patch3 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

cp /usr/share/fonts/ttf/dejavu/DejaVuSans.ttf res/

%build
%make depend
%make_build -C mkres
pushd res && ../mkres/mkres --source resources.descr --output ../einstein.res && popd
%make_build PREFIX=/usr

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot/%_datadir/%name/res
%makeinstall PREFIX=%buildroot%_usr
mv %buildroot%_bindir/%name %buildroot%_bindir/%name.bin
install %SOURCE2 %buildroot%_bindir/%name
chmod 755 %buildroot%_bindir/%name
mkdir -p %buildroot/%_defaultdocdir/%name-%version
#install doc/* %buildroot/%_defaultdocdir/%name-%version
install -Dm 0644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %SOURCE5 %buildroot%_niconsdir/%name.png

%files 
%_bindir/*
%doc doc/*
%_datadir/%name/
%_desktopdir/*
%_niconsdir/*

%changelog
* Tue Apr 05 2011 Fr. Br. George <george@altlinux.ru> 2.0-alt7
- Forbidden requires eliminated

* Tue Sep 21 2010 Fr. Br. George <george@altlinux.ru> 2.0-alt6
- Desktop and icon fix (closes #22534)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for einstein
  * postclean-05-filetriggers for spec file

* Tue Oct 28 2008 Fr. Br. George <george@altlinux.ru> 2.0-alt5
- GCC4.3 build fix

* Sun Jul 29 2007 Fr. Br. George <george@altlinux.ru> 2.0-alt4
- A bunch of patches by Alexey Morozov. Many thanks!
- Synchronizing descriptions :)
- Upstream is dead now, be careful

* Sun Jul 15 2007 Alexey Morozov <morozov@altlinux.org> 2.0-alt3.2
- NMU: added einstein-2.0-alt-translation_fix.patch (#9) to fix
  a Russian translation typo

* Fri Jul 06 2007 Alexey Morozov <morozov@altlinux.org> 2.0-alt3.1
- NMU: merged Debian/Ubuntu changes from einstein_2.0.dfsg.2-3:
  + added program icon (einstein-2.0-deb-icon_change.patch (#4) and icon.bmp(S#3))
  + switched to DejaVuSans.ttf font (einstein-2.0-deb-font_change.patch (#5)) to
    avoid possible copyright problems with fonts supplied in game resources
  + a proper random generator initialization (einstein-2.0-deb-random_init.patch (#6))
  + rules clarification (einstein-2.0-alt-rules_clarification.patch (#7))
  + desktop and icon file (S#4 & S#5)
- switched to re-generated resources file rather the pre-generated one, added
  resource source files, including three questionable (copyrighted) fonts
  (not used now).
- moved all patches to files/ folder
- setup macro invocation cleaned up
- added einstein-2.0-alt-fix_mkres_link.patch (#8) to properly link mkres

* Sun Feb 25 2007 Fr. Br. George <george@altlinux.ru> 2.0-alt3
- GEAR adaptation
- cast from void* to int fixed

* Wed Mar 15 2006 Fr. Br. George <george@altlinux.ru> 2.0-alt2
- ld --as-needed by default affects old makefile

* Mon Dec 26 2005 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- New version

* Fri Jan 14 2005 Fr. Br. George <george@altlinux.ru> 1.0-alt3
- Some strange-missed includes in source code added

* Mon Jan 10 2005 Fr. Br. George <george@altlinux.ru> 1.0-alt2
- ALT packaging policy tuned

* Fri Jan 07 2005 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial ALT built

