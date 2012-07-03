Name: fonts-otf-stix
Version: 1.0.0
Release: alt2

Summary: MathML STIX OpenType font family
License: STIX Font License

Group: System/Fonts/True type
Url: http://www.stixfonts.org/
Source: STIXv%version.zip

BuildArch: noarch
PreReq: fontconfig >= 2.4.2
BuildRequires: unzip rpm-build-fonts

%description
The mission of the Scientific and Technical Information Exchange (STIX)
font creation project is the preparation of a comprehensive set of fonts
that serve the scientific and engineering community in the process from
manuscript creation through final publication, both in electronic and
print formats. Toward this purpose, the STIX fonts will be made
available, under royalty-free license, to anyone, including publishers,
software developers, scientists, students, and the general public.

%prep
%setup -n STIXv%version

%build

%install
cd Fonts
%otf_fonts_install stix

%post
%post_fonts

%postun
%postun_fonts

%files -f Fonts/stix.files
%doc Blocks Glyphs HTML License *.pdf

%changelog
* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- Rebuild according to ALT font policy

* Tue Jun 01 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Version up

* Sun Nov 16 2008 Fr. Br. George <george@altlinux.ru> 0.2007-alt1
- Initial build from scratch

