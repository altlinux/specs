%define _name hyprmag

# no tests defined
%def_disable check

Name: %_name
Version: 2.2.0
Release: alt1

Summary: A wlroots-compatible Wayland screen magnifier
License: BSD-3-Clause
Group: Accessibility
Url: https://github.com/SIMULATAN/hyprmag

Vcs: https://github.com/SIMULATAN/hyprmag.git

Source: %url/archive/%version/%_name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: /usr/bin/wayland-scanner
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libjpeg)
%{?_enable_check:BuildRequires: ctest}

%description
A wlroots-compatible Wayland screen magnifier with basic customization
options.

%prep
%setup -n %_name-%version

%build
%cmake -DCMAKE_INSTALL_MANDIR=%_mandir
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files
%_bindir/%_name
%_man1dir/%_name.1*
%doc README*

%changelog
* Sun Jun 14 2026 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Jun 11 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Sat Jan 04 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- first build for Sisyphus



