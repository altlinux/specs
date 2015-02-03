# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

# Copyright (C) 2012 Michael Shigorin <mike@altlinux.org>

%def_without check
%def_without ksrc
%def_without xenserver
%def_with debugtools

Name: openvswitch
Version: 2.3.1
Release: alt1

Summary: An open source, production quality, multilayer virtual switch
License: Apache
Group: Networking/Other

Url: http://openvswitch.org
Source0: %url/releases/%name-%version.tar
Source1: %name.init
Source3: 01-%name
Source4: create-ovsbr
Source5: create-ovsbond
Source6: create-ovsport
Source7: destroy-ovsbr
Source8: destroy-ovsbond
Source9: destroy-ovsport
Source10: setup-ovsbr
Source11: %name.service
Source12: %name.tmpfiles

Patch: openvswitch-2.0_alt_fix_function.patch
Patch2: openvswitch-2.3.1-fix-link.patch

# backported patches from upstream
Patch11: 0001-Build-Add-support-for-shared-libraries-and-versioning.patch
Patch12: 0001-lib-Correctly-pass-collected-AM_LDFLAGS-to-linker.patch
Patch13: 0001-include-Use-include--in-public-headers.patch
Patch14: 0001-include-Install-openflow-and-openvswitch-headers.patch
Patch15: 0001-lib-Add-support-for-pkgconfig-for-libopenvswitch.patch
Patch16: 0001-lib-Add-support-for-pkgconfig-for-libofproto.patch
Patch17: 0001-lib-Add-support-for-pkgconfig-for-libovsdb.patch
Patch18: 0001-lib-Add-support-for-pkgconfig-for-libsflow.patch
Patch19: 0001-lib-Add-new-header-openvswitchversionh-to-versioning-info.patch
Patch20: 0001-lib-Add-API-to-set-program-name-and-version.patch
Patch21: 0001-pkg-config-Fix-Cflags-in-package-config-files.patch

Obsoletes: %name-controller <= %name-%version
Obsoletes: %name-ovsdbmonitor <= %name-%version

BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: python-modules python-modules-logging python-modules-xml

%define ksrcdir %_usrsrc/kernel/sources

%description
Open vSwitch is a production quality, multilayer virtual switch
licensed under the open source Apache 2.0 license. It is designed
to enable massive network automation through programmatic
extension, while still supporting standard management interfaces
and protocols (e.g. NetFlow, sFlow, RSPAN, ERSPAN, CLI, LACP,
802.1ag). In addition, it is designed to support distribution
across multiple physical servers similar to VMware's vNetwork
distributed vswitch or Cisco's Nexus 1000V.

%if_with ksrc
%package -n kernel-source-%name
Group: Development/Kernel
License: GPLv2+
Summary: Open vSwitch Linux kernel modules source
BuildArch: noarch

%description -n kernel-source-%name
Source for kernel modules supporting the openvswitch datapath
%endif

%if_with debugtools
%package debugtools
Group: Networking/Other
License: Apache-2.0
Summary: Open vSwitch bug reporting tool
BuildArch: noarch
Requires: %name-common = %version-%release

%description debugtools
This package contains ovs-bugtool to generate a debug bundle
with useful information about Open vSwitch on this system
and place it in %_logdir/ovs-bugtool, and ovs-test to check
Linux drivers for performance and vlan problems.
%endif

%package common
Group: Networking/Other
License: Apache-2.0
Summary: Common Open vSwitch code

%description common
This package provides components required by both openvswitch
and openvswitch-controller.

%package vtep
Group: Networking/Other
License: Apache-2.0
Summary: Open vSwitch VTEP emulator
Requires: %name = %version-%release

%description vtep
A VTEP emulator that uses Open vSwitch for forwarding.

%package devel
Summary: Open vSwitch Devel Libraries
License: Apache-2.0
Group: Development/C
Requires: %name = %version-%release

%description devel
Devel files for Open vSwitch.

%package -n python-module-openvswitch
Summary: Open vSwitch python bindings
Group: Networking/Other
License: Python-2.0
BuildArch: noarch

%description -n python-module-openvswitch
Python bindings for the Open vSwitch database

%prep
%setup
%patch -p0
%patch2 -p1

#upstream patches
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%if_with ksrc
# it's not datapath/linux due to shared configure script; thx led@
pushd ..
mkdir kernel-source-%name-%version
cp -al  %name-%version/{config.h.in,configure,Makefile.in} \
	%name-%version/{build-aux,datapath,include,tests} \
	kernel-source-%name-%version/
tar cf kernel-source-%name-%version.tar kernel-source-%name-%version
rm -r kernel-source-%name-%version
popd
%endif

%build
%autoreconf
%configure \
	--disable-static \
	--enable-shared \
	--with-rundir=%_runtimedir/%name \
	--with-logdir=%_logdir/%name \
	--with-dbdir=%_localstatedir/%name \
	--with-pkidir=%_localstatedir/%name/pki

%make_build

# test 591 fails, reported upstream
%if_with check
%check
LC_CTYPE=en_US.UTF-8 LC_COLLATE=en_US.UTF-8 make check
%endif

%install
%makeinstall_std

%if_with ksrc
mkdir -p %buildroot%ksrcdir
install -pm644 ../kernel-source-%name-%version.tar %buildroot%ksrcdir/
%endif

install -dm755 %buildroot%_sysconfdir/%name
install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm644 vswitchd/vswitch.ovsschema \
         %buildroot%_datadir/%name/vswitch.ovsschema
install -pDm644 xenserver/etc_logrotate.d_openvswitch \
         %buildroot%_sysconfdir/logrotate.d/%name
install -pDm644 xenserver/etc_profile.d_openvswitch.sh \
         %buildroot%_sysconfdir/profile.d/openvswitch.sh
install -pDm644 xenserver/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot%_sysconfdir/sysconfig/%name
#etcnet
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/net/options.d/01-openvswitch
install -pDm755 %SOURCE4 %buildroot%_sysconfdir/net/scripts/create-ovsbr
install -pDm755 %SOURCE5 %buildroot%_sysconfdir/net/scripts/create-ovsbond
install -pDm755 %SOURCE6 %buildroot%_sysconfdir/net/scripts/create-ovsport
install -pDm755 %SOURCE7 %buildroot%_sysconfdir/net/scripts/destroy-ovsbr
install -pDm755 %SOURCE8 %buildroot%_sysconfdir/net/scripts/destroy-ovsbond
install -pDm755 %SOURCE9 %buildroot%_sysconfdir/net/scripts/destroy-ovsport
install -pDm755 %SOURCE10 %buildroot%_sysconfdir/net/scripts/setup-ovsbr

install -pDm644 %SOURCE11 %buildroot%_unitdir/%name.service
install -pDm644 %SOURCE12 %buildroot%_tmpfilesdir/%name.conf

# FIXME
%if_with xenserver
install -pDm755 xenserver/etc_init.d_openvswitch-xapi-update \
         %buildroot%_initdir/openvswitch-xapi-update
install -pDm755 xenserver/etc_xapi.d_plugins_openvswitch-cfg-update \
         %buildroot%_sysconfdir/xapi.d/plugins/openvswitch-cfg-update
install -pDm755 xenserver/opt_xensource_libexec_interface-reconfigure \
             %buildroot%_datadir/%name/scripts/interface-reconfigure
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigure.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigure.py
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigureBridge.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigureBridge.py
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigureVswitch.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigureVswitch.py
install -pDm755 xenserver/etc_xensource_scripts_vif \
             %buildroot%_datadir/%name/scripts/vif
install -pDm644 xenserver/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot%_datadir/%name/scripts/sysconfig.template
install -pDm644 \
        xenserver/usr_lib_xsconsole_plugins-base_XSFeatureVSwitch.py \
               %buildroot%_libdir/xsconsole/plugins-base/XSFeatureVSwitch.py
%endif

install -d -m 0755 %buildroot%python_sitelibdir_noarch
mv %buildroot%_datadir/%name/python/* %buildroot%python_sitelibdir_noarch

touch %buildroot%_sysconfdir/%name/conf.db
touch %buildroot%_sysconfdir/%name/system-id.conf

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS DESIGN INSTALL.* NOTICE
%doc REPORTING-BUGS NEWS PORTING
%doc CodingStyle README README-lisp
%doc WHY-OVS COPYING
%_bindir/ovs-dpctl
%_bindir/ovs-dpctl-top
%_bindir/ovs-pcap
%_bindir/ovs-tcpundump

%_bindir/ovs-vsctl
%_bindir/ovsdb-tool
%_sbindir/ovs-vlan-bug-workaround
%_sbindir/ovs-vswitchd
%_sbindir/ovsdb-server
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%_man1dir/ovs-pcap.1*
%_man1dir/ovs-tcpundump.1*
%_man1dir/ovsdb-server.1*
%_man1dir/ovsdb-tool.1*
%_man5dir/ovs-vswitchd.conf.db.5*
%_man8dir/ovs-ctl.8*
%_man8dir/ovs-dpctl.8*
%_man8dir/ovs-dpctl-top.8*
%_man8dir/ovs-vlan-bug-workaround.8*

%_man8dir/ovs-vsctl.8*
%_man8dir/ovs-vswitchd.8*

%_datadir/%name/vswitch.ovsschema
%_datadir/%name/scripts/ovs-lib
%_datadir/%name/scripts/ovs-save
%_datadir/%name/scripts/ovs-ctl
%_datadir/%name/scripts/ovs-check-dead-ifs
%dir %_sysconfdir/openvswitch
%config(noreplace) %ghost %_sysconfdir/openvswitch/conf.db
%config(noreplace) %ghost %_sysconfdir/openvswitch/system-id.conf
%config(noreplace) %_sysconfdir/profile.d/openvswitch.sh
%config(noreplace) %_sysconfdir/sysconfig/%name
%config %_sysconfdir/logrotate.d/openvswitch
%config(noreplace) %_sysconfdir/net/options.d/01-openvswitch
%_sysconfdir/net/scripts/*

%if_with debugtools
%files debugtools
%_bindir/ovs-test
%_bindir/ovs-vlan-test
%_bindir/ovs-l3ping
%_sbindir/ovs-bugtool
%_man8dir/ovs-bugtool.8*
%_man8dir/ovs-l3ping.8*
%_man8dir/ovs-test.8*
%_man8dir/ovs-vlan-test.8*
%_datadir/%name/bugtool-plugins/
%_datadir/%name/scripts/ovs-bugtool*
%python_sitelibdir_noarch/ovstest
%endif

%files common
%_logdir/%name
%_localstatedir/%name
%_runtimedir/%name
%_libdir/*.so.*
%_bindir/ovs-appctl
%_bindir/ovs-benchmark
%_bindir/ovs-ofctl
%_bindir/ovs-parse-backtrace
%_bindir/ovs-pki
%_bindir/ovsdb-client
%_man1dir/ovs-benchmark.1*
%_man1dir/ovsdb-client.1*
%_man8dir/ovs-appctl.8*
%_man8dir/ovs-ofctl.8*
%_man8dir/ovs-parse-backtrace.8*
%_man8dir/ovs-pki.8*

# TODO
#files ipsec
#_initdir/openvswitch-ipsec

#if_with xenserver
#files xenserver
#_initdir/openvswitch-xapi-update
#dir %_sysconfdir/xapi.d
#dir %dir %_sysconfdir/xapi.d/plugins
#_sysconfdir/xapi.d/plugins/openvswitch-cfg-update
#dir %_libdir/xsconsole/
#dir %_libdir/xsconsole/plugins-base/
#_libdir/xsconsole/plugins-base/XSFeatureVSwitch.py*
#_datadir/%name/scripts/InterfaceReconfigure.py
#_datadir/%name/scripts/InterfaceReconfigureBridge.py
#_datadir/%name/scripts/InterfaceReconfigureVswitch.py
#_datadir/%name/scripts/interface-reconfigure
#_datadir/%name/scripts/vif
#endif

%files vtep
%_bindir/vtep-ctl
%_man5dir/vtep.5.*
%_man8dir/vtep-ctl.8.*
%_datadir/%name/scripts/ovs-vtep
%_datadir/%name/vtep.ovsschema

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n python-module-openvswitch
%python_sitelibdir_noarch/ovs
#python_sitelibdir_noarch/uuid.py

%if_with ksrc
%files -n kernel-source-%name
%ksrcdir/*
%endif

%changelog
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
- Add %_datadir/%name/scripts/ovs-check-dead-ifs
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
