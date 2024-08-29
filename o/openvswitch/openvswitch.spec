%define _unpackaged_files_terminate_build 1

%def_disable check
%def_with debugtools
# According to the "ExclusiveArch:" from the dpdk.
%ifarch x86_64 %ix86 aarch64 ppc64le
%def_with dpdk
# afxdp build with numa, disable it for arm
# Disable until updating to version v3.1.0 where was added support for building
# with libxdp and libbpf >= 0.7.
%def_enable afxdp
%endif

Name: openvswitch
Version: 3.3.2
Release: alt1

Summary: An open source, production quality, multilayer virtual switch
# All code is Apache-2.0 except
# - lib/sflow* which is SISSL
# - utilities/bugtool which is LGPL-2.1
License: Apache-2.0 AND LGPL-2.1-only AND SISSL
Group: Networking/Other

Url: http://openvswitch.org
Source0: %name-%version.tar
Source11: %name.init
Source12: %name.tmpfiles

Patch0001: 0001-execute-openvswitch-as-openvswitch-user.patch
Patch0003: 0003-ovs-use-strongswan-for-ipsec.patch
Patch0004: 0004-ovs-update-systemd-unit-for-ALT.patch
Patch0005: 0005-ovs-fix-linking.patch
Patch0006: 0006-ovs-Python-3-support.patch
Patch0007: 0007-Use-local-LSB-functions.patch
Patch0008: 0008-Avoid-autoreq-on-systemd-utils.patch

Obsoletes: %name-controller <= 2.3.1-alt1
Obsoletes: %name-ovsdbmonitor <= 2.3.1-alt1
Obsoletes: bash-completion-%name < %EVR
Provides: openvswitch-common = %EVR
Obsoletes: openvswitch-common < 2.14.0-alt1
# force apt to update openvswith with etcnet
Conflicts: etcnet <= 0.9.18

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
%{?_with_dpdk:BuildRequires: dpdk-devel >= 23.11.1 libpcap-devel libnuma-devel rdma-core-devel libmnl-devel}
%{?_enable_afxdp:BuildRequires: libbpf-devel >= 0.7 libxdp-devel libelf-devel libnuma-devel}

%description
Open vSwitch is a production quality, multilayer virtual switch
licensed under the open source Apache 2.0 license. It is designed
to enable massive network automation through programmatic
extension, while still supporting standard management interfaces
and protocols (e.g. NetFlow, sFlow, RSPAN, ERSPAN, CLI, LACP,
802.1ag). In addition, it is designed to support distribution
across multiple physical servers similar to VMware's vNetwork
distributed vswitch or Cisco's Nexus 1000V.

%package -n kernel-source-%name
Group: Development/Kernel
License: GPLv2+
Summary: Open vSwitch Linux kernel modules source
BuildArch: noarch

%description -n kernel-source-%name
Source for kernel modules supporting the openvswitch datapath

%package debugtools
Group: Networking/Other
# All code is Apache-2.0 except
# - utilities/bugtool which is LGPL-2.1
License: Apache-2.0 AND LGPL-2.1-only
Summary: Open vSwitch bug reporting tool
BuildArch: noarch
Requires: %name = %EVR

%description debugtools
This package contains ovs-bugtool to generate a debug bundle
with useful information about Open vSwitch on this system
and place it in %_logdir/ovs-bugtool, and ovs-test to check
Linux drivers for performance and vlan problems.

%package -n lib%name
License: Apache-2.0
Summary: Open vSwitch core libraries
Group: System/Libraries

%description -n lib%name
Contains the shared libraries used by Open vSwitch and any eventual extensions.

%package vtep
Group: Networking/Other
License: Apache-2.0
Summary: Open vSwitch VTEP emulator
Requires: %name = %EVR

%description vtep
A VTEP emulator that uses Open vSwitch for forwarding.

%package -n lib%name-devel
Summary: Open vSwitch Devel Libraries
License: Apache-2.0
Group: Development/C
Requires: lib%name = %EVR
Provides: %name-devel = %EVR
Obsoletes: %name-devel < 2.14.0-alt1

%description -n lib%name-devel
Devel files for Open vSwitch.

%package ipsec
Summary: Open vSwitch IPsec tunneling support
License: Apache-2.0
Group: Networking/Other
BuildArch: noarch
Requires: %name = %EVR
# libreswan
Requires: python3-module-%name = %EVR

%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%package -n python3-module-%name
Summary: Open vSwitch python3 bindings
Group: Development/Python3
License: Apache-2.0
%add_python3_req_skip pywintypes win32con win32file msvcrt

%description -n python3-module-%name
Python3 bindings for the Open vSwitch database

%prep
%setup
%patch0001 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%ifarch %e2k
sed -i "s/__has_extension(c_atomic)/0/" lib/ovs-atomic.h
%endif

%build
export PYTHON3=%__python3
%autoreconf
%configure \
    --disable-static \
    --enable-shared \
    --enable-ndebug \
    --enable-ssl \
    %{subst_enable afxdp} \
%if_with dpdk
    --with-dpdk=shared \
%endif
    --with-rundir=/run/%name \
    --with-logdir=%_logdir/%name \
    --with-dbdir=%_localstatedir/%name \
    --with-pkidir=%_localstatedir/%name/pki

%make_build
make rhel/usr_lib_systemd_system_ovs-vswitchd.service

%install
export PYTHON3=%__python3
%makeinstall_std

install -dm0755 %buildroot%_sysconfdir/%name
install -pDm0755 %SOURCE11 %buildroot%_initdir/%name
install -dm0750 %buildroot%_logdir/%name
install -dm0755 %buildroot%_sysconfdir/%name

install -pDm0644 vswitchd/vswitch.ovsschema \
         %buildroot%_datadir/%name/vswitch.ovsschema
install -pDm0644 rhel/etc_logrotate.d_openvswitch \
         %buildroot%_sysconfdir/logrotate.d/%name
install -pDm0644 rhel/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot%_sysconfdir/sysconfig/%name
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
        %buildroot%_datadir/%name/scripts/ovs-systemd-reload

install -pDm644 %SOURCE12 %buildroot%_tmpfilesdir/%name.conf

install -d -m 0755 %buildroot%python3_sitelibdir_noarch
cp -a %buildroot%_datadir/%name/python/ovstest %buildroot%python3_sitelibdir_noarch

pushd python
export CPPFLAGS="-I ../include"
export LDFLAGS="-L %buildroot%_libdir"
%python3_build
%python3_install
popd

rm -rf %buildroot%_datadir/%name/python

touch %buildroot%_localstatedir/%name/conf.db
touch %buildroot%_sysconfdir/%name/system-id.conf
mkdir -p %buildroot%_logdir/%name

# move completions to datadir
mkdir -p %buildroot%_datadir/bash-completion/completions
mv %buildroot%_sysconfdir/bash_completion.d/* %buildroot%_datadir/bash-completion/completions/

# remove unpackaged files
rm -f %buildroot%_libdir/*.{a,la}
rm -f %buildroot%_bindir/ovs-benchmark \
    %buildroot%_bindir/ovs-parse-backtrace \
    %buildroot%_bindir/ovs-testcontroller \
    %buildroot%_man1dir/ovs-benchmark.* \
    %buildroot%_man8dir/ovs-parse-backtrace.* \
    %buildroot%_man8dir/ovs-testcontroller.*

# test 591 fails, reported upstream
%check
LC_CTYPE=en_US.UTF-8 LC_COLLATE=en_US.UTF-8 make check

%pre
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -n -g %name -d %_localstatedir/%name -M -s /sbin/nologin -c "Open vSwitch Daemons" %name >/dev/null 2>&1 ||:

%post
if [ $1 -eq 2 ] && [ -f %_sysconfdir/openvswitch/system-id.conf ] ; then
    chown %name:%name %_sysconfdir/openvswitch/system-id.conf
    chown -R %name:%name %_localstatedir/%name
    chown -R %name:%name %_logdir/%name
fi
%post_service %name

%preun
%preun_service %name

%post ipsec
%post_service %name-ipsec

%preun ipsec
%preun_service %name-ipsec

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
%_initdir/%name
%_unitdir/%name.service
%_unitdir/ovs-vswitchd.service
%_unitdir/ovsdb-server.service
%_unitdir/ovs-delete-transient-ports.service
%_tmpfilesdir/%name.conf
%_man1dir/ovsdb-client.*
%_man1dir/ovsdb-server.*
%_man1dir/ovsdb-tool.*
%_man5dir/ovs-vswitchd.conf.db.*
%_man5dir/ovsdb.local-config.*
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
%dir %_datadir/%name
%_datadir/%name/local-config.ovsschema
%_datadir/%name/vswitch.ovsschema
%dir %_datadir/%name/scripts
%_datadir/%name/scripts/ovs-check-dead-ifs
%_datadir/%name/scripts/ovs-lib
%_datadir/%name/scripts/ovs-save
%_datadir/%name/scripts/ovs-ctl
%_datadir/%name/scripts/ovs-kmod-ctl
%_datadir/%name/scripts/ovs-systemd-reload
%_datadir/bash-completion/completions/*
%dir %attr(0775, root, %name) %_sysconfdir/openvswitch
%config(noreplace) %attr(0755, %name, %name) %ghost %_sysconfdir/openvswitch/system-id.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/openvswitch/default.conf
%config(noreplace) %_sysconfdir/logrotate.d/openvswitch
%dir %attr(0755, %name, %name) %_logdir/%name
%dir %attr(0755, %name, %name) %_localstatedir/%name
%dir %attr(0755, %name, %name) %_localstatedir/%name/pki
%config(noreplace) %ghost %attr(0644,%name,%name) %verify(not md5 size mtime) %_localstatedir/%name/conf.db

%if_with debugtools
%files debugtools
%_sbindir/ovs-bugtool
%_bindir/ovs-dpctl-top
%_bindir/ovs-pcap
%_bindir/ovs-tcpdump
%_bindir/ovs-tcpundump
%_bindir/ovs-test
%_bindir/ovs-vlan-test
%_bindir/ovs-l3ping
%_datadir/%name/scripts/ovs-bugtool*
%_datadir/%name/bugtool-plugins
# TODO: add this scripts
%exclude %_datadir/%name/scripts/usdt
%_man8dir/ovs-bugtool.*
%_man8dir/ovs-dpctl-top.*
%_man1dir/ovs-pcap.*
%_man8dir/ovs-tcpdump.*
%_man1dir/ovs-tcpundump.*
%_man8dir/ovs-test.*
%_man8dir/ovs-vlan-test.*
%_man8dir/ovs-l3ping.*
%python3_sitelibdir_noarch/ovstest
%endif

# TODO
%files ipsec
#_initdir/openvswitch-ipsec
%_datadir/openvswitch/scripts/ovs-monitor-ipsec
%_unitdir/openvswitch-ipsec.service

%files vtep
%_bindir/vtep-ctl
%_man5dir/vtep.*
%_man8dir/vtep-ctl.*
%_datadir/%name/scripts/ovs-vtep
%_datadir/%name/vtep.ovsschema

%files -n lib%name
%_libdir/libofproto*.so.*
%_libdir/libopenvswitch*.so.*
%_libdir/libovsdb*.so.*
%_libdir/libsflow*.so.*
%_libdir/libvtep*.so.*

%files -n lib%name-devel
%_includedir/openflow
%_includedir/openvswitch
%_libdir/libofproto*.so
%_libdir/libopenvswitch*.so
%_libdir/libovsdb*.so
%_libdir/libsflow*.so
%_libdir/libvtep*.so
%_pkgconfigdir/*.pc

%files -n python3-module-openvswitch
%python3_sitelibdir/ovs
%python3_sitelibdir/ovs-*.egg-info

%changelog
* Thu Aug 29 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.2-alt1
- 3.3.2

* Wed Apr 10 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.0-alt1
- 3.3.0

* Tue Jan 16 2024 Alexey Shabalin <shaba@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Oct 10 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.0-alt1
- 3.2.0 (Fixes: CVE-2023-5366).

* Fri Jul 07 2023 Alexey Shabalin <shaba@altlinux.org> 3.1.2-alt1
- 3.1.2.
- Cleanup spec (remove kernel souce package, xenserver support).
- Enable afxdp.

* Fri Jul 07 2023 Alexey Shabalin <shaba@altlinux.org> 2.17.7-alt1
- 2.17.7

* Tue May 30 2023 Alexey Gladkov <legion@altlinux.ru> 2.17.6-alt2
- Disable afxdp until update v3.1.0.

* Wed May 03 2023 Alexey Shabalin <shaba@altlinux.org> 2.17.6-alt1
- 2.17.6 (Fixes: CVE-2021-3905, CVE-2023-1668, CVE-2022-4337, CVE-2022-4338)

* Mon Nov 29 2021 Alexey Shabalin <shaba@altlinux.org> 2.16.1-alt2
- Avoid autoreq on systemd-utils.

* Tue Nov 23 2021 Alexey Shabalin <shaba@altlinux.org> 2.16.1-alt1
- 2.16.1 (Fixes: CVE-2022-0669, CVE-2021-36980)

* Wed Oct 13 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.14.2-alt2
- fixed build for Elbrus

* Sun Mar 14 2021 Alexey Shabalin <shaba@altlinux.org> 2.14.2-alt1
- 2.14.2 (Fixes: CVE-2020-35498)

* Tue Jan 19 2021 Alexey Shabalin <shaba@altlinux.org> 2.14.1-alt1
- 2.14.1 (Fixes: CVE-2015-8011, CVE-2020-27827)

* Wed Dec 30 2020 Alexey Shabalin <shaba@altlinux.org> 2.14.0-alt4
- Build ipsec subpackage as noarch.

* Sun Dec 27 2020 Alexey Shabalin <shaba@altlinux.org> 2.14.0-alt3
- Fixed post script for update.

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 2.14.0-alt2
- enable NDEBUG
- build with experimental AF_XDP support for OVS netdev

* Thu Sep 24 2020 Alexey Shabalin <shaba@altlinux.org> 2.14.0-alt1
- 2.14.0
- Use strongswan for ipsec
- Execute services with openvswitch user privileges
- Drop openvswitch-common package
- Drop ovn packages
- Rename openvswitch-devel to libopenvswitch-devel
- Add libopenvswitch package

* Fri Jul 10 2020 Anton Farygin <rider@altlinux.ru> 2.12.0-alt5
- openvswitch support for etcnet has been moved to etcnet package

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt4
- Add support vlan for ovsport (ALT #38578)
- Add --may-exist option for ovsbond

* Sun Mar 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt3
- Fixed build with python3.8.

* Sun Mar 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt2
- fixed reload services with systemd

* Fri Nov 01 2019 Alexey Shabalin <shaba@altlinux.org> 2.12.0-alt1
- 2.12.0
- switch use from /var/run to /run
- drop python2 support
- move bash completions to main package
- Build openvswitch with dpdk only for list of supported architectures(arei@)

* Wed Jun 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.11.1-alt1
- 2.11.1

* Tue Mar 12 2019 Alexey Shabalin <shaba@altlinux.org> 2.11.0-alt1
- 2.11.0

* Tue Oct 30 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.1-alt1
- 2.10.1

* Thu Sep 13 2018 Anton Farygin <rider@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Fri Jun 01 2018 Anton Farygin <rider@altlinux.ru> 2.9.2-alt1
- 2.9.2
- removed selinux policy subpackage

* Thu Aug 03 2017 Anton Farygin <rider@altlinux.ru> 2.7.2-alt1
- 2.7.2

* Thu Jul 13 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1 with security fixes:
  + CVE-2017-9214 Buffer overrread in ofputil_pull_queue_get_config_reply10().
  + CVE-2017-9263 remote DoS attack by a malicious switch.
  + CVE-2017-9265 buffer over-read while parsing the group mod OpenFlow message sent from the controller

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- 2.7.0
- build python3 package
- add ovn packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- build branch-2.4

* Tue Feb 03 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- build branch-2.3
- add systemd unit
- drop controller, ovsdbmonitor packages
- add vtep and devel packages
- build with --disable-static and --enable-shared
- fixed link shared libs
- backport upstream patches for devel package

* Fri Dec 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt2
- Add OVS_REMOVE and remove ports and bridges ony if set yes

* Wed Dec 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt1
- Fix runtimedir
- Add %%_datadir/%%name/scripts/ovs-check-dead-ifs
- Add etcnet support
- Fix initscript for etcnet support

* Sat Dec 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- 2.0
- Remove package brcompat (from upstream v1.10.0)
- Add packages ovsdbmonitor and python-module-openvswitch

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Feb 22 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- debugtools subpackage made noarch, optional, and off by default
  (until python part is there)

* Tue Feb 21 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- built for ALT Linux (based on openSUSE 1.2.1-1 spec)
- split into subpackages (largely inspired by debian 1.2.1-3 ones)
- neglected python-related parts for now
- *heavy* spec cleanup, buildreq
- NB: you will need kernel-modules-openvswitch (or linux-3.3+)
