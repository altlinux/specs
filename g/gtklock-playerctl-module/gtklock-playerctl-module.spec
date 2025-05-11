%define _unpackaged_files_terminate_build 1

Name: gtklock-playerctl-module
Version: 4.0.0
Release: alt1

Summary: gtklock module adding media player controls to the lockscreen
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/jovanlanik/gtklock-playerctl-module

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(playerctl)
BuildRequires: pkgconfig(libsoup-3.0)

%description
Adds a mpris media player controller to the lockscreen.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_libdir/gtklock/playerctl-module.so

%changelog
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
