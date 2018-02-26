%define fname gost

Name: fonts-ttf-%fname
Version: 7.2
Release: alt3

Summary: GOST TrueType fonts
Summary (ru_RU.KOI8-R): Шрифты GOST TrueType

License: restricted
Group: System/Fonts/True type
Url: http://www.kompas.kolomna.ru/main/download.htm

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2
Source2: %name-README

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

Provides: ascon-fonts-ttf
Provides: %fname-fonts-ttf
Obsoletes: %fname-fonts-ttf

%description
Standart GOST font. GOST 2.304-81
Pay attention to copyright issues before
any commercial use this fonts.
Copyright (c) 1996-2005. ASCON. All Rights Reserved.

%description -l ru_RU.KOI8-R
Шрифты GOST сделаны в соответствии с ГОСТ 2.304-81.
В шрифте имеется русская, английская, цифровая части и знаки препинания.
Кернинг (более 488 кернинговых пар).
Авторские права на содержащиеся здесь шрифты принадлежат ЗАО "АСКОН" (c) 1996-2005
 
%prep
%setup
cp %SOURCE2 README.koi8-r.txt

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts
		
%files -f %fname.files
%doc README.koi8-r.txt

%changelog
* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 7.2-alt3
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 7.2-alt2
- rewrote spec with rpm-build-fonts

* Wed May 18 2005 Vitaly Lipatov <lav@altlinux.ru> 7.2-alt1
- updated version
- add SYMBOL_A, SYMBOL_B fonts (for ASCON products)

* Sat Jan 15 2005 Vitaly Lipatov <lav@altlinux.ru> 1.6553-alt2
- rebuild with ttmkfdir
- spec fixes
- removed link to encodings.dir

* Tue Oct 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.6553-alt1
- first ALTLinux build
