%define _unpackaged_files_terminate_build 1

Name: numix-icon-theme-circle
Version: 26.02.11
Release: alt1

Summary: Circle icon theme from the Numix project
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://github.com/numixproject/numix-icon-theme-circle

Source: %name-%version.tar

Requires: numix-icon-theme

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
install -d %buildroot%_iconsdir
 
mkdir -p %buildroot%_datadir/doc/%name
cp -pr Numix-Circle %buildroot%_iconsdir/Numix-Circle
cp -pr Numix-Circle-Light %buildroot%_iconsdir/Numix-Circle-Light

%files
%doc LICENSE README.md
%_iconsdir/Numix-Circle
%_iconsdir/Numix-Circle-Light

# prevent "find-provides: broken symbolic link" messages
%exclude %_iconsdir/Numix-Circle-Light/16/panel
%exclude %_iconsdir/Numix-Circle-Light/22/panel
%exclude %_iconsdir/Numix-Circle-Light/24/panel
%exclude %_iconsdir/Numix-Circle/16/panel
%exclude %_iconsdir/Numix-Circle/22/panel
%exclude %_iconsdir/Numix-Circle/24/panel

%changelog
* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 26.02.11-alt1
- New version 26.02.11.

* Mon Jan 12 2026 Nikolay Strelkov <snk@altlinux.org> 26.01.11-alt1
- New version 26.01.11.

* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 25.12.27-alt1
- New version 25.12.27.

* Sat Dec 20 2025 Nikolay Strelkov <snk@altlinux.org> 25.12.15-alt1
- New version 25.12.15.

* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 25.11.15-alt1
- New version 25.11.15.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 25.10.14-alt2
- Remove strict version requirement on numix-icon-theme.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 25.10.14-alt1
- New version 25.10.14.

* Sun Feb 09 2025 Nikolay Strelkov <snk@altlinux.org> 25.01.31-alt1
- Initial build for Sisyphus
