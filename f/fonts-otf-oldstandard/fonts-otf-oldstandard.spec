%define fname oldstandard

Name: fonts-otf-%fname
Version: 2.2
Release: alt1

Summary: OpenType version of Old Standard fonts

License: SIL OFL
Group: System/Fonts/True type
Url: http://www.thessalonica.org.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Provides: fonts-otf-oldstandart
Obsoletes: fonts-otf-oldstandart

Source: http://www.thessalonica.org.ru/downloads/%fname-%version.otf.zip

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
%otf_fonts_install %fname

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
- new version 1.0 (with rpmrb script)

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- rewrote spec with rpm-build-fonts

* Thu Dec 14 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.1
- new version 0.9 (with rpmrb script)

* Tue Oct 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt0.1
- new version 0.8
- fix package name, description

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt0.1
- new version (0.6)

* Sat Feb 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt0.1
- initial build for ALT Linux Sisyphus
