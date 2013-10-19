%define fname imperial

Name: fonts-ttf-%fname
Version: 1.0.0
Release: alt1

Summary: TrueType font Imperial

License: SIL OFL 1.1
Group: System/Fonts/True type
Url: http://lemonad.livejournal.com/198540.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://jovanny.ru/fonts/Imperial.zip
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
This font is based on the corporate font for the game The Mandate.
The Mandate is a science fiction roleplaying game which sees the player
as a disgraced space captain who gets one chance at redemption
and is the last desperate hope for the newly crowned Empress to restore peace and secure the future of humanity.

%prep
%setup

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc *.txt

%changelog
* Sat Oct 19 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
