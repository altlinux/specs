Name: fonts-ttf-golos-text
Version: 2.004
Release: alt1
VCS: https://github.com/googlefonts/golos-text
Source: %name-%version.tar
Summary: Golos is a versatile closed sans-serif for state and social service websites
License: OFL-1.1-RFN
Group: System/Fonts/True type
BuildRequires(pre): rpm-build-fonts
BuildArch: noarch

%description
Golos is a versatile closed sans-serif commissioned by Smena and AIC
Media for state and social service websites. Golos Text suits perfectly
for continuous reading on screen. As a variable font, it includes
a weight axis that spans named weight styles from Regular (400) to Black
(900). Golos was designed by Alexandra Korolkova and Vitaly Kuzmin and
released by Paratype in 2019.

%package -n fonts-otf-golos-text
Group: System/Fonts/True type
Summary: %summary (OTF version)
%description -n fonts-otf-golos-text
%summary

%prep
%setup

%build

%install
%ttf_fonts_install golos-text
%otf_fonts_install golos-text-otf

%files -f golos-text.files
%doc *.pdf *.txt *.md

%files -n fonts-otf-golos-text -f golos-text-otf.files
%doc *.txt *.md

%changelog
* Sat Aug 01 2026 Fr. Br. George <george@altlinux.org> 2.004-alt1
- Initial build for ALT
