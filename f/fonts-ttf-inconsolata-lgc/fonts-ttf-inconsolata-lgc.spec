%define fname inconsolata-lgc
%define oname inconsolata-lgc-fonts-ttf

Name: fonts-ttf-%fname
Version: 1.1.0
Release: alt1

Summary: modified version of Inconsolata with added the Cyrillic alphabet
License:  OFL
Group: System/Fonts/True type
# github fork with ttf fonts
Url: https://github.com/DeLaGuardo/Inconsolata-LGC 
# original git is https://github.com/MihailJP/Inconsolata-LGC


Packager: Vladimir Didenko <cow@altlinux.org>

Source: %oname-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts

%description
Inconsolata is one of the most suitable font for programmers created by Raph
Levien. Since the original Inconsolata does not contain Cyrillic alphabet,
it was slightly inconvenient for not a few programmers from Russia.

Inconsolata LGC is a modified version of Inconsolata with added the Cyrillic
alphabet which directly descends from Inconsolata Hellenic supporting modern
Greek.

%prep
%setup -n %oname-%version

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc README

%changelog
* Sat Apr 6 2013 Vladimir Didenko <cow@altlinux.ru> 1.1.0-alt1
- first build for Sisiphus - git20130314
