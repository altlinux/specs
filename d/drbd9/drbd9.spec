Name: drbd9
Version: 9.0.21
Release: alt2
%define githash 449d6bf22b01af7d14a297a4ed3e281aa84c94a5

Summary: The Linux kernel code for DRBD9.
License: GPLv2
Group: System/Kernel and hardware
BuildArch: noarch

Url: https://github.com/LINBIT/drbd.git
Source0: %name-%version.tar
Source1: %name-headers-%version.tar

BuildRequires(pre): rpm-build-kernel kernel-headers-modules-std-def
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

%build

%install
mkdir -p %kernel_srcdir
cd ..
tar -cf %kernel_srcdir/kernel-source-%name-%version.tar %name-%version

%check
# sed -i s/SUBDIRS=/M=/g Makefile
# make -C drbd KDIR=/lib/modules/*/build

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md COPYING

%changelog
* Thu Mar 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt2
- Fix build for un-def.

* Mon Feb 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt1
- Initial import for ALT.

