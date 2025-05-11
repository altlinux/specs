%define _unpackaged_files_terminate_build 1

Name: nwg-shell-wallpapers
Version: 1.5
Release: alt1

Summary: Selection of wallpapers contributed to the nwg-shell project 
License: CC0-1.0
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/nwg-shell-wallpapers

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
The nwg-shell-wallpapers repository contains a selection of wallpapers
contributed to the nwg-shell project. 

%prep
%setup
%patch -p1

%build
# nothing to build here

%install
install -Dm 644 wallpapers/* -t %buildroot/%_datadir/backgrounds/nwg-shell/

%files
%doc LICENSE README.md logo.svg
%dir %_datadir/backgrounds/nwg-shell
%_datadir/backgrounds/nwg-shell/*

%changelog
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 1.5-alt1
- Initial build for Sisyphus
