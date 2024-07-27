Name: fonts-ttf-inter
Version: 4.0
Release: alt1
Summary: TTF font family carefully crafted & designed for computer screens
License: OFL-1.1
Group: System/Fonts/True type
Url: https://rsms.me/inter/
Source: Inter-%version.zip
BuildArch: noarch

BuildRequires: rpm-build-fonts

# Automatically added by buildreq on Mon Nov 19 2012
BuildRequires: unzip

%description
Inter features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like
contextual alternates that adjusts punctuation depending on the shape of
surrounding glyphs, slashed zero for when you need to disambiguate "0"
from "o", tabular numbers, etc.

This is TTF version of the familly, although OTF version is preferred for Linux.

%package -n fonts-otf-inter
Group: System/Fonts/True type
Summary: OTF font family carefully crafted & designed for computer screens

%description -n fonts-otf-inter
Inter features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like
contextual alternates that adjusts punctuation depending on the shape of
surrounding glyphs, slashed zero for when you need to disambiguate "0"
from "o", tabular numbers, etc.

This is OTF version of the familly (preferred).

%prep
%setup -c

%build
%install
cd 'extras/ttf' && %ttf_fonts_install inter
ln -s 'extras/ttf'/inter.files ../../inter.files
cd ../..
cd 'extras/otf' && %otf_fonts_install inter
ln -s 'extras/otf'/inter.files ../../inter-otf.files

%files -f inter.files
%doc *.txt

%files -n fonts-otf-inter -f inter-otf.files
%doc *.txt

%changelog
* Sat Jul 27 2024 Fr. Br. George <george@altlinux.org> 4.0-alt1
- Autobuild version bump to 4.0 (Closes: #50867)

* Thu Apr 02 2020 Fr. Br. George <george@altlinux.ru> 3.12-alt1
- Autobuild version bump to 3.12
- Introduce OTF version

* Tue May 28 2019 Fr. Br. George <george@altlinux.ru> 3.6-alt1
- Autobuild version bump to 3.6

* Tue May 28 2019 Fr. Br. George <george@altlinux.ru> 3.5-alt1
- Initial build for ALT

