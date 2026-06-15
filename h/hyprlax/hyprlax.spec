%define _unpackaged_files_terminate_build 1
%def_with check

Name: hyprlax
Version: 2.2.4
Release: alt1

Summary: Buttery smooth parallax wallpaper daemon for wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://hyprlax.com
VCS: https://github.com/sandwichfarm/hyprlax

# Source-url: https://github.com/sandwichfarm/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: libwayland-egl-devel
BuildRequires: libglvnd-devel
BuildRequires: libcheck-devel
%if_with check
BuildRequires: /proc
%endif

%description
Dynamic parallax wallpaper engine with multi-compositor support for
Linux.

%prep
%setup
%if_with check
%patch1 -p1
%endif
# Dependence on builder CPU harms portability and reproducibility
sed -i 's/-march=native//' Makefile

echo "%version" > VERSION

%build
%make_build

%install
install -Dpm 755 %name %buildroot%_bindir/%name

%check
%make test

%files
%_bindir/%name

%changelog
* Mon Jun 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2.4-alt1
- new version

* Tue Mar 17 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2.2-alt1
- new version

* Fri Feb 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2.1-alt2
- fix incorrect version display (closes: 57941)

* Mon Feb 16 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2.1-alt1
- new version

* Tue Feb 10 2026 Ilya Sorochan <k0tran@altlinux.org> 2.2.0-alt2
- remove `-march=native` flag (fixes riscv64 FTBFS)

* Wed Feb 04 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.2.0-alt1
- initial build for ALT Linux
