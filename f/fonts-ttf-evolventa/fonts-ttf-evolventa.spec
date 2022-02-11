%define fname evolventa

Name: fonts-ttf-%fname
Version: 1.0
Release: alt1

Summary: TrueType version of geometric sans-serif font with Cyrillic support based on URW Gothic L

License: GPLv2 
Group: System/Fonts/True type
Url: https://evolventa.github.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/evolventa/evolventa/releases/download/%version/evolventa-%version.7z
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.3

%description
An open source geometric sans-serif font with Cyrillic support based on URW Gothic L.

%prep
%setup
mv ttf/*.ttf .

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc doc/*.txt

%changelog
* Fri Feb 11 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
