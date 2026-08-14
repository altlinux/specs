Name:    rot8
Version: 1.0.1
Release: alt1

Summary: screen rotation daemon
License: MIT
Group:   Graphical desktop/Other
URL:     https://github.com/efernau/rot8

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
rot8 is a daemon that automatically rotates the desktop screen and input
devices using the built-in accelerometer. Handy for convertible touchscreen
notebooks and Linux phones.

It supports X11 and Wayland compositors implementing the wlr_output_management_v1
protocol (such as sway and hyprland). Rotation sensitivity, device selection,
axis inversion and post-rotation hooks can be tuned via command-line options.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri Aug 14 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
