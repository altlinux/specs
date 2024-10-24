%global _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: vitastor
Version: 1.9.2
Release: alt1
Summary: Vitastor, a fast software-defined clustered block storage
Group: System/Base

License: VNPL-1.1
Url: https://vitastor.io/
Source0: %name-%version.tar
Source2: cpp-btree.tar
Source3: json11.tar

Patch: %name-%version.patch
Patch2000: %name-e2k.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build

BuildRequires: pkgconfig(liburing)
BuildRequires: pkgconfig(libnl-3.0) pkgconfig(libnl-genl-3.0)
BuildRequires: libgperftools-devel
BuildRequires: node >= 10
BuildRequires: libjerasure-devel pkgconfig(libisal)
BuildRequires: libgf-complete-devel
BuildRequires: rdma-core-devel

# For PVE
%ifarch x86_64 aarch64
BuildRequires(pre): rpm-build-perl
BuildRequires: pve-storage
%add_perl_lib_path %buildroot%perl_vendor_privlib
%endif

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

%package -n lib%name-kv
Group: System/Libraries
Summary: Vitastor shared key/value database library

%description -n lib%name-kv
Vitastor shared key/value database library.

%package -n lib%name-devel
Group: Development/C++
Summary: Vitastor SDS headers of client and blk library
License: VNPL-1.1 OR GPL-2.0+
Requires: lib%name-blk = %EVR lib%name-client = %EVR

%description -n lib%name-devel
This package contains libraries and headers needed to develop programs
that use Vitastor SDS library.

%package -n pve-storage-vitastor
Group: System/Servers
Summary: Vitastor Proxmox VE Plugin
License: VNPL-1.1 OR GPL-2.0+
Requires: /usr/bin/vitastor-cli
Requires: /usr/bin/vitastor-nbd
Requires: pve-manager pve-storage

%description -n pve-storage-vitastor
Vitastor Proxmox VE Plugin.

%prep
%setup
%patch -p1
%ifarch %e2k
%patch2000 -p1
%endif
tar -xf %SOURCE2 -C cpp-btree
tar -xf %SOURCE3 -C json11
sed -i 's|fdiagnostics-color=always|fdiagnostics-color=auto|' src/CMakeLists.txt

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
        -DWITH_QEMU=OFF \
        -DWITH_FIO=OFF \
        -GNinja
%cmake_build

%install
%cmake_install

mkdir -p %buildroot{%_sysconfdir,%_libexecdir,%_localstatedir}/%name
cp -r mon %buildroot%_libexecdir/%name
mkdir -p %buildroot{%_unitdir,%_udevrulesdir}
install -m 0644 mon/scripts/vitastor.target %buildroot%_unitdir
install -m 0644 mon/scripts/vitastor-mon.service %buildroot%_unitdir
install -m 0644 mon/scripts/vitastor-osd@.service %buildroot%_unitdir
install -m 0644 mon/scripts/90-vitastor.rules %buildroot%_udevrulesdir

# Install PVE plugin
%ifarch x86_64 aarch64
install -D -m 0644 patches/VitastorPlugin.pm %buildroot%perl_vendor_privlib/PVE/Storage/Custom/VitastorPlugin.pm
%endif

# Cleanup
rm -f %buildroot%_libexecdir/%name/mon/scripts/90-vitastor.rules
rm -f %buildroot%_libexecdir/%name/mon/scripts/make-etcd
rm -f %buildroot%_libexecdir/%name/mon/scripts/vitastor-mon.service
rm -f %buildroot%_libexecdir/%name/mon/scripts/vitastor-osd@.service
rm -f %buildroot%_libexecdir/%name/mon/scripts/vitastor.target

%pre common
groupadd -r -f %name 2>/dev/null ||:
useradd  -r -g %name -s /sbin/nologin -c "Vitastor daemons" -M -d %_localstatedir/%name %name 2>/dev/null ||:

%post mon
%post_service vitastor-mon

%preun mon
%preun_service vitastor-mon

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

%post -n pve-storage-vitastor
service pvedaemon condrestart ||:

%postun -n pve-storage-vitastor
if [ $1 = 0 ]; then
    service pvedaemon condrestart ||:
fi

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
%_bindir/vitastor-kv

%files -n lib%name-blk
%_libdir/lib%{name}_blk.so.*

%files -n lib%name-client
%_libdir/lib%{name}_client.so.*

%files -n lib%name-kv
%_libdir/lib%{name}_kv.so.*

%files -n lib%name-devel
%_bindir/vitastor-kv-stress
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%ifarch x86_64 aarch64
%files -n pve-storage-vitastor
%perl_vendor_privlib/PVE/Storage/Custom/VitastorPlugin.pm
%endif

%changelog
* Thu Oct 24 2024 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt1
- 1.9.2

* Sat Sep 14 2024 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt1
- 1.9.1

* Sat Sep 14 2024 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Aug 13 2024 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Jul 16 2024 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- 1.7.1

* Mon Jul 15 2024 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Apr 24 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.6.0-alt1.1
- fixed build for Elbrus

* Thu Apr 11 2024 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Mar 16 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.4.8-alt1.1
- fixed build for Elbrus

* Sun Mar 03 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.8-alt1
- 1.4.8

* Thu Feb 22 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.7-alt1
- 1.4.7

* Tue Feb 20 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.5-alt1
- 1.4.5

* Wed Feb 14 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.4-alt1
- 1.4.4

* Fri Feb 09 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.3-alt1
- 1.4.3

* Tue Jan 23 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Dec 04 2023 Alexey Shabalin <shaba@altlinux.org> 1.3.1-alt1
- 1.3.1

* Thu Nov 09 2023 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Nov 03 2023 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- 1.1.0 (hotfix-1.1.0 branch)

* Wed Oct 18 2023 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1
- 1.0.0 (hotfix-1.0.0 branch)

* Tue Aug 29 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.9.6-alt3.1
- fixed build for Elbrus

* Mon Aug 28 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.6-alt3
- update vitastor-osd@.service for send logs to journald

* Thu Aug 03 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.6-alt2
- cleanup files in mon package
- enable post and preun service for vitastor-mon

* Mon Jul 31 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.6-alt1
- 0.9.6

* Fri Jul 28 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.5-alt1
- 0.9.5

* Mon Jul 03 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.3-alt1
- 0.9.3

* Fri Jun 30 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.2-alt1
- 0.9.2

* Mon May 22 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- 0.9.0
- add pve-storage-vitastor package

* Sun May 14 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.9-alt1
- 0.8.9

* Fri Apr 28 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.8-alt1
- 0.8.8

* Thu Apr 13 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.7-alt1
- 0.8.7

* Thu Jan 19 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.4-alt1
- 0.8.4

* Wed Dec 28 2022 Alexey Shabalin <shaba@altlinux.org> 0.8.3-alt1
- 0.8.3

* Mon Dec 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.8.2-alt1
- 0.8.2

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

