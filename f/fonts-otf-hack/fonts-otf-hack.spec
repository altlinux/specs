%define fname hack
%define _version 2_010

Name: fonts-otf-%fname
Version: 2.010
Release: alt1

Summary: A typeface designed for source code
License: Modified SIL Open Font License
Group: System/Fonts/True type

Url: http://sourcefoundry.org/hack/
Source0: https://github.com/chrissimpkins/Hack/releases/download/v%version/Hack-v%_version-otf.zip
Source1: https://raw.githubusercontent.com/chrissimpkins/Hack/master/LICENSE.md

BuildArch: noarch
BuildRequires: unzip
BuildPreReq: rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

Summary(ru_RU.UTF-8): Шрифты, предназначенные для исходного кода

%description
Type design features to improve legibility in the harsh conditions
of the screen.
* Minimal stroke contrast
* Large x-height
* Open counters
* Wide apertures
* Sturdy terminals

Functional with a bit of personality
* Oval fill in the zero counter
* Curved tails on select glyphs
* Rounded square alphabetic points
* Round analphabetic points
* Semi-bold punctuation weight
* Angled vertical tails & extenders
* Widely set punctuation

%prep
%setup -c

%install
%otf_fonts_install %fname
cp -a %SOURCE1 .

%files -f %fname.files
%doc LICENSE.md

%changelog
* Mon Aug 31 2015 Michael Shigorin <mike@altlinux.org> 2.010-alt1
- built for ALT Linux

