Name: fonts-ttf-unifont
Version: 9.0.04
Release: alt1

Summary: GNU Unifont, with glyphs for every printable code point in the Unicode 8.0
License: GPLv2
Group: System/Fonts/True type
Url: http://unifoundry.com/unifont.html
Source: unifont-9.0.04.ttf

BuildArch: noarch
PreReq: fontconfig

BuildRequires: rpm-build-fonts

%description
GNU Unifont, with glyphs for every printable code point in the Unicode
Basic Multilingual Plane (BMP). The BMP occupies the first 65,536
code points of the Unicode space, denoted as U+0000..U+FFFF.

%prep
cp %SOURCE0 .

%build
%install
%ttf_fonts_install unifont

%files -f unifont.files
%changelog
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 9.0.04-alt1
- Autobuild version bump to 9.0.04

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 9.0.01-alt1
- Autobuild version bump to 9.0.01

* Mon Aug 31 2015 Fr. Br. George <george@altlinux.ru> 8.0.01-alt1
- Autobuild version bump to 8.0.01

* Sun Aug 30 2015 Fr. Br. George <george@altlinux.ru> 0.0.01-alt1
- Initial empty build

