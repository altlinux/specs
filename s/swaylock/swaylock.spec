%define _unpackaged_files_terminate_build 1

Name: swaylock
Version: 1.8.0
Release: alt1

Summary: Swaylock is a screen locking utility for Wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/swaywm/swaylock

# Source-url: https://github.com/swaywm/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch1: alt-rename-pam-login-module.patch

BuildRequires(pre): meson
BuildRequires: pkgconfig(pam)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(cairo)
BuildRequires: libxkbcommon-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: pkgconfig(scdoc)

%description
Swaylock is a screen locking utility for Wayland compositors. It is
compatible with any Wayland compositor which implements the
ext-session-lock-v1 Wayland protocol.

%prep
%setup
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%config(noreplace) %_sysconfdir/pam.d/%name
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_man1dir/%name.1.xz
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Feb 17 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 1.8.0-alt1
- 1.8.0-alt1
- rename the name of the pam login module

* Sat Apr 06 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.7.2-alt2
- add pam to the package build dependencies
- don't overwrite PAM policies when updating the package

* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.7.2-alt1
- Initial build for ALT Linux
