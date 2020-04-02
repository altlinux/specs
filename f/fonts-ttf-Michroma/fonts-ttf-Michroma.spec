Name: fonts-ttf-Michroma
Version: 1.00
Release: alt1
Summary: A reworking and remodelling of the rounded-square sans genre
License: OFL-1.1
Group: System/Fonts/True type
Url: https://fonts.google.com/specimen/Michroma
Source: Michroma.zip
BuildArch: noarch

# Automatically added by buildreq on Thu Apr 02 2020
# optimized out: python2-base sh4
BuildRequires: libfreetype-demos unzip

BuildRequires: rpm-build-fonts

%description
Michroma is a reworking and remodelling of the rounded-square sans genre
that is closely associated with a 1960s feeling of the future. This is
due to the popularity of Microgramma, designed by Aldo Novarese and
Alessandro Buttiin in 1952, which pioneered the style; and the most
famous typeface family of the genre that came 10 years later in
Novarese's Eurostile.

Michroma has character widths and stem weights perfectly formed to fit
today's digital screens; Vernon Adams has pioneered a design process
with this font that produces excellent results on screen with no manual
hinting involved.

%prep
%setup -c

%build
test `ftdump Michroma-Regular.ttf | sed -En 's/^[[:space:]]*revision:[[:space:]]*(.*)/\1/p'` = %version

%install
%ttf_fonts_install Michroma

%files -f Michroma.files

%changelog
* Thu Apr 02 2020 Fr. Br. George <george@altlinux.ru> 1.00-alt1
- Initial build from Google fonts

