%define _unpackaged_files_terminate_build 1

Name: numix-icon-theme-circle
Version: 25.01.31
Release: alt1

Summary: Circle icon theme from the Numix project
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://github.com/numixproject/numix-icon-theme-circle

Source: %name-%version.tar

Requires: numix-icon-theme = %version-%release

BuildArch: noarch

%description
Numix Circle is an icon theme using simple symbols and vivid backgrounds for a
fresh, swishy, and modern look. It is developed by the Numix project and
serves as a companion to the base Numix icon theme (numix-icon-theme).

%prep
%setup

%build
# nothing to build here

%install
install -d %{buildroot}%{_datadir}/icons
 
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr Numix-Circle %{buildroot}%{_datadir}/icons/Numix-Circle
cp -pr Numix-Circle-Light %{buildroot}%{_datadir}/icons/Numix-Circle-Light

%files
%doc LICENSE README.md
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light

%changelog
* Sun Feb 09 2025 Nikolay Strelkov <snk@altlinux.org> 25.01.31-alt1
- Initial build for Sisyphus
