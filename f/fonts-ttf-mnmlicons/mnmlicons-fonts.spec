Name: fonts-ttf-mnmlicons
Version: 1.1
Release: alt1
Summary: Perkins Less Web Framework webfonts

Group: System/Fonts/True type
License: MIT
Url: http://code.google.com/p/perkins-less/
Source0: http://perkins-less.googlecode.com/files/perkins-%version.zip
# TODO
#Source1: %name-fontconfig.conf
BuildArch: noarch

BuildRequires: unzip rpm-build-fonts

%description
Fonts from the deprecated old version of the Perkins Less web framework.

%prep
%setup -c
ln stylesheets/perkins/mnmlicons/mnmliconsv21-webfont.ttf mnmlicons.ttf


%install
%ttf_fonts_install mnmlicons

%files -f mnmlicons.files
%doc LICENSE

%changelog
* Tue Apr 01 2014 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from FC

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Alec Leamas <leamas@nowhere.net> - 1.1-1
- Initial release
