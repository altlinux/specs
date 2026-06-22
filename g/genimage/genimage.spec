# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%ifarch %ix86 x86_64 aarch64 ppc64le riscv64 loongarch64
%def_enable QEMU
%endif
%ifarch %ix86 x86_64 aarch64 %arm riscv64 loongarch64
%def_enable UBOOT
%endif

Name: genimage
Version: 20
Release: alt1

Summary: Tool to generate multiple filesystem and flash images

License: GPL-2.0
Group: Development/Other
URL: https://github.com/pengutronix/genimage
VCS: https://github.com/pengutronix/genimage

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libconfuse-devel

# for check
BuildRequires: /proc
BuildRequires: e2fsprogs
BuildRequires: sfdisk fdisk
BuildRequires: dosfstools
BuildRequires: genisoimage
BuildRequires: squashfs-tools
BuildRequires: mtd-utils
BuildRequires: mtools
%{?_enable_UBOOT:BuildRequires: dtc u-boot-tools}
%{?_enable_QEMU:BuildRequires: qemu-img}

%description
genimage is a tool to generate multiple filesystem and flash/disk images
from a given root filesystem tree. genimage is intended to be run in a
fakeroot environment. It also supports creating flash/disk images out
of different file-system images and files.

Configuration is done in a config file parsed by libconfuse. Options
like the path to tools can be given via environment variables, the
config file or from commandline switches.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check || cat test-suite.log

%files
%doc README.rst
%_bindir/%name

%changelog
* Mon Jun 22 2026 Anton Midyukov <antohami@altlinux.org> 20-alt1
- New version 20.

* Sat Jul 05 2025 Anton Midyukov <antohami@altlinux.org> 19-alt1
- New version 19.

* Fri Nov 01 2024 Anton Midyukov <antohami@altlinux.org> 18-alt2
- Remove "BuildRequires: genext2fs".

* Thu Jul 04 2024 Anton Midyukov <antohami@altlinux.org> 18-alt1
- New version 18.

* Sat Jan 20 2024 Anton Midyukov <antohami@altlinux.org> 17-alt1
- New version 17.
- Enable qemu and uboot support on looongarch64, riscv64.

* Fri Sep 02 2022 Anton Midyukov <antohami@altlinux.org> 16-alt1
- New version 16.

* Sun Jan 23 2022 Anton Midyukov <antohami@altlinux.org> 15-alt1
- Initial build.
