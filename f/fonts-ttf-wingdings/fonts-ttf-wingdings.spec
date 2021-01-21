%define fname wingdings

Name: fonts-ttf-%fname
Version: 1.001
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

Requires(pre): fontconfig >= 2.4.2

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
* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.001-alt1
- update to the latest version from wine sources
- replace PreReq with Requires(pre)

* Tue Oct 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt1
- initial build for ALT Linux Sisyphus (ALT bug #29429)
