Name:    fonts-ttf-libre-franklin
Version: 1.500
Release: alt1

Summary: Libre Franklin Fonts
License: OFL-1.1
Group:   Other
Url:     https://github.com/impallari/Libre-Franklin

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-fonts

%description
Libre Franklin is an interpretation and expansion based on the 1912 Morris
Fuller Benton's classic.

%prep
%setup

%install
cd fonts/TTF
%ttf_fonts_install LibreFranklin

%files -f fonts/TTF/LibreFranklin.files
%doc *.txt README.md

%changelog
* Wed Jan 22 2025 Andrey Cherepanov <cas@altlinux.org> 1.500-alt1
- Initial build for Sisyphus.
