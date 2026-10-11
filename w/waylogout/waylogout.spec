%define _unpackaged_files_terminate_build 1

Name: waylogout
Version: 0.4
Release: alt1

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
BuildRequires: libgomp-devel

Requires: fonts-font-awesome

%description
%summary

%prep
%setup
sed -i "s/Font Awesome 7 Free/FontAwesome/" main.c

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
* Sun Oct 11 2026 Nikolay Strelkov <snk@altlinux.org> 0.4-alt1
- New version 0.4.

* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.3-alt3
- Use libgomp-devel instead of libgomp15-devel.

* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 0.3-alt2
- Fixed FTBFS caused by gcc15.

* Wed Jul 02 2025 Nikolay Strelkov <snk@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
