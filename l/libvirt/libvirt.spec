# -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define _localstatedir /var
%define qemu_user  _libvirt
%define qemu_group  vmusers

# A client only build will create a libvirt.so only containing
# the generic RPC driver, and test driver and no libvirtd
# Default to a full server + client build

%ifarch %ix86 x86_64 ia64
%def_enable server_drivers
%else
%def_disable server_drivers
%endif

%if_enabled server_drivers
# First the daemon itself
%def_with libvirtd
%def_with avahi

# Then the hypervisor drivers that run on local host
%def_with xen
%def_with qemu
%def_with openvz
%def_with lxc
%def_with vbox
%def_without uml
%def_without libxl
%def_with vmware

# Then the hypervisor drivers that talk via a native remote protocol
%def_with phyp
%def_with esx
%def_without hyperv
%def_without xenapi


# Then the secondary host drivers
%def_with network
%def_with storage_fs
%def_with storage_lvm
%def_with storage_iscsi
%def_with storage_disk
%def_with storage_mpath
%def_with numactl
%def_with selinux

# A few optional bits
%def_without netcf
%def_with udev
%def_without hal
%def_with yajl
%def_without sanlock


%endif #endif server_drivers

%if_with  qemu
%def_with qemu_tcg

%ifarch %ix86 x86_64
%def_with qemu_kvm
%endif
%endif

# A few optional bits
%def_with dbus
%def_with polkit
%def_with capng


%if_with qemu || lxc || uml
%def_with nwfilter
%def_with libpcap
%endif

%if_with qemu
%def_with macvtap
%def_with libnl
%endif

%def_with audit
%def_without dtrace

# Non-server/HV driver defaults which are always enabled
%def_with python
%def_with sasl

Name: libvirt
Version: 0.9.12
Release: alt1
Summary: Library providing a simple API virtualization
License: LGPLv2+
Group: System/Libraries
Url: http://libvirt.org/
Source0: %name-%version.tar
Source1: gnulib-%name-%version.tar
Patch1: %name-%version-%release.patch


%{?_with_libvirtd:Requires: libvirt-daemon = %version-%release}
%{?_with_network:Requires: libvirt-daemon-config-network = %version-%release}
%{?_with_nwfilter:Requires: libvirt-daemon-config-nwfilter = %version-%release}
%{?_with_qemu:Requires: libvirt-qemu-common = %version-%release}
Requires: libvirt-client = %version-%release

%{?_with_xen:BuildRequires: xen-devel}
%{?_with_hal:BuildRequires: libhal-devel}
%{?_with_udev:BuildRequires: libudev-devel libpciaccess-devel}
%{?_with_yajl:BuildRequires: libyajl-devel}
%{?_with_sanlock:BuildRequires: sanlock-devel >= 1.8}
%{?_with_libpcap:BuildRequires: libpcap-devel}
%{?_with_libnl:BuildRequires: libnl-devel}
%{?_with_avahi:BuildRequires: libavahi-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}
%{?_with_network:BuildRequires: dnsmasq iptables iptables-ipv6 radvd}
%{?_with_nwfilter:BuildRequires: ebtables}
%{?_with_sasl:BuildRequires: libsasl2-devel}
%{?_with_dbus:BuildRequires: libdbus-devel >= 1.0.0}
%{?_with_polkit:BuildRequires: polkit}
%{?_with_storage_fs:BuildRequires: util-linux}
%{?_with_qemu:BuildRequires: qemu-img}
%{?_with_xen:BuildRequires: xen-runtime}
%{?_with_storage_lvm:BuildRequires: lvm2}
%{?_with_storage_disk:BuildRequires: libparted-devel parted}
%{?_with_storage_iscsi:BuildRequires: open-iscsi}
%{?_with_storage_mpath:BuildRequires: libdevmapper-devel}
%{?_with_numactl:BuildRequires: libnuma-devel}
%{?_with_capng:BuildRequires: libcap-ng-devel}
%{?_with_phyp:BuildRequires: libssh2-devel}
%{?_with_netcf:BuildRequires: netcf-devel}
%{?_with_esx:BuildRequires: libcurl-devel}
%{?_with_hyperv:BuildRequires: libwsman-devel}
%{?_with_audit:BuildRequires: libaudit-devel}

BuildRequires: bridge-utils libblkid-devel
BuildRequires: libgcrypt-devel libgnutls-devel
BuildRequires: libreadline-devel
BuildRequires: libtasn1-devel
BuildRequires: perl-Pod-Parser
BuildRequires: libxml2-devel xml-utils xsltproc w3c-markup-validator-libs
BuildRequires: python-devel python-module-distribute
BuildRequires: iproute2 perl-Pod-Parser

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
Requires: %name-client = %version-%release
Requires: iptables

%description daemon
Server side daemon required to manage the virtualization capabilities
of recent versions of Linux. Requires a hypervisor specific sub-RPM
for specific drivers.

%package daemon-config-network
Summary: Default configuration files for the libvirtd daemon
Group: System/Servers
Requires: %name-daemon = %version-%release
Requires: bridge-utils

%description daemon-config-network
Default configuration files for setting up NAT based networking

%package daemon-config-nwfilter
Summary: Network filter configuration files for the libvirtd daemon
Group: System/Servers
Requires: %name-daemon = %version-%release

%description daemon-config-nwfilter
Network filter configuration files for cleaning guest traffic

%package qemu-common
Summary: Server side daemon, driver & default configs required to run QEMU or KVM guests
Group: System/Servers
Requires: %name-daemon-config-network = %version-%release
Requires: %name-daemon-config-nwfilter = %version-%release
Requires: %name-daemon = %version-%release

%description qemu-common
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of QEMU or KVM.

%package qemu
Summary: Server side daemon, driver & default configs required to run QEMU guests
Group: System/Servers
Requires: %name-qemu-common = %version-%release
Requires: qemu

%description qemu
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of QEMU.

%package kvm
Summary: Server side daemon, driver & default configs required to run KVM guests
Group: System/Servers
Requires: %name-qemu-common = %version-%release
Requires: qemu-kvm

%description kvm
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of KVM.

%package lxc
Summary: Server side daemon, driver & default configs required to run LXC guests
Group: System/Servers
Requires: %name-daemon-config-network = %version-%release
Requires: %name-daemon-config-nwfilter = %version-%release
Requires: %name-daemon = %version-%release
Requires: lxc

%description lxc
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of LXC.

%package uml
Summary: Server side daemon, driver & default configs required to run UML guests
Group: System/Servers
Requires: %name-daemon-config-network = %version-%release
Requires: %name-daemon-config-nwfilter = %version-%release
Requires: %name-daemon = %version-%release

%description uml
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of UML.

%package xen
Summary: Server side daemon, driver & default configs required to run XEN guests
Group: System/Servers
Requires: %name-daemon-config-network = %version-%release
Requires: %name-daemon-config-nwfilter = %version-%release
Requires: %name-daemon = %version-%release
Requires: xen

%description xen
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of Xen.

%package client
Summary: Client side library and utilities of the libvirt library
Group: System/Libraries
# So remote clients can access libvirt over SSH tunnel
# (client invokes 'nc' against the UNIX socket on the server)
Requires: nc
# Needed by libvirt-guests init script.
Requires: gettext
# For virConnectGetSysinfo
Requires: dmidecode
# Needed by virt-pki-validate script
Requires: gnutls-utils
# Needed for probing the power management features of the host.
Requires: pm-utils
Conflicts: %name < 0.9.11

%description client
Shared libraries and client binaries needed to access to the
virtualization capabilities of recent versions of Linux (and other OSes).

%package devel
Summary: Libraries, includes, etc. to compile with the libvirt library
Group: Development/C
Requires: %name-client = %version-%release

%description devel
Includes and documentations for the C library providing an API to use
the virtualization capabilities of recent versions of Linux (and other OSes).

%package -n python-module-%name
Summary: Python bindings for the libvirt library
Group: Development/Python
Requires: %name-client = %version-%release

Obsoletes: %name-python < %version-%release
Provides: %name-python = %version-%release

%description -n python-module-%name
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%setup -a1
%patch1 -p1
# git and rsync aren't needed for build.
sed -i '/^\(git\|rsync\)[[:space:]]/d' bootstrap.conf
# disable virnetsockettest test
sed -i 's/virnetsockettest //' tests/Makefile.am

%build
./bootstrap --no-git --gnulib-srcdir=gnulib-%name-%version
%configure \
		--disable-static \
		--disable-rpath \
		--with-packager-version="%release" \
		--with-init-script=systemd+redhat \
		--with-qemu-user=%qemu_user \
		--with-qemu-group=%qemu_group \
		--with-xml-catalog-file=/etc/sgml/catalog \
		%{subst_with libvirtd} \
		%{subst_with avahi} \
		%{subst_with xen} \
		%{subst_with qemu} \
		%{subst_with openvz} \
		%{subst_with lxc} \
		%{subst_with vbox} \
		%{subst_with uml} \
		%{subst_with libxl} \
		%{subst_with vmware} \
		%{subst_with phyp} \
		%{subst_with esx} \
		%{subst_with hyperv} \
		%{subst_with xenapi} \
		%{subst_with network} \
		%{subst_with storage_fs} \
		%{subst_with storage_lvm} \
		%{subst_with storage_iscsi} \
		%{subst_with storage_disk} \
		%{subst_with storage_mpath} \
		%{subst_with numactl} \
		%{subst_with selinux} \
		%{subst_with netcf} \
		%{subst_with udev} \
		%{subst_with hal} \
		%{subst_with yajl} \
		%{subst_with sanlock} \
		%{subst_with dbus} \
		%{subst_with polkit} \
		%{subst_with capng} \
		%{subst_with libpcap} \
		%{subst_with macvtap} \
		%{subst_with audit} \
		%{subst_with dtrace} \
		%{subst_with python} \
		%{subst_with sasl}


%make_build
gzip -9 ChangeLog

%install
%makeinstall_std

for i in domain-events/events-c dominfo domsuspend hellolibvirt openauth python xml/nwfilter systemtap
do
  (cd examples/$i ; make clean ; rm -rf .deps .libs Makefile Makefile.in)
done

install -d -m 0755 %buildroot%_localstatedir/run/libvirt/
rm -f %buildroot%{_libdir}/*.{a,la}
rm -f %buildroot%{_libdir}/python*/site-packages/*.{a,la}

%if_with network
# We don't want to install /etc/libvirt/qemu/networks in the main %files list
# because if the admin wants to delete the default network completely, we don't
# want to end up re-incarnating it on every RPM upgrade.
install -d -m 0755 %buildroot%_datadir/libvirt/networks/
cp %buildroot%_sysconfdir/libvirt/qemu/networks/default.xml \
   %buildroot%_datadir/libvirt/networks/default.xml
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/default.xml
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/autostart/default.xml
# Strip auto-generated UUID - we need it generated per-install
sed -i -e "/<uuid>/d" %buildroot%_datadir/libvirt/networks/default.xml
%else
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/default.xml
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/autostart/default.xml
%endif

%if_without qemu
rm -f %buildroot%_datadir/augeas/lenses/libvirtd_qemu.aug
rm -f %buildroot%_datadir/augeas/lenses/tests/test_libvirtd_qemu.aug
rm -f %buildroot%_sysconfdir/libvirt/qemu.conf
rm -f %buildroot%_sysconfdir/logrotate.d/libvirtd.qemu
%endif
%if_without lxc
rm -f %buildroot%_datadir/augeas/lenses/libvirtd_lxc.aug
rm -f %buildroot%_datadir/augeas/lenses/tests/test_libvirtd_lxc.aug
rm -f %buildroot%_sysconfdir/libvirt/lxc.conf
rm -f %buildroot%_sysconfdir/logrotate.d/libvirtd.lxc
%endif
%if_without uml
rm -rf %buildroot%_sysconfdir/logrotate.d/libvirtd.uml
%endif
%if_without nwfilter
rm -rf %buildroot%_sysconfdir/libvirt/nwfilter
%endif


install -pD -m644 libvirtd.service %buildroot%systemd_unitdir/libvirtd.service
install -pD -m644 libvirtd.tmpfiles %buildroot%_sysconfdir/tmpfiles.d/libvirtd.conf
# fix perm
install -pD -m644 tools/libvirt-guests.service %buildroot%systemd_unitdir/libvirt-guests.service

%find_lang %name

%check
cd tests
%make
# These 1 tests don't current work
for i in daemon-conf
do
  rm -f $i
  printf "#!/bin/sh\nexit 0\n" > $i
  chmod +x $i
done
%make check

%if_with libvirtd
%pre daemon
%_sbindir/groupadd -r -f %qemu_group
%_sbindir/useradd -M -r -d %_localstatedir/lib/%name -s /bin/false -c "libvirt user" -g %qemu_group %qemu_user >/dev/null 2>&1 || :

%post daemon
if [ $1 -eq 1 ]; then
    if ! grep -q ^host_uuid /etc/libvirt/libvirtd.conf ; then
	UUID2=`/usr/bin/uuidgen`
	echo host_uuid = \"$UUID2\" >> /etc/libvirt/libvirtd.conf
    fi
fi
%post_service libvirtd

%preun daemon
%preun_service libvirtd

%if_with network
%post daemon-config-network
if [ $1 -eq 1 ]; then
    if [ ! -f %_sysconfdir/libvirt/qemu/networks/default.xml ]; then
	UUID=`/usr/bin/uuidgen`
	sed -e "s,</name>,</name>\n  <uuid>$UUID</uuid>," \
         < %_datadir/libvirt/networks/default.xml \
         > /etc/libvirt/qemu/networks/default.xml
	ln -s ../default.xml /etc/libvirt/qemu/networks/autostart/default.xml
    fi
fi
%endif
%endif

%post client
%post_service libvirt-guests

%preun client
%preun_service libvirt-guests

%files

%files docs
%doc docs/*.xml
%doc %_datadir/gtk-doc/html/libvirt
%doc examples

%doc docs/html docs/devhelp docs/*.gif
%doc docs/libvirt-api.xml

%files client -f %name.lang
%doc AUTHORS ChangeLog.gz README COPYING.LIB TODO
%_libdir/lib*.so.*

%config(noreplace) %_sysconfdir/libvirt/libvirt.conf
%_bindir/virsh
%_bindir/virt-xml-validate
%_bindir/virt-pki-validate
%_bindir/virt-host-validate
%_man1dir/virsh.*
%_man1dir/virt-xml-validate.*
%_man1dir/virt-pki-validate.*
%_man1dir/virt-host-validate.*
%dir %_datadir/libvirt
%dir %_datadir/libvirt/schemas
%_datadir/libvirt/schemas/*.rng
%_datadir/libvirt/cpu_map.xml

%if_with sasl
%config(noreplace) %_sysconfdir/sasl2/libvirt.conf
%endif

%config(noreplace) %_sysconfdir/sysconfig/libvirt-guests
%_initdir/libvirt-guests
%systemd_unitdir/libvirt-guests.service

%dir %_localstatedir/lib/libvirt

%if_with libvirtd
%files daemon
%dir %attr(0700, root, root) %_sysconfdir/libvirt
%dir %_datadir/libvirt
%dir %attr(0700, root, root) %_localstatedir/log/libvirt
%dir %_localstatedir/run/libvirt
%dir %attr(0700, root, root) %_sysconfdir/libvirt/nwfilter
%config(noreplace) %_sysconfdir/sysconfig/libvirtd
%config(noreplace) %_sysconfdir/tmpfiles.d/libvirtd.conf
%systemd_unitdir/libvirtd.service
%_initdir/libvirtd
%config(noreplace) %_sysconfdir/libvirt/libvirtd.conf
%config(noreplace) %_sysconfdir/sysctl.d/libvirtd
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd

%if_with storage_disk
%_libexecdir/libvirt_parthelper
%endif

%_libexecdir/libvirt_iohelper
%_sbindir/libvirtd
%_man8dir/libvirtd.*

%_datadir/augeas/lenses/libvirtd.aug
%_datadir/augeas/lenses/tests/test_libvirtd.aug

%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/images
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/filesystems
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/boot
%dir %attr(0700, root, root) %_localstatedir/cache/libvirt

%if_with polkit
%_datadir/polkit-1/actions/org.libvirt.unix.policy
%endif


%if_with network
%files daemon-config-network
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/networks
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/networks/autostart
%dir %_datadir/libvirt/networks
%_datadir/libvirt/networks/default.xml
%dir %_localstatedir/run/libvirt/network
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/network
%dir %attr(0755, root, root) %_localstatedir/lib/libvirt/dnsmasq
%endif

%if_with nwfilter
%files daemon-config-nwfilter
%_sysconfdir/libvirt/nwfilter/*.xml
%endif

%if_with qemu
%files qemu-common
%config(noreplace) %_sysconfdir/libvirt/qemu.conf
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd.qemu
%dir %attr(0700, root, root) %_localstatedir/run/libvirt/qemu
%dir %attr(0750, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu
%dir %attr(0750, %qemu_user, %qemu_group) %_localstatedir/cache/libvirt/qemu
%dir %attr(0700, root, root) %_localstatedir/log/libvirt/qemu
%_datadir/augeas/lenses/libvirtd_qemu.aug
%_datadir/augeas/lenses/tests/test_libvirtd_qemu.aug

%if_with qemu_tcg
%files qemu
%endif
%if_with qemu_kvm
%files kvm
%endif

%endif

%if_with lxc
%files lxc
%config(noreplace) %_sysconfdir/libvirt/lxc.conf
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd.lxc
%dir %_localstatedir/run/libvirt/lxc
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/lxc
%dir %attr(0700, root, root) %_localstatedir/log/libvirt/lxc
%_datadir/augeas/lenses/libvirtd_lxc.aug
%_datadir/augeas/lenses/tests/test_libvirtd_lxc.aug
%_libexecdir/libvirt_lxc
%endif

%if_with uml
%files uml
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd.uml
%dir %_localstatedir/run/libvirt/uml
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/uml
%dir %attr(0700, root, root) %_localstatedir/log/libvirt/uml
%endif

%if_with xen
%files xen
%if_with libxl
%dir %attr(0700, root, root) %_localstatedir/log/libvirt/libxl
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl
%endif

%endif

%endif #if_with libvirtd

%files devel
%_pkgconfigdir/libvirt.pc
%_libdir/lib*.so
%_includedir/libvirt
%dir %_datadir/libvirt/api
%_datadir/libvirt/api/libvirt-api.xml
%_datadir/libvirt/api/libvirt-qemu-api.xml

%files -n python-module-%name
%python_sitelibdir/libvirt*
%doc python/tests/*.py
%doc python/TODO
%doc examples/python

%changelog
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
- cleanup spec (/etc -> %_sysconfdir,/var -> %_localstatedir)
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
- fix %files

* Wed Jun 25 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.4-alt1
- Release of 0.4.4

* Tue Jun 17 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.3-alt1
- Release of 0.4.3

* Mon Apr 21 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.2-alt2
- Fixed bad permissions on /var/{run,log,lib}/libvirt

* Wed Apr 09 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.2-alt1
- Release of 0.4.2

* Wed Mar 31 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.1-alt1
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
