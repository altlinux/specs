Name:    pciex
Version: 0.0.2
Release: alt1

Summary: PCI topology EXplorer
License: GPL-2.0-only
Group:   Monitoring
Url:     https://github.com/s0nx/pciex

Source: %name-%version.tar
Patch0: pciex-0.0.2-alt-unbundle-deps.patch
Patch1: pciex-0.0.2-alt-compile-error-fix.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(ftxui)
BuildRequires: pkgconfig(CLI11)

Requires: hwdata

%description
terminal-based PCI topology explorer for Linux.

Features
* whole topology overview in compact or verbose mode
* visual representation of the device configuration space layout
* detailed information about each register within header/capability
* ability to display only needed register information
* virtual-to-physical address mapping info for BARs
* additional information decoding for VirtIO devices
* quick navigation with keyboard & mouse
* topology snapshots
* ... more to come :)

%prep
%setup
%patch0
%patch1

%build
%cmake
%cmake_build

%install
%cmake_install
%__install -d %buildroot%_bindir
%__install -m755 %_cmake__builddir/%name %buildroot%_bindir

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Thu Jan 09 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus.
