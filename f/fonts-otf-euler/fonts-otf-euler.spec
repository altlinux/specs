Name:		fonts-otf-euler
Version:	000.002
Release:	alt4
License:	OFL
Group:		System/Fonts/True type
Summary:	OpenType MATH-enabled font
URL:		http://github.com/khaledhosny/euler-otf
Source:		%name-%version.tar
BuildArch:	noarch

BuildRequires:	rpm-build-fonts

%description
Our goal is to create an OpenType MATH-enabled font euler.otf, by
combining the existing Euler math fonts with new glyphs from Hermann
Zapf and adding MATH table information.

The MATH table work is almost done, and initial glyph review by Zapf
have been conducted and implemented, see
http://tug.org/TUGboat/Articles/tb29-2/tb92hagen-euler.pdf and
http://river-valley.tv/reshaping-euler-a-collaboration-with-hermann-zapf/
for more details about the review process. We are planning for another
review before the first official beta.

%prep
%setup

%build

%install
%otf_fonts_install euler

%post
%post_fonts

%postun
%postun_fonts

%files -f euler.files
%doc README tests utils *.txt

%changelog
* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 000.002-alt4
- Merged with Wed Oct 20 upstream
- Rebuilt according to ALT font policy

* Sat Jun 19 2010 Fr. Br. George <george@altlinux.ru> 000.002-alt3
- Merge with 11-6-2010 upstream

* Fri Jun 04 2010 Fr. Br. George <george@altlinux.ru> 000.002-alt2
- Fonts path corrected

* Thu Jun 03 2010 Fr. Br. George <george@altlinux.ru> 000.002-alt1
- Initial build from scratch

