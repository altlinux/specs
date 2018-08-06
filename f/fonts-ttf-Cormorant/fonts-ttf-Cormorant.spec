%define fname Cormorant
%define __unzip /usr/bin/unzip -oj

Name: fonts-ttf-%fname
Version: 3.504
Release: alt1

Summary: Cormorant open-source display font family
License: SIL OFL
Group: System/Fonts/True type
Url: https://github.com/CatharsisFonts/Cormorant
Source: https://github.com/CatharsisFonts/Cormorant/releases/download/v%version/Cormorant_Install_v%version.zip

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildArch: noarch
BuildRequires: rpm-build-fonts >= 0.4
BuildRequires: unzip
PreReq: fontconfig >= 2.4.2

%description
Cormorant is an original design for an extravagant display serif typeface
inspired by the Garamond heritage, hand-drawn and produced by Christian
Thalmann (Catharsis Fonts). The design goal of Cormorant was to distill the
aesthetic essence of Garamond, unfetter it from the limitations of metal
printing, and allow it to bloom into its natural refined form at high
definition.

%prep
%setup -qc

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc README.md *.txt

%changelog
* Mon Aug 06 2018 Ivan A. Melnikov <iv@altlinux.org> 3.504-alt1
- Initial build for Sisyphus
