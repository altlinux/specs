%global import_path github.com/coreos/ignition
%define dracutlibdir %{_prefix}/lib/dracut

Name:     ignition
Version:  2.12.0
Release:  alt1

Summary:  First boot installer and configuration tool
License:  Apache-2.0
Group:    System/Configuration/Boot and Init
Url:      https://github.com/coreos/ignition

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libblkid-devel

Requires: btrfs-progs
Requires: dosfstools
Requires: gdisk
Requires: dracut
Requires: dracut-network

%description
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, networkd units, etc.), and configuring
users. On first boot, Ignition reads its configuration from a source
of truth (remote URL, network metadata service, hypervisor bridge, etc.)
and applies the configuration.

%package validate
Summary:  Validation tool for Ignition configs
License:  Apache-2.0
Group:    System/Configuration/Boot and Init

%description validate
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, networkd units, etc.), and configuring
users. On first boot, Ignition reads its configuration from a source
of truth (remote URL, network metadata service, hypervisor bridge, etc.)
and applies the configuration.

This package contains a tool for validating Ignition configurations.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version

%golang_prepare

pushd .build/src/%import_path
#%golang_build .
%make_build
popd

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version

pushd .build/src/%import_path
#%golang_install
%makeinstall_std
popd

%files
%doc README.md NEWS docs
%dracutlibdir/modules.d/*

%files validate
%doc README.md
%_bindir/%name-validate

%changelog
* Sat Sep 04 2021 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt1
- new version 2.12.0

* Fri Jul 30 2021 Andrey Sokolov <keremet@altlinux.org> 2.11.0-alt2
- compile without relabeling support

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 2.11.0-alt1
- 2.11.0

* Tue Jun 15 2021 Alexey Shabalin <shaba@altlinux.org> 2.10.1-alt1
- 2.10.1

* Sun Jan 17 2021 Alexey Shabalin <shaba@altlinux.org> 2.9.0-alt1
- 2.9.0

* Wed Dec 02 2020 Alexey Shabalin <shaba@altlinux.org> 2.8.0-alt1
- 2.8.0

* Sun Nov 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus
