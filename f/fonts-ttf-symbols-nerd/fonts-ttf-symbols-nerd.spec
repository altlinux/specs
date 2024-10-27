%define fname symbols-nerd
%define upstream NerdFontsSymbolsOnly

Name: fonts-ttf-%fname
Version: 3.2.1
Release: alt1
License: MIT

Summary: Nerd Fonts patched Symbols Only font

Group: System/Fonts/True type

Url: https://www.nerdfonts.com/

BuildArch: noarch

# Source-url: https://github.com/ryanoasis/nerd-fonts/releases/download/v%version/%upstream.tar.xz
Source: %upstream-%version.tar

BuildRequires(pre): rpm-build-fonts

%description
%summary.

%prep
%setup -n %upstream-%version

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc LICENSE README.*

%changelog
* Sun Oct 27 2024 Kirill Unitsaev <fiersik@altlinux.org> 3.2.1-alt1
- Initial build
