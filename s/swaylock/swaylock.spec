%define _unpackaged_files_terminate_build 1

Name: swaylock
Version: 1.7.2
Release: alt1

Summary: Swaylock is a screen locking utility for Wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/swaywm/swaylock

# Source-url: https://github.com/swaywm/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(cairo)
BuildRequires: libxkbcommon-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: pkgconfig(scdoc)

%description
Swaylock is a screen locking utility for Wayland compositors. It is compatible
with any Wayland compositor which implements the ext-session-lock-v1 Wayland
protocol.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_sysconfdir/pam.d/%name
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_man1dir/%name.1.xz
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.7.2-alt1
- Initial build for ALT Linux
