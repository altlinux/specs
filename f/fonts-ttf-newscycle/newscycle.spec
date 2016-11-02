Name: fonts-ttf-newscycle
Version: 0.5.2
Release: alt1
Summary: A realist sans-serif font family based on specimens of the 1908 News Gothic typeface from ATF
License: OFL
Group: System/Fonts/True type
Url: https://launchpad.net/newscycle
Source: newscycle-%version.zip
BuildArch: noarch

BuildRequires: rpm-build-fonts

# Automatically added by buildreq on Mon Nov 19 2012
BuildRequires: unzip

%description
Inspired by the original News Gothic, which found an eminently useful
life in print media news coverage, the goal of this project is to design
a highly readable open font suitable for large bodies of text, even at
small sizes, and that is available at multiple weights. In addition to
the readability and weight, however, the project is extending News
Gothic's glyph coverage to alphabets derived from Latin, Cyrillic, and
Greek, including the accent marks and diacritics required by languages
outside of Western Europe.

%prep
%setup -c

%build
%install
%ttf_fonts_install newscycle

%files -f newscycle.files
%doc FontLog.txt OFL.txt OFLB-sample-image.svg

%changelog
* Wed Nov 02 2016 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Autobuild version bump to 0.5.2

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Autobuild version bump to 0.5.1

* Tue Nov 20 2012 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Autobuild version bump to 0.5

