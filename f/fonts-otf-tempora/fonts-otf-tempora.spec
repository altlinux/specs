%define fname tempora

Name: fonts-otf-%fname
Version: 0.2
Release: alt2

Summary: OpenType fonts of Tempora LGC Unicode font

License: see README
# FIXME: Open Type needs
Group: System/Fonts/True type
Url: http://www.thessalonica.org.ru/ru/fonts.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.thessalonica.org.ru/downloads/tempora-lgc.otf.zip

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
Tempora LGC Unicode is a font family, designed to provide a free  typeface
suitable for word processing in languages which use 3 European alphabets:
Latin, Greek and Cyrillic. It may be especially useful for philologists
(mainly slavists and classicists), since it supports historical Cyrillic
letters available in the Unicode standard (including letters used in
Russian  pre-1918 orthography) as well as all accented combinations and
additional characters needed for fully accented Greek (both classical and
modern). Tempora LGC Unicode is a "smart" font, intended to demonstrate
nicities of the OpenType technologie, applicable to European scripts.

%prep
unzip -o %SOURCE0

%install
%otf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc COPYING README

%changelog
* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- rewrote spec with rpm-build-fonts

* Tue Nov 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt0.1
- initial build for ALT Linux Sisyphus
