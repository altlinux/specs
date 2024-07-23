%define fname fira-code-nerd
%define upstream FiraCode

Name: fonts-ttf-%fname
Version: 3.2.1
Release: alt1
License: OFL-1.1

Summary: Nerd Fonts patched FiraCode font

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
* Tue Jul 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 3.2.1-alt1
- Initial build
