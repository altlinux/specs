%define oname Cuprum
%define fname cuprum

Name: fonts-ttf-%fname
Version: 1.001
Release: alt1

Summary: TrueType font Cuprum

License: SIL OFL
Group: System/Fonts/True type
Url: http://lemonad.livejournal.com/140903.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://jovanny.ru/fonts/Cuprum_typefamily.zip
Source: http://jovanny.ru/fonts/%oname.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
Cuprum font with 4 faces.

%prep
%setup -n %oname

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc OFL.txt

%changelog
* Mon Apr 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.001-alt1
- initial build for ALT Linux Sisyphus
