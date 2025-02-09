%define _unpackaged_files_terminate_build 1

Name: numix-icon-theme-square
Version: 25.01.31
Release: alt1

Summary: Square icon theme from the Numix project
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://github.com/numixproject/numix-icon-theme-square

Source: %name-%version.tar

Requires: numix-icon-theme = %version-%release

BuildArch: noarch

%description
Numix Square is an icon theme using simple symbols and vivid backgrounds for a
fresh, swishy, and modern look. It is developed by the Numix project and
serves as a companion to the base Numix icon theme (numix-icon-theme).

%prep
%setup

%build
# nothing to build here

%install
install -d %{buildroot}%{_datadir}/icons

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr Numix-Square %{buildroot}%{_datadir}/icons/Numix-Square
cp -pr Numix-Square-Light %{buildroot}%{_datadir}/icons/Numix-Square-Light

%files
%doc LICENSE README.md
%{_datadir}/icons/Numix-Square
%{_datadir}/icons/Numix-Square-Light

%changelog
* Sun Feb 09 2025 Nikolay Strelkov <snk@altlinux.org> 25.01.31-alt1
- Initial build for Sisyphus
