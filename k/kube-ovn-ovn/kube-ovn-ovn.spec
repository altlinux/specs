# based on https://git.altlinux.org/gitoskop/#/gears/o/ovn.git/-/blob/sisyphus/ovn.spec

%define _unpackaged_files_terminate_build 1
%define oname ovn
# kube-ovn-openvswitch this is built against: the same OVS commit and patches
%define ovs_version 3.5.4.0.40.b57a5

Name: kube-ovn-ovn
# git describe --tags --abbrev=1
Version: 25.03.3.0.44.caa2a
Release: alt1

Summary: Open Virtual Network with the Kube-OVN patches
License: Apache-2.0 AND LGPL-2.1-only AND SISSL
Group: Networking/Other

URL: https://www.ovn.org
Vcs: https://github.com/ovn-org/ovn.git
Source0: %name-%version.tar
# Open vSwitch sources at the kube-ovn-openvswitch commit: OVN builds against
# an OVS source tree, not against installed headers
Source1: ovs.tar
Source2: %oname.tmpfiles

# Kube-OVN patches, applied in the order of dist/images/Dockerfile.base
# kube-ovn: v1.15.26
# change default hash type from dp_hash to hash with field src_ip
Patch1: e490f5ac0b644101913c2a3db8e03d85e859deff.patch
# modify src route priority
Patch2: 9ee66bd91be65605cffb9a490b4dba3bc13358e9.patch
# northd: Use MC_UNKNOWN for broadcast ARP requests
Patch3: northd-use-mc-unknown-for-broadcast-arp-requests.patch
# ovn-controller: do not send GARP on localnet for Kube-OVN ports
Patch4: f9e97031b56ab5747b5d73629198331a6daacdfd.patch
# add support for conditionally skipping conntrack
Patch5: 78cade01874292e2c101c39b975290ef6c812a50.patch
# northd: skip conntrack when access node local dns ip
Patch6: 85aa6263ad5b3648eb7ceec90c812328dbb7c6c0.patch
# lflow: do not send direct traffic between lports to conntrack
Patch7: 34dc3e3fcfacec6597293765ecd6e20fe15581f1.patch
# direct output to lsp for dnat packets in logical switch ingress pipelines
Patch8: a297b840c2c9f118c7ce6133077087b5999f12dd.patch
# ovn-controller: make activation strategy work for single chassis
Patch9: 03e35ed9c5b4de0fa8acbc2c057cdd5957a8d605.patch
# skip node local dns ip conntrack when set acl
Patch10: e7d3ba53cdcbc524bb29c54ddb07b83cc4258ed7.patch
# loadbalancer select local backend first
Patch11: 9286e1fd578fdb8f565a0f4aa9066b538295e1ac.patch
# fix lr-lb dnat with multiple distributed gateway ports
Patch12: e5916eb53abc3b7d28c407c3c47566c46116090a.patch
# support dedicated BFD LRP
Patch13: e4e6ea9c5f4ba080b719924e470daa8094ff38a7.patch
# northd: skip arp/nd request for lrp addresses from localnet ports
Patch14: 477695a010affe56efdd66b60510fa612f8704c1.patch
# add skip conntrack ipcidrs support
Patch15: 737d9f932edada5a91f315b5f382daada8dee952.patch
# set dl_src for packets redirected by router port
Patch16: 52b727b3315463668669ff423ce8bfa129861162.patch
# add null check before sbrec delete calls
Patch17: sbrec-delete-null-check.patch
# adapt to the compose_nd_ns() signature change in ovs branch-3.5 commit 33825c273
Patch18: pinctrl-adapt-ovs-compose-nd-ns.patch

# ALT patches, as in ovn.spec
Patch101: 0001-ovn-fix-linking.patch
Patch102: 0002-ovn-var_run-to-run.patch
Patch103: 0003-execute-ovn-as-openvswitch-user.patch
# find the ovs module in its private directory
# python3-module-kube-ovn-openvswitch
Patch104: alt-ovn-detrace-private-python-dir.patch

# Patches of kube-ovn-openvswitch that change code, applied to Source1 so
# that OVN is built against the same headers and ABI as the
# libkube-ovn-openvswitch it runs with
Patch201: 4228eab1d722087ba795e310eadc9e25c4513ec1.patch
Patch202: 54056ea65dc28aa1c4c721a2a34d7913f79f8376.patch
Patch203: 6b4dcb311f171d81a5d40ea51a273fc356c123db.patch
Patch204: f627b7721ec282f2edaf798913b1559b939687f0.patch
Patch205: 3f3e3a436ff5eb2eaafbeeae8ea9dc0c514fe8a3.patch
Patch206: a6cb8215a80635129e4fada4c0d25c25fb746bf7.patch
Patch207: d4d76ddb2e12cdd9e73bb5e008ebb9fd1b4d6ca6.patch
Patch208: 53b9837f7fe89cd63af735b039b8c26107d6579d.patch
Patch209: ffd2328d4a55271569e2b89e54a2c18f4e186af8.patch
Patch210: alt-netdev-linux-get-addr-list-pass-struct-netdev.patch
Patch211: d088c5d8c263552c5a31d87813991aee30ab74de.patch
Patch212: 1b31f07dc60c016153fa35d936cdda0e02e58492.patch
Patch213: 54b767822916606dbb78335a3197983f435b5b8a.patch

Conflicts: %oname
Requires: lib%name = %EVR
Requires: kube-ovn-openvswitch = %ovs_version

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc-c++
BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: libcap-ng-devel
BuildRequires: libunwind-devel
BuildRequires: libunbound-devel
BuildRequires: glibc-kernheaders
BuildRequires: python3-devel python3-module-setuptools python3-module-OpenSSL python3-module-sphinx
BuildRequires: libkube-ovn-openvswitch = %ovs_version

%define ovs_dir %_builddir/ovs

%description
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

This build carries the patches Kube-OVN applies to OVN. Only the parts the
Kube-OVN image uses are packaged.

%package -n lib%name
License: Apache-2.0
Summary: Open Virtual Network core libraries (Kube-OVN build)
Group: System/Libraries

%description -n lib%name
This subpackage contains the OVN shared libraries.

%package central
Summary: Open Virtual Network central components (Kube-OVN build)
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Conflicts: %oname-central

%description central
OVN DB servers and ovn-northd running on a central node.

%package host
Summary: Open Virtual Network host components (Kube-OVN build)
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Conflicts: %oname-host

%description host
OVN controller running on each host.

%prep
%setup
mkdir -p %ovs_dir
tar -xf %SOURCE1 -C %ovs_dir

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
sed -i 's|@KUBE_OVN_OVS_PYTHON_DIR@|%_libdir/kube-ovn-openvswitch/python|' \
    utilities/ovn_detrace.py.in

pushd %ovs_dir
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
popd

%build
export PYTHON3=%__python3

# OVN source code is now separate.
# Build openvswitch first, configured as kube-ovn-openvswitch is.
pushd %ovs_dir
%autoreconf
%configure \
    --disable-static \
    --enable-shared \
    --enable-ndebug \
    --enable-ssl \
    --disable-afxdp \
    --with-rundir=/run/openvswitch \
    --with-logdir=%_logdir/openvswitch \
    --with-dbdir=%_localstatedir/openvswitch \
    --with-pkidir=%_localstatedir/openvswitch/pki

%make_build
popd

%autoreconf
%configure \
    --with-ovs-source=%ovs_dir \
    --disable-static \
    --enable-shared \
    --enable-ssl \
    --with-rundir=/run/%oname \
    --with-logdir=%_logdir/%oname \
    --with-dbdir=%_localstatedir/%oname \
    --with-pkidir=%_localstatedir/openvswitch/pki
%make_build

%install
export PYTHON3=%__python3
# libtool relinks libovn with -lopenvswitch at install time; the stock
# package finds it through libopenvswitch-devel, take it from the OVS tree
# built above instead
export LIBRARY_PATH=%ovs_dir/lib/.libs
%makeinstall_std

install -dm0755 %buildroot%_localstatedir/%oname
install -dm0750 %buildroot%_logdir/%oname

install -pDm0644 rhel/usr_share_ovn_scripts_systemd_sysconfig.template \
        %buildroot%_sysconfdir/sysconfig/%oname
install -pDm0644 rhel/etc_logrotate.d_ovn \
        %buildroot%_logrotatedir/%oname
for service in ovn-controller ovn-northd ovn-ic ovn-ic-db; do
    install -pDm0644 \
            rhel/usr_lib_systemd_system_${service}.service \
            %buildroot%_unitdir/${service}.service
done

install -pDm644 %SOURCE2 %buildroot%_tmpfilesdir/%oname.conf

install -d %buildroot%_prefix/lib/firewalld/services
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-central-firewall-service.xml \
        %buildroot%_prefix/lib/firewalld/services/ovn-central-firewall-service.xml
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-host-firewall-service.xml \
        %buildroot%_prefix/lib/firewalld/services/ovn-host-firewall-service.xml

install -d -m 0755 %buildroot%_prefix/lib/ocf/resource.d/ovn
ln -s %_datadir/ovn/scripts/ovndb-servers.ocf \
      %buildroot%_prefix/lib/ocf/resource.d/ovn/ovndb-servers

# Kube-OVN image (OCI) does not use:
# - debug tools
# - VTEP tool
# - devel files
# so we can remove it
rm -f %buildroot%_bindir/ovn-controller-vtep \
    %buildroot%_man8dir/ovn-controller-vtep.* \
    %buildroot%_bindir/ovn-docker-overlay-driver \
    %buildroot%_bindir/ovn-docker-underlay-driver
rm -rf %buildroot%_datadir/%oname/bugtool-plugins
rm -f %buildroot%_datadir/%oname/scripts/ovn-bugtool-*
rm -rf %buildroot%_includedir/%oname
rm -f %buildroot%_libdir/lib%{oname}*.so \
    %buildroot%_libdir/*.{a,la}

%post central
%post_systemd_postponed ovn-northd.service ovn-ic.service ovn-ic-db.service

%preun central
%preun_systemd ovn-northd.service ovn-ic.service ovn-ic-db.service

%post host
%post_systemd_postponed ovn-controller.service

%preun host
%preun_systemd ovn-controller.service

%files
%config(noreplace) %_logrotatedir/%oname
%config(noreplace) %_sysconfdir/sysconfig/%oname
%_bindir/ovn-appctl
%_bindir/ovn_detrace*
%_bindir/ovn-nbctl
%_bindir/ovn-sbctl
%_bindir/ovn-ic-nbctl
%_bindir/ovn-ic-sbctl
%_bindir/ovn-debug
%_bindir/ovn-trace
%_bindir/ovn-detrace
%dir %_datadir/%oname
%dir %_datadir/%oname/scripts
%_datadir/%oname/scripts/ovn-ctl
%_datadir/%oname/scripts/ovn-lib
%_datadir/%oname/scripts/ovndb-servers.ocf
%_prefix/lib/ocf/resource.d/ovn
%_man8dir/ovn-appctl.*
%_man1dir/ovn-detrace.*
%_man8dir/ovn-ctl.*
%_man8dir/ovn-nbctl.*
%_man8dir/ovn-ic-nbctl.*
%_man8dir/ovn-ic-sbctl.*
%_man8dir/ovn-debug.*
%_man5dir/ovn-ic-nb.*
%_man5dir/ovn-ic-sb.*
%_man8dir/ovn-trace.*
%_man7dir/ovn-architecture.*
%_man8dir/ovn-sbctl.*
%_man5dir/ovn-nb.*
%_man5dir/ovn-sb.*
%dir %attr(0755, openvswitch, openvswitch) %_logdir/%oname
%dir %attr(0755, openvswitch, openvswitch) %_localstatedir/%oname
%_tmpfilesdir/%oname.conf

%files -n lib%name
%_libdir/lib%{oname}*.so.*

%files central
%_bindir/ovn-northd
%_bindir/ovn-ic
%_man8dir/ovn-northd.*
%_man8dir/ovn-ic.*
%_datadir/%oname/ovn-nb.ovsschema
%_datadir/%oname/ovn-sb.ovsschema
%_datadir/%oname/ovn-ic-nb.ovsschema
%_datadir/%oname/ovn-ic-sb.ovsschema
%_unitdir/ovn-northd.service
%_unitdir/ovn-ic.service
%_unitdir/ovn-ic-db.service
%_prefix/lib/firewalld/services/ovn-central-firewall-service.xml

%files host
%_bindir/ovn-controller
%_man8dir/ovn-controller.*
%_unitdir/ovn-controller.service
%_prefix/lib/firewalld/services/ovn-host-firewall-service.xml

%changelog
* Fri Oct 16 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 25.03.3.0.44.caa2a-alt1
- Initial build for ALT.

