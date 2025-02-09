%define _unpackaged_files_terminate_build 1

Name: numix-icon-theme
Version: 25.01.31
Release: alt1

Summary: Official base icon theme from the Numix project
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://github.com/numixproject/numix-icon-theme

Source: %name-%version.tar

BuildArch: noarch

%description
The Numix icon theme is designed to look fresh, swishy and modern using
white symbols on vividly coloured background for applications and simplistic
devices, toolbars and status icons.

%prep
%setup

%build
# nothing to build here

%install
install -d %{buildroot}%{_datadir}/icons
 
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr Numix %{buildroot}%{_datadir}/icons/Numix
cp -pr Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light

%files
%doc license readme.md
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light

%changelog
* Sun Feb 09 2025 Nikolay Strelkov <snk@altlinux.org> 25.01.31-alt1
- Initial build for Sisyphus
