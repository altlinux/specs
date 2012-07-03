%define fname oldstandard

Name: fonts-ttf-%fname
Version: 2.2
Release: alt1

Summary: TrueType version of Old Standard fonts

License: SIL OFL
Group: System/Fonts/True type
Url: http://www.thessalonica.org.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.thessalonica.org.ru/downloads/%fname-%version.ttf.zip

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
The Old Standard font family is an attempt to revive a specific type of
modern (classicistic) antiqua, very commonly used in various editions
printed in the late 19th and early 20th century, but almost completely
abandoned later.
Designed by Alexey Krukov.

%prep
%setup -c %name

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc OFL*.txt

%changelog
* Thu Jun 02 2011 Michael Shigorin <mike@altlinux.org> 2.2-alt1
- NMU: 2.2 (30.04.2011)
- use original zip file as a source archive

* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version 2.0 (with rpmrb script)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sun May 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
