%define fname 3270NerdFont

Name: fonts-ttf-%fname
Version: 3.2.1
Release: alt1

Summary: Nerd Fonts patched IBM 3270 font
License: BSD-3-Clause
Group: System/Fonts/True type
Url: https://www.nerdfonts.com/
Vcs: https://github.com/ryanoasis/nerd-fonts
BuildArch: noarch

Source: %fname-%version.tar
Source1: LICENSE.txt
Source2: README.md

BuildRequires(pre): rpm-build-fonts

%description
%summary.

%prep
%setup -c
cp -a %SOURCE1 . && cp -a %SOURCE2 .

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc LICENSE.* README.*

%changelog
* Sat Jun 29 2024 Anton Kurachenko <srebrov@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus.
