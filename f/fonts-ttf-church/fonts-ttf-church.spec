%define fname church

Name: fonts-ttf-%fname
Version: 20100220
Release: alt1

Summary: Church Slavonic TrueType fonts
Summary (ru_RU.UTF-8): Церковно-славянские шрифты TrueType

License: see LICENSE file
Group: System/Fonts/True type
Url: http://irmologion.ru/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# repacked from http://www.irmologion.ru/fonts.html
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: rpm-build-fonts

Provides: %fname-fonts-ttf
Obsoletes: %fname-fonts-ttf

%description
This Package provides a Church Slavonic TrueType fonts
from Irmologion project:
 - Akathistos
 - Irmologion (obsoletes)
 - Hirmos (update version of Irmologion)
 - Kathisma
 - Zlatoust
 - Triodion
 - StaroUspenskaya
 - Ostrog
 - Oglavie
 - Posad
 - Indycton
 - Vertograd
 - Bukvica

%description -l ru_RU.UTF-8
В этом пакете находятся церковно-славянские
шрифты TrueType проекта Ирмологион.
 - Akathistos (большой кегль для крупноформатных изданий второй половины 19 - начала 20 века)
 - Irmologion (устарел)
 - Hirmos (Ирмос) (развитие Irmologion, гарнитура из изданий Синодальной типографии начала 20 века)
 - Kathisma (заголовочная гарнитура из дореволюционных изданий 18 - 20 вв.)
 - Zlatoust (рисунок букв родственен рукописной вязи 15-16 вв.)
 - Triodion (распространена в синодальной типографии конца 19-начала 20 века)
 - StaroUspenskaya (из Псалтири издания Киево-Печерской лавры предположительно середины 19 в)
 - Ostrog (из изданий второй половины 16 века (типографии городов Вильно и Острога))
 - Oglavie (наиболее распространенная заголовочная гарнитура из дореволюционных изданий)
 - Posad (декоративный, подходящий для оформления заголовков)
 - Indycton (буквицы)
 - Vertograd (буквицы)
 - Bukvica (буквицы из зимней (1642 г.) и летней (1643 г.) частей Пролога)

%prep
%setup

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc AUTHORS README ReadMe.txt LICENSE

%changelog
* Fri Jun 25 2010 Vitaly Lipatov <lav@altlinux.ru> 20100220-alt1
- recode texts to UTF-8, build from git
- add Bukvica, Akathistos fonts

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 20081115-alt1
- cleanup spec, add font list
- add Kathisma, Hirmos, Ostrog, Oglavie fonts
- update Vertograd font

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt4
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt3
- rewrote spec with rpm-build-fonts

* Thu Mar 24 2005 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt2
- remove special version of fonts for IE and Finale

* Sat Jan 15 2005 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt1
- new font StaroUspenskaya
- fix spec
- rebuild with new ttmkfdir

* Fri Dec 17 2004 Vitaly Lipatov <lav@altlinux.ru> 20040618-alt2
- spec fixes from Vyacheslav Dikonov <slava@altlinux.ru>
- link to encodings.dir is removed

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 20040618-alt1
- correct postun section (bug #3673). Thanks to Michael Shigorin
- new fonts Indycton, Triodion, Vertograd, Zlatoust, Orthodox

* Mon Jan 12 2004 Vitaly Lipatov <lav@altlinux.ru> 20030330-alt3
- rebuild with some changes and fonts.dir inside

* Wed Aug 27 2003 Vyacheslav Dikonov <slava@altlinux.ru> 20030330-alt2
- Changed dir
- Cleanups

* Thu Apr 03 2003 Vitaly Lipatov <lav@altlinux.ru> 20030330-alt1
- first ALTLinux build
