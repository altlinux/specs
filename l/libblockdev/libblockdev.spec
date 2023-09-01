%def_disable snapshot

%define _name blockdev
%define ver_major 3
%define rev 1

%def_with tools
%def_enable check

Name: lib%_name
Version: %ver_major.0.3
Release: alt1

Summary: A library for low-level manipulation with block devices
Group: System/Libraries
License: LGPLv2+
Url: https://github.com/storaged-project/%name

%if_disabled snapshot
Vcs: https://github.com/storaged-project/libblockdev.git
Source: %url/releases/download/%version-%rev/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: autoconf-archive
BuildRequires: python3-devel
BuildRequires: gtk-doc
BuildRequires: libgio-devel gobject-introspection-devel
BuildRequires: libcryptsetup-devel libdevmapper-devel
BuildRequires: systemd-devel libudev-devel libmount-devel
BuildRequires: libvolume_key-devel >= 0.3.9
BuildRequires: libnss-devel
BuildRequires: libkmod-devel
BuildRequires: libparted-devel
BuildRequires: libfdisk-devel
BuildRequires: libkeyutils-devel
BuildRequires: libe2fs-devel
BuildRequires: libblkid-devel
BuildRequires: libbytesize-devel
BuildRequires: libuuid-devel
BuildRequires: libndctl-devel
BuildRequires: libnvme-devel
%{?_enable_check:BuildRequires: python3-module-pylint python3-module-pygobject3}

%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif

%description
The libblockdev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a thin wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of libblockdev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package devel
Summary: Development files for libblockdev
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains header files and pkg-config files needed for development
with the libblockdev library.

%package -n python3-module-blockdev
Summary: Python3 gobject-introspection bindings for libblockdev
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-blockdev
This package contains enhancements to the gobject-introspection bindings for
libblockdev in Python3.

%package utils
Summary: A library with utility functions for the libblockdev library
Group: System/Libraries

%description utils
The libblockdev-utils is a library providing utility functions used by the
libblockdev library and its plugins.

%package utils-devel
Summary: Development files for libblockdev-utils
Group: Development/C
Requires: %name-utils = %EVR

%description utils-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-utils library.

%package btrfs
Summary: The BTRFS plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: btrfs-progs

%description btrfs
The libblockdev library plugin (and in the same time a standalone library)
providing the BTRFS-related functionality.

%package btrfs-devel
Summary: Development files for the libblockdev-btrfs plugin/library
Group: Development/C
Requires: %name-btrfs = %EVR
Requires: %name-utils-devel = %EVR

%description btrfs-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-btrfs plugin/library.

%package crypto
Summary: The crypto plugin for the libblockdev library
Group: System/Libraries

%description crypto
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to encrypted devices (LUKS).

%package crypto-devel
Group: Development/C
Summary: Development files for the libblockdev-crypto plugin/library
Requires: %name-crypto = %EVR

%description crypto-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-crypto plugin/library.

%package dm
Summary: The Device Mapper plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: dmsetup

%description dm
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to Device Mapper.

%package dm-devel
Summary: Development files for the libblockdev-dm plugin/library
Group: Development/C
Requires: %name-dm = %EVR
Requires: %name-utils-devel = %EVR

%description dm-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-dm plugin/library.

%package fs
Summary: The FS plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
# ntfsinfo used for bd_fs_ntfs_get_info()
Requires: ntfs-3g

%description fs
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to operations with file systems.

%package fs-devel
Summary: Development files for the libblockdev-fs plugin/library
Group: Development/C
Requires: %name-fs = %EVR
Requires: %name-utils-devel = %EVR

%description fs-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-fs plugin/library.

%package nvme
Summary: The NVME plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: nvme

%description nvme
The libblockdev library plugin (and in the same time a standalone
library) providing the functionality related to NVME devices.

%package nvme-devel
Summary: Development files for the libblockdev-nvme plugin/library
Group: Development/C
Requires: %name-nvme = %EVR
Requires: %name-utils-devel = %EVR

%description nvme-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-nvme plugin/library.

%package loop
Summary: The loop plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: agetty cfdisk coreutils eject fdisk getopt hwclock login look losetup
Requires: lsblk mount msulogin schedutils setarch sfdisk su sysvinit-utils util-linux

%description loop
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to loop devices.

%package loop-devel
Summary: Development files for the libblockdev-loop plugin/library
Group: Development/C
Requires: %name-loop = %EVR
Requires: %name-utils-devel = %EVR

%description loop-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-loop plugin/library.

%package lvm
Summary: The LVM plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: lvm2

%description lvm
The libblockdev library plugin (and in the same time a standalone library)
providing the LVM-related functionality.

%package lvm-devel
Summary: Development files for the libblockdev-lvm plugin/library
Group: Development/C
Requires: %name-lvm = %EVR
Requires: %name-utils-devel = %EVR

%description lvm-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-lvm plugin/library.

%package lvm-dbus
Summary: The LVM plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: lvm2

%description lvm-dbus
The libblockdev library plugin (and in the same time a standalone library)
providing the LVM-related functionality utilizing the LVM DBus API.

%package lvm-dbus-devel
Summary: Development files for the libblockdev-lvm-dbus plugin/library
Group: Development/C
Requires: %name-lvm-dbus = %EVR
Requires: %name-utils-devel = %EVR

%description lvm-dbus-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-lvm-dbus plugin/library.

%package mdraid
Summary: The MD RAID plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: mdadm

%description mdraid
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to MD RAID.

%package mdraid-devel
Summary: Development files for the libblockdev-mdraid plugin/library
Group: Development/C
Requires: %name-mdraid = %EVR
Requires: %name-utils-devel = %EVR

%description mdraid-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-mdraid plugin/library.

%package mpath
Summary: The multipath plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: multipath-tools

%description mpath
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to multipath devices.

%package mpath-devel
Summary: Development files for the libblockdev-mpath plugin/library
Group: Development/C
Requires: %name-mpath = %EVR
Requires: %name-utils-devel = %EVR

%description mpath-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-mpath plugin/library.

%package part
Summary: The partitioning plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: cgdisk fixparts gdisk

%description part
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to partitioning.

%package part-devel
Summary: Development files for the libblockdev-part plugin/library
Group: Development/C
Requires: %name-part = %EVR
Requires: %name-utils-devel = %EVR

%description part-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-part plugin/library.

%package swap
Summary: The swap plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: agetty cfdisk coreutils eject fdisk getopt hwclock login look losetup lsblk
Requires: mount msulogin schedutils setarch sfdisk su sysvinit-utils util-linux

%description swap
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to swap devices.

%package swap-devel
Summary: Development files for the libblockdev-swap plugin/library
Group: Development/C
Requires: %name-swap = %EVR
Requires: %name-utils-devel = %EVR

%description swap-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-swap plugin/library.

%package nvdimm
Summary: The ndctl plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %EVR
Requires: ndctl daxctl

%description nvdimm
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to NVDIMM devices.

%package nvdimm-devel
Summary: Development files for the libblockdev-nvdimm plugin/library
Group: Development/C
Requires: %name-nvdimm = %EVR
Requires: %name-utils-devel = %EVR

%description nvdimm-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-nvdimm plugin/library.

%package s390
Summary: The s390 plugin for the libblockdev library
Group: System/Libraries
Requires: s390utils

%description s390
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to s390 devices.

%package s390-devel
Summary: Development files for the libblockdev-s390 plugin/library
Group: Development/C
Requires: %name-s390 = %EVR
Requires: %name-utils-devel = %EVR

%description s390-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-s390 plugin/library.

%package plugins
Summary: Meta-package that pulls all the libblockdev plugins as dependencies
Group: System/Libraries
BuildArch: noarch
Requires: %name-btrfs = %EVR
Requires: %name-crypto = %EVR
Requires: %name-dm = %EVR
Requires: %name-fs = %EVR
Requires: %name-loop = %EVR
Requires: %name-lvm = %EVR
Requires: %name-mdraid = %EVR
Requires: %name-mpath = %EVR
Requires: %name-part = %EVR
Requires: %name-swap = %EVR
Requires: %name-nvdimm = %EVR
Requires: %name-nvme = %EVR
%ifarch s390 s390x
Requires: %name-s390 = %EVR
%endif

%description plugins
A meta-package that pulls all the libblockdev plugins as dependencies.

%package tools
Summary: Tools from libblockdev package
Group: System/Kernel and hardware
Requires: %name-lvm = %EVR

%description tools
This package contains cli libblockdev tools.
vm-cache-stats -- for displaying stats for LVM cache devices.

%prep
%setup -n %name-%version
sed -i 's/\(pylint\)-3/\1.py3/' Makefile.*

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
    %{subst_with tools}
%nil
%make_build

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -print0| xargs -r0 rm -f --

%check
%make check

%files
%_libdir/libblockdev.so.*
%_typelibdir/BlockDev*.typelib
%config %_sysconfdir/libblockdev/%ver_major/conf.d/00-default.cfg
%doc *.md LICENSE

%files devel
%_libdir/libblockdev.so
%dir %_includedir/blockdev
%_includedir/blockdev/blockdev.h
%_includedir/blockdev/dev_utils.h
%_includedir/blockdev/extra_arg.h
%_includedir/blockdev/plugins.h
%_pkgconfigdir/blockdev.pc
%_datadir/gtk-doc/html/libblockdev
%_girdir/BlockDev*.gir

%files -n python3-module-blockdev
%python3_sitelibdir/gi/overrides/BlockDev*
%python3_sitelibdir/gi/overrides/__pycache__/BlockDev*

%files utils
%_libdir/libbd_utils.so.*

%files utils-devel
%_libdir/libbd_utils.so
%dir %_includedir/blockdev
%_includedir/blockdev/utils.h
%_includedir/blockdev/sizes.h
%_includedir/blockdev/exec.h
%_includedir/blockdev/module.h
%_includedir/blockdev/dbus.h
%_includedir/blockdev/logging.h
%_pkgconfigdir/blockdev-utils.pc

%files btrfs
%_libdir/libbd_btrfs.so.*

%files btrfs-devel
%_libdir/libbd_btrfs.so
%dir %_includedir/blockdev
%_includedir/blockdev/btrfs.h

%files crypto
%_libdir/libbd_crypto.so.*

%files crypto-devel
%_libdir/libbd_crypto.so
%dir %_includedir/blockdev
%_includedir/blockdev/crypto.h

%files dm
%_libdir/libbd_dm.so.*

%files dm-devel
%_libdir/libbd_dm.so
%dir %_includedir/blockdev
%_includedir/blockdev/dm.h

%files fs
%_libdir/libbd_fs.so.*

%files fs-devel
%_libdir/libbd_fs.so
%dir %_includedir/blockdev
%_includedir/blockdev/fs.h
%_includedir/blockdev/fs/

%files nvme
%_libdir/libbd_nvme.so.*

%files nvme-devel
%_libdir/libbd_nvme.so
%dir %_includedir/blockdev
%_includedir/blockdev/nvme.h

%files loop
%_libdir/libbd_loop.so.*

%files loop-devel
%_libdir/libbd_loop.so
%dir %_includedir/blockdev
%_includedir/blockdev/loop.h

%files lvm
%_libdir/libbd_lvm.so.*

%files lvm-devel
%_libdir/libbd_lvm.so
%dir %_includedir/blockdev
%_includedir/blockdev/lvm.h

%files lvm-dbus
%_libdir/libbd_lvm-dbus.so.*
%config %_sysconfdir/libblockdev/%ver_major/conf.d/10-lvm-dbus.cfg

%files lvm-dbus-devel
%_libdir/libbd_lvm-dbus.so
%dir %_includedir/blockdev
#%_includedir/blockdev/lvm.h

%files mdraid
%_libdir/libbd_mdraid.so.*

%files mdraid-devel
%_libdir/libbd_mdraid.so
%dir %_includedir/blockdev
%_includedir/blockdev/mdraid.h

%files mpath
%_libdir/libbd_mpath.so.*

%files mpath-devel
%_libdir/libbd_mpath.so
%dir %_includedir/blockdev
%_includedir/blockdev/mpath.h

%files part
%_libdir/libbd_part.so.*

%files part-devel
%_libdir/libbd_part.so
%dir %_includedir/blockdev
%_includedir/blockdev/part.h

%files swap
%_libdir/libbd_swap.so.*

%files swap-devel
%_libdir/libbd_swap.so
%dir %_includedir/blockdev
%_includedir/blockdev/swap.h

%files nvdimm
%_libdir/libbd_nvdimm.so.*

%files nvdimm-devel
%_libdir/libbd_nvdimm.so
%dir %_includedir/blockdev
%_includedir/blockdev/nvdimm.h

%ifarch s390 s390x
%files s390
%_libdir/libbd_s390.so.*

%files s390-devel
%_libdir/libbd_s390.so
%dir %_includedir/blockdev
%_includedir/blockdev/s390.h
%endif

%files plugins

%if_with tools
%files tools
%_bindir/lvm-cache-stats
%_bindir/vfat-resize
%endif

%changelog
* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Thu Jul 20 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Wed Jul 05 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Thu Jun 29 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.28-alt1
- 2.28

* Wed Jun 01 2022 Yuri N. Sedunov <aris@altlinux.org> 2.27-alt1
- 2.27

* Wed Jul 28 2021 Yuri N. Sedunov <aris@altlinux.org> 2.26-alt1
- 2.26

* Tue Jan 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.25-alt1
- 2.25

* Fri Jan 01 2021 Yuri N. Sedunov <aris@altlinux.org> 2.24-alt2
- more fixes for dosfstools without compatibility symlinks (ALT #39495)
- %%name-{fs,part}: removed obsolete multipath-tools dependency (ALT #39482)

* Thu May 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.24-alt1
- 2.24

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 2.23-alt1
- 2.23

* Thu Jun 13 2019 Yuri N. Sedunov <aris@altlinux.org> 2.22-alt1
- 2.22

* Fri Feb 22 2019 Yuri N. Sedunov <aris@altlinux.org> 2.21-alt1
- 2.21
- new tools subpackage

* Sat Sep 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20-alt1
- 2.20

* Sat Aug 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.19-alt1
- 2.19

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18-alt1
- 2.18 with
- prepared optional vdo* subpackages (vdo and kvdo required)
- added conditionals for dmraid support

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.17-alt1
- 2.17 with new nvdimm* subpackages

* Fri Feb 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.16-alt1
- 2.16

* Mon Jan 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.15-alt2
- rebuilt against libcryptsetup.so.12

* Wed Dec 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.15-alt1
- 2.15

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14-alt1
- 2.14

* Fri Oct 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.13-alt1
- 2.13

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 2.11.1-alt1
- 2.11-1

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10-1

* Tue Jun 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt1
- first build for Sisyphus



