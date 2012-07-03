%define fname znamen

Name: fonts-ttf-%fname
Version: 20051015
Release: alt2

Summary: TrueType fonts of Znamen Fund 
Summary (ru_RU.KOI8-R): Шрифты фонда знаменных песнопений в формате TrueType

License: see LICENSE file
Group: System/Fonts/True type
Url: http://znamen.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/%name.tar.bz2

Provides: %fname-fonts-ttf
Obsoletes: %fname-fonts-ttf

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
This Package provides a TrueType fonts of Znamen Fund

%description -l ru_RU.KOI8-R
В этом пакете находятся шрифты фонда знаменных песнопений

%prep
%setup -q -n %name

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc LICENSE MANIFEST

%changelog
* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 20051015-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 20051015-alt1
- rewrote spec with rpm-build-fonts

* Sat Oct 15 2005 Vitaly Lipatov <lav@altlinux.ru> 20051015-alt0.1
- initial build for ALT Linux Sisyphus
