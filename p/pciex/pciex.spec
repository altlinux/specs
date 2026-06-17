# XXX: Actual commit hash of build tag(git log -1 --format=%%h %%version)
%define tag_hash 53bd21a

Name:    pciex
Version: 0.0.2.0.11.git%tag_hash
Release: alt1

Summary: PCI topology EXplorer
License: GPL-2.0-only
Group:   Monitoring
Url:     https://github.com/s0nx/pciex

Source: %name-%version.tar
Patch0: pciex-0.0.2-alt-unbundle-deps.patch
Patch1: pciex-0.0.2-alt-setversion.patch
Patch2: pciex-0.0.2-alt-adapt-ftxui7.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(ftxui)
BuildRequires: pkgconfig(CLI11)
BuildRequires: glaze-devel

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
%autopatch
%ifarch %e2k
# error: no instance of function template "std::construct_at" matches the argument list
sed -i 's/devices\.emplace_back(/&DeviceDesc{/;T;:a;s/);$/}&/;t;n;ba' \
    src/{snapshot,linux-sysfs}.cpp
%endif

%build
%cmake \
    -DPCIEX_VERSION=%version \
    -DPCIEX_HASH=%tag_hash
%cmake_build

%install
%cmake_install
%__install -d %buildroot%_bindir
%__install -m755 %_cmake__builddir/%name %buildroot%_bindir

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Wed Jun 17 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.0.2.0.11.git53bd21a-alt1
- Fix compatibility with FTXUI v7.0.0.

* Sat Sep 20 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.2-alt3.1
- fix build with fmt 12

* Tue Sep 09 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.0.2-alt3
- e2k build fix

* Fri Mar 28 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.0.2-alt2
- Applied hotfix patch from upstream to link libftxui-6.0.0.
- Added some fixes to create pciex_version.h which provides
  correct output with --version argument.

* Thu Jan 09 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus.
