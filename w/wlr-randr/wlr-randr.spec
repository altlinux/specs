Name: wlr-randr
Version: 0.2.0.2.g2a7601b
Release: alt1
License: MIT
Summary: Utility to manage outputs of a Wayland compositor
URL: https://git.sr.ht/~emersion/wlr-randr
Group: Graphics

Source: %name-%version.tar

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

BuildRequires: cmake meson
BuildRequires: pkgconfig(wayland-client)

%description
wlr-randr is a command line utility to manage outputs of a Wayland compositor.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/wlr-randr

%changelog
* Thu May 05 2022 Alexey Gladkov <legion@altlinux.ru> 0.2.0.2.g2a7601b-alt1
- Initial build.
