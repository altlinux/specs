# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_with gtk

Name: kvmtool
Version: 3.18.0
Release: alt6
Summary: Linux Native KVM Tool
License: GPL-2.0
Group: Emulators
Url: https://git.kernel.org/cgit/linux/kernel/git/will/kvmtool.git
Source: %name-%version.tar

# Do not build on architectures where kvmtool definitely does not work.
#   armh:    Error: '/dev/kvm' KVM driver not available.
#   ppc64le: Warning: Host CPU unsupported by kvmtool
ExcludeArch: armh

BuildRequires: binutils-devel
BuildRequires: glibc-devel-static
BuildRequires: libaio-devel
BuildRequires: libfdt-devel
BuildRequires: libvncserver-devel
BuildRequires: zlib-devel
%if_with gtk
BuildRequires: libgtk+3-devel
BuildRequires: libSDL-devel
%endif
%{?!_without_check:%{?!_disable_check:
BuildRequires(pre): rpm-build-vm
}}

%description
kvmtool is a lightweight tool for hosting KVM guests. As a pure virtualization
tool it only supports guests using the same architecture, though it supports
running 32-bit guests on those 64-bit architectures that allow this.

%prep
%setup

%build
%make_build V=1 prefix=%prefix

%install
%makeinstall_std V=1 prefix=%prefix
install -D Documentation/kvmtool.1 %buildroot%_man1dir/lkvm.1

%ifnarch ppc64le
# Should be workable on ppc64 but ain't: hangs without console output on
# KVM-HV, fails with `KVM_RUN failed: Device or resource busy` on KVM-PR.

%check
./lkvm setup test
ln -s /boot/vmlinuz-*-alt* bzImage
vm-initrd initrd.img --modules='9pnet_virtio 9p virtio_pci'
uuidgen > uuid
# `sleep 1` because power off sometimes eats program output.
# x86 cannot handle a lot of memory causing "Fatal: Failed to read initrd" error
# on girar due to EFAULT, but all can handle around 1G.
timeout 60 \
./lkvm sandbox -m 1024 -i initrd.img -d test -n mode=none -- bash -xc "cat /host/$PWD/uuid; sleep 1" |& tee boot.log
grep -f uuid boot.log
%endif

%files
%define _customdocdir %_docdir/%name
%doc README COPYING CREDITS* Documentation/*.txt
%_bindir/lkvm
%_man1dir/lkvm.1*

%changelog
* Sat Jul 15 2023 Vitaly Chikunov <vt@altlinux.org> 3.18.0-alt6
- Update to git commit bd4ba57 (2023-07-07).
- spec: Update packaging (add GTK, SDL, sframe, and man page).
- spec: Add simple %%check section.

* Mon Jan 23 2023 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt5.git.e17d182a
- update to upstream master (e17d182ad3f797f01947fc234d95c96c050c534b)

* Mon Mar 29 2021 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt4.git.117d6495
- update to upstream master (117d64953228afa90b52f6e1b4873770643ffdc9)

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt3.git.a0eab49a
- update to upstream master (a0eab49a8876ad29a200ce688d1055b566c69b38)

* Tue Jan 15 2019 Alexey Shabalin <shaba@altlinux.org> 3.18.0-alt2.git.fdd26ecb
- update to upstream master (fdd26ecb4bc52ac7e06455d5ea2cf5ebf7d500bc)
- add patch from suse for fix build with gcc8
- build with vncserver support

* Thu Feb 08 2018 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1.git.a508ea
- Initial build
