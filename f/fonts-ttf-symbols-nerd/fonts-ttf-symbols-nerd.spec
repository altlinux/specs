%define fname symbols-nerd
%define upstream NerdFontsSymbolsOnly
%define fconf 10-nerd-font-symbols.conf

Name: fonts-ttf-%fname
Version: 3.3.0
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

install -d %buildroot%_fontconfig_templatedir %buildroot%_fontconfig_confdir

cp %fconf %buildroot%_fontconfig_templatedir
ln -s %_fontconfig_templatedir/%fconf %buildroot%_fontconfig_confdir/%fconf

%files -f %fname.files
%doc LICENSE README.*
%_fontconfig_templatedir/%fconf
%config(noreplace) %_fontconfig_confdir/%fconf

%changelog
* Sat Jan 11 2025 Kirill Unitsaev <fiersik@altlinux.org> 3.3.0-alt1
- new version 3.3.0 (with rpmrb script)
- add a font config file

* Sun Oct 27 2024 Kirill Unitsaev <fiersik@altlinux.org> 3.2.1-alt1
- Initial build
