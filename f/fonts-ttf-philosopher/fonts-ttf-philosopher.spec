%define fname philosopher

Name: fonts-ttf-%fname
Version: 2.000
Release: alt1

Summary: TrueType version of Philosopher font

License: OFL
Group: System/Fonts/True type
Url: https://lemonad.livejournal.com/37348.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.3

%description
Philosopher font.

%prep
%setup

%install
%ttf_fonts_install %fname

%files -f %fname.files

%changelog
* Fri Feb 11 2022 Vitaly Lipatov <lav@altlinux.ru> 2.000-alt1
- initial build for ALT Sisyphus
