Name:    fonts-ttf-montserrat
Version: 7.222
Release: alt1

Summary: The Montserrat Font Project
License: OFL-1.1
Group:   System/Fonts/True type
Url:     https://github.com/JulietaUla/Montserrat

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-fonts

%description
%summary

%prep
%setup

%install
cd fonts/ttf
%ttf_fonts_install Montserrat

%files -f fonts/ttf/Montserrat.files
%doc AUTHORS.txt CONTRIBUTORS.txt DESCRIPTION.en_us.html README.md

%changelog
* Tue Nov 21 2023 Andrey Cherepanov <cas@altlinux.org> 7.222-alt1
- Initial build for Sisyphus.
