
%def_without check
%def_without ksrc
%def_without xenserver
%def_with debugtools

Name: openvswitch
Version: 2.5.1
Release: alt1

Summary: An open source, production quality, multilayer virtual switch
License: ASL 2.0 and LGPLv2+ and SISSL
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

Patch1: %name-%version-%release.patch
Patch2: openvswitch-2.0_alt_fix_function.patch
Patch3: openvswitch-2.5.0-fix-link.patch

Obsoletes: %name-controller <= %name-%version
Obsoletes: %name-ovsdbmonitor <= %name-%version

BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: libcap-ng-devel
BuildRequires: glibc-kernheaders
BuildRequires: python-modules python-modules-logging python-modules-xml
BuildRequires: checkpolicy selinux-policy-devel

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
License: ASL 2.0
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
License: ASL 2.0 and LGPLv2+ and SISSL
Summary: Common Open vSwitch code

%description common
This package provides components required by both openvswitch
and openvswitch-controller.

%package vtep
Group: Networking/Other
License: ASL 2.0
Summary: Open vSwitch VTEP emulator
Requires: %name = %version-%release

%description vtep
A VTEP emulator that uses Open vSwitch for forwarding.

%package devel
Summary: Open vSwitch Devel Libraries
License: ASL 2.0
Group: Development/C
Requires: %name = %version-%release

%description devel
Devel files for Open vSwitch.

%package -n python-module-%name
Summary: Open vSwitch python bindings
Group: Networking/Other
License: Python-2.0
BuildArch: noarch

%description -n python-module-%name
Python bindings for the Open vSwitch database

%package -n bash-completion-%name
Summary: Bash completion for systemd utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %EVR

%description -n bash-completion-%name
Bash completion for %name.

%package selinux-policy
Summary: Open vSwitch SELinux policy
Group: System/Base
License: ASL 2.0
BuildArch: noarch
Requires: selinux-policy-targeted

%description selinux-policy
Tailored Open vSwitch SELinux policy

%prep
%setup
%patch1 -p1
%patch2 -p0
%patch3 -p1

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
	--enable-ssl \
	--with-rundir=%_runtimedir/%name \
	--with-logdir=%_logdir/%name \
	--with-dbdir=%_localstatedir/%name \
	--with-pkidir=%_localstatedir/%name/pki

%make_build

cd selinux
make -f %_datadir/selinux/devel/Makefile

# test 591 fails, reported upstream
%if_with check
%check
LC_CTYPE=en_US.UTF-8 LC_COLLATE=en_US.UTF-8 make check
%endif

%install
%makeinstall_std

%if_with ksrc
mkdir -p %buildroot%ksrcdir
install -pm0644 ../kernel-source-%name-%version.tar %buildroot%ksrcdir/
%endif

install -dm0755 %buildroot%_sysconfdir/%name
install -pDm0755 %SOURCE1 %buildroot%_initdir/%name
install -pDm0644 vswitchd/vswitch.ovsschema \
         %buildroot%_datadir/%name/vswitch.ovsschema
install -pDm0644 rhel/etc_logrotate.d_openvswitch \
         %buildroot%_sysconfdir/logrotate.d/%name
install -pDm0644 rhel/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot/%_sysconfdir/sysconfig/%name

# without ovn services ovn-controller ovn-controller-vtep ovn-northd
for service in openvswitch ovsdb-server ovs-vswitchd ; do
    install -pDm0644 \
            rhel/usr_lib_systemd_system_${service}.service \
            %buildroot%_unitdir/${service}.service
done

#etcnet
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/net/options.d/01-openvswitch
install -pDm755 %SOURCE4 %buildroot%_sysconfdir/net/scripts/create-ovsbr
install -pDm755 %SOURCE5 %buildroot%_sysconfdir/net/scripts/create-ovsbond
install -pDm755 %SOURCE6 %buildroot%_sysconfdir/net/scripts/create-ovsport
install -pDm755 %SOURCE7 %buildroot%_sysconfdir/net/scripts/destroy-ovsbr
install -pDm755 %SOURCE8 %buildroot%_sysconfdir/net/scripts/destroy-ovsbond
install -pDm755 %SOURCE9 %buildroot%_sysconfdir/net/scripts/destroy-ovsport
install -pDm755 %SOURCE10 %buildroot%_sysconfdir/net/scripts/setup-ovsbr

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

install -p -m 644 -D selinux/openvswitch-custom.pp \
        %buildroot%_datadir/selinux/packages/%name/openvswitch-custom.pp

# remove unpackaged files
rm -f %buildroot%_bindir/ovs-benchmark \
    %buildroot%_bindir/ovs-parse-backtrace \
    %buildroot%_bindir/ovs-pcap \
    %buildroot%_bindir/ovs-tcpundump \
    %buildroot%_sbindir/ovs-vlan-bug-workaround \
    %buildroot%_man1dir/ovs-benchmark.1* \
    %buildroot%_man8dir/ovs-parse-backtrace.8* \
    %buildroot%_man1dir/ovs-pcap.1* \
    %buildroot%_man1dir/ovs-tcpundump.1* \
    %buildroot%_man8dir/ovs-vlan-bug-workaround.8* \
    %buildroot%_datadir/openvswitch/scripts/ovs-save

# OVN disabled for now by upstream request
find $RPM_BUILD_ROOT -name "ovn-*" | xargs rm -f

%post
%post_service %name

%preun
%preun_service %name

%post selinux-policy
/usr/sbin/semodule -i %_datadir/selinux/packages/%name/openvswitch-custom.pp &> /dev/null || :

%postun selinux-policy
if [ $1 -eq 0 ] ; then
  /usr/sbin/semodule -r openvswitch-custom &> /dev/null || :
fi

%files
%doc AUTHORS DESIGN.md INSTALL.* NOTICE
%doc REPORTING-BUGS.md NEWS PORTING.md
%doc CodingStyle.md README.md README-lisp.md FAQ.md
%doc WHY-OVS.md COPYING
%_bindir/ovs-dpctl
%_bindir/ovs-dpctl-top
%_bindir/ovs-testcontroller
%_bindir/ovs-docker
%_bindir/ovs-vsctl
%_bindir/ovsdb-tool
%_sbindir/ovs-vswitchd
%_sbindir/ovsdb-server
%_initdir/%name
%_unitdir/%name.service
%_unitdir/ovs-vswitchd.service
%_unitdir/ovsdb-server.service
%_tmpfilesdir/%name.conf
%_man1dir/ovsdb-server.1*
%_man1dir/ovsdb-tool.1*
%_man5dir/ovs-vswitchd.conf.db.5*
%_man8dir/ovs-ctl.8*
%_man8dir/ovs-dpctl.8*
%_man8dir/ovs-dpctl-top.8*
%_man8dir/ovs-testcontroller.8*
%_man8dir/ovs-vsctl.8*
%_man8dir/ovs-vswitchd.8*

%_datadir/%name/vswitch.ovsschema
%_datadir/%name/scripts/ovs-lib
%_datadir/%name/scripts/ovs-ctl
%_datadir/%name/scripts/ovs-check-dead-ifs
%dir %_sysconfdir/openvswitch
%config(noreplace) %ghost %_sysconfdir/openvswitch/conf.db
%config(noreplace) %ghost %_sysconfdir/openvswitch/system-id.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/logrotate.d/openvswitch
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
%_bindir/ovs-ofctl
%_bindir/ovs-pki
%_bindir/ovsdb-client
%_man1dir/ovsdb-client.1*
%_man8dir/ovs-appctl.8*
%_man8dir/ovs-ofctl.8*
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
%doc vtep/README.ovs-vtep.md
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

%files selinux-policy
%_datadir/selinux/packages/%name/openvswitch-custom.pp

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/*

%if_with ksrc
%files -n kernel-source-%name
%ksrcdir/*
%endif

%changelog
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
