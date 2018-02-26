%define fname church

Name: fonts-type1-%fname
Version: 20050115
Release: alt5

Summary: Church Slavonic Type1 fonts
Summary (ru_RU.KOI8-R): Церковно-славянские шрифты Type1

License: see LICENSE file
Group: System/Fonts/Type1
Url: http://irmologion.ru/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name.tar.bz2

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

Provides: %fname-fonts
Obsoletes: %fname-fonts

%description
This Package provides a Church Slavonic Type1 fonts
from Irmologion project.

%description -l ru_RU.KOI8-R
В этом пакете находятся церковно-славянские
шрифты Type1 проекта Ирмологион.

%prep
%setup -q -n %name

%install
%type1_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc AUTHORS ChangeLog README* LICENSE

%changelog
* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt5
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt4
- add obsoletes/provides (thanks to Dmitry Levin)

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt3
- rewrote spec for rpm-build-fonts

* Thu Mar 24 2005 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt2
- remove special version of fonts for IE and Finale

* Sat Jan 15 2005 Vitaly Lipatov <lav@altlinux.ru> 20050115-alt1
- new font StaroUspenskaya
- fix spec

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 20040618-alt1
- correct postun section (bug #3672). Thanks to Michael Shigorin
- new fonts Indycton, Triodion, Vertograd, Zlatoust

* Thu Feb 12 2004 Vitaly Lipatov <lav@altlinux.ru> 20030330-alt2
- rebuild with new font packaging rules

* Fri Apr 04 2003 Vitaly Lipatov <lav@altlinux.ru> 20030330-alt1.1
- add IzhitsaCS font

* Thu Apr 03 2003 Vitaly Lipatov <lav@altlinux.ru> 20030330-alt1
- first ALTLinux build

