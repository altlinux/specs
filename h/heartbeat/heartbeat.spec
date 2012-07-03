%define ENABLE_SNMP_SUBAGENT 0
%define ENABLE_MGMT 1
%define gname haclient
%define uname hacluster
# XXX FIXME!
#%%define _localstatedir %%_var
%define _libha_dir %_libdir/%name
%define _ha_coredir %_var/lib/%name/cores
%define _ocf_ra_dir /usr/lib/ocf/resource.d

%def_disable static

Summary: Heartbeat subsystem for High-Availability Linux
Name: heartbeat
Version: 2.1.3
Release: alt5.1
License: GPL/LGPL
Url: http://linux-ha.org/
Group: System/Servers
Source: http://linux-ha.org/download/%name-%version.tar
Source1: heartbeat.init.alt
Source2: ldirectord.init.alt

BuildRequires(pre): rpm-build-linux-ha
# Automatically added by buildreq on Thu Oct 16 2008
BuildRequires: bzlib-devel flex glib2-devel iputils libgnutls-devel libltdl-devel libncurses-devel libnet-snmp-devel libnet2-devel libpam-devel libuuid-devel libxml2-devel python-devel swig perl-Pod-Parser zlib-devel
%if %ENABLE_MGMT
Requires: gettext
%endif

#For hb_report
Requires: perl-TimeDate

Requires: %_ha_dir
# XXX hack for %_libdir/ocf/resource.d/heartbeat/ClusterMon
#Provides: %_libdir/%name/crm_mon
# XXX hack for findreq-python
%add_python_req_skip _pymgmt
%add_python_req_skip pymgmt
%add_findreq_skiplist %_ocf_ra_dir/*
%add_findreq_skiplist %_libdir/stonith/plugins/*/*
# We haven't perl module Authen::Radius
%add_findreq_skiplist %_sbindir/ldirectord

%description
heartbeat is a basic high-availability subsystem for Linux-HA.
It will run scripts at initialization, and when machines go up or down.
This version will also perform IP address takeover using gratuitous ARPs.
It supports "n-node" clusters with significant capabilities for managing
resources and dependencies.

In addition it continues to support the older release 1 style of
2-node clustering.

It implements the following kinds of heartbeats:
        - Serial ports
        - UDP/IP multicast (ethernet, etc)
        - UDP/IP broadcast (ethernet, etc)
        - UDP/IP heartbeats
        - "ping" heartbeats (for routers, switches, etc.)
           (to be used for breaking ties in 2-node systems)

%package -n heartbeat-gui
Summary: gui interface
Group: System/Servers
Requires: python-module-pygtk >= 2.4
Requires: python-module-pygtk-libglade

%description -n heartbeat-gui
GUI for management heartbeat cluster. Works with R2-style configurations.

%package devel
Summary: Heartbeat development package
Group: Development/C
Requires: heartbeat = %version-%release

%description devel
Heartbeat development package.

%package devel-static
Summary: Heartbeat static libs
Group: Development/C

%description devel-static
Heartbeat static libs.

%prep
%setup -q
#%%patch0 -p1

%build
%autoreconf
# disable-fatal-warnings flag used to disable gcc4.x warnings of 'difference in signedness'
CFLAGS="%optflags" \
%configure \
 --disable-fatal-warnings \
%if %ENABLE_MGMT
  --enable-mgmt \
%else
  --disable-mgmt \
%endif
  --localstatedir=/var \
  %{subst_enable static}
%make DESTDIR=%buildroot

%install
%make install DESTDIR=%buildroot
#(
#  cd %buildroot%_sysconfdir/ha.d/resource.d
#  ln -s %_sbindir/ldirectord ldirectord
#)

# cleanup
[ -d %%buildroot%%_initdir ] && rm -rf %%buildroot%%_initdir/*
#[ -d %%buildroot/usr/man ] && rm -rf %%buildroot/usr/man
#[ -d %%buildroot%_datadir/libtool ] && rm -rf %%buildroot%_datadir/libtool
find %buildroot -type f -name *.la -exec rm -f {} ';'

%__subst '1i# -*-Shell-script-*-' %buildroot%_libdir/heartbeat/ocf-shellfuncs
%__subst '1i# -*-Shell-script-*-' %buildroot%_sysconfdir/ha.d/shellfuncs
#chmod -x %buildroot%_libdir/heartbeat/ocf-shellfuncs
#chmod -x %buildroot%_sysconfdir/ha.d/shellfuncs
#chmod -x %buildroot%_libdir/heartbeat/pymgmt.py
install -pD -m755 %SOURCE1  %buildroot%_initdir/heartbeat
install -pD -m755 %SOURCE2  %buildroot%_initdir/ldirectord
install -d -m755 %buildroot/%_ha_coredir
install -d %buildroot/%_ha_coredir/root
install -d %buildroot/%_ha_coredir/nobody
install -d %buildroot/%_ha_coredir/%gname
install -d -m755 %buildroot/%_var/run/%name
install -d %buildroot/%_var/run/%name/ccm
install -d %buildroot/%_var/run/%name/crm
install -d %buildroot/%_var/lib/%name/crm
install -d %buildroot/%_var/lib/%name/pengine

%pre
%_sbindir/groupadd -r -f %gname &>/dev/null || :
%_sbindir/useradd -r -n -s /dev/null -d %_var/lib/heartbeat/cores/hacluster -M \
        -c 'heartbeat user' -g %gname %uname &>/dev/null || :

%post
%post_service heartbeat
%post_service ldirectord

%preun
%preun_service heartbeat
%preun_service ldirectord

%files
%_ha_dir/harc
%_ha_dir/shellfuncs
%_ha_dir/rc.d
%_ha_dir/README.config
%_libdir/libapphb.so.*
%_libdir/libccmclient.so.*
%_libdir/libcib.so.*
%_libdir/libclm.so.*
%_libdir/libcrmcommon.so.*
%_libdir/libtransitioner.so.*
%_libdir/libhbclient.so.*
%_libdir/liblrm.so.*
%_libdir/libpengine.so.*
%_libdir/libplumb.so.*
%_libdir/libplumbgpl.so.*
%_libdir/librecoverymgr.so.*
%_libdir/libstonithd.so.*
%_libdir/libpe_rules.so.*
%_libdir/libpe_status.so.*
%_libdir/%name/BasicSanityCheck
%_libdir/%name/ResourceManager
%_libdir/%name/TestHeartbeatComm
%_libdir/%name/api_test
%_libdir/%name/apphbd
%_libdir/%name/apphbtest
%_libdir/%name/atest
%_libdir/%name/attrd
%_libdir/%name/base64_md5_test
%_libdir/%name/ccm
%_libdir/%name/ccm_testclient
%_libdir/%name/cib
%_libdir/%name/cibmon
%_libdir/%name/clmtest
%_libdir/%name/crm.dtd
%_libdir/%name/crm_commands.py
%_libdir/%name/crm_commands.pyc
%_libdir/%name/crm_commands.pyo
%_libdir/%name/crm_primitive.py
%_libdir/%name/crm_primitive.pyc
%_libdir/%name/crm_primitive.pyo
%_libdir/%name/crm_utils.py
%_libdir/%name/crm_utils.pyc
%_libdir/%name/crm_utils.pyo
%_libdir/%name/crmd
%_libdir/%name/cts
%_libdir/%name/dopd
%_libdir/%name/drbd-peer-outdater
%_libdir/%name/findif
%_libdir/%name/ha_config
%_libdir/%name/ha_logd
%_libdir/%name/ha_logger
%_libdir/%name/ha_propagate
%_libdir/%name/haresources2cib.py
%_libdir/%name/hb_addnode
%_libdir/%name/hb_delnode
%_libdir/%name/hb_setsite
%_libdir/%name/hb_setweight
%_libdir/%name/hb_standby
%_libdir/%name/hb_takeover
%_libdir/%name/heartbeat
%_libdir/%name/ipctest
%_libdir/%name/ipctransientclient
%_libdir/%name/ipctransientserver
%_libdir/%name/ipfail
%_libdir/%name/logtest
%_libdir/%name/lrmadmin
%_libdir/%name/lrmd
%_libdir/%name/lrmtest
%_libdir/%name/mach_down
%_libdir/%name/mgmtd
%_libdir/%name/mgmtdtest
%_libdir/%name/mlock
%_libdir/%name/ocf-returncodes
%_libdir/%name/ocf-shellfuncs
%_libdir/%name/pengine
%_libdir/%name/pingd
%_libdir/%name/quorumd
%_libdir/%name/quorumdtest
%_libdir/%name/recoverymgrd
%_libdir/%name/req_resource
%_libdir/%name/send_arp
%_libdir/%name/stonithd
%_libdir/%name/stonithdtest/apitest
%_libdir/%name/tengine
%_libdir/%name/transient-test.sh
%_libdir/%name/ttest
%_libdir/%name/utillib.sh
%_ha_dir/resource.d/
%config(noreplace) %_initdir/heartbeat
%config(noreplace) %_sysconfdir/logrotate.d/heartbeat
%_var/lib/%name
#%%_ha_coredir
%attr (0700, root, root) %_ha_coredir/root
%attr (0700, nobody, root) %_ha_coredir/nobody
%attr (0700, %uname, root) %_ha_coredir/%uname
%_var/run/%name
%attr (0755, %uname, %gname) %_bindir/cl_status
%_datadir/%name/BasicSanityCheck
%_datadir/%name/ResourceManager
%_datadir/%name/TestHeartbeatComm
%_datadir/%name/crm.dtd
%_datadir/%name/ha_*
%_datadir/%name/hb_*
%_datadir/%name/mach_down
%_datadir/%name/req_resource
%_datadir/%name/utillib.sh
%_bindir/cl_respawn
%_sbindir/ciblint
%_sbindir/ptest
%_sbindir/crmadmin
%_sbindir/cibadmin
%_sbindir/ccm_tool
%_sbindir/crm_diff
%_sbindir/crm_uuid
%_sbindir/crm_mon
%_sbindir/ocf-tester
%_sbindir/hb_report
%_sbindir/iso8601
%_sbindir/crm_master
%_sbindir/crm_standby
%_sbindir/crm_attribute
%_sbindir/crm_resource
%_sbindir/crm_verify
%_sbindir/attrd_updater
%_sbindir/crm_failcount
%_sbindir/crm_sh
%_sbindir/ha_logger
%attr (750, %uname, %gname) %_var/lib/%name/crm
%attr (750, %uname, %gname) %_var/lib/%name/pengine
%_ocf_ra_dir/%name
%_datadir/%name/cts
%_datadir/%name/lrmtest
%_man1dir/cl_status.1*
%_man1dir/ha_logger.1*
%_man1dir/hb_standby.1*
%_man1dir/hb_takeover.1*
%_man1dir/hb_addnode.1*
%_man1dir/hb_delnode.1*
%_man8dir/crm_resource.8*
%_man8dir/heartbeat.8*
%_man8dir/apphbd.8*
%_man8dir/ha_logd.8*
%_man8dir/cibadmin.8*
%if %ENABLE_SNMP_SUBAGENT
	%MIBS_DIR/LINUX-HA-MIB.mib
%endif
%if %ENABLE_MGMT
	%_libdir/libhbmgmt.*
	%_libdir/libhbmgmtclient.*
	%_libdir/libhbmgmtcommon.*
	%_libdir/libhbmgmttls.*
	%_sysconfdir/pam.d/hbmgmtd
#	%%exclude %%_datadir/heartbeat-gui
#	%%exclude %%_libdir/heartbeat-gui
%endif
%_sbindir/ldirectord
%_sysconfdir/logrotate.d/ldirectord
%_initdir/ldirectord
%_ha_dir/resource.d/ldirectord
%_ocf_ra_dir/heartbeat/ldirectord
%_man8dir/ldirectord.8*
%doc ldirectord/ldirectord.cf
%doc doc/AUTHORS
%doc doc/ChangeLog
%doc doc/README
%_libdir/libstonith.*
%_libdir/stonith
%_sbindir/stonith
%_sbindir/meatclient
%_datadir/%name/stonithdtest/STONITHDBasicSanityCheck
%_man8dir/stonith.8*
%_man8dir/meatclient.8*
%_libdir/libpils.*
%_libdir/pils/plugins
%_libdir/%name/plugins

%if %ENABLE_MGMT
%files -n %name-gui
%_libdir/%name-gui
%_datadir/%name-gui
%_bindir/hb_gui
%_datadir/locale/zh_CN/LC_MESSAGES/haclient.mo
%endif

%files -n %name-devel
%_includedir/heartbeat/
%_includedir/clplumbing/
%_includedir/saf/
%_includedir/ocf/
%_includedir/stonith/
%_includedir/pils/
%_libdir/libapphb.so
%_libdir/libccmclient.so
%_libdir/libcib.so
%_libdir/libclm.so
%_libdir/libcrmcommon.so
%_libdir/libtransitioner.so
%_libdir/libhbclient.so
%_libdir/liblrm.so
%_libdir/libpengine.so
%_libdir/libplumb.so
%_libdir/libplumbgpl.so
%_libdir/librecoverymgr.so
%_libdir/libstonithd.so
%_libdir/libpe_rules.so
%_libdir/libpe_status.so

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif #static

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt5.1
- Rebuild with Python-2.7

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 2.1.3-alt5
- Fix build: add zlib-devel to BR.

* Mon Nov 15 2010 Mikhail Efremov <sem@altlinux.org> 2.1.3-alt4
- added perl-TimeDate requires (for hb_report).
- fix build: add perl-Pod-Parser to build reqiures.
- drop Packager from spec.

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt3.1
- Rebuilt with python 2.6

* Mon Sep 21 2009 Mikhail Efremov <sem@altlinux.org> 2.1.3-alt3
- remove obsoleted constructions (used rpmcs).
- fix build.
- Taken from orphaned

* Thu Oct 16 2008 Vitaly A. Ostanin <vyt@altlinux.ru> 2.1.3-alt2
- Taken from orphaned
- Fixed build and now works both in R1 and R2 style cluster
- Merged subpackages to main package (pils, stonith, ldirectord)
- Fixed init script
- Updated buildreqs

* Thu Jan 31 2008 Lebedev Sergey <barabashka@altlinux.org> 2.1.3-alt1
- new version
  + fix build

* Tue Dec 19 2006 L.A. Kostis <lakostis@altlinux.ru> 2.0.7-alt2.1
- Apply patch from Eugene Prokopiev <enp (fix for altbug #10455):
  - add %_ha_resource_dir/hto-mapfuncs and %_ha_resource_dir/Filesystem to
    heartbeat package

* Sat Dec 02 2006 L.A. Kostis <lakostis@altlinux.ru> 2.0.7-alt2
- release for Sisyphus.
- add dependency to linux-ha-common and remove directory intersections.
- Added patches:
  + heartbeat-alt-deps.patch - remove extra deps from BuildChecks scripts
    (tnx to Eugene Prokopiev);

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 2.0.7-alt1
- Version 2.0.7.
- remove obsoleted patches from Fedora.
- update -alt-build patch.
- update .spec for new files/layout changes.
- update buildrequires.

* Sun Apr 23 2006 LAKostis <lakostis at altlinux.org> 2.0.4-alt1
- First build for ALTLinux;
- fix build with --as-needed;
- rewrite/cleanup init.d scripts (FIXME! need more work);
- .spec based on 2.0.4-2 FC6 package.

