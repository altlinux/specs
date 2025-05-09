%define _unpackaged_files_terminate_build 1

Name: havoc
Version: 0.6.0
Release: alt1

Summary: minimal terminal emulator for wayland
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/ii8/havoc

Source: %name-%version.tar

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: /usr/bin/wayland-scanner

Requires: fonts-ttf-dejavu

%description
A minimal terminal emulator for Wayland on Linux.

%prep
%setup
sed -i "s|/usr/share/fonts/TTF/DejaVuSansMono.ttf|/usr/share/fonts/ttf/dejavu/DejaVuSansMono.ttf|" havoc.cfg

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc LICENSE README.md havoc.cfg
%_bindir/*

%changelog
* Fri May 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
