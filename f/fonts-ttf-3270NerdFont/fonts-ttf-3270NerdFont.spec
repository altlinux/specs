%define fname 3270NerdFont

Name: fonts-ttf-%fname
Version: 3.4.0
Release: alt2

Summary: Nerd Fonts patched IBM 3270 font
License: BSD-3-Clause
Group: System/Fonts/True type
Url: https://www.nerdfonts.com/
Vcs: https://github.com/ryanoasis/nerd-fonts.git
BuildArch: noarch

Source: %fname-%version.tar
Source1: LICENSE.txt
Source2: README.md

BuildRequires(pre): rpm-build-fonts

%description
%summary.

%prep
%setup -c
cp -a %SOURCE1 %SOURCE2 .

%install
%ttf_fonts_install %fname

%post
%_bindir/fc-cache %_fontsdir ||:

%files -f %fname.files
%doc LICENSE.* README.*

%changelog
* Sat Jul 04 2026 Anton Kurachenko <srebrov@altlinux.org> 3.4.0-alt2
- Added %post to update the font cache after installation.

* Sat Apr 26 2025 Anton Kurachenko <srebrov@altlinux.org> 3.4.0-alt1
- New version 3.4.0.

* Sat Nov 23 2024 Anton Kurachenko <srebrov@altlinux.org> 3.3.0-alt1
- New version 3.3.0.

* Sat Jun 29 2024 Anton Kurachenko <srebrov@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus.
