%define oname khartiya-ttf
%define fname khartiya

Name: fonts-ttf-%fname
Version: 1.0.1
Release: alt1

Summary: TrueType font Khartiya

License: SIL OFL
Group: System/Fonts/True type
Url: http://code.google.com/p/khartiya/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://khartiya.googlecode.com/files/%oname-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
These fonts are based on Bitstream Charter font which was released by Bitstream
for X Window System. The cyrillic glyphs are added.

%prep
%setup -n %oname-%version

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc *.txt

%changelog
* Tue Sep 18 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus
