%def_without check

Name: drbd9
Version: 9.2.1
Release: alt1
%define githash 86ec2326fef3aede9f4d46f52bfd35aac4d5eb7e

Summary: The Linux kernel code for DRBD9.
License: GPLv2
Group: System/Kernel and hardware
# ExclusiveArch: x86_64 aarch64 ppc64le
BuildArch: noarch

Url: https://github.com/LINBIT/drbd.git
Source0: %name-%version.tar
Source1: %name-headers-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def kernel-headers-modules-un-def kernel-headers-modules-ovz-el7
BuildRequires: coccinelle >= 1.0.8
BuildRequires: libelf-devel

%description
DRBD, developed by LINBIT, is a software that allows RAID 1 functionality over
TCP/IP and RDMA for GNU/Linux. DRBD is a block device which is designed
to build high availability clusters and software defined storage by providing
a virtual shared device which keeps disks in nodes synchronised using TCP/IP
or RDMA. This simulates RAID 1 but avoids the use of uncommon hardware
(shared SCSI buses or Fibre Channel).

%package -n kernel-source-%name
Summary: The Linux kernel code for DRBD9.
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
The Linux kernel code for DRBD9.

%prep
%setup -q
tar -xf %SOURCE1 -C drbd/drbd-headers
echo "GIT-hash: %githash" >drbd/.drbd_git_revision
%patch -p1

%build

%install
mkdir -p %kernel_srcdir
cd ..
tar -cf %kernel_srcdir/kernel-source-%name-%version.tar %name-%version

%check
make -C drbd KDIR=/lib/modules/*-ovz*/build -k
make -C drbd KDIR=/lib/modules/*-std-def-*/build -k
make -C drbd KDIR=/lib/modules/*-un-def-*/build -k

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md COPYING

%changelog
* Tue Nov 15 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.2.1-alt1
- 9.2.1

* Tue Oct 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.2.0-alt2
- Fix build for 6.0.

* Mon Oct 10 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.2.0-alt1
- 9.2.0

* Wed Sep 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.11-alt1
- 9.1.11

* Fri Sep 02 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.10-alt1
- 9.1.10

* Fri Jul 15 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.8-alt1
- 9.1.8

* Thu Apr 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.7-alt1
- 9.1.7
- Fix build for 5.16, revert changes up to 5.15.

* Mon Feb 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.6-alt1
- 9.1.6

* Sun Feb 13 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.5-alt3
- Fix build for 3.10 ovz7.

* Sat Feb 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 9.1.5-alt2
- Fix build for 5.15 and 5.16.

* Fri Dec 17 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.5-alt1
- 9.1.5

* Fri Nov 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.4-alt2
- Disable check for un-def until upstream make fix for 5.15 kernel.

* Tue Oct 05 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.4-alt1
- 9.1.4

* Fri Sep 03 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.3-alt2
- Fix build for 5.14.

* Fri Jul 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.3-alt1
- 9.1.3

* Fri May 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.2-alt1
- 9.1.2

* Fri Mar 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.1-alt1
- 9.1.1

* Sat Mar 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.0-alt2
- Fix build for 5.11.
- Enable check for std-def and un-def.

* Fri Feb 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.1.0-alt1
- 9.1.0

* Fri Feb 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.0.28-alt1
- 9.0.28

* Tue Dec 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.27-alt1
- 9.0.27

* Tue Dec 15 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.26-alt0.rc4
- 9.0.26rc4

* Sat Oct 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.25-alt2
- Build for kernel 5.9.

* Tue Oct 13 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.25-alt1
- 9.0.25

* Tue Sep 01 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.24-alt2
- Build for kernel 5.8.

* Thu Jul 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.24-alt1
- 9.0.24

* Sun Jun 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.23-alt1
- 9.0.23

* Thu Jun 04 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.23-alt0.rc3.1
- 9.0.23rc3

* Thu May 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.23-alt0.rc1.1
- 9.0.23rc1

* Tue Apr 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.22-alt1
- 9.0.22

* Fri Mar 06 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt3
- Fix pr_warning().

* Thu Mar 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt2
- Fix build for un-def.

* Mon Feb 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt1
- Initial import for ALT.

