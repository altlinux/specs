%define fname wingdings

Name: fonts-ttf-%fname
Version: 1.000
Release: alt1

Summary: TrueType font WingDings

License: LGPL
Group: System/Fonts/True type
Url: http://wine.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# copied from the wine source
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: fontforge
BuildRequires: rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
WingDings font from the Wine project.

%prep
%setup

%build
%make

%install
%ttf_fonts_install %fname

%files -f %fname.files

%changelog
* Tue Oct 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt1
- initial build for ALT Linux Sisyphus (ALT bug #29429)
