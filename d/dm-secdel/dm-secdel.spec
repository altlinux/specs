# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: dm-secdel
Version: 1.0.9
Release: alt2

Summary: dm-linear with secure deletion on discard
License: GPL-2.0-only
Group: System/Kernel and hardware
Requires: /sbin/dmsetup /sbin/blockdev /usr/bin/expr
BuildArch: noarch

Url: https://github.com/vt-alt/dm-secdel
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel
%{?!_without_check:%{?!_disable_check:
BuildRequires: banner
BuildRequires: kernel-headers-modules-std-def
BuildRequires: kernel-headers-modules-un-def
BuildRequires: rpm-build-vm
}}

%description
Linear device-mapper target with secure deletion on discard.

%package -n kernel-source-%name
Summary: dm-linear with secure deletion on discard (source)
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Linear device-mapper target with secure deletion on discard (source).

%prep
%setup

%install
make install-bin DESTDIR=%buildroot
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar
mkdir %buildroot/etc
echo '# <target name> <source device> <options>' > %buildroot/etc/secdeltab

%check
# Do a dummy build of the module.
banner std-def
make KDIR=$(echo /lib/modules/*-std-def-*/build) VERSION=%version clean all
# Cannot run tests, because "forbidden dependencies: kernel-image-std-def"

# Build and run functional tests
banner un-def
make KDIR=$(echo /lib/modules/*-un-def-*/build) VERSION=%version clean all
timeout 60 \
vm-run --kvm=cond --sbin --udevd --kernel=un-def ./tests.sh

%files -n kernel-source-%name
%kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md
%config /etc/secdeltab
/sbin/secdelsetup
%_unitdir/secdeltab.service

%post
%post_service secdeltab
systemctl -q enable secdeltab

%preun
%preun_service secdeltab

%changelog
* Mon Oct 31 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.9-alt2
- Fix build on v6.0 (bio_op).

* Mon Oct 24 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.9-alt1
- Fix incorrect build for Linux v5.16.

* Sun Aug 07 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt1
- Fix build for v5.18 (bio_alloc), v5.15, and v5.10.
- Run functional tests on un-def kernel (in %%check).
- Fix kernel panic when erasing with FF pattern.

* Sat Jun 11 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.7-alt6
- Fix build for v5.19.

* Sun Oct 03 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.7-alt5
- Fix building for v5.14.

* Sat Jun 12 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.7-alt4
- Fix building for v5.12.

* Tue Apr 06 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.7-alt3
- Fix building for v5.5 (tested on v5.11).

* Thu Feb 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.7-alt2
- Fix building for 5.4 again.

* Wed Feb 05 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.7-alt1
- Fix building for 5.4.

* Mon Oct 07 2019 Vitaly Chikunov <vt@altlinux.org> 1.0.6-alt1
- Replace audit record with dmesg message.

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.0.5-alt1
- Compatibility with kernels up to 5.2.
- Add audit record.
- Multi-pass erase with specified patterns.

* Sat Oct 13 2018 Vitaly Chikunov <vt@altlinux.org> 1.0.4-alt1
- Compatibility with kernel 4.18

* Mon Jul 09 2018 Vitaly Chikunov <vt@altlinux.org> 1.0.3-alt1
- Compatibility with kernel 4.14

* Mon May 28 2018 Vitaly Chikunov <vt@altlinux.org> 1.0.2-alt1
- Proper install of secdel user space.

* Sun May 27 2018 Vitaly Chikunov <vt@altlinux.org> 1.0.1-alt1
- Systemd support.

* Thu May 24 2018 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt1
- Package for ALT.
