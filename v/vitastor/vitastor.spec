
%global _unpackaged_files_terminate_build 1

Name: vitastor
Version: 0.8.1
Release: alt1
Summary: Vitastor, a fast software-defined clustered block storage
Group: System/Base

License: VNPL-1.1
Url: https://vitastor.io/
Source0: %name-%version.tar
Source2: cpp-btree.tar
Source3: json11.tar

Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: pkgconfig(liburing)
BuildRequires: libgperftools-devel
BuildRequires: node >= 10
BuildRequires: libjerasure-devel
# BuildRequires: libisa-l-devel
BuildRequires: libgf-complete-devel
BuildRequires: rdma-core-devel

%description
Vitastor is a small, simple and fast clustered block storage (storage for VM drives),
architecturally similar to Ceph which means strong consistency, primary-replication,
symmetric clustering and automatic data distribution over any number of drives of any
size with configurable redundancy (replication or erasure codes/XOR).

%package common
Summary: Vitastor SDS Common
Group: System/Base
BuildArch: noarch

%description common
Common utilities for Vitastor.

%package mon
Summary: Vitastor SDS monitor service
Group: System/Base
BuildArch: noarch
Requires: node
Requires: lp_solve
Requires: %name-common = %EVR

%description mon
Vitastor SDS monitor service.
Monitor is a separate daemon that watches cluster state and handles failures.

%package osd
Summary: Vitastor SDS Object Storage Daemon
Group: System/Base
Requires: %name-common = %EVR
Requires: %name-client = %EVR
Requires: sfdisk util-linux parted udev

%description osd
Vitastor SDS Object Storage Daemon is a process that stores data and serves read/write requests.

%package client
Summary: Vitastor SDS client
Group: System/Base

%description client
Vitastor client library and command-line interface.

%package nbd
Summary: Vitastor SDS NBD proxy
Group: System/Base

%description nbd
NBD stands for "Network Block Device", but in fact it also functions as "BUSE"
(Block Device in UserSpace). NBD is currently required to mount Vitastor via kernel.
NBD slighly lowers the performance due to additional overhead, but performance still
remains decent.

Vitastor Kubernetes CSI driver is based on NBD.

%package nfs
Summary: Vitastor SDS NFS proxy
Group: System/Base

%description nfs
Vitastor has a simplified NFS 3.0 proxy for file-based image access emulation. It's not
suitable as a full-featured file system, at least because all file/image metadata is stored
in etcd and kept in memory all the time - thus you can't put a lot of files in it.

However, NFS proxy is totally fine as a method to provide VM image access and allows to
plug Vitastor into, for example, VMWare. It's important to note that for VMWare it's a much
better access method than iSCSI, because with iSCSI we'd have to put all VM images into one
Vitastor image exported as a LUN to VMWare and formatted with VMFS. VMWare doesn't use VMFS
over NFS.

NFS proxy is stateless if you use immediate_commit=all mode (for SSD with capacitors or
HDDs with disabled cache), so you can run multiple NFS proxies and use a network load
balancer or any failover method you want to in that case.

%package -n lib%name-client
Group: System/Libraries
Summary: Vitastor SDS user-space client library
License: VNPL-1.1 OR GPL-2.0+

%description -n lib%name-client
Vitastor SDS user-space client library.

%package -n lib%name-blk
Group: System/Libraries
Summary: Vitastor SDS blk library

%description -n lib%name-blk
Vitastor SDS blk library.

%package -n lib%name-devel
Group: Development/C++
Summary: Vitastor SDS headers of client and blk library
License: VNPL-1.1 OR GPL-2.0+
Requires: lib%name-blk = %EVR lib%name-client = %EVR

%description -n lib%name-devel
This package contains libraries and headers needed to develop programs
that use Vitastor SDS library.

%prep
%setup
%patch -p1
tar -xf %SOURCE2 -C cpp-btree
tar -xf %SOURCE3 -C json11

%build
%cmake \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DWITH_QEMU=OFF \
	-DWITH_FIO=OFF
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot{%_sysconfdir,%_libexecdir,%_localstatedir}/%name
cp -r mon %buildroot%_libexecdir/%name
mkdir -p %buildroot{%_unitdir,%_udevrulesdir}
install -m 0644 mon/vitastor.target %buildroot%_unitdir
install -m 0644 mon/vitastor-mon.service %buildroot%_unitdir
install -m 0644 mon/vitastor-osd@.service %buildroot%_unitdir
install -m 0644 mon/90-vitastor.rules %buildroot%_udevrulesdir

%pre common
groupadd -r -f %name 2>/dev/null ||:
useradd  -r -g %name -s /sbin/nologin -c "Vitastor daemons" -M -d %_localstatedir/%name %name 2>/dev/null ||:

#%post mon
#%post_service vitastor-mon

#%preun mon
#%preun_service vitastor-mon

#%post osd
#systemctl daemon-reload ||:
#if [ "$1" -eq 1 ]; then
#        systemctl -q preset vitastor-osd@\*.service vitastor-osd.target ||:
#else
#        systemctl try-restart vitastor-osd.target ||:
#fi

#%preun osd
#if [ "$1" -eq 0 ]; then
#        systemctl --no-reload -q disable vitastor-osd@\*.service vitastor-osd.target ||:
#        systemctl stop vitastor-osd@\*.service  vitastor-osd.target ||:
#fi

%files common
%doc README.md README-ru.md VNPL-1.1.txt GPL-2.0.txt
%attr(770,root,%name) %dir %_localstatedir/%name
%attr(770,root,%name) %dir %_sysconfdir/%name

%files osd
%_bindir/%name-osd
%_bindir/%name-disk
# ? may be to utils package?
%_bindir/%name-dump-journal

%_unitdir/%name-osd@.service
%_unitdir/%name.target
%_udevrulesdir/90-%name.rules

%files mon
%_libexecdir/%name
%_unitdir/%name-mon.service

%files client
%_bindir/%name-cli
%_bindir/%name-rm
%_bindir/vita

%files nbd
%_bindir/%name-nbd

%files nfs
%_bindir/%name-nfs

%files -n lib%name-blk
%_libdir/lib%{name}_blk.so.*

%files -n lib%name-client
%_libdir/lib%{name}_client.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Thu Dec 01 2022 Alexey Shabalin <shaba@altlinux.org> 0.8.1-alt1
- 0.8.1

* Tue Sep 06 2022 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- 0.8.0

* Fri Apr 15 2022 Alexey Shabalin <shaba@altlinux.org> 0.6.16-alt1
- 0.6.16

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.6.12-alt1
- 0.6.12

* Sat Jan 15 2022 Alexey Shabalin <shaba@altlinux.org> 0.6.11-alt1
- 0.6.11

* Fri Dec 17 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.10-alt1
- 0.6.10

* Sun Jul 11 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.5-alt1
- 0.6.5

* Fri Jul 02 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.4-alt2
- build master snapshot 30bb6026818b66bbe05bde38d70673e4633313e9
- package client header to devel package
- merge blk and client devel packages

* Wed May 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.4-alt1
- 0.6.4

* Thu May 06 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.3-alt1
- 0.6.3

* Mon Apr 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.2-alt1
- 0.6.2

* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.5.10-alt1
- Initial build.

