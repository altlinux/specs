%define _unpackaged_files_terminate_build 1

Name: hyprlax
Version: 2.2.0
Release: alt2

Summary: Buttery smooth parallax wallpaper daemon for wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://hyprlax.com
VCS: https://github.com/sandwichfarm/hyprlax

# Source-url: https://github.com/sandwichfarm/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: libwayland-egl-devel
BuildRequires: libglvnd-devel
BuildRequires: libcheck-devel

%description
Dynamic parallax wallpaper engine with multi-compositor support for
Linux.

%prep
%setup
# Dependence on builder CPU harms portability and reproducibility
sed -i 's/-march=native//' Makefile

%build
%make_build

%install
install -Dpm 755 %name %buildroot%_bindir/%name

%check
%make test

%files
%_bindir/%name

%changelog
* Tue Feb 10 2026 Ilya Sorochan <k0tran@altlinux.org> 2.2.0-alt2
- remove `-march=native` flag (fixes riscv64 FTBFS)

* Wed Feb 04 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2.0-alt1
- initial build for ALT Linux
