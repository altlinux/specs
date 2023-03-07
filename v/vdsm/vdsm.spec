%define _unpackaged_files_terminate_build 1

# Required users and groups
%define vdsm_user vdsm
%define vdsm_group vmusers
%define qemu_user _libvirt
%define qemu_group vmusers
%define snlk_group sanlock
%define snlk_user sanlock
%define cdrom_group cdrom
%define imageio_user ovirtimg
%define imageio_group ovirtimg

# Features
%def_enable ovirt_vmconsole
%def_enable gluster_mgmt
%def_enable libvirt_sanlock
%def_enable hooks
%def_enable vhostmd

%define gluster_version 6.0
%define _localstatedir /var
%define _libexecdir /usr/libexec

Name: vdsm
Version: 4.50.4.1
Release: alt1
Summary: Virtual Desktop Server Manager

Group: System/Configuration/Other
License: GPLv2+
Url: http://www.ovirt.org/develop/developer-guide/vdsm/vdsm/
BuildArch: noarch
VCS: https://github.com/oVirt/vdsm
Source: %name-%version.tar
Source2: %name.filetrigger
Patch: %name-%version.patch

%define _vdsm_log_dir %_logdir/%name
%define vdsm_repo %_sharedstatedir/%name/data-center

BuildRequires(pre): rpm-build-python3 rpm-macros-systemd
BuildRequires: python3-devel
BuildRequires: openssl
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-dateutil

# Numactl is not available on s390[x] and ARM
%ifnarch s390 s390x %arm
Requires: numactl
%endif

%ifarch x86_64
Requires: python3-module-dmidecode
Requires: dmidecode
Requires: virt-v2v
%endif

Requires: chrony
Requires: crontabs
Requires: which
Requires: sudo >= 1.7.3
Requires: logrotate
Requires: lshw
Requires: lsof
Requires: ndctl
Requires: swtpm-tools
Requires: xz
Requires: python3-module-rpm
Requires: python3-module-six >= 1.9.0
Requires: python3-module-requests
Requires: curl
Requires: python3-module-%name-rpc-http = %version-%release
Requires: python3-module-%name-rpc = %version-%release
Requires: mom >= 0.5.14
Requires: util-linux
Requires: nfs-utils
Requires: ksmtuned

# For kvm2ovirt
Requires: ovirt-imageio-common
# For controlling /tickets
Requires: ovirt-imageio-daemon

%{?_enable_ovirt_vmconsole:Requires: ovirt-vmconsole}

Requires: libvirt-client
Requires: libvirt-daemon-config-nwfilter
Requires: libvirt-lock-sanlock
Requires: libvirt-kvm >= 7.6.0
Requires: python3-module-libvirt
Requires: open-iscsi
Requires: sanlock >= 3.8.3 python3-module-sanlock
Requires: multipath-tools
Requires: python3-module-augeas

#Requires: policycoreutils-python
Requires: fence-agents-all >= 4.2.1
Requires: systemd >= 219
Requires: cyrus-sasl2
Requires: lvm2 >= 2.02.177

Requires: qemu-kvm >= 6.0.0

# GlusterFS client-side RPMs needed for Gluster SD
%ifnarch ppc64le
Requires: glusterfs-client >= %gluster_version
%endif

Requires: psmisc >= 22.6
Requires: sos >= 3.7
Requires: tree
Requires: dosfstools
Requires: xorriso
Requires: guestfs-tools

%description
The VDSM service is required by a Virtualization Manager to manage the
Linux hosts. VDSM manages and monitors the host's storage, memory and
networks as well as virtual machine creation, other host administration
tasks, statistics gathering, and log collection.


%package -n python3-module-%name-rpc-http
Summary: VDSM http API
Group: Development/Python3
BuildArch: noarch
Provides: %name-xmlrpc = %version-%release
Provides: %name-http = %version-%release
Obsoletes: %name-xmlrpc < %version-%release

%description -n python3-module-%name-rpc-http
A http interface for interacting with vdsmd when using OVF store image
download or upload.

%package client
Summary: VDSM client
Group: System/Configuration/Other
BuildArch: noarch
# A hack for unbreaking external packages that expect vdsm-cli.
Provides: %name-cli = %version-%release
Requires: python3-module-%name-api = %version-%release
Requires: python3-module-yajsonrpc = %version-%release
Obsoletes: %name-cli < %version-%release

%description client
Access vdsm API from the command line.

%package -n python3-module-%name-api
Summary: VDSM API
Group: Development/Python3
BuildArch: noarch
BuildRequires: python3-module-pyaml
Provides: %name-api = %version-%release

%description -n python3-module-%name-api
Contains api schema files

%package -n python3-module-%name-rpc
Summary: VDSM API Server
Group: Development/Python3
BuildArch: noarch
Provides: %name-jsonrpc = %version-%release
Requires: python3-module-%name = %version-%release
Requires: python3-module-%name-api = %version-%release
Requires: python3-module-yajsonrpc = %version-%release
Obsoletes: %name-api < 4.16

%description -n python3-module-%name-rpc
A Json-based RPC interface that serves as the protocol for libvdsm.

%package -n python3-module-yajsonrpc
Summary: JSON RPC server and client implementation
Group: Development/Python3
BuildArch: noarch
Provides: %name-yajsonrpc = %version-%release

%description -n python3-module-yajsonrpc
A JSON RPC server and client implementation.

%package -n python3-module-%name-common
Summary: common VDSM python libraries, required by all subsystems
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-dbus
Requires: python3-module-dateutil
Requires: python3-module-six >= 1.9.0
Requires: python3-module-decorator
Requires: python3-module-libvirt >= 3.7.0
Provides: %name-common = %version-%release

%description -n python3-module-%name-common
VDSM libraries that are imported by all subsystems

%package -n python3-module-%name-network
Summary: VDSM network python libraries
Group: Development/Python3
Provides: %name-network = %version-%release
Requires: NetworkManager-config-server
Requires: NetworkManager-ovs
Requires: ethtool
#Requires: initscripts
Requires: iproute2
Requires: openvswitch >= 2.15
Requires: python3-module-openvswitch >= 2.15
Requires: nmstate >= 1.2.1
Requires: lldpad
Requires: python3-module-%name-common  = %version-%release
Requires: python3-module-cryptography
Provides: %name-network = %version-%release

%description -n python3-module-%name-network
VDSM network python libraries

%package -n python3-module-%name
Summary: VDSM python libraries
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-ioprocess >= 1.4.1
Requires: python3-module-%name-common  = %version-%release
Requires: python3-module-%name-api  = %version-%release
Requires: python3-module-%name-network = %version-%release
Provides: %name-python = %version-%release
%py3_provides hooking

%description -n python3-module-%name
Shared libraries between the various VDSM packages.

%package hook-allocate_net
Summary: random_network allocation hook for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-allocate_net
VDSM hook used to allocate networks for vms in a random fashion

%package hook-boot_hostdev
Summary: allows setting boot order for hostdev
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-boot_hostdev
VDSM hook used to boot vms from passthrough devices via custom property

%package hook-checkimages
Summary: Qcow2 disk image format check hook for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-checkimages
VDSM hook used to perform consistency check on a qcow2 format disk image
using the QEMU disk image utility.

%package hook-checkips
Summary: Check connectivity from the host to designated IPs
Group: System/Configuration/Other
Requires: %name = %version-%release
%add_python3_req_skip checkips_utils

%description hook-checkips
VDSM hook used to check connectivity from the host network to designated IPs

%package hook-diskunmap
Summary: Activate UNMAP for disk/lun devices
Group: System/Configuration/Other
BuildArch: noarch
Requires: qemu-kvm >= 1.5

%description hook-diskunmap
VDSM hooks which allow to activate disk UNMAP.

%package hook-ethtool-options
Summary: Allow setting custom ethtool options for vdsm controlled nics
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-ethtool-options
VDSM hook used for applying custom network properties that define ethtool
options for vdsm network nics

%package hook-extra-ipv4-addrs
Summary: Set extra ipv4 addresses for vdsm networks
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-extra-ipv4-addrs
This hook allows the user to set extra ipv4
addresses for vdsm networks.

%package hook-vhostmd
Summary: VDSM hook set for interaction with vhostmd
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: vhostmd

%description hook-vhostmd
VDSM hook to use vhostmd per VM according to Virtualization Manager requests.

%package hook-faqemu
Summary: Fake qemu process for VDSM quality assurance
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-faqemu
VDSM hook used for testing VDSM with multiple fake virtual machines without
running real guests.
To enable this hook on your host, set vars.fake_kvm_support=True in your
/etc/vdsm/vdsm.conf before adding the host to ovirt-Engine.

%package hook-localdisk
Summary: Use a local image instead of a shared storage image
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-localdisk
This hook adds the ability to use fast local storage instead of shared
storage, while using shared storage for managing VM templates.
To enable this hook, the VM should have a custom property of 'localdisk=lvm'.
The system administrator will be responsible for creating the host "ovirt-local"
volume group and extending it with new devices if needed.
The VM must be pinned to the host.

%package hook-log-firmware
Summary: Log VM's firmware to a file
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-log-firmware
This hook allows logging a VM firmware to a file.

%package hook-log-console
Summary: Log VM's serial console to a file
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-log-console
This hook allows logging a VM serial console to a file.

%package hook-macbind
Summary: Bind a vNIC to a Bridge
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-macbind
VDSM hooks which allow to bind a vNIC to a Bridge, managed or not by engine.

%package hook-extnet
Summary: Force a vNIC to connect to a specific libvirt network
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-extnet
VDSM hook which allows to connect a vNIC to a libvirt network that is managed
outside of oVirt, such as an openvswitch network.

%package hook-fakevmstats
Summary: Generate random VM statistics
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-fakevmstats
Hook intercepts VM's stats and randomizes various fields.
To enable this hook on your host, set vars.fake_vmstats_enable=true in your
/etc/vdsm/vdsm.conf.

%package hook-fileinject
Summary: Allow uploading file to VMs disk
Group: System/Configuration/Other
BuildArch: noarch
Requires: python3-module-libguestfs
Requires: %name = %version-%release

%description hook-fileinject
Hook is getting target file name and its content and
create that file in target machine.

%package hook-httpsisoboot
Summary: Allow directly booting from an https available ISO
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-httpsisoboot
Let the VM boot from an ISO image made available via an https URL without
the need to import the ISO into an ISO storage domain.
It doesn't support plain http.

%package hook-nestedvt
Summary: Nested Virtualization support for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-nestedvt
If the nested virtualization is enabled in your kvm module
this hook will expose it to the guests.

%package hook-openstacknet
Summary: OpenStack Network vNICs support for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-openstacknet
Hook for OpenStack Network vNICs.

%package hook-qemucmdline
Summary: QEMU cmdline hook for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-qemucmdline
Provides support for injecting QEMU cmdline via VDSM hook.
It exploits libvirt's qemu:commandline facility available in the
qemu xml namespace.

%package hook-scratchpad
Summary: One time disk creation for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-scratchpad
scratchpad hook for VDSM
Hook creates a disk for a VM onetime usage,
the disk will be erased when the VM destroyed.
VM cannot be migrated when using scratchpad hook

%package hook-smbios
Summary: Adding custom smbios entries to libvirt domain via VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-smbios
Adding custom smbios entries to libvirt domain via VDSM
such as: vendor, version, date and release

%package hook-spiceoptions
Summary: To configure spice options for vm
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-spiceoptions
This vdsm hook can be used to configure some of
the spice optimization attributes and values..

%package hook-vmfex-dev
Summary: VM-FEX vNIC support for VDSM
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-vmfex-dev
Allows to use custom device properties to connect a guest vNIC to a host
VM-FEX Virtual Function (SR-IOV with macvtap mode).

%package hook-fcoe
Summary: Hook to enable FCoE support
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: fcoe-utils

%description hook-fcoe
VDSM hook used for configure specified NICs as FCoE interface through custom
network properties

%package hook-cpuflags
Summary: Hook that modifies guest's CPU flags
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-cpuflags
Hook that modifies guest's CPU flags using custom properties.

%package hook-hostdev-scsi
Summary: Hook to optimize hostdev SCSI devices translating their config.
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description hook-hostdev-scsi
Hook to optimizet hostdev SCSI generic devices translating their configuration
into more specific one.

%package -n python3-module-%name-gluster
Summary: Gluster Plugin for VDSM
Group: Development/Python
Provides: %name-gluster = %version-%release
Requires: %name = %version-%release
Requires: glusterfs-server >= %gluster_version
Requires: glusterfs-georeplication >= %gluster_version
#Requires: glusterfs-events >= %gluster_version
Requires: libblockdev-plugins
Requires: xfsprogs
%ifarch x86_64
Requires: vdo
%endif

%description -n python3-module-%name-gluster
Gluster plugin enables VDSM to serve Gluster functionalities.

%prep
%setup
%patch -p1
echo v%version > VERSION

%build
%autoreconf
%configure \
    %{subst_enable hooks} \
    %{subst_enable vhostmd} \
    %{?_enable_gluster_mgmt:--enable-gluster-mgmt} \
    %{?_enable_ovirt_vmconsole:--enable-ovirt-vmconsole} \
    %{?_enable_libvirt_sanlock:--enable-libvirt-sanlock} \
    --disable-libvirt-selinux \
    --with-qemu-user=%qemu_user \
    --with-qemu-group=%qemu_group \
    --with-data-center=%vdsm_repo \
    --with-polkitdir=%_datadir/polkit-1/rules.d \
    --with-ovirt-vmconsole-user=ovirt-vmconsole \
    --with-ovirt-vmconsole-group=ovirt-vmconsole

%make_build

%install
%makeinstall_std
install -pD -m 755 %SOURCE2 %buildroot%_rpmlibdir/%name.filetrigger

rm -rf %buildroot%python3_sitelibdir/dnf-plugins


%pre
# Force standard locale behavior (English)
export LC_ALL=C

groupadd -r -f %vdsm_group >/dev/null 2>&1 ||:
useradd -r -u 36 -g %vdsm_group -d /var/lib/vdsm \
        -s /sbin/nologin -c "Node Virtualization Manager" %vdsm_user >/dev/null 2>&1 ||:
usermod -a -G %qemu_group,%snlk_group %vdsm_user >/dev/null 2>&1 ||:
usermod -a -G %cdrom_group %qemu_user >/dev/null 2>&1 ||:
usermod -a -G %qemu_group,%vdsm_group %imageio_user >/dev/null 2>&1 ||:
usermod -a -G %imageio_group %vdsm_user >/dev/null 2>&1 ||:

# We keep the previous rpm version number in a file for managing upgrade flow
if [ "$1" -gt 1 ]; then
    rpm -q %name > "%_localstatedir/lib/%name/upgraded_version"
    # Both vdsm and supervdsm should be managed here and must be restarted if
    # ran before the upgrade
    if systemctl status vdsmd >/dev/null 2>&1; then
        touch "%_localstatedir/lib/%name/vdsmd_start_required"
    fi
    if systemctl status supervdsmd >/dev/null 2>&1; then
        touch "%_localstatedir/lib/%name/supervdsmd_start_required"
    fi

fi

%post
# After vdsm install we should create the logs files.
# In the install session we create it but since we use
# the ghost macro (in files session) the files are not included
touch %_vdsm_log_dir/{mom.log,supervdsm.log,vdsm.log}
chmod 0644 %_vdsm_log_dir/{mom.log,supervdsm.log,vdsm.log}
chown %vdsm_user:%vdsm_group %_vdsm_log_dir/{mom.log,vdsm.log}
chown root:root %_vdsm_log_dir/supervdsm.log

systemd-tmpfiles --create %name.conf

# VDSM installs vdsm-modules-load.d.conf file - the following command will
# refresh vdsm kernel modules requirements to start on boot
systemctl restart systemd-modules-load.service >/dev/null 2>&1 ||:
# VDSM installs unit files - daemon-reload will refresh systemd
systemctl daemon-reload >/dev/null 2>&1 ||:

%preun
if [ "$1" -eq 0 ]; then
        %_bindir/vdsm-tool remove-config
fi
%systemd_preun dev-hugepages1G.mount
%systemd_preun vdsmd.service
%systemd_preun vdsm-network.service
%systemd_preun supervdsmd.service
%systemd_preun mom-vdsm.service
%systemd_preun ksmtuned.service

%post hook-checkips
%systemd_post vdsm-checkips.service

%preun hook-checkips
%systemd_preun vdsm-checkips.service

%post hook-fcoe
%systemd_post lldpad.service
%systemd_post fcoe.service

%files
%doc README.md
%doc lib/vdsm/vdsm.conf.sample
%doc README.logging
%doc COPYING
%_unitdir/dev-hugepages1G.mount
%_unitdir/vdsmd.service
%_unitdir/vdsm-network.service
%_unitdir/supervdsmd.service
%_unitdir/mom-vdsm.service
%_sysconfdir/systemd/system/libvirtd.service.d/unlimited-core.conf
%_rpmlibdir/%name.filetrigger

%dir %attr(-, %vdsm_user, %vdsm_group) %vdsm_repo
%ghost %config %attr(0644, %vdsm_user, %vdsm_group) %_vdsm_log_dir/mom.log
%ghost %config %attr(0644, root, root) %_vdsm_log_dir/supervdsm.log
%ghost %config %attr(0644, %vdsm_user, %vdsm_group) %_vdsm_log_dir/vdsm.log
%ghost %dir %attr(-, %vdsm_user, %vdsm_group) %vdsm_repo/hsm-tasks
%ghost %dir %attr(-, %vdsm_user, %vdsm_group) %vdsm_repo/mnt
%dir %_libexecdir/%name
%dir %_sysconfdir/%name/vdsm.conf.d
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/mom.d
%dir %_sysconfdir/%name/logrotate
%dir %_datadir/%name
#%_datadir/%name/__pycache__
%_libexecdir/%name/daemonAdapter
%_libexecdir/%name/sitecustomize.py*
%_libexecdir/%name/__pycache__
%_libexecdir/%name/supervdsmd
%_libexecdir/%name/vdsmd

%config(noreplace) %_sysconfdir/%name/vdsm.conf
%config(noreplace) %_sysconfdir/%name/logger.conf
%config(noreplace) %_sysconfdir/%name/svdsm.logger.conf
%config(noreplace) %_sysconfdir/%name/mom.conf
%config(noreplace) %_sysconfdir/%name/mom.d/*.policy
%config(noreplace) %_sysconfdir/%name/logrotate/vdsm
%config(noreplace) %_sysconfdir/sysctl.d/vdsm.conf
%config(noreplace) %_sysconfdir/modules-load.d/vdsm.conf
%_sysconfdir/ovirt-imageio/conf.d/60-vdsm.conf
%_tmpfilesdir/%name.conf
%_sysconfdir/modprobe.d/vdsm-bonding-modprobe.conf
%_sysconfdir/NetworkManager/conf.d/vdsm.conf
%attr(400, root, root) %_sysconfdir/sudoers.d/50_vdsm
%_sysconfdir/cron.hourly/vdsm-logrotate
%_sysconfdir/libvirt/hooks/qemu
%_libexecdir/%name/curl-img-wrap
%_libexecdir/%name/fc-scan
%_libexecdir/%name/managedvolume-helper
%_libexecdir/%name/vdsm-gencerts.sh
%_libexecdir/%name/vdsmd_init_common.sh
%_libexecdir/%name/vm_libvirt_hook.py*
%_libexecdir/%name/kvm2ovirt
%_libexecdir/%name/fallocate
%_libexecdir/%name/spmprotect.sh
%_libexecdir/%name/spmstop.sh
%dir %_libexecdir/%name/hooks
%dir %_libexecdir/%name/hooks/*
%exclude %_libexecdir/%name/hooks/checkipsd

%_libexecdir/%name/get-conf-item
%_udevrulesdir/12-vdsm-lvm.rules
%_sysconfdir/security/limits.d/99-vdsm.conf
%_man8dir/vdsmd.8*
%_datadir/polkit-1/rules.d/10-vdsm-libvirt-access.rules

%defattr(-, %vdsm_user, %qemu_group, -)
%dir %_localstatedir/lib/libvirt/qemu/channels

%defattr(-, %vdsm_user, %vdsm_group, -)
%dir %_sysconfdir/pki/%name
%dir %_sysconfdir/pki/%name/keys
%dir %_sysconfdir/pki/%name/certs
%_sysconfdir/pki/%name/libvirt-migrate
%dir %_sysconfdir/pki/%name/libvirt-spice
%config(noreplace) %_sysconfdir/pki/%name/keys/libvirt_password
%dir %_localstatedir/lib/%name
%dir %_localstatedir/lib/%name/netconfback
%dir %_localstatedir/lib/%name/persistence
%dir %_localstatedir/lib/%name/staging
%dir %_localstatedir/lib/%name/storage
%dir %_localstatedir/lib/%name/upgrade
%dir %_localstatedir/log/%name
%dir %_localstatedir/log/%name/backup
%dir %_localstatedir/log/%name/import
%dir %attr(750, %vdsm_user, %vdsm_group) %_localstatedir/log/%name/commands

%_datadir/%name/autounattend
%_datadir/%name/lvmlocal.conf

%files -n python3-module-%name-common
%python3_sitelibdir/%name/common

%files -n python3-module-%name-network
%python3_sitelibdir/%name/network

%files -n python3-module-%name
%_man1dir/vdsm-tool.1*
%_bindir/vdsm-tool
%python3_sitelibdir/%name
%exclude %python3_sitelibdir/%name/common
%exclude %python3_sitelibdir/%name/network
%exclude %python3_sitelibdir/%name/api
%exclude %python3_sitelibdir/%name/rpc
%exclude %python3_sitelibdir/%name/gluster

%files hook-openstacknet
%attr(400, root, root) %_sysconfdir/sudoers.d/50_vdsm_hook_openstacknet
%_libexecdir/%name/hooks/*/*openstacknet*

%if_enabled vhostmd
%files hook-vhostmd
%attr(400, root, root) %_sysconfdir/sudoers.d/50_vdsm_hook_vhostmd
%_libexecdir/%name/hooks/*/*vhostmd*
%else
%exclude %_sysconfdir/sudoers.d/50_vdsm_hook_vhostmd
%exclude %_libexecdir/%name/hooks/*/*vhostmd*
%endif

%files hook-qemucmdline
%_libexecdir/%name/hooks/before_vm_start/50_qemucmdline

%files hook-ethtool-options
%_libexecdir/%name/hooks/after_network_setup/30_ethtool_options

%files hook-fcoe
%_presetdir/85-vdsm-hook-fcoe.preset
%_libexecdir/%name/hooks/before_network_setup/50_fcoe

%files hook-localdisk
%_sysconfdir/sudoers.d/50_vdsm_hook_localdisk
%_libexecdir/%name/hooks/after_disk_prepare/localdisk
%_libexecdir/%name/hooks/before_vm_migrate_source/localdisk
%_libexecdir/%name/localdisk-helper
%_udevrulesdir/12-vdsm-localdisk.rules

%files hook-log-console
%_libexecdir/%name/hooks/before_vm_start/50_log_console

%files hook-log-firmware
%_libexecdir/%name/hooks/before_vm_start/50_log_firmware

%files hook-vmfex-dev
%_libexecdir/%name/hooks/before_device_create/50_vmfex
%_libexecdir/%name/hooks/before_device_migrate_destination/50_vmfex
%_libexecdir/%name/hooks/before_nic_hotplug/50_vmfex

%files hook-cpuflags
%_libexecdir/%name/hooks/before_vm_start/50_cpuflags

%if_enabled hooks
%files hook-allocate_net
%_libexecdir/%name/hooks/before_device_create/10_allocate_net

%files hook-boot_hostdev
%_libexecdir/%name/hooks/before_vm_start/50_boot_hostdev

%files hook-checkimages
%_libexecdir/%name/hooks/before_vm_start/60_checkimages

%files hook-checkips
%_libexecdir/%name/hooks/after_get_stats/10_checkips
%_libexecdir/%name/hooks/checkipsd
%_libexecdir/%name/hooks/after_get_stats/checkips_utils.py
%_unitdir/vdsm-checkips.service

%files hook-extra-ipv4-addrs
%_libexecdir/%name/hooks/after_network_setup/40_extra_ipv4_addrs

%files hook-diskunmap
%_libexecdir/%name/hooks/before_vm_start/50_diskunmap

%files hook-fakevmstats
%_libexecdir/%name/hooks/after_get_all_vm_stats/10_fakevmstats

%files hook-fileinject
%_libexecdir/%name/hooks/before_vm_start/50_fileinject

%files hook-httpsisoboot
%_libexecdir/%name/hooks/before_vm_start/50_httpsisoboot

%files hook-macbind
%_libexecdir/%name/hooks/before_vm_start/50_macbind

%files hook-extnet
%_libexecdir/%name/hooks/before_device_create/50_extnet
%_libexecdir/%name/hooks/before_nic_hotplug/50_extnet

%files hook-nestedvt
%_sysconfdir/modprobe.d/vdsm-nestedvt.conf
%_libexecdir/%name/hooks/before_vm_start/50_nestedvt

%files hook-scratchpad
%_libexecdir/%name/hooks/before_vm_start/50_scratchpad
%_libexecdir/%name/hooks/before_vm_migrate_source/50_scratchpad
%_libexecdir/%name/hooks/after_vm_destroy/50_scratchpad

%files hook-smbios
%_libexecdir/%name/hooks/before_vm_start/50_smbios

%files hook-spiceoptions
%_libexecdir/%name/hooks/before_vm_start/50_spiceoptions
%endif

%files -n python3-module-%name-rpc-http
%python3_sitelibdir/%name/rpc/http.py

%files client
%_bindir/vdsm-client
%python3_sitelibdir/vdsmclient
%_man1dir/vdsm-client.1*

%files -n python3-module-%name-rpc
%python3_sitelibdir/%name/rpc
%exclude %python3_sitelibdir/%name/rpc/http.py
%exclude %python3_sitelibdir/%name/rpc/vdsm-api.pickle
%exclude %python3_sitelibdir/%name/rpc/vdsm-events.pickle
%if_enabled gluster_mgmt
%exclude %python3_sitelibdir/%name/rpc/vdsm-api-gluster.pickle
%endif

%files -n python3-module-%name-api
%doc lib/vdsm/api/vdsm-api.html
%python3_sitelibdir/%name/api
%python3_sitelibdir/%name/rpc/vdsm-api.pickle
%python3_sitelibdir/%name/rpc/vdsm-events.pickle

%files -n python3-module-yajsonrpc
%python3_sitelibdir/yajsonrpc

%files hook-faqemu
%_libexecdir/%name/hooks/after_get_caps/10_faqemu
%_libexecdir/%name/hooks/before_vm_start/10_faqemu

%if_enabled gluster_mgmt
%files -n python3-module-%name-gluster
%python3_sitelibdir/%name/gluster
%python3_sitelibdir/%name/rpc/vdsm-api-gluster.pickle
%endif

%changelog
* Wed Mar 01 2023 Alexey Shabalin <shaba@altlinux.org> 4.50.4.1-alt1
- 4.50.4.1

* Wed Sep 01 2021 Alexey Shabalin <shaba@altlinux.org> 4.40.80.6-alt1
- Initial build for ALT.

