%define fname philosopher

Name: fonts-otf-%fname
Version: 1.000
Release: alt3

Summary: Philosopher open type font

License: distributable
Group: System/Fonts/True type
Url: http://lemonad.livejournal.com/37348.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://jovanny.ru/fonts/Philosopher.tar.bz2

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.3

%description
Philosopher font.

%prep
%setup -c %name-%version

%install
%otf_fonts_install %fname

%files -f %fname.files

%changelog
* Mon Apr 04 2022 Igor Vlasenko <viy@altlinux.org> 1.000-alt3
- NMU: dropped deprecated post/un_fonts (closes: #41861)

* Tue Feb 09 2010 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt2
- drop out broken provides

* Thu Dec 10 2009 Vitaly Lipatov <lav@altlinux.ru> 1.000-alt1
- initial build for ALTLinux Sisyphus
