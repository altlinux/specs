%define _unpackaged_files_terminate_build 1
%define fname cmu

Name:    fonts-ttf-%fname
Version: 0.7.0
Release: alt1

Summary: Computer Modern Unicode fonts
License: OFL-1.1
Group:   System/Fonts/True type
Url:     https://salsa.debian.org/fonts-team/fonts-cmu

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-fonts

%description
Computer Modern Unicode fonts were converted from metafont sources
using mftrace with autotrace backend and fontforge. Some characters
in several fonts are copied from Blue Sky type 1 fonts released by
AMS. Their main purpose is to create free good quality fonts for use
in X applications supporting many languages. Currently the fonts
contain glyphs from Latin (Metafont ec, tc, vnr), Cyrillic (lh), Greek
(cbgreek when available) code sets and IPA extensions (from tipa).

%prep
%setup

%build

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc FAQ OFL-FAQ.txt OFL.txt README TODO

%changelog
* Sat Feb 01 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
