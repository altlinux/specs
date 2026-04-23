%define _unpackaged_files_terminate_build 1

Name: waylogout
Version: 0.3
Release: alt2

Summary: Graphical logout/suspend/reboot/shutdown dialog for wayland
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/loserMcloser/waylogout

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: libgomp15-devel

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%{name}.fish
%_datadir/zsh/site-functions/_%{name}

%changelog
* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 0.3-alt2
- Fixed FTBFS caused by gcc15.

* Wed Jul 02 2025 Nikolay Strelkov <snk@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
