%define _unpackaged_files_terminate_build 1

Name: gtklock-powerbar-module
Version: 5.0.1
Release: alt1

Summary: gtklock module adding power controls to the lockscreen
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/jovanlanik/gtklock-powerbar-module

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)

%description
Adds a reboot and poweroff button the the lockscreen.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_libdir/gtklock/powerbar-module.so

%changelog
* Sat Oct 31 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
