# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: fsverity-utils
Version: 1.6
Release: alt1
Summary: Userspace utilities for fs-verity
License: MIT
Group: System/Kernel and hardware
Url: https://www.kernel.org/doc/html/latest/filesystems/fsverity.html
Vcs: https://git.kernel.org/pub/scm/fs/fsverity/fsverity-utils.git
Source: %name-%version.tar

BuildRequires: openssl-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm}}

%description
This is fsverity-utils, a set of userspace utilities for fs-verity.
fs-verity is a Linux kernel feature that does transparent on-demand
integrity/authenticity verification of the contents of read-only
files, using a hidden Merkle tree (hash tree) associated with the
file. It is similar to dm-verity, but implemented at the file level
rather than at the block device level.

%package devel
Summary: Development package for fsverity-utils
Group: Development/C
Requires: %name = %EVR

%description devel
Development package for fsverity-utils.

%prep
%setup

%build
%make_build CFLAGS="%optflags" USE_SHARED_LIB=1 V=1

%install
%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir CFLAGS="%optflags" USE_SHARED_LIB=1 V=1
rm %buildroot%_libdir/libfsverity.a

%check
%make_build check CFLAGS="%optflags" USE_SHARED_LIB=1 V=1
export LD_LIBRARY_PATH=%buildroot%_libdir
PATH=%buildroot%_bindir:$PATH
fsverity --version | grep -Fx 'fsverity v%version'
if grep CONFIG_FS_VERITY=y /boot/config-*; then
	# Brief test from README.
	# `getconf PAGE_SIZE` for powerpc where block is 64K
	timeout 120 \
	vm-run --kvm=cond --sbin --heredoc <<-'EOF'
	truncate -s 11M disk.img
	BS=$(getconf PAGE_SIZE)
	mkfs.ext4 -O verity -b $BS disk.img
	tune2fs -l disk.img | grep verity
	tune2fs -l disk.img | grep Block.size
	mount disk.img /mnt
	cd /mnt
	head -c 1000000 /dev/urandom > file
	sha256sum file > sum.txt
	fsverity digest file
	fsverity enable --block-size=$BS file
	fsverity measure file
	sha256sum -c sum.txt
	! date >> file || exit 2
	EOF
fi

%files
%doc README.md LICENSE NEWS.md
%_bindir/fsverity
%_libdir/*.so.*
%_man1dir/fsverity.1*

%files devel
%_includedir/libfsverity.h
%_libdir/libfsverity.so
%_pkgconfigdir/libfsverity.pc

%changelog
* Sun Mar 24 2024 Vitaly Chikunov <vt@altlinux.org> 1.6-alt1
- Update to v1.6 (2024-03-20).

* Tue Feb 08 2022 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- Updated to v1.5 (2022-02-06).

* Thu Jun 17 2021 Vitaly Chikunov <vt@altlinux.org> 1.4-alt1
- Update to v1.4 (2021-06-14).

* Fri Jan 22 2021 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- First import of v1.3 (2021-01-19).
