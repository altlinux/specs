%define PName Asana-Math
Name: fonts-otf-asana-math
Version: 000.955
Release: alt2
License: OFL
Group: System/Fonts/True type
Summary: OpenType MATH-enabled Asana font
Url: http://www.ctan.org/tex-archive/fonts/Asana-Math/
Source: Asana-Math.zip
BuildArch: noarch

# Automatically added by buildreq on Thu Jun 03 2010
BuildRequires: unzip rpm-build-fonts

%description
The Asana-Math OpenType font includes almost all mathematical symbols
included in the latest version of Unicode. In addition, it includes
a MATH OpenType table so as to be useful for the typesetting of
mathematical text. It has beeb tested with XeTeX 0.997 and the
output is comparable to the output produced with Cambria-Math.
The font is not finished yet, but it is released as beta software
in the hope that people will use it, diccover bugs and report
them back to me. Last but certainly least, I used the pxfonts as
a basis for the design of most glyphs.

%prep
%setup -n %PName

%build
%install
%otf_fonts_install %PName

%files -f %PName.files
%doc README FontLog.txt

%changelog
* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 000.955-alt2
- TTF package remove

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 000.955-alt1
- Autobuild version bump to 000.955

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 000.954-alt1
- Autobuild version bump to 000.954

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 000.952-alt1
- Autobuild version bump to 000.952

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 000.951-alt1
- Autobuild version bump to 000.951

* Wed Aug 28 2013 Fr. Br. George <george@altlinux.ru> 000.949-alt1
- Autobuild version bump to 000.949
- Fix docs

* Fri Jun 04 2010 Fr. Br. George <george@altlinux.ru> 000.926-alt1
- Initial build from scratch

