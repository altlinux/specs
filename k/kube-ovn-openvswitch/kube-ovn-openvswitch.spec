# based on https://git.altlinux.org/gitoskop/#/gears/o/openvswitch.git/-/blob/sisyphus/openvswitch.spec
%define _unpackaged_files_terminate_build 1
%define oname openvswitch
%def_disable check

Name: kube-ovn-openvswitch
# commit `b57a505b0d31` is version used in kube-ovn v1.15.26 OCI image
# git describe --tags --abbrev=1
Version: 3.5.4.0.40.b57a5
Release: alt1

Summary: Open vSwitch with the Kube-OVN patches
# All code is Apache-2.0 except
# - lib/sflow* which is SISSL
# - utilities/bugtool which is LGPL-2.1
License: Apache-2.0 AND LGPL-2.1-only AND SISSL
Group: Networking/Other

Url: https://www.openvswitch.org/
Vcs: https://github.com/openvswitch/ovs.git
Source0: %name-%version.tar
Source11: %oname.init
Source12: %oname.tmpfiles

# Kube-OVN patches, applied in the order of dist/images/Dockerfile.base
# kube-ovn: v1.15.26
# fix memory leak by ofport_usage and trim memory periodically
Patch1: 4228eab1d722087ba795e310eadc9e25c4513ec1.patch
# increase election timer
Patch2: 54056ea65dc28aa1c4c721a2a34d7913f79f8376.patch
# add fdb update logging
Patch3: 6b4dcb311f171d81a5d40ea51a273fc356c123db.patch
# fdb: fix mac learning in environments with hairpin enabled
Patch4: f627b7721ec282f2edaf798913b1559b939687f0.patch
# ovsdb-tool: add optional server id parameter for "join-cluster" command
Patch5: 3f3e3a436ff5eb2eaafbeeae8ea9dc0c514fe8a3.patch
# fix memory leak in qos
Patch6: a6cb8215a80635129e4fada4c0d25c25fb746bf7.patch
# ovsdb-tool: add command fix-cluster
Patch7: d4d76ddb2e12cdd9e73bb5e008ebb9fd1b4d6ca6.patch
# ovsdb-tool: add commands db-raft-header/rejoin-cluster
Patch8: 53b9837f7fe89cd63af735b039b8c26107d6579d.patch
# netdev: reduce cpu utilization for getting device addresses
Patch9: ffd2328d4a55271569e2b89e54a2c18f4e186af8.patch
# ovs-router: skip getting source address for kube-ipvs0
Patch10: d088c5d8c263552c5a31d87813991aee30ab74de.patch
# increase the default probe interval for large cluster
Patch11: 1b31f07dc60c016153fa35d936cdda0e02e58492.patch
# update ovs-sandbox for docker run
Patch12: 54b767822916606dbb78335a3197983f435b5b8a.patch

# ALT patches, as in openvswitch.spec
Patch101: 0001-execute-openvswitch-as-openvswitch-user.patch
Patch104: 0004-ovs-update-systemd-unit-for-ALT.patch
Patch105: 0005-ovs-fix-linking.patch
Patch106: 0006-ovs-Python-3-support.patch
Patch107: 0007-Use-local-LSB-functions.patch
Patch108: 0008-Avoid-autoreq-on-systemd-utils.patch
# GCC 14+ build fix for Patch9
Patch201: alt-netdev-linux-get-addr-list-pass-struct-netdev.patch
# find the ovs module in its private directory
Patch202: alt-ovs-monitor-ipsec-private-python-dir.patch

# The ovs python module lives in a private directory, so that it does not
# provide python3(ovs) alongside python3-module-openvswitch
%define ovs_python_dir %_libdir/%name/python

Conflicts: %oname

Requires: lib%name = %EVR
# util-linux-2.32-alt2
Requires: pam0(runuser)
%filter_from_requires /lsb-release/d

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: libcap-ng-devel
%ifnarch %e2k
BuildRequires: libunwind-devel
%endif
BuildRequires: libunbound-devel
BuildRequires: glibc-kernheaders
BuildRequires: python3-devel python3-module-setuptools python3-module-OpenSSL python3-module-sphinx python3-module-netaddr python3-module-pyparsing

%description
Open vSwitch is a production quality, multilayer virtual switch
licensed under the open source Apache 2.0 license. It is designed
to enable massive network automation through programmatic
extension, while still supporting standard management interfaces
and protocols (e.g. NetFlow, sFlow, RSPAN, ERSPAN, CLI, LACP,
802.1ag). In addition, it is designed to support distribution
across multiple physical servers similar to VMware's vNetwork
distributed vswitch or Cisco's Nexus 1000V.

This build carries the patches Kube-OVN applies to Open vSwitch.
Only the parts the Kube-OVN image uses are packaged.

%package -n lib%name
License: Apache-2.0
Summary: Open vSwitch core libraries (Kube-OVN build)
Group: System/Libraries

%description -n lib%name
Contains the shared libraries used by Open vSwitch and any eventual extensions.

%package ipsec
Summary: Open vSwitch IPsec tunneling support (Kube-OVN build)
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: python3-module-%name = %EVR
Conflicts: %oname-ipsec
%add_python3_req_skip ovs.daemon ovs.db.idl ovs.dirs ovs.unixctl ovs.unixctl.server ovs.util ovs.vlog

%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%package -n python3-module-%name
Summary: Open vSwitch python3 bindings (Kube-OVN build)
Group: Development/Python3
License: Apache-2.0
Conflicts: python3-module-%oname
# The module is outside the python3 paths
AutoReqProv: yes, nopython, nopython3
Requires: python3

%description -n python3-module-%name
Python3 bindings for the Open vSwitch database.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch201 -p1
%patch202 -p1
sed -i 's|@KUBE_OVN_OVS_PYTHON_DIR@|%ovs_python_dir|' ipsec/ovs-monitor-ipsec.in
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch101 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%ifarch %e2k
sed -i "s/__has_extension(c_atomic)/0/" lib/ovs-atomic.h
%endif
sed -i "s/ike-daemon=libreswan/ike-daemon=strongswan/" rhel/usr_lib_systemd_system_openvswitch-ipsec.service

%build
export PYTHON3=%__python3
%autoreconf
# Kube-OVN builds without DPDK and AF_XDP
%configure \
    --disable-static \
    --enable-shared \
    --enable-ndebug \
    --enable-ssl \
    --disable-afxdp \
    --with-rundir=/run/%oname \
    --with-logdir=%_logdir/%oname \
    --with-dbdir=%_localstatedir/%oname \
    --with-pkidir=%_localstatedir/%oname/pki

%make_build
make rhel/usr_lib_systemd_system_ovs-vswitchd.service

%install
export PYTHON3=%__python3
%makeinstall_std

install -dm0755 %buildroot%_sysconfdir/%oname
install -pDm0755 %SOURCE11 %buildroot%_initdir/%oname
install -dm0750 %buildroot%_logdir/%oname

install -pDm0644 vswitchd/vswitch.ovsschema \
         %buildroot%_datadir/%oname/vswitch.ovsschema
install -pDm0644 rhel/etc_logrotate.d_openvswitch \
         %buildroot%_sysconfdir/logrotate.d/%oname
install -pDm0644 rhel/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot%_sysconfdir/sysconfig/%oname
install -pDm0644 rhel/etc_openvswitch_default.conf \
        %buildroot%_sysconfdir/openvswitch/default.conf

for service in openvswitch ovsdb-server ovs-vswitchd ovs-delete-transient-ports \
               openvswitch-ipsec; do
    install -pDm0644 \
            rhel/usr_lib_systemd_system_${service}.service \
            %buildroot%_unitdir/${service}.service
done

install -p -D -m 0755 \
        rhel/usr_share_openvswitch_scripts_ovs-systemd-reload \
        %buildroot%_datadir/%oname/scripts/ovs-systemd-reload

install -pDm644 %SOURCE12 %buildroot%_tmpfilesdir/%oname.conf

pushd python
export CPPFLAGS="-I ../include"
export LDFLAGS="-L %buildroot%_libdir"
%python3_build
%python3_install
popd

mkdir -p %buildroot%ovs_python_dir
mv %buildroot%python3_sitelibdir/ovs %buildroot%python3_sitelibdir/ovs-*.egg-info \
   %buildroot%ovs_python_dir/

rm -rf %buildroot%_datadir/%oname/python

touch %buildroot%_localstatedir/%oname/conf.db
touch %buildroot%_sysconfdir/%oname/system-id.conf
mkdir -p %buildroot%_logdir/%oname

# move completions to datadir
mkdir -p %buildroot%_datadir/bash-completion/completions
mv %buildroot%_sysconfdir/bash_completion.d/ovs-appctl-bashcomp.bash %buildroot%_datadir/bash-completion/completions/ovs-appctl
mv %buildroot%_sysconfdir/bash_completion.d/ovs-vsctl-bashcomp.bash %buildroot%_datadir/bash-completion/completions/ovs-vsctl

# remove unpackaged files
rm -f %buildroot%_libdir/*.{a,la}
rm -f %buildroot%_bindir/ovs-benchmark \
    %buildroot%_bindir/ovs-parse-backtrace \
    %buildroot%_bindir/ovs-testcontroller \
    %buildroot%_man1dir/ovs-benchmark.* \
    %buildroot%_man8dir/ovs-parse-backtrace.* \
    %buildroot%_man8dir/ovs-testcontroller.*

# Kube-OVN image (OCI) does not use:
# - debug tools
# - VTEP tool
# - devel files
# so we can remove it
rm -f %buildroot%_sbindir/ovs-bugtool \
    %buildroot%_bindir/ovs-dpctl-top \
    %buildroot%_bindir/ovs-flowviz \
    %buildroot%_bindir/ovs-pcap \
    %buildroot%_bindir/ovs-tcpdump \
    %buildroot%_bindir/ovs-tcpundump \
    %buildroot%_bindir/ovs-test \
    %buildroot%_bindir/ovs-vlan-test \
    %buildroot%_bindir/ovs-l3ping \
    %buildroot%_man1dir/ovs-pcap.* \
    %buildroot%_man1dir/ovs-tcpundump.* \
    %buildroot%_man8dir/ovs-bugtool.* \
    %buildroot%_man8dir/ovs-dpctl-top.* \
    %buildroot%_man8dir/ovs-flowviz.* \
    %buildroot%_man8dir/ovs-tcpdump.* \
    %buildroot%_man8dir/ovs-test.* \
    %buildroot%_man8dir/ovs-vlan-test.* \
    %buildroot%_man8dir/ovs-l3ping.*
rm -rf %buildroot%_datadir/%oname/scripts/ovs-bugtool* \
    %buildroot%_datadir/%oname/bugtool-plugins \
    %buildroot%_datadir/%oname/scripts/usdt
rm -f %buildroot%_bindir/vtep-ctl \
    %buildroot%_man5dir/vtep.* \
    %buildroot%_man8dir/vtep-ctl.* \
    %buildroot%_datadir/%oname/scripts/ovs-vtep \
    %buildroot%_datadir/%oname/vtep.ovsschema \
    %buildroot%_libdir/libvtep*
rm -rf %buildroot%_includedir/openflow \
    %buildroot%_includedir/openvswitch \
    %buildroot%_pkgconfigdir
rm -f %buildroot%_libdir/*.so

%check
LC_CTYPE=en_US.UTF-8 LC_COLLATE=en_US.UTF-8 make check

%pre
%_sbindir/groupadd -r -f %oname
%_sbindir/useradd -r -n -g %oname -d %_localstatedir/%oname -M -s /sbin/nologin -c "Open vSwitch Daemons" %oname >/dev/null 2>&1 ||:

%post
if [ $1 -eq 2 ] && [ -f %_sysconfdir/openvswitch/system-id.conf ] ; then
    chown %oname:%oname %_sysconfdir/openvswitch/system-id.conf
    chown -R %oname:%oname %_localstatedir/%oname
    chown -R %oname:%oname %_logdir/%oname
fi
%post_service %oname

%preun
%preun_service %oname

%post ipsec
%post_service %oname-ipsec

%preun ipsec
%preun_service %oname-ipsec

%files
%doc AUTHORS.rst LICENSE NEWS NOTICE README.rst
%_bindir/ovs-appctl
%_bindir/ovs-docker
%_bindir/ovs-dpctl
%_bindir/ovs-ofctl
%_bindir/ovs-vsctl
%_bindir/ovs-pki
%_bindir/ovsdb-client
%_bindir/ovsdb-tool
%_sbindir/ovs-vswitchd
%_sbindir/ovsdb-server
%_initdir/%oname
%_unitdir/%oname.service
%_unitdir/ovs-vswitchd.service
%_unitdir/ovsdb-server.service
%_unitdir/ovs-delete-transient-ports.service
%_tmpfilesdir/%oname.conf
%_man1dir/ovsdb-client.*
%_man1dir/ovsdb-server.*
%_man1dir/ovsdb-tool.*
%_man5dir/ovs-vswitchd.conf.db.*
%_man5dir/ovsdb-server.*
%_man5dir/ovsdb.*
%_man7dir/ovs-fields.*
%_man7dir/ovsdb-server.*
%_man7dir/ovsdb.*
%_man7dir/ovs-actions.*
%_man8dir/ovs-ctl.*
%_man8dir/ovs-dpctl.*
%_man8dir/ovs-kmod-ctl.*
%_man8dir/ovs-vsctl.*
%_man8dir/ovs-vswitchd.*
%_man8dir/ovs-appctl.*
%_man8dir/ovs-ofctl.*
%_man8dir/ovs-pki.*
%dir %_datadir/%oname
%_datadir/%oname/local-config.ovsschema
%_datadir/%oname/vswitch.ovsschema
%dir %_datadir/%oname/scripts
%_datadir/%oname/scripts/ovs-check-dead-ifs
%_datadir/%oname/scripts/ovs-lib
%_datadir/%oname/scripts/ovs-save
%_datadir/%oname/scripts/ovs-ctl
%_datadir/%oname/scripts/ovs-kmod-ctl
%_datadir/%oname/scripts/ovs-systemd-reload
%_datadir/bash-completion/completions/*
%dir %attr(0775, root, %oname) %_sysconfdir/openvswitch
%config(noreplace) %attr(0755, %oname, %oname) %ghost %_sysconfdir/openvswitch/system-id.conf
%config(noreplace) %_sysconfdir/sysconfig/%oname
%config(noreplace) %_sysconfdir/openvswitch/default.conf
%config(noreplace) %_sysconfdir/logrotate.d/openvswitch
%dir %attr(0755, %oname, %oname) %_logdir/%oname
%dir %attr(0755, %oname, %oname) %_localstatedir/%oname
%dir %attr(0755, %oname, %oname) %_localstatedir/%oname/pki
%config(noreplace) %ghost %attr(0644,%oname,%oname) %verify(not md5 size mtime) %_localstatedir/%oname/conf.db

%files ipsec
%_datadir/openvswitch/scripts/ovs-monitor-ipsec
%_unitdir/openvswitch-ipsec.service

%files -n lib%name
%_libdir/libofproto*.so.*
%_libdir/libopenvswitch*.so.*
%_libdir/libovsdb*.so.*
%_libdir/libsflow*.so.*

%files -n python3-module-%name
%dir %_libdir/%name
%ovs_python_dir

%changelog
* Fri Oct 16 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.5.4.0.40.b57a5-alt1
- Initial build for ALT.
