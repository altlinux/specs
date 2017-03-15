Name: fonts-otf-stix
Version: 2.0.0
Release: alt1

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
cd Fonts/OTF
%otf_fonts_install stix

%files -f Fonts/OTF/stix.files
%doc docs

%changelog
* Wed Mar 15 2017 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Autobuild version bump to 2.0.0
- Major upstream changes, beware!

* Mon Nov 19 2012 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0
- remove post macros in favour of file triggers

* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- Rebuild according to ALT font policy

* Tue Jun 01 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Version up

* Sun Nov 16 2008 Fr. Br. George <george@altlinux.ru> 0.2007-alt1
- Initial build from scratch

