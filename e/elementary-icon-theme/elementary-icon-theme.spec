%define _name elementaryicons
%define ver_major 4

Name: elementary-icon-theme
Version: %ver_major.3.1
Release: alt1

Summary: simple and appealing Tango-styled icon theme
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/elementaryicons

# VCS:https://github.com/elementary/icons.git
Source: https://launchpad.net/%_name/%{ver_major}.x/%version/+download/elementary-icon-theme-%version.tar.xz

BuildArch: noarch

Requires: icon-theme-hicolor

BuildRequires: cmake

%description
The official elementary icons are designed to be simple and appealing.

These icons are the inspiration behind Ubuntu's default Humanity icon
theme.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_datadir/icons/elementary
%doc AUTHORS CONTRIBUTORS README*

%changelog
* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.1-alt1
- 4.3.1

* Thu Sep 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 3.2-alt1
- 3.1 -> 3.2 (bzr -r1136)

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 3.1-alt1
- build for Sisyphus


