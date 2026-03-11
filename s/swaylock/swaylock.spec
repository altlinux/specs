%define _unpackaged_files_terminate_build 1

Name: swaylock
Version: 1.8.5
Release: alt1

Summary: Swaylock is a screen locking utility for Wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/swaywm/swaylock

# Source-url: https://github.com/swaywm/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch1: alt-fix-pam-config.patch
Patch2: alt-allow-sgid.patch

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
%patch2 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/%name
%attr(2711,root,chkpwd) %_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_man1dir/%name.1.xz
%_datadir/zsh/site-functions/_%name

%changelog
* Wed Mar 11 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.8.5-alt1
- new version

* Wed Nov 26 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 1.8.4-alt1
- new version

* Thu Mar 27 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 1.8.2-alt1
- fixed inconsistent package changelog
- new version

* Wed Mar 26 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 1.8.1-alt1
- fixed unlocking with the correct password (closes: 53567)
- new version

* Mon Feb 17 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 1.8.0-alt1
- 1.8.0-alt1
- rename the name of the pam login module

* Sat Apr 06 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.7.2-alt2
- add pam to the package build dependencies
- don't overwrite PAM policies when updating the package

* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.7.2-alt1
- Initial build for ALT Linux
