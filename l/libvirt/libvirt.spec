%define _unpackaged_files_terminate_build 1

%ifndef _priority_distbranch
# We have it defined in macros but not in buildmacros.
%define _priority_distbranch %(rpm --eval %%_priority_distbranch)
%endif

%define enabled_ifwith() %{expand:%%{?_with_%{1}:enabled}%%{!?_with_%{1}:disabled}}
%define libvirt_sysconfig_rename() \
    for sc in %{?*} ; do \
        [ ! -f "%_sysconfdir/sysconfig/${sc}" ] || continue ; \
        if [ -f "%_sysconfdir/sysconfig/${sc}.rpmsave" ]; then \
            mv -v "%_sysconfdir/sysconfig/${sc}.rpmsave" "%_sysconfdir/sysconfig/${sc}" \
        fi \
    done \
    %{nil}

# For daemons with only UNIX sockets
%define libvirt_systemd_unix_posttrans() %{expand:%%post_systemd_postponed %1.service %1.socket %1-ro.socket %1-admin.socket}
%define libvirt_systemd_unix_preun() %{expand:%%preun_systemd %1.service %1.socket %1-ro.socket %1-admin.socket}

# For daemons with UNIX and INET sockets
%define libvirt_systemd_inet_posttrans() %{expand:%%post_systemd_postponed %1.service %1.socket %1-ro.socket %1-admin.socket %1-tls.socket %1-tcp.socket}
%define libvirt_systemd_inet_preun() %{expand:%%preun_systemd %1.service %1.socket %1-ro.socket %1-admin.socket %1-tls.socket %1-tcp.socket}

# For daemons with only UNIX sockets and no unprivileged read-only access
%define libvirt_systemd_privileged_posttrans() %{expand:%%post_systemd_postponed %1.service %1.socket %1-admin.socket}
%define libvirt_systemd_privileged_preun() %{expand:%%preun_systemd %1.service %1.socket %1-admin.socket}

%define _localstatedir /var
%define _libexecdir %_prefix/libexec
%define _runtimedir /run
%define qemu_user  _libvirt
%define qemu_group  vmusers

# Locations for QEMU data
%define qemu_moddir %_libdir/qemu
%define qemu_datadir %_datadir/qemu

%def_enable server_drivers

# Always build with dlopen'd modules
%def_with driver_modules

# First the daemon itself
%def_with libvirtd

# Then the hypervisor drivers that run on local host
%def_with qemu
%def_with openvz
%def_with lxc
%if_with lxc
%def_with login_shell
%else
%def_without login_shell
%endif
%ifarch %ix86 x86_64
%def_with vbox
%else
%def_without vbox
%endif
%def_without libxl
%ifarch %ix86 x86_64
%def_with vmware
%else
%def_without vmware
%endif

# Then the hypervisor drivers that talk via a native remote protocol
%ifarch %ix86 x86_64
%def_with esx
%else
%def_without esx
%endif
%def_without hyperv

# Then the secondary host drivers
%def_with network
%def_with storage_fs
%def_with storage_lvm
%def_with storage_scsi
%def_with storage_iscsi
%def_with storage_iscsi_direct
%def_with storage_disk
%ifarch x86_64 aarch64 ppc64le loongarch64
%def_with storage_rbd
%else
%def_without storage_rbd
%endif
%def_with storage_mpath
%ifarch %ix86 %arm %mips32 ppc riscv64
%def_without storage_gluster
%else
%def_with storage_gluster
%endif
%def_with storage_zfs
%def_without storage_vstorage
%ifarch %ix86 x86_64 ppc64le aarch64 s390x loongarch64
%def_with numactl
%else
%def_without numactl
%endif
%def_with selinux
%define selinux_mount "/sys/fs/selinux"

# A few optional bits
%def_without netcf
%def_with udev
%def_with yajl
%def_with sanlock
%if_with lxc
%def_with fuse
%else
%def_without fuse
%endif
%def_without pm_utils


%if_with  qemu
%def_with qemu_tcg
%def_with libnbd
%ifarch %ix86 x86_64 armh aarch64 ppc64le loongarch64
%def_with qemu_kvm
%endif
%endif

# A few optional bits
%def_with polkit
%def_with capng
%def_with firewalld
%def_with firewalld_zone

%if_with qemu || lxc
%def_with nwfilter
%def_with libpcap
%else
%def_without nwfilter
%def_without libpcap
%endif

%def_with libnl
%def_with audit
%def_without dtrace

# Non-server/HV driver defaults which are always enabled
%def_with sasl
%def_with libssh
%def_with libssh2
%def_with ssh_proxy

%def_without wireshark

# nss plugin depends on network
%if_with network
%def_with nss
%else
%def_without nss
%endif

# TODO: switch to modular daemons
%if "%_priority_distbranch" == "p10"
%def_without modular_daemons
%define rootprefix /
%define firewall_backend_priority iptables,nftables
%def_without nftables
%else
%def_with modular_daemons
%define rootprefix %_prefix
%define firewall_backend_priority nftables,iptables
%def_with nftables
%endif

Name: libvirt
Version: 10.7.0
Release: alt1
Summary: Library providing a simple API virtualization
License: GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND OFL-1.1
Group: System/Libraries
Url: https://libvirt.org/
Source0: %name-%version.tar
Source2: keycodemapdb-%name-%version.tar

Source10: libvirt.dm-mod.modules
Source11: libvirtd.init
Source12: virtlockd.init
Source13: virtlogd.init
Source14: libvirt-guests.init

Patch1: %name-%version.patch
Patch2: 0001-Add-Vitastor-support.patch

%{?_with_libvirtd:Requires: %name-daemon = %EVR}
%{?_with_network:Requires: %name-daemon-config-network = %EVR}
%{?_with_nwfilter:Requires: %name-daemon-config-nwfilter = %EVR}
%{?_with_qemu:Requires: %name-qemu-common = %EVR %name-client-qemu = %EVR}
%{?_with_polkit:Requires: polkit}
Requires: %name-client = %EVR
Requires: %name-libs = %EVR

BuildRequires(pre): meson >= 0.56.0
%{?_with_libxl:BuildRequires: xen-devel}
%{?_with_udev:BuildRequires: udev libudev-devel >= 219 libpciaccess-devel}
%{?_with_yajl:BuildRequires: libyajl-devel >= 2.0.1}
%{?_with_sanlock:BuildRequires: sanlock-devel >= 1.8}
%{?_with_libpcap:BuildRequires: libpcap-devel >= 1.5.0}
%{?_with_libnl:BuildRequires: libnl-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}
%{?_with_sasl:BuildRequires: libsasl2-devel >= 2.1.6}
%{?_with_libssh:BuildRequires: pkgconfig(libssh) >= 0.8.1}
%{?_with_libssh2:BuildRequires: pkgconfig(libssh2) >= 1.3}
%{?_with_polkit:BuildRequires: polkit}
%{?_with_storage_fs:BuildRequires: util-linux}
%{?_with_qemu:BuildRequires: qemu-img}
%{?_with_storage_lvm:BuildRequires: lvm2}
%{?_with_storage_disk:BuildRequires: libparted-devel parted libuuid-devel dmsetup libdevmapper-devel}
%{?_with_storage_rbd:BuildRequires: ceph-devel}
%{?_with_storage_iscsi:BuildRequires: open-iscsi}
%{?_with_storage_iscsi_direct:BuildRequires: libiscsi-devel >= 1.18.0}
%{?_with_storage_mpath:BuildRequires: libdevmapper-devel}
%{?_with_storage_gluster:BuildRequires: libglusterfs-devel}
%{?_with_numactl:BuildRequires: libnuma-devel >= 2.0.6}
%{?_with_capng:BuildRequires: libcap-ng-devel}
%{?_with_netcf:BuildRequires: netcf-devel >= 0.1.8}
%{?_with_esx:BuildRequires: libcurl-devel >= 7.19.1}
%{?_with_hyperv:BuildRequires: libwsman-devel >= 2.6.3}
%{?_with_audit:BuildRequires: libaudit-devel}
%{?_with_fuse:BuildRequires: libfuse-devel >= 2.8.6}
%{?_with_libnbd:BuildRequires: libnbd-devel}
%{?_with_pm_utils:BuildRequires: pm-utils}
%{?_with_wireshark:BuildRequires: glib2-devel wireshark tshark wireshark-devel >= 2.1.0}
BuildRequires: pkgconfig(bash-completion) >= 2.0

BuildRequires: /proc
BuildRequires: libblkid-devel
BuildRequires: libgcrypt-devel libgnutls-devel >= 3.2.0 libp11-kit-devel
BuildRequires: libreadline-devel
BuildRequires: libtasn1-devel
BuildRequires: libattr-devel attr
BuildRequires: libacl-devel
BuildRequires: glib2-devel >= 2.58 libgio-devel
BuildRequires: libxml2-devel xml-utils xsltproc
BuildRequires: python3 python3-devel python3-module-pytest
BuildRequires: python3-module-docutils
BuildRequires: zlib-devel
BuildRequires: iproute2
BuildRequires: dmidecode
#BuildRequires: augeas
BuildRequires: libtirpc-devel
BuildRequires: glibc-utils
BuildRequires: kmod
BuildRequires: mdevctl

%description
Libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes).
The main package includes the libvirtd server exporting the virtualization support.

%package docs
Summary: Documentation for libvirt library and daemon
Group: Development/Documentation
BuildArch: noarch

%description docs
Copy of the libvirt website documentation

%package daemon
Summary: Server side daemon and supporting files for libvirt library
Group: System/Servers
Requires: %name-libs = %EVR
Requires: %name-daemon-common = %EVR
Requires: %name-daemon-lock = %EVR
Requires: %name-daemon-plugin-lockd = %EVR
Requires: %name-daemon-log = %EVR
Requires: %name-daemon-proxy = %EVR

%description daemon
Server side daemon required to manage the virtualization capabilities
of recent versions of Linux. Requires a hypervisor specific sub-RPM
for specific drivers.

%package daemon-common
Summary: Files and utilities used by daemons
Group: System/Servers
Requires: %name-libs = %EVR
Requires: iproute2
%{?_with_pm_utils:Requires: pm-utils}
%ifarch %ix86 x86_64
Requires: dmidecode
%endif
# libvirtd depends on 'messagebus' service
Requires: dbus
Requires: nc
# Needed for /usr/libexec/libvirt-guests.sh script.
Requires: gettext
Obsoletes: %name-admin < 7.3.0
Provides: %name-admin = %EVR
Obsoletes: bash-completion-%name < 7.3.0

%description daemon-common
Miscellaneous files and utilities used by other libvirt daemons

%package daemon-lock
Summary: Server side daemon for managing locks
Group: System/Servers
Requires: %name-libs = %EVR
 
%description daemon-lock
Server side daemon used to manage locks held against virtual machine
resources
 
%package daemon-plugin-lockd
Summary: lockd client plugin for virtlockd
Group: System/Servers
Requires: %name-libs = %EVR
Requires: %name-daemon-lock = %EVR
 
%description daemon-plugin-lockd
A client-side plugin that implements disk locking using POSIX fcntl advisory
locks via communication with the virtlockd daemon
 
%package daemon-log
Summary: Server side daemon for managing logs
Group: System/Servers
Requires: %name-libs = %EVR
 
%description daemon-log
Server side daemon used to manage logs from virtual machine consoles
 
%package daemon-proxy
Summary: Server side daemon providing libvirtd proxy
Group: System/Servers
Requires: %name-libs = %EVR

%description daemon-proxy
Server side daemon providing functionality previously provided by
the monolithic libvirtd

%package daemon-config-network
Summary: Default configuration files for the libvirtd daemon
Group: System/Servers
BuildArch: noarch
%if_with driver_modules
Requires: %name-daemon-driver-network = %EVR
%endif

%description daemon-config-network
Default configuration files for setting up NAT based networking

%package daemon-config-nwfilter
Summary: Network filter configuration files for the libvirtd daemon
Group: System/Servers
BuildArch: noarch
%if_with driver_modules
Requires: %name-daemon-driver-nwfilter = %EVR
%endif

%description daemon-config-nwfilter
Network filter configuration files for cleaning guest traffic

%package daemon-driver-network
Summary: Network driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-common = %EVR
Requires: dnsmasq
%if_with nftables
Requires: nftables
%else
Requires: iptables iptables-nft iptables-ipv6
%endif

%description daemon-driver-network
The network driver plugin for the libvirtd daemon, providing
an implementation of the virtual network APIs using the Linux
bridge capabilities.

%package daemon-driver-nwfilter
Summary: Nwfilter driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: ebtables
Requires: iptables iptables-nft iptables-ipv6
Requires: %name-daemon-common = %EVR

%description daemon-driver-nwfilter
The nwfilter driver plugin for the libvirtd daemon, providing
an implementation of the firewall APIs using the ebtables,
iptables and ip6tables capabilities

%package daemon-driver-nodedev
Summary: Nodedev driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-common = %EVR
Requires: mdevctl

%description daemon-driver-nodedev
The nodedev driver plugin for the libvirtd daemon, providing
an implementation of the node device APIs using the udev
capabilities.

%package daemon-driver-interface
Summary: Interface driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-common = %EVR

%description daemon-driver-interface
The interface driver plugin for the libvirtd daemon, providing
an implementation of the network interface APIs using the
netcf library or udev.

%package daemon-driver-secret
Summary: Secret driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-common = %EVR

%description daemon-driver-secret
The secret driver plugin for the libvirtd daemon, providing
an implementation of the secret key APIs.

%package daemon-driver-storage
Summary: Storage driver plugin including all backends for the libvirtd daemon
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
%if_with storage_fs
Requires: %name-daemon-driver-storage-fs = %EVR
%endif
%if_with storage_disk
Requires: %name-daemon-driver-storage-disk = %EVR
%endif
%if_with storage_lvm
Requires: %name-daemon-driver-storage-logical = %EVR
%endif
%if_with storage_scsi
Requires: %name-daemon-driver-storage-scsi = %EVR
%endif
%if_with storage_iscsi
Requires: %name-daemon-driver-storage-iscsi = %EVR
%endif
%if_with storage_iscsi_direct
Requires: %name-daemon-driver-storage-iscsi-direct = %EVR
%endif
%if_with storage_mpath
Requires: %name-daemon-driver-storage-mpath = %EVR
%endif
%if_with storage_gluster
Requires: %name-daemon-driver-storage-gluster = %EVR
%endif
%if_with storage_rbd
Requires: %name-daemon-driver-storage-rbd = %EVR
%endif

%description daemon-driver-storage
The storage driver plugin for the libvirtd daemon, providing
an implementation of the storage APIs using files, local disks, LVM, SCSI,
iSCSI, and multipath storage.

%package daemon-driver-storage-core
Summary: Storage driver plugin including base backends for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-common = %EVR
Requires: nfs-utils
# For mkfs
Requires: util-linux
Requires: scrub
%{?_with qemu:Requires: %_bindir/qemu-img}

%description daemon-driver-storage-core
The storage driver plugin for the libvirtd daemon, providing
an implementation of the storage APIs.

%package daemon-driver-storage-fs
Summary: Storage driver plugin for fs
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-fs
The storage driver backend adding implementation of the storage APIs for block
volumes using fs.

%package daemon-driver-storage-logical
Summary: Storage driver plugin for lvm volumes
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: lvm2

%description daemon-driver-storage-logical
The storage driver backend adding implementation of the storage APIs for block
volumes using lvm.

%package daemon-driver-storage-disk
Summary: Storage driver plugin for disk
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: parted
Requires: dmsetup

%description daemon-driver-storage-disk
The storage driver backend adding implementation of the storage APIs for block
volumes using the host disks.

%package daemon-driver-storage-scsi
Summary: Storage driver plugin for local scsi devices
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-scsi
The storage driver backend adding implementation of the storage APIs for scsi
host devices.

%package daemon-driver-storage-iscsi
Summary: Storage driver plugin for iscsi
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: iscsi-initiator-utils

%description daemon-driver-storage-iscsi
The storage driver backend adding implementation of the storage APIs for iscsi
volumes using the host iscsi stack.

%package daemon-driver-storage-iscsi-direct
Summary: Storage driver plugin for iscsi-direct
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-iscsi-direct
The storage driver backend adding implementation of the storage APIs for iscsi
volumes using libiscsi direct connection.

%package daemon-driver-storage-mpath
Summary: Storage driver plugin for multipath volumes
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: dmsetup
Requires: multipath-tools

%description daemon-driver-storage-mpath
The storage driver backend adding implementation of the storage APIs for
multipath storage using device mapper.

%package daemon-driver-storage-gluster
Summary: Storage driver plugin for gluster
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: glusterfs-client
Requires: /usr/sbin/gluster

%description daemon-driver-storage-gluster
The storage driver backend adding implementation of the storage APIs for gluster
volumes using libgfapi.

%package daemon-driver-storage-rbd
Summary: Storage driver plugin for rbd
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-rbd
The storage driver backend adding implementation of the storage APIs for rbd
volumes using the ceph protocol.

%package daemon-driver-storage-zfs
Summary: Storage driver plugin for zfs
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: zfs-utils

%description daemon-driver-storage-zfs
The storage driver backend adding implementation of the storage APIs for
zfs volumes using.

%package daemon-driver-qemu
Summary: Qemu driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-driver-network = %EVR
Requires: %name-daemon-driver-storage-fs = %EVR
Requires: %name-daemon-log = %EVR
Requires: %_bindir/qemu-img
Requires: qemu-kvm-core >= 5.2.0
# For image compression
Requires: gzip
Requires: bzip2
Requires: lzop
Requires: xz
Requires: zstd
Requires: systemd-container
Requires: swtpm-tools
Requires: passt
# Requires: nbdkit

%description daemon-driver-qemu
The qemu driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
QEMU

%package daemon-driver-lxc
Summary: LXC driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-driver-network = %EVR
Requires: %name-daemon-common = %EVR
Requires: systemd-container

%description daemon-driver-lxc
The LXC driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
the Linux kernel

%package daemon-driver-libxl
Summary: Libxl driver plugin for the libvirtd daemon
Group: System/Libraries
Obsoletes: %name-daemon-driver-xen < 4.3.0
Requires: %name-daemon-common = %EVR

%description daemon-driver-libxl
The Libxl driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
Libxl

%package daemon-driver-vbox
Summary: VirtualBox driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-common = %EVR

%description daemon-driver-vbox
The vbox driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
VirtualBox

%package qemu-common
Summary: Server side daemon, driver & default configs required to run QEMU or KVM guests
Group: System/Servers
BuildArch: noarch
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
Requires: %name-daemon-log = %EVR
Requires: %name-daemon-lock = %EVR
Requires: %name-daemon-plugin-lockd = %EVR
Requires: %name-daemon-proxy = %EVR
%if_with driver_modules
Requires: %name-daemon-driver-qemu = %EVR
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage-fs = %EVR
Requires: %name-daemon-driver-interface = %EVR
%endif
%if_with ssh_proxy
Requires: %name-ssh-proxy = %EVR
%endif

%description qemu-common
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of QEMU or KVM.

%package qemu
Summary: Server side daemon, driver & default configs required to run QEMU guests
Group: System/Servers
BuildArch: noarch
Requires: %name-qemu-common = %EVR
Requires: qemu

%description qemu
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of QEMU.

%package kvm
Summary: Server side daemon, driver & default configs required to run KVM guests
Group: System/Servers
BuildArch: noarch
Requires: %name-qemu-common = %EVR
Requires: qemu-kvm

%description kvm
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of KVM.

%package lxc
Summary: Server side daemon, driver & default configs required to run LXC guests
Group: System/Servers
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
Requires: %name-daemon-proxy = %EVR
Requires: lxc
%if_with driver_modules
Requires: %name-daemon-driver-lxc = %EVR
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage = %EVR
%endif

%description lxc
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of LXC.

%package xen
Summary: Server side daemon, driver & default configs required to run XEN guests
Group: System/Servers
BuildArch: noarch
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
Requires: %name-daemon-proxy = %EVR
Requires: xen
%if_with driver_modules
%if_with libxl
Requires: %name-daemon-driver-libxl = %EVR
%endif
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage = %EVR
%endif #driver_modules

%description xen
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of Xen.

%package vbox
Summary: Server side daemon, driver & default configs required to run VirtualBox guests
Group: System/Servers
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
Requires: %name-daemon-proxy = %EVR
%if_with driver_modules
Requires: %name-daemon-driver-vbox = %EVR
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage = %EVR
%endif

%description vbox
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of VirtualBox.

%package client
Summary: Client side utilities of the libvirt library
Group: System/Libraries
Requires: %name-libs = %EVR
Obsoletes: bash-completion-%name < 6.7.0
# Needed for probing the power management features of the host.
Conflicts: %name < 0.9.11

%description client
The client binaries needed to access the virtualization
capabilities of recent versions of Linux (and other OSes).

%package client-qemu
Summary: Additional client side utilities for QEMU
Group: System/Libraries
Requires: %name-libs = %EVR
Requires: python3-module-libvirt >= 3.7.0
Requires: python3-module-cryptography
Requires: python3-module-lxml

%description client-qemu
The additional client binaries are used to interact
with some QEMU specific features of libvirt.

%package libs
Summary: Client side libraries
Group: System/Libraries
# So remote clients can access libvirt over SSH tunnel
# (client invokes 'nc' against the UNIX socket on the server)
Requires: /etc/sasl2
Requires: libsasl2-plugin-gssapi

%description libs
Shared libraries for accessing the libvirt daemon.

%package -n wireshark-plugin-%name
Summary: Wireshark dissector plugin for libvirt RPC transactions
Group: Networking/Other
Requires: wireshark
Requires: %name-libs = %EVR

%description -n wireshark-plugin-%name
Wireshark dissector plugin for better analysis of libvirt RPC traffic.

%package login-shell
Summary: Login shell for connecting users to an LXC container
Group: System/Libraries
Requires: %name-libs = %EVR

%description login-shell
Provides the set-uid virt-login-shell binary that is used to
connect a user to an LXC container when they login, by switching
namespaces.

%package devel
Summary: Libraries, includes, etc. to compile with the libvirt library
Group: Development/C
Requires: %name-libs = %EVR

%description devel
Includes and documentations for the C library providing an API to use
the virtualization capabilities of recent versions of Linux (and other OSes).

%package daemon-plugin-sanlock
Summary: Sanlock lock manager plugin for QEMU driver
Group: System/Libraries
Requires: sanlock >= 2.4
#for virt-sanlock-cleanup require augeas
Requires: augeas
Requires: %name-libs = %EVR
Obsoletes: %name-lock-sanlock < 10.5.0
Provides: %name-lock-sanlock = %EVR

%description daemon-plugin-sanlock
Includes the Sanlock lock manager plugin for the QEMU
driver

%package -n nss-%name
Summary: Libvirt plugin for Name Service Switch
Group: System/Libraries

%description -n nss-%name
Libvirt plugin for NSS for translating domain names into IP addresses.

%package ssh-proxy
Summary: Libvirt SSH proxy
Group: System/Libraries
Requires: %name-libs = %EVR
 
%description ssh-proxy
Allows SSH into domains via VSOCK without need for network.
 
%prep
%setup
mkdir -p src/keycodemapdb
tar -xf %SOURCE2 -C subprojects/keycodemapdb --strip-components 1

%patch1 -p1
%patch2 -p1

%build
%meson \
    -Drootprefix=%rootprefix \
    -Drpath=disabled \
    -Drunstatedir=%_runtimedir \
    -Dinitconfdir=%_sysconfdir/sysconfig \
    -Dpackager_version="%release" \
    -Dinit_script=systemd \
    -Dunitdir=%_unitdir \
    -Dqemu_user=%qemu_user \
    -Dqemu_group=%qemu_group \
    -Dqemu_moddir=%qemu_moddir \
    -Dqemu_datadir=%qemu_datadir \
%if_with modular_daemons
    -Dremote_default_mode=direct \
%else
    -Dremote_default_mode=legacy \
%endif
%if_with libvirtd
    -Ddriver_libvirtd=enabled \
    -Dhost_validate=enabled \
    -Dinit_script=systemd \
%else
    -Ddriver_libvirtd=disabled \
    -Dhost_validate=disabled \
    -Dinit_script=none \
%endif
    -Ddriver_qemu=%{enabled_ifwith qemu} \
    -Ddriver_openvz=%{enabled_ifwith openvz} \
    -Ddriver_lxc=%{enabled_ifwith lxc} \
    -Dlogin_shell=%{enabled_ifwith login_shell} \
    -Ddriver_vbox=%{enabled_ifwith vbox} \
    -Ddriver_libxl=%{enabled_ifwith libxl} \
    -Ddriver_vmware=%{enabled_ifwith vmware} \
    -Ddriver_esx=%{enabled_ifwith esx} \
    -Ddriver_hyperv=%{enabled_ifwith hyperv} \
    -Ddriver_ch=disabled \
    -Ddriver_network=%{enabled_ifwith network} \
    -Dstorage_fs=%{enabled_ifwith storage_fs} \
    -Dstorage_lvm=%{enabled_ifwith storage_lvm} \
    -Dstorage_iscsi=%{enabled_ifwith storage_iscsi} \
    -Dstorage_iscsi_direct=%{enabled_ifwith storage_iscsi_direct} \
    -Dstorage_scsi=%{enabled_ifwith storage_scsi} \
    -Dstorage_disk=%{enabled_ifwith storage_disk} \
    -Dstorage_rbd=%{enabled_ifwith storage_rbd} \
    -Dstorage_mpath=%{enabled_ifwith storage_mpath} \
    -Dstorage_gluster=%{enabled_ifwith storage_gluster} \
    -Dstorage_zfs=%{enabled_ifwith storage_zfs} \
    -Dstorage_vstorage=%{enabled_ifwith storage_vstorage} \
    -Dnumactl=%{enabled_ifwith numactl} \
    -Dselinux=%{enabled_ifwith selinux} \
%if_with selinux
    -Dselinux_mount=%selinux_mount \
%endif
    -Dnetcf=%{enabled_ifwith netcf} \
    -Dudev=%{enabled_ifwith udev} \
    -Dyajl=%{enabled_ifwith yajl} \
    -Dsanlock=%{enabled_ifwith sanlock} \
    -Dfuse=%{enabled_ifwith fuse} \
    -Dpm_utils=%{enabled_ifwith pm_utils} \
    -Dpolkit=%{enabled_ifwith polkit} \
    -Dfirewalld=%{enabled_ifwith firewalld} \
    -Dfirewalld_zone=%{enabled_ifwith firewalld_zone} \
    -Dfirewall_backend_priority=%{firewall_backend_priority} \
    -Dcapng=%{enabled_ifwith capng} \
    -Dlibpcap=%{enabled_ifwith libpcap} \
    -Dlibssh=%{enabled_ifwith libssh} \
    -Dlibssh2=%{enabled_ifwith libssh2} \
    -Daudit=%{enabled_ifwith audit} \
    -Ddtrace=%{enabled_ifwith dtrace} \
    -Dnss=%{enabled_ifwith nss} \
    -Dssh_proxy=%{enabled_ifwith ssh_proxy} \
    -Dsshconfdir=%_sysconfdir/openssh/ssh_config.d \
    -Dsasl=%{enabled_ifwith sasl} \
    -Ddocs=enabled \
    -Dexpensive_tests=enabled

%meson_build

%install
%meson_install

# Install sysv init scripts
%if_with libvirtd
install -pD -m 755 %SOURCE11  %buildroot%_initdir/libvirtd
install -pD -m 755 %SOURCE12  %buildroot%_initdir/virtlockd
install -pD -m 755 %SOURCE13  %buildroot%_initdir/virtlogd
install -pD -m 755 %SOURCE14  %buildroot%_initdir/libvirt-guests
%else
rm -f %buildroot%_libexecdir/libvirt-guests.sh
%endif

# delete docs
rm -rf %buildroot%_datadir/doc/libvirt

rm -f %buildroot/usr/lib/sysusers.d/libvirt-qemu.conf

%if_with qemu
# We install /etc/libvirt/qemu/networks/autostart/default.xml as ghost
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/autostart/default.xml
touch %buildroot%_sysconfdir/libvirt/qemu/networks/autostart/default.xml
%else
rm -f %buildroot%_datadir/augeas/lenses/libvirtd_qemu.aug
rm -f %buildroot%_datadir/augeas/lenses/tests/test_libvirtd_qemu.aug
rm -f %buildroot%_sysconfdir/libvirt/qemu.conf
rm -f %buildroot%_logrotatedir/libvirtd.qemu
%endif
%if_without lxc
rm -f %buildroot%_datadir/augeas/lenses/libvirtd_lxc.aug
rm -f %buildroot%_datadir/augeas/lenses/tests/test_libvirtd_lxc.aug
rm -f %buildroot%_sysconfdir/libvirt/lxc.conf
rm -f %buildroot%_logrotatedir/libvirtd.lxc
%endif
%if_without nwfilter
rm -rf %buildroot%_sysconfdir/libvirt/nwfilter
%endif
%if_without libxl
rm -f %buildroot%_logrotatedir/libvirtd.libxl
%endif

%if_with nss
# Relocate nss library from %%_libdir/libnss_libvirt.so.* to /%%_lib/libnss_libvirt.so.* .
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/libnss_libvirt.so.* %buildroot/%_lib/
ln -sf ../../%_lib/libnss_libvirt.so.2 %buildroot%_libdir/libnss_libvirt.so
mv %buildroot%_libdir/libnss_libvirt_guest.so.2 %buildroot/%_lib/
ln -sf ../../%_lib/libnss_libvirt_guest.so.2 %buildroot%_libdir/libnss_libvirt_guest.so
%endif

%if_with libvirtd
install -pD -m644 %SOURCE10 %buildroot%_sysconfdir/modules-load.d/libvirt-dm-mod.conf
%endif

%find_lang %name

%check
VIR_TEST_DEBUG=1 %__meson_test --no-suite syntax-check --timeout-multiplier 10

%pre login-shell
groupadd -r -f virtlogin > /dev/null 2>&1 || :

%post daemon
if sd_booted; then
    %libvirt_systemd_inet_posttrans libvirtd
else
    %post_service_posttrans_restart libvirtd
fi
%preun daemon
if sd_booted; then
    %libvirt_systemd_inet_preun libvirtd
else
    %preun_service libvirtd
fi

%preun daemon-common
%preun_service libvirt-guests

%post daemon-lock
if sd_booted; then
    %libvirt_systemd_privileged_posttrans virtlockd
else
    %post_service_posttrans_restart virtlockd
fi
%preun daemon-lock
if sd_booted; then
    %libvirt_systemd_privileged_preun virtlockd
else
    %preun_service virtlockd
fi

%post daemon-log
if sd_booted; then
    %libvirt_systemd_privileged_posttrans virtlogd
else
    %post_service_posttrans_restart virtlogd
fi
%preun daemon-log
if sd_booted; then
    %libvirt_systemd_privileged_preun virtlogd
else
    %preun_service virtlogd
fi

%post daemon-proxy
%libvirt_systemd_inet_posttrans virtproxyd
%preun daemon-proxy
%libvirt_systemd_inet_preun virtproxyd

%post daemon-driver-network
%libvirt_systemd_unix_posttrans virtnetworkd
%preun daemon-driver-network
%libvirt_systemd_unix_preun virtnetworkd

%post daemon-driver-nwfilter
%libvirt_systemd_unix_posttrans virtnwfilterd

%preun daemon-driver-nwfilter
%libvirt_systemd_unix_preun virtnwfilterd

%post daemon-driver-nodedev
%libvirt_systemd_unix_posttrans virtnodedevd
%preun daemon-driver-nodedev
%libvirt_systemd_unix_preun virtnodedevd

%post daemon-driver-interface
%libvirt_systemd_unix_posttrans virtinterfaced
%preun daemon-driver-interface
%libvirt_systemd_unix_preun virtinterfaced

%post daemon-driver-secret
%libvirt_systemd_unix_posttrans virtsecretd
%preun daemon-driver-secret
%libvirt_systemd_unix_preun virtsecretd

%post daemon-driver-storage-core
%libvirt_systemd_unix_posttrans virtstoraged
%preun daemon-driver-storage-core
%libvirt_systemd_unix_preun virtstoraged

%pre daemon-driver-qemu
groupadd -r -f %qemu_group > /dev/null 2>&1 || :
useradd -M -r -d %_localstatedir/lib/%name -s /bin/false -c "libvirt user" -g %qemu_group %qemu_user >/dev/null 2>&1 || :
%post daemon-driver-qemu
%libvirt_systemd_unix_posttrans virtqemud
%preun daemon-driver-qemu
%libvirt_systemd_unix_preun virtqemud

%post daemon-driver-lxc
%libvirt_systemd_unix_posttrans virtlxcd
%preun daemon-driver-lxc
%libvirt_systemd_unix_preun virtlxcd

%post daemon-driver-vbox
%libvirt_systemd_unix_posttrans virtvboxd
%preun daemon-driver-vbox
%libvirt_systemd_unix_preun virtvboxd

%post daemon-driver-libxl
%libvirt_systemd_unix_posttrans virtxend
%preun daemon-driver-libxl
%libvirt_systemd_unix_preun virtxend

%triggerpostun daemon -- %name-daemon < 1.3.0
# In upgrade scenario we must explicitly enable virtlockd/virtlogd
# sockets, if libvirtd is already enabled and start them if
# libvirtd is running, otherwise you'll get failures to start
# guests
if [ $1 -ge 1 ] ; then
    if service libvirtd status; then
        chkconfig virtlogd on && service virtlogd start
        chkconfig virtlockd on && service virtlockd start
    fi
fi

%triggerpostun daemon -- %name-daemon < 8.6.0
%libvirt_sysconfig_rename libvirtd virtproxyd virtlogd virtlockd libvirt-guests

%triggerpostun daemon-driver-network -- %name-daemon-driver-network < 8.6.0
%libvirt_sysconfig_rename virtnetworkd

%triggerpostun daemon-driver-nwfilter -- %name-daemon-driver-nwfilter < 8.6.0
%libvirt_sysconfig_rename virtnwfilterd

%triggerpostun daemon-driver-nodedev -- %name-daemon-driver-nodedev < 8.6.0
%libvirt_sysconfig_rename virtnodedevd

%triggerpostun daemon-driver-interface -- %name-daemon-driver-interface < 8.6.0
%libvirt_sysconfig_rename virtinterfaced

%triggerpostun daemon-driver-secret -- %name-daemon-driver-secret < 8.6.0
%libvirt_sysconfig_rename virtsecretd

%triggerpostun daemon-driver-qemu -- %name-daemon-driver-qemu < 8.6.0
%libvirt_sysconfig_rename virtqemud

%triggerpostun daemon-driver-lxc -- %name-daemon-driver-lxc < 8.6.0
%libvirt_sysconfig_rename virtlxcd

%triggerpostun daemon-driver-vbox -- %name-daemon-driver-vbox < 8.6.0
%libvirt_sysconfig_rename virtvboxd

%triggerpostun daemon-driver-libxl -- %name-daemon-driver-libxl < 8.6.0
%libvirt_sysconfig_rename virtxend

%files

%files docs
%doc NEWS.rst README.rst
%doc docs/*.xml
%doc docs/html

%files client
%_bindir/virsh
%_bindir/virt-xml-validate
%_bindir/virt-pki-query-dn
%_bindir/virt-pki-validate
%_man1dir/virsh.*
%_man1dir/virt-xml-validate.*
%_man1dir/virt-pki-query-dn.*
%_man1dir/virt-pki-validate.*
%_man7dir/virkey*
%_datadir/bash-completion/completions/virsh

%if_with qemu
%files client-qemu
%_man1dir/virt-qemu-qmp-proxy.*
%_man1dir/virt-qemu-sev-validate.1*
%_bindir/virt-qemu-qmp-proxy
%_bindir/virt-qemu-sev-validate
%endif

%files libs -f %name.lang
%doc COPYING COPYING.LESSER
%dir %attr(0700, root, root) %_sysconfdir/libvirt
%config(noreplace) %_sysconfdir/libvirt/libvirt.conf
%config(noreplace) %_sysconfdir/libvirt/libvirt-admin.conf
%_libdir/lib*.so.*
%dir %_datadir/libvirt
%dir %_datadir/libvirt/schemas
%_datadir/libvirt/schemas/*.rng
%_datadir/libvirt/cpu_map
%_datadir/libvirt/test-screenshot.png

%if_with sasl
%config(noreplace) %_sysconfdir/sasl2/libvirt.conf
%endif

%if_with libvirtd
%files daemon
%_unitdir/libvirtd*
%_initdir/libvirtd
%config(noreplace) %_sysconfdir/libvirt/libvirtd.conf
%_sysctldir/60-libvirtd.conf
%config(noreplace) %_logrotatedir/libvirtd
%_datadir/augeas/lenses/libvirtd.aug
%_datadir/augeas/lenses/tests/test_libvirtd.aug
%_sbindir/libvirtd
%_man8dir/libvirtd.*

%files daemon-common
%_unitdir/virt-guest-shutdown.target
%_unitdir/libvirt-guests.service
%_initdir/libvirt-guests
%dir %_datadir/libvirt
%dir %_localstatedir/lib/libvirt
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/images
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/filesystems
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/boot
%dir %attr(0700, root, root) %_localstatedir/cache/libvirt
%dir %_libdir/%name
%dir %_libdir/%name/connection-driver
%dir %_libdir/%name/storage-backend
%dir %_libdir/%name/storage-file
%if_with polkit
%_datadir/polkit-1/actions/org.libvirt.unix.policy
%_datadir/polkit-1/actions/org.libvirt.api.policy
%_datadir/polkit-1/rules.d/50-libvirt.rules
%endif
%dir %attr(0700, root, root) %_logdir/libvirt
%_libexecdir/libvirt_iohelper
%_bindir/virt-ssh-helper
%_libexecdir/libvirt-guests.sh
%_man1dir/virt-admin.1*
%_man1dir/virt-host-validate.*
%_man8dir/virt-ssh-helper.*
%_man8dir/libvirt-guests.*
%_bindir/virt-host-validate
%_bindir/virt-admin
%_datadir/bash-completion/completions/virt-admin

%files daemon-lock
%_unitdir/virtlockd*
%_initdir/virtlockd
%config(noreplace) %_sysconfdir/libvirt/virtlockd.conf
%_datadir/augeas/lenses/virtlockd.aug
%_datadir/augeas/lenses/tests/test_virtlockd.aug
%_sbindir/virtlockd
%_man8dir/virtlockd*

%files daemon-plugin-lockd
%_datadir/augeas/lenses/libvirt_lockd.aug
%_datadir/augeas/lenses/tests/test_libvirt_lockd.aug
%_libdir/%name/lock-driver/lockd.so
%dir %_libdir/libvirt/lock-driver

%files daemon-log
%_unitdir/virtlogd*
%_initdir/virtlogd
%config(noreplace) %_sysconfdir/libvirt/virtlogd.conf
%_datadir/augeas/lenses/virtlogd.aug
%_datadir/augeas/lenses/tests/test_virtlogd.aug
%_sbindir/virtlogd
%_man8dir/virtlogd*

%files daemon-proxy
%_unitdir/virtproxyd*
%config(noreplace) %_sysconfdir/libvirt/virtproxyd.conf
%_datadir/augeas/lenses/virtproxyd.aug
%_datadir/augeas/lenses/tests/test_virtproxyd.aug
%_sbindir/virtproxyd
%_man8dir/virtproxyd.*

%if_with network
%files daemon-config-network
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/networks
%config(noreplace) %attr(0600, root, root) %_sysconfdir/libvirt/qemu/networks/default.xml
%ghost %_sysconfdir/libvirt/qemu/networks/autostart/default.xml
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/networks/autostart
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/network
%dir %attr(0755, root, root) %_localstatedir/lib/libvirt/dnsmasq
%endif

%if_with nwfilter
%files daemon-config-nwfilter
%dir %attr(0700, root, root) %_sysconfdir/libvirt/nwfilter
%config(noreplace) %attr(0600, root, root) %_sysconfdir/libvirt/nwfilter/*.xml
%endif

%if_with driver_modules
%if_with network
%files daemon-driver-network
%config(noreplace) %_sysconfdir/libvirt/virtnetworkd.conf
%_datadir/augeas/lenses/virtnetworkd.aug
%_datadir/augeas/lenses/tests/test_virtnetworkd.aug
%config(noreplace) %_sysconfdir/libvirt/network.conf
%_datadir/augeas/lenses/libvirtd_network.aug
%_datadir/augeas/lenses/tests/test_libvirtd_network.aug
%_unitdir/virtnetworkd*
%_sbindir/virtnetworkd
%_libdir/%name/connection-driver/libvirt_driver_network.so
%_libexecdir/libvirt_leaseshelper
%_man8dir/virtnetworkd.*
%if_with firewalld_zone
%_prefix/lib/firewalld/zones/libvirt.xml
%_prefix/lib/firewalld/zones/libvirt-routed.xml
%_prefix/lib/firewalld/policies/libvirt-routed-in.xml
%_prefix/lib/firewalld/policies/libvirt-routed-out.xml
%_prefix/lib/firewalld/policies/libvirt-to-host.xml
%endif
%endif

%if_with udev
%files daemon-driver-nodedev
%config(noreplace) %_sysconfdir/libvirt/virtnodedevd.conf
%_datadir/augeas/lenses/virtnodedevd.aug
%_datadir/augeas/lenses/tests/test_virtnodedevd.aug
%_unitdir/virtnodedevd*
%_sbindir/virtnodedevd
%_libdir/%name/connection-driver/libvirt_driver_nodedev.so
%_man8dir/virtnodedevd.*

%files daemon-driver-interface
%config(noreplace) %_sysconfdir/libvirt/virtinterfaced.conf
%_datadir/augeas/lenses/virtinterfaced.aug
%_datadir/augeas/lenses/tests/test_virtinterfaced.aug
%_unitdir/virtinterfaced*
%_sbindir/virtinterfaced
%_libdir/%name/connection-driver/libvirt_driver_interface.so
%_man8dir/virtinterfaced.8*
%endif #if_with udev

%if_with nwfilter
%files daemon-driver-nwfilter
%config(noreplace) %_sysconfdir/libvirt/virtnwfilterd.conf
%_datadir/augeas/lenses/virtnwfilterd.aug
%_datadir/augeas/lenses/tests/test_virtnwfilterd.aug
%_unitdir/virtnwfilterd*
%_sbindir/virtnwfilterd
%_libdir/%name/connection-driver/libvirt_driver_nwfilter.so
%_man8dir/virtnwfilterd.*
%endif

%files daemon-driver-secret
%config(noreplace) %_sysconfdir/libvirt/virtsecretd.conf
%dir %attr(0700, root, root) %_sysconfdir/libvirt/secrets
%_datadir/augeas/lenses/virtsecretd.aug
%_datadir/augeas/lenses/tests/test_virtsecretd.aug
%_unitdir/virtsecretd*
%_sbindir/virtsecretd
%_libdir/%name/connection-driver/libvirt_driver_secret.so
%_man8dir/virtsecretd.*

%files daemon-driver-storage

%files daemon-driver-storage-core
%config(noreplace) %_sysconfdir/modules-load.d/libvirt-dm-mod.conf
%config(noreplace) %_sysconfdir/libvirt/virtstoraged.conf
%dir %attr(0700, root, root) %_sysconfdir/libvirt/storage
%dir %attr(0700, root, root) %_sysconfdir/libvirt/storage/autostart
%_datadir/augeas/lenses/virtstoraged.aug
%_datadir/augeas/lenses/tests/test_virtstoraged.aug
%_unitdir/virtstoraged*
%_sbindir/virtstoraged
%if_with storage_disk
%_libexecdir/libvirt_parthelper
%endif
%_libdir/%name/connection-driver/libvirt_driver_storage.so
%_libdir/%name/storage-file/libvirt_storage_file_fs.so
%_man8dir/virtstoraged.*

%if_with storage_fs
%files daemon-driver-storage-fs
%_libdir/%name/storage-backend/libvirt_storage_backend_fs.so
%endif


%if_with storage_disk
%files daemon-driver-storage-disk
%_libdir/%name/storage-backend/libvirt_storage_backend_disk.so
%endif

%if_with storage_lvm
%files daemon-driver-storage-logical
%_libdir/%name/storage-backend/libvirt_storage_backend_logical.so
%endif

%if_with storage_scsi
%files daemon-driver-storage-scsi
%_libdir/%name/storage-backend/libvirt_storage_backend_scsi.so
%endif

%if_with storage_iscsi
%files daemon-driver-storage-iscsi
%_libdir/%name/storage-backend/libvirt_storage_backend_iscsi.so
%endif

%if_with storage_iscsi_direct
%files daemon-driver-storage-iscsi-direct
%_libdir/%name/storage-backend/libvirt_storage_backend_iscsi-direct.so
%endif

%if_with storage_mpath
%files daemon-driver-storage-mpath
%_libdir/%name/storage-backend/libvirt_storage_backend_mpath.so
%endif

%if_with storage_gluster
%files daemon-driver-storage-gluster
%_libdir/%name/storage-backend/libvirt_storage_backend_gluster.so
%_libdir/%name/storage-file/libvirt_storage_file_gluster.so
%endif

%if_with storage_rbd
%files daemon-driver-storage-rbd
%_libdir/%name/storage-backend/libvirt_storage_backend_rbd.so
%endif

%if_with storage_zfs
%files daemon-driver-storage-zfs
%_libdir/%name/storage-backend/libvirt_storage_backend_zfs.so
%endif

%if_with qemu
%files daemon-driver-qemu
%config(noreplace) %_sysconfdir/libvirt/virtqemud.conf
%config(noreplace) %_sysconfdir/libvirt/qemu-lockd.conf
%_sysctldir/60-qemu-postcopy-migration.conf
%_datadir/augeas/lenses/virtqemud.aug
%_datadir/augeas/lenses/tests/test_virtqemud.aug
%_unitdir/virtqemud*
%_sbindir/virtqemud
%_libdir/%name/connection-driver/libvirt_driver_qemu.so
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/autostart
%config(noreplace) %_sysconfdir/libvirt/qemu.conf
%config(noreplace) %_logrotatedir/libvirtd.qemu
%dir %attr(0750, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu
%dir %attr(0751, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu/checkpoint
%dir %attr(0751, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu/dump
%dir %attr(0751, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu/nvram
%dir %attr(0751, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu/ram
%dir %attr(0751, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu/save
%dir %attr(0751, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu/snapshot
%dir %attr(0750, root, root) %_cachedir/libvirt/qemu
%dir %attr(0700, root, root) %_logdir/libvirt/qemu
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/swtpm
%dir %attr(0770, tss, tss) %_logdir/swtpm/libvirt/qemu
%_datadir/augeas/lenses/libvirtd_qemu.aug
%_datadir/augeas/lenses/tests/test_libvirtd_qemu.aug
%_bindir/virt-qemu-run
%_man1dir/virt-qemu-run.*
%_man8dir/virtqemud.*
%endif

%if_with lxc
%files daemon-driver-lxc
%config(noreplace) %_sysconfdir/libvirt/virtlxcd.conf
%dir %attr(0700, root, root) %_sysconfdir/libvirt/lxc
%dir %attr(0700, root, root) %_sysconfdir/libvirt/lxc/autostart
%_datadir/augeas/lenses/virtlxcd.aug
%_datadir/augeas/lenses/tests/test_virtlxcd.aug
%_unitdir/virtlxcd*
%_sbindir/virtlxcd
%_libdir/%name/connection-driver/libvirt_driver_lxc.so
%config(noreplace) %_sysconfdir/libvirt/lxc.conf
%config(noreplace) %_logrotatedir/libvirtd.lxc
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/lxc
%dir %attr(0700, root, root) %_logdir/libvirt/lxc
%_datadir/augeas/lenses/libvirtd_lxc.aug
%_datadir/augeas/lenses/tests/test_libvirtd_lxc.aug
%_libexecdir/libvirt_lxc
%_man8dir/virtlxcd.*
%endif

%if_with libxl
%files daemon-driver-libxl
%config(noreplace) %_sysconfdir/libvirt/virtxend.conf
%dir %attr(0700, root, root) %_sysconfdir/libvirt/libxl
%dir %attr(0700, root, root) %_sysconfdir/libvirt/libxl/autostart
%_datadir/augeas/lenses/virtxend.aug
%_datadir/augeas/lenses/tests/test_virtxend.aug
%_unitdir/virtxend*
%_sbindir/virtxend
%_libdir/%name/connection-driver/libvirt_driver_libxl.so
%dir %attr(0700, root, root) %_logdir/libvirt/libxl
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl/channel
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl/channel/target
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl/dump
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl/save
%config(noreplace) %_sysconfdir/libvirt/libxl*.conf
%config(noreplace) %_logrotatedir/libvirtd.libxl
%_datadir/augeas/lenses/libvirtd_libxl.aug
%_datadir/augeas/lenses/tests/test_libvirtd_libxl.aug
%_man8dir/virtxend.*
%endif

%if_with vbox
%files daemon-driver-vbox
%config(noreplace) %_sysconfdir/libvirt/virtvboxd.conf
%_datadir/augeas/lenses/virtvboxd.aug
%_datadir/augeas/lenses/tests/test_virtvboxd.aug
%_unitdir/virtvboxd*
%_sbindir/virtvboxd
%_libdir/%name/connection-driver/libvirt_driver_vbox.so
%_man8dir/virtvboxd.*
%endif
%endif #driver_modules

%if_with qemu
%files qemu-common
%if_with qemu_tcg
%files qemu
%endif
%if_with qemu_kvm
%files kvm
%endif

%endif #if_with qemu

%if_with lxc
%files lxc
%endif

%if_with libxl
%files xen
%endif #if_with libxl

%if_with vbox
%files vbox
%endif

%if_with sanlock
%files daemon-plugin-sanlock
%_libdir/libvirt/lock-driver/sanlock.so

%if_with qemu
%config(noreplace) %_sysconfdir/libvirt/qemu-sanlock.conf
%endif

%if_with libxl
%config(noreplace) %_sysconfdir/libvirt/libxl-sanlock.conf
%endif

%_datadir/augeas/lenses/libvirt_sanlock.aug
%_datadir/augeas/lenses/tests/test_libvirt_sanlock.aug
%dir %attr(0770, root, sanlock) %_localstatedir/lib/libvirt/sanlock
%_sbindir/virt-sanlock-cleanup
%_man8dir/virt-sanlock-cleanup.*
%_libexecdir/libvirt_sanlock_helper
%endif #if_with sanlock
%endif #if_with libvirtd

%if_with nss
%files  -n nss-%name
/%_lib/libnss_libvirt.so.*
/%_lib/libnss_libvirt_guest.so.*
%endif

%if_with wireshark
%files -n wireshark-plugin-%name
%_libdir/wireshark/plugins/%name.so
%endif

%if_with lxc
%if_with login_shell
%files login-shell
%config(noreplace) %_sysconfdir/libvirt/virt-login-shell.conf
%attr(4710, root, virtlogin) %_bindir/virt-login-shell
%_libexecdir/virt-login-shell-helper
%_man1dir/virt-login-shell.*
%endif
%endif

%if_with ssh_proxy
%files ssh-proxy
%config(noreplace) %_sysconfdir/openssh/ssh_config.d/30-libvirt-ssh-proxy.conf
%_libexecdir/libvirt-ssh-proxy
%endif



%files devel
%_pkgconfigdir/*.pc
%_libdir/*.so
%_includedir/libvirt
%_datadir/libvirt/api

%changelog
* Thu Sep 26 2024 Alexey Shabalin <shaba@altlinux.org> 10.7.0-alt1
- 10.7.0 (Fixes: CVE-2024-8235)

* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 10.6.0-alt1
- 10.6.0

* Thu Jul 11 2024 Alexey Shabalin <shaba@altlinux.org> 10.5.0-alt1
- 10.5.0 (Fixes: CVE-2024-4418)
- Add ssh-proxy, daemon-common, daemon-lock, daemon-log packages
- Rename lock-sanlock to daemon-plugin-sanlock
- Build with modular_daemons on p11 and sisyphus
- Update requires

* Mon Apr 08 2024 Alexey Shabalin <shaba@altlinux.org> 10.2.0-alt1
- 10.2.0 (Fixes: CVE-2024-1441)

* Thu Mar 21 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 9.8.0-alt5
- Check for negative array lengths before allocation (Fixes: CVE-2024-2494)

* Tue Mar 04 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 9.8.0-alt4
- Fix off-by-one error in udevListInterfacesByStatus (Fixes: CVE-2024-1441)

* Tue Feb 27 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 9.8.0-alt3
- Added LoongArch support patches based on
  https://gitlab.com/lixianglai/libvirt/-/tree/loongarch
- spec: build libvirt-kvm for LoongArch.

* Sat Dec 02 2023 Ivan A. Melnikov <iv@altlinux.org> 9.8.0-alt2
- Enable server dirvers on loongarch64.

* Wed Oct 18 2023 Alexey Shabalin <shaba@altlinux.org> 9.8.0-alt1
- 9.8.0
- Build with nbdkit.
- Add requires libvirt-client-qemu to main package.
- Drop tmpfiles config (and fixed perm to swtpm runtime dir ALT#47442).
- Update vitastor support patch.

* Wed Sep 06 2023 Alexey Shabalin <shaba@altlinux.org> 9.7.0-alt2
- Add patch for vitastor support.

* Tue Sep 05 2023 Alexey Shabalin <shaba@altlinux.org> 9.7.0-alt1
- 9.7.0

* Tue Sep 05 2023 Alexey Shabalin <shaba@altlinux.org> 9.6.0-alt2
- Update Requires, add R:swtpm-tools to daemon-driver-qemu (ALT#47442)

* Wed Aug 30 2023 Alexey Shabalin <shaba@altlinux.org> 9.6.0-alt1
- 9.6.0 (Fixes: CVE-2023-3750)
- Disabled support glusterfs for 32-bit arches and riscv64.

* Tue May 16 2023 Alexey Shabalin <shaba@altlinux.org> 9.3.0-alt1
- 9.3.0

* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 9.0.0-alt1
- 9.0.0

* Tue Nov 15 2022 Alexey Shabalin <shaba@altlinux.org> 8.9.0-alt1
- 8.9.0

* Wed Oct 05 2022 Alexey Shabalin <shaba@altlinux.org> 8.8.0-alt1
- 8.8.0

* Fri Aug 12 2022 Ivan A. Melnikov <iv@altlinux.org> 8.6.0-alt2
- Fix build w/o server_drivers

* Thu Aug 11 2022 Alexey Shabalin <shaba@altlinux.org> 8.6.0-alt1
- 8.6.0

* Tue Feb 01 2022 Michael Shigorin <mike@altlinux.org> 8.0.0-alt3
- moved virt-pki-query-dn(1) to appropriate subpackage

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 8.0.0-alt2
- Add requires on iptables-nft to daemon package

* Fri Jan 21 2022 Alexey Shabalin <shaba@altlinux.org> 8.0.0-alt1
- 8.0.0 (Fixes: CVE-2021-4147)

* Fri Dec 17 2021 Alexey Shabalin <shaba@altlinux.org> 7.10.0-alt1
- 7.10.0

* Wed Nov 17 2021 Alexey Shabalin <shaba@altlinux.org> 7.9.0-alt1
- 7.9.0

* Thu Sep 02 2021 Alexey Shabalin <shaba@altlinux.org> 7.7.0-alt1
- 7.7.0 (Fixes: CVE-2021-3667, CVE-2021-3631)

* Tue Jun 15 2021 Alexey Shabalin <shaba@altlinux.org> 7.4.0-alt1
- 7.4.0

* Wed Jun 09 2021 Ivan A. Melnikov <iv@altlinux.org> 7.3.0-alt2
- Fix build without server_drivers, again.
- Package virt-admin separately.

* Wed May 05 2021 Alexey Shabalin <shaba@altlinux.org> 7.3.0-alt1
- 7.3.0
- Merge libvirt-admin package into libvirt-daemon.
- Move libvirt-guests script, init and unit from libvirt-client to libvirt-daemon.
- Move virt-host-validate from libvirt-client to libvirt-daemon.
- Add test-screenshot.png for tests in python package.

* Tue Apr 06 2021 Alexey Shabalin <shaba@altlinux.org> 7.2.0-alt1
- 7.2.0

* Wed Mar 10 2021 Alexey Shabalin <shaba@altlinux.org> 7.1.0-alt1
- 7.1.0

* Wed Feb 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.0-alt2
- add more Kunpeng920 features and tests

* Mon Jan 18 2021 Alexey Shabalin <shaba@altlinux.org> 7.0.0-alt1
- 7.0.0

* Sun Dec 27 2020 Alexey Shabalin <shaba@altlinux.org> 6.10.0-alt3
- Drop obsoleted nvram option in qemu.conf.

* Mon Dec 21 2020 Alexey Shabalin <shaba@altlinux.org> 6.10.0-alt2
- fixed rebuild

* Fri Dec 04 2020 Alexey Shabalin <shaba@altlinux.org> 6.10.0-alt1
- 6.10.0

* Fri Oct 09 2020 Alexey Shabalin <shaba@altlinux.org> 6.8.0-alt1
- 6.8.0 (Fixes: CVE-2020-15708, CVE-2020-25637)

* Tue Sep 08 2020 Alexey Shabalin <shaba@altlinux.org> 6.7.0-alt2
- fix rpm filetrigger

* Mon Sep 07 2020 Alexey Shabalin <shaba@altlinux.org> 6.7.0-alt1
- 6.7.0
- build with firewalld_zone
- build with libssh2
- package bash completion to libvirt-client
- build without pm-utils (not used if build with dbus and systemd)
- add dm-mod kernel module to autoload

* Mon Aug 10 2020 Alexey Shabalin <shaba@altlinux.org> 6.6.0-alt1
- 6.6.0 (Fixes: CVE-2020-14339)

* Fri Jul 10 2020 Alexey Shabalin <shaba@altlinux.org> 6.5.0-alt1
- 6.5.0

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 6.3.0-alt1
- 6.3.0

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.0-alt2
- drop requires on bridge-utils

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.0-alt1
- 6.2.0

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 6.1.0-alt1
- 6.1.0

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt2
- use glusterfs without version

* Fri Jan 24 2020 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- 6.0.0

* Mon Dec 16 2019 Alexey Shabalin <shaba@altlinux.org> 5.10.0-alt1
- 5.10.0

* Mon Oct 14 2019 Alexey Shabalin <shaba@altlinux.org> 5.8.0-alt1
- 5.8.0

* Mon Sep 09 2019 Alexey Shabalin <shaba@altlinux.org> 5.7.0-alt1
- 5.7.0

* Mon Aug 19 2019 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt1
- 5.6.0

* Thu Jul 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.5.0-alt1
- 5.5.0 (Fixes: CVE-2019-10161, CVE-2019-10166, CVE-2019-10167, CVE-2019-10168)
- build with glusterfs6

* Wed Jun 05 2019 Ivan A. Melnikov <iv@altlinux.org> 5.4.0-alt3
- fix build without server_drivers

* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.0-alt2
- move files of qemu,lxc,xen to daemon drivers

* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.0-alt1
- 5.4.0 (Fixes: CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091, CVE-2019-10132)

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0

* Thu Mar 14 2019 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- 5.1.0
- fix build without server_drivers (ALT#36248)

* Thu Jan 31 2019 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- 5.0.0

* Wed Jan 02 2019 Alexey Shabalin <shaba@altlinux.org> 4.10.0-alt1
- 4.10.0

* Thu Nov 29 2018 Alexey Shabalin <shaba@altlinux.org> 4.9.0-alt1
- 4.9.0
- add requires qemu-kvm-core to libvirt-daemon-driver-qemu (ALT#33801)

* Tue Oct 09 2018 Alexey Shabalin <shaba@altlinux.org> 4.8.0-alt1
- 4.8.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.7.0-alt1
- 4.7.0
- add daemon-driver-storage-iscsi-direct package
  (instead of unsing iscsiadm, it uses libiscsi)

* Sat Aug 11 2018 Alexey Shabalin <shaba@altlinux.org> 4.6.0-alt1
- 4.6.0
- build with ceph storage support only for x86_64 and aarch64

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 4.5.0-alt1
- 4.5.0
- not install zfs storage support by default

* Tue Jun 05 2018 Alexey Shabalin <shaba@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Mon Jun 04 2018 Alexey Shabalin <shaba@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Sun Apr 01 2018 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1
- 4.2.0 (Fixes: CVE-2018-5748)
- Use Python 3 for building
- fix package login-shell

* Fri Mar 09 2018 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0 (Fixes: CVE-2018-6764, CVE-2017-5715)

* Fri Feb 02 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt2
- enabled server part on arm arches

* Sat Jan 27 2018 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1
- 4.0.0 (Fixes: CVE-2018-5748)
- add filetrigger that restart libvirtd after install any plugin

* Fri Dec 08 2017 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0 (Fixes: CVE-2017-1000256)

* Mon Sep 04 2017 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Tue Jul 11 2017 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt2
- backport fixes from upstream master (ALT#33413)

* Thu Apr 13 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0
- check running messagebus service before run libvirtd(ALT#32479)

* Fri Mar 10 2017 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt2
- update R: for qemu-common

* Thu Mar 09 2017 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt1
- 3.1.0
- split libvirt-daemon-driver-storage to subpackages

* Wed Feb 15 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt2
- added patches from upstream to fix work with lvm

* Fri Jan 27 2017 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt2
- add new path to edk2 uefi nvram

* Wed Dec 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt2
- libvirt-daemon must will update after all subpackes for restart successfuly

* Sat Nov 05 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Oct 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2
- add requires dmidecode to daemon package
- drop generate host_uuid in post_install, default host_uuid_source = smbios

* Fri Oct 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Aug 23 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0
- build with sanlock
- move libs from libvirt-client to lilbvirt-libs
- add new subpackages:
  + libvirt-libs
  + libvirt-admin
  + libvirt-shell
  + libvirt-nss
  + libvirt-lock-sanlock

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Jun 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5 release

* Mon May 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt0.rc1
- 1.3.5-rc1

* Fri May 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4
- build without xen support

* Tue Apr 05 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt3
- fixed typo in trigger

* Fri Mar 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt2
- add Requires dnsmasq, but disable autostart default network
- add Requires dbus to libvirt-daemon
- backport some patches from upstream

* Mon Mar 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2
- build with zfs support

* Fri Dec 18 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- fixed CVE-2015-5313

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.21-alt1
- 1.2.21

* Thu Oct 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.20-alt1
- 1.2.20
- fixed CVE-2015-5247

* Tue Aug 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.18-alt1
- 1.2.18

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.16-alt2
- update OVMF nvram path

* Fri Jun 19 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.16-alt1
- 1.2.16
- build with firewalld support
- allow password-less access with polkit for 'vmusers' group
- define default OVMF nvram path

* Tue May 05 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.15-alt1
- 1.2.15
- build with glusterfs support

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.14-alt1
- 1.2.14

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.13-alt1
- 1.2.13

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.12-alt1
- 1.2.12
- fixed CVE-2015-0236

* Thu Dec 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.11-alt1
- 1.2.11
- fixed CVE-2014-7823,CVE-2014-8135,CVE-2014-8136,CVE-2014-8131

* Fri Nov 07 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Tue Oct 21 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.9-alt2
- rebuild with parted-3.2-alt1

* Fri Oct 03 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.9-alt1
- 1.2.9
- fixed CVE-2014-3633, CVE-2014-3657

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Wed Aug 06 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Fri Jul 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Mon Jun 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Apr 01 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- 1.2.3
- build with libxl

* Wed Mar 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- 1.2.2
- fixed CVE-2013-6436, CVE-2013-6456, CVE-2013-6457, CVE-2013-6458, CVE-2014-1447, CVE-2014-0028
- add wireshark-plugin-libvirt package, but disabled now

* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0
- drop python module package

* Wed Nov 06 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4
- fixed CVE-2013-4400, CVE-2013-4401

* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.3-alt1
- 1.1.3
- fixed CVE-2013-4297, CVE-2013-4311, CVE-2013-4296

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.2-alt1
- 1.1.2
- fixed CVE-2013-4291, CVE-2013-4292, CVE-2013-5651

* Mon Aug 26 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt2
- snapshot of v1.1.1-maint branch (fixed CVE-2013-4239)

* Thu Aug 08 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1
- fixed CVE-2013-2230, CVE-2013-4153, CVE-2013-4154

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- v1.1.0-maint branch
- add vbox subpackages

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.5.1-alt1
- 1.0.5.1

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Tue Apr 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt2
- add workaround for paranoid permitions of dnsmasq

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4
- add patches from v1.0.4-maint

* Wed Mar 13 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3 release

* Fri Mar 01 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt0.1.rc2
- upstream snapshot

* Wed Feb 20 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Nov 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- build libvirt-daemon-driver-interface package

* Tue Nov 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- drop local systemd unit files, use upstream
- move tmpfiles to /lib

* Mon Oct 29 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.2.1-alt1
- 0.10.2.1

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Wed Jul 18 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.13-alt1
- 0.9.13
- build drivers as loadable modules; split driver packages
- add storage backend RBD (RADOS Block Device) support

* Thu May 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Wed May 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11.3-alt1
- 0.9.11.3

* Wed Apr 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt4
- fix update: add "Conflicts: libvirt < 0.9.11" to libvirt-client

* Mon Apr 09 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt3
- really fix post scripts

* Thu Apr 05 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt2
- fix post scripts

* Tue Apr 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt1
- 0.9.11
- refactor the libvirt spec
- split package to libvirt-client and libvirt-daemon( and qemu,kvm,lxc subpackages)
- install libvirt-guests systemd service

* Mon Mar 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt2
- fixed build for arm (patch by sbolshakov@)

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Thu Dec 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6-alt1.1
- Rebuild with Python-2.7

* Thu Sep 29 2011 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Wed Jun 15 2011 Anton Protopopov <aspsk@altlinux.org> 0.9.1-alt2
- Add dependency on dmidecode package (ALT 25752)
- Create vmusers group in %%pre (ALT 25751)

* Fri May 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1
- add /etc/tmpfiles.d/libvirtd.conf for systemd and /var/run on tmpfs

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt3
- cleanup spec (/etc -> %%_sysconfdir,/var -> %%_localstatedir)
- add generate host_uuid for libvirtd.conf
- generate UUID for first rpm install only
- run qemu with "_libvirt" user and "vmusers" group privileges
- add systemd service file

* Mon Apr 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.9.0-alt2
- implement rigth cond{stop,restart,reload} (ALT 23023)

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0
- fixed CVE-2011-1146

* Sat Mar 26 2011 Anton Farygin <rider@altlinux.ru> 0.8.8-alt1
- new version

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt3
- rebuild with new libdevmapper

* Fri Jan 21 2011 Anton Farygin <rider@altlinux.ru> 0.8.7-alt2
- add (post,preun)_service, disabled by default
- added 'host' model to cpu list
- removed dnsmasq requires for system with bridged networks

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7
- fix and enable polkit support
- build with udev support
- build with yajl support
- build with selinux support
- build with phyp (libssh2) support
- build with libpcap support
- build with libcap-ng support for manage capabilities
- build with audit support
- build with numa support

* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 0.8.6-alt1
- new version
- enabled xen support (closes: #24579)
- removed post-service (closes: #23023)

* Wed Nov 24 2010 Anton Farygin <rider@altlinux.ru> 0.8.5-alt2
- removed binaries from /usr/share

* Tue Nov 09 2010 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- Release of 0.8.5

* Sat Oct 02 2010 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- Release of 0.8.4

* Tue Jul 06 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt2
- Add --with-storage-lvm (ALT #23580)

* Tue Jul 06 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt1
- Release of 0.8.2

* Fri Jul 02 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.1-alt1
- Release of 0.8.1

* Sun Apr 18 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt2
- Close a reopened bug (ALT #22433).

* Tue Apr 13 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt1
- Release of 0.8.0

* Mon Apr 12 2010 Anton Protopopov <aspsk@altlinux.org> 0.7.7-alt2
- Use 'notifemty' instead of 'minsize/size 100k' in logrotate config.
  This prevents logrotate from rotating empty logs (Closes: #22433).

* Sat Mar 20 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.7-alt1
- NMU
- Release of 0.7.7 (Closes: #23095)

* Wed Feb 10 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.6-alt2
- NMU
- Return %%_pkgconfigdir/libvirt.pc in subpackage %%name-devel (Closes: #22932)
  (thanks to Alexey Borovskoy <alb altlinux ru>)
- Fix status function in initscript (thanks to Alexey Borovskoy <alb altlinux ru>)

* Mon Feb 08 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.6-alt1
- NMU
- Release of 0.7.6

* Mon Feb 08 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.5-alt1
- NMU
- Release of 0.7.5

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.1
- Rebuilt with python 2.6

* Mon Nov 23 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.4-alt1
- Release of 0.7.4

* Tue Sep 22 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.1-alt2
- Provide libvirt-python

* Wed Sep 16 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.1-alt1
- Release of 0.7.1

* Fri Sep 11 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt2
- merge with upstream (more than 200 commits)
- Disable storage_mpath and add libdevmapper-devel to %%buildrequires
- update .gnulib

* Fri Aug 07 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt1
- Release of 0.7.0
- Run libvirt with "devel" version of kvm

* Mon Aug 03 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.5-alt1
- Migrate to new git sources

* Tue Jun 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.4-alt1
- Release of 0.6.4

* Fri May 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.3-alt1
- Update to svn head (>= 0.6.3)

* Tue Apr 14 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.2-alt1
- Release of 0.6.2
- Use --config the same as --ostemplate

* Tue Mar 10 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.1-alt1
- Release of 0.6.1

* Mon Mar 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.0-alt2
- Fix python policy

* Sat Jan 31 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.0-alt1
- Release of 0.6.0

* Tue Dec 23 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt4
- Fix host MAC (Eugeny Sokolov)
- Remove static library (repocop)
- Remove RPM_BUILD_ROOTs

* Thu Dec 18 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt3
- Fix openvz crash when setting vcpus & initialize mutex

* Mon Dec 08 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt2
- Fix rpm install (by adding libgnutls26)

* Fri Dec 05 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt1
- Release of 0.5.1
- Fix repocop warnings
- Link condrestart to restart

* Tue Nov 18 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.6-alt3
- Merged with upstream to fix a bug in openvzWriteParam

* Thu Nov 13 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.6-alt2
- Merged with upstream version with OpenVZ bridge support enabled

* Wed Sep 24 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.6-alt1
- Release of 0.4.6

* Mon Sep 15 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.5-alt1
- Release of 0.4.5

* Mon Sep 08 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.4-alt1.1
- Merge with upstream
- fix %%files

* Wed Jun 25 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.4-alt1
- Release of 0.4.4

* Tue Jun 17 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.3-alt1
- Release of 0.4.3

* Mon Apr 21 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.2-alt2
- Fixed bad permissions on /var/{run,log,lib}/libvirt

* Wed Apr 09 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.2-alt1
- Release of 0.4.2

* Mon Mar 31 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.1-alt1
- Release of 0.4.1

* Wed Mar 12 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.1-alt0.1
- Switch to 0.4.1

* Tue Dec 18 2007 Anton Protopopov <aspsk@altlinux.ru> 0.4.0-alt0.1
- Initial pre-build :)

* Tue Dec 18 2007 Daniel Veillard <veillard@redhat.com> - 0.4.0-1
- Release of 0.4.0
- SASL based authentication
- PolicyKit authentication
- improved NUMA and statistics support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Sun Sep 30 2007 Daniel Veillard <veillard@redhat.com> - 0.3.3-1
- Release of 0.3.3
- Avahi support
- NUMA support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Tue Aug 21 2007 Daniel Veillard <veillard@redhat.com> - 0.3.2-1
- Release of 0.3.2
- API for domains migration
- APIs for collecting statistics on disks and interfaces
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Tue Jul 24 2007 Daniel Veillard <veillard@redhat.com> - 0.3.1-1
- Release of 0.3.1
- localtime clock support
- PS/2 and USB input devices
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Mon Jul  9 2007 Daniel Veillard <veillard@redhat.com> - 0.3.0-1
- Release of 0.3.0
- Secure remote access support
- unification of daemons
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Fri Jun  8 2007 Daniel Veillard <veillard@redhat.com> - 0.2.3-1
- Release of 0.2.3
- lot of assorted bugfixes and cleanups
- support for Xen-3.1
- new scheduler API

* Tue Apr 17 2007 Daniel Veillard <veillard@redhat.com> - 0.2.2-1
- Release of 0.2.2
- lot of assorted bugfixes and cleanups
- preparing for Xen-3.0.5

* Thu Mar 22 2007 Jeremy Katz <katzj@redhat.com> - 0.2.1-2.fc7
- don't require xen; we don't need the daemon and can control non-xen now
- fix scriptlet error (need to own more directories)
- update description text

* Fri Mar 16 2007 Daniel Veillard <veillard@redhat.com> - 0.2.1-1
- Release of 0.2.1
- lot of bug and portability fixes
- Add support for network autostart and init scripts
- New API to detect the virtualization capabilities of a host
- Documentation updates

* Fri Feb 23 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-4.fc7
- Fix loading of guest & network configs

* Fri Feb 16 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-3.fc7
- Disable kqemu support since its not in Fedora qemu binary
- Fix for -vnc arg syntax change in 0.9.0  QEMU

* Thu Feb 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-2.fc7
- Fixed path to qemu daemon for autostart
- Fixed generation of <features> block in XML
- Pre-create config directory at startup

* Wed Feb 14 2007 Daniel Veillard <veillard@redhat.com> 0.2.0-1.fc7
- support for KVM and QEmu
- support for network configuration
- assorted fixes

* Mon Jan 22 2007 Daniel Veillard <veillard@redhat.com> 0.1.11-1.fc7
- finish inactive Xen domains support
- memory leak fix
- RelaxNG schemas for XML configs

* Wed Dec 20 2006 Daniel Veillard <veillard@redhat.com> 0.1.10-1.fc7
- support for inactive Xen domains
- improved support for Xen display and vnc
- a few bug fixes
- localization updates

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.1.9-2
- rebuild against python 2.5

* Wed Nov 29 2006 Daniel Veillard <veillard@redhat.com> 0.1.9-1
- better error reporting
- python bindings fixes and extensions
- add support for shareable drives
- add support for non-bridge style networking
- hot plug device support
- added support for inactive domains
- API to dump core of domains
- various bug fixes, cleanups and improvements
- updated the localization

* Tue Nov  7 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-3
- it's pkgconfig not pgkconfig !

* Mon Nov  6 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-2
- fixing spec file, added %%dist, -devel requires pkgconfig and xen-devel
- Resolves: rhbz#202320

* Mon Oct 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-1
- fix missing page size detection code for ia64
- fix mlock size when getting domain info list from hypervisor
- vcpu number initialization
- don't label crashed domains as shut off
- fix virsh man page
- blktapdd support for alternate drivers like blktap
- memory leak fixes (xend interface and XML parsing)
- compile fix
- mlock/munlock size fixes

* Fri Sep 22 2006 Daniel Veillard <veillard@redhat.com> 0.1.7-1
- Fix bug when running against xen-3.0.3 hypercalls
- Fix memory bug when getting vcpus info from xend

* Fri Sep 22 2006 Daniel Veillard <veillard@redhat.com> 0.1.6-1
- Support for localization
- Support for new Xen-3.0.3 cdrom and disk configuration
- Support for setting VNC port
- Fix bug when running against xen-3.0.2 hypercalls
- Fix reconnection problem when talking directly to http xend

* Tue Sep  5 2006 Jeremy Katz <katzj@redhat.com> - 0.1.5-3
- patch from danpb to support new-format cd devices for HVM guests

* Tue Sep  5 2006 Daniel Veillard <veillard@redhat.com> 0.1.5-2
- reactivating ia64 support

* Tue Sep  5 2006 Daniel Veillard <veillard@redhat.com> 0.1.5-1
- new release
- bug fixes
- support for new hypervisor calls
- early code for config files and defined domains

* Mon Sep  4 2006 Daniel Berrange <berrange@redhat.com> - 0.1.4-5
- add patch to address dom0_ops API breakage in Xen 3.0.3 tree

* Mon Aug 28 2006 Jeremy Katz <katzj@redhat.com> - 0.1.4-4
- add patch to support paravirt framebuffer in Xen

* Mon Aug 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-3
- another patch to fix network handling in non-HVM guests

* Thu Aug 17 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-2
- patch to fix virParseUUID()

* Wed Aug 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-1
- vCPUs and affinity support
- more complete XML, console and boot options
- specific features support
- enforced read-only connections
- various improvements, bug fixes

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-6
- add patch from pvetere to allow getting uuid from libvirt

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-5
- build on ia64 now

* Thu Jul 27 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-4
- don't BR xen, we just need xen-devel

* Thu Jul 27 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-3
- need rebuild since libxenstore is now versionned

* Mon Jul 24 2006 Mark McLoughlin <markmc@redhat.com> - 0.1.3-2
- Add BuildRequires: xen-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.3-1.1
- rebuild

* Tue Jul 11 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-1
- support for HVM Xen guests
- various bugfixes

* Mon Jul  3 2006 Daniel Veillard <veillard@redhat.com> 0.1.2-1
- added a proxy mechanism for read only access using httpu
- fixed header includes paths

* Wed Jun 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.1-1
- extend and cleanup the driver infrastructure and code
- python examples
- extend uuid support
- bug fixes, buffer handling cleanups
- support for new Xen hypervisor API
- test driver for unit testing
- virsh --conect argument

* Mon Apr 10 2006 Daniel Veillard <veillard@redhat.com> 0.1.0-1
- various fixes
- new APIs: for Node information and Reboot
- virsh improvements and extensions
- documentation updates and man page
- enhancement and fixes of the XML description format

* Tue Feb 28 2006 Daniel Veillard <veillard@redhat.com> 0.0.6-1
- added error handling APIs
- small bug fixes
- improve python bindings
- augment documentation and regression tests

* Thu Feb 23 2006 Daniel Veillard <veillard@redhat.com> 0.0.5-1
- new domain creation API
- new UUID based APIs
- more tests, documentation, devhelp
- bug fixes

* Fri Feb 10 2006 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- fixes some problems in 0.0.3 due to the change of names

* Wed Feb  8 2006 Daniel Veillard <veillard@redhat.com> 0.0.3-1
- changed library name to libvirt from libvir, complete and test the python
  bindings

* Sun Jan 29 2006 Daniel Veillard <veillard@redhat.com> 0.0.2-1
- upstream release of 0.0.2, use xend, save and restore added, python bindings
  fixed

* Wed Nov  2 2005 Daniel Veillard <veillard@redhat.com> 0.0.1-1
- created
