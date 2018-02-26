%define oname Prosto
%define fname prosto

Name: fonts-ttf-%fname
Version: 1.000
Release: alt2

Summary: TrueType font Prosto

License: SIL OFL
Group: System/Fonts/True type
Url: http://lemonad.livejournal.com/134193.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://jovanny.ru/fonts/Prosto.rar
Source: %oname.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
Prosto font with more then 400 glyphs.

%prep
%setup -n %oname

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc OFL.txt

%changelog
* Mon Apr 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt2
- cleanup spec

* Sat Mar 03 2012 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt1
- initial build for ALT Linux Sisyphus
