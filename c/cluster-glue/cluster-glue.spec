Name: cluster-glue
Summary: Reusable cluster components
Version: 1.0.12
Release: alt1
License: GPLv2+ and LGPLv2+
Url: http://www.linux-ha.org/wiki/Cluster_Glue
Group: System/Base
# hg clone http://hg.linux-ha.org/glue
Source: %name-%version.tar

Obsoletes: heartbeat < 2.1.4
Conflicts: heartbeat < 2.1.4

Requires: resource-agents

# Automatically added by buildreq on Fri Mar 29 2013
# optimized out: libgpg-error libnet-snmp30 libssl-devel libwrap-devel net-snmp-config perl-Encode perl-Locale-gettext perl-podlators pkg-config python-base python-modules xml-common
BuildRequires: bzlib-devel docbook-dtds docbook-style-xsl glib2-devel help2man libcorosync2-devel libcurl-devel libltdl7-devel libnet-snmp-devel libnet-devel libopenipmi-devel libuuid-devel libxml2-devel python-devel xsltproc zlib-devel setproctitle-devel libaio-devel

BuildPreReq: perl-podlators asciidoc libsocket-devel libesmtp-devel
BuildPreReq: libucd-snmp-devel asciidoc-a2x

%define gname haclient
%define uname hacluster
%define nogroup nobody

# Directory where we install documentation
%define glue_docdir %_defaultdocdir/%name-%version

%add_findreq_skiplist */stonith/plugins/external/ibmrsa
%add_findreq_skiplist */stonith/plugins/external/sbd
%add_findreq_skiplist */cibsecret
%add_findreq_skiplist */xen0-ha-dom0-stonith-helper

%description
A collection of common tools that are useful for writing cluster managers
such as Pacemaker.
Provides a local resource manager that understands the OCF and LSB
standards, and an interface to common STONITH devices.

%package logd
License: GPLv2+ and LGPLv2+
Summary: Non-blocking log service
Group: System/Servers

%description logd
Non-blocking log service

%package stonith
License: GPLv2+ and LGPLv2+
Summary: A mechanism for node fencing
Group: System/Servers

%description stonith
In case a node is considered "dead" by the cluster as a whole, STONITH ("Shoot The Other Node In The Head") forcefully removes
is from the cluster so it can no longer pose a risk of interacting with other nodes in an uncoordinated fashion.

%package -n lib%name
Summary: Reusable cluster libraries
Group: System/Libraries
Obsoletes: libheartbeat2

%description -n lib%name
A collection of libraries that are useful for writing cluster managers
such as Pacemaker.

%package -n lib%name-devel
Summary: Headers and libraries for writing cluster managers
Group: Development/C++
Requires: lib%name = %version-%release %name = %version-%release
Obsoletes: libheartbeat-devel

%description -n lib%name-devel
Headers and shared libraries for a useful for writing cluster managers
such as Pacemaker.

%prep
%setup

%autoreconf
export docdir=%glue_docdir
%add_optflags -DUCD_COMPATIBLE=1
export CPPFLAGS="%optflags"
%configure \
    --enable-fatal-warnings=no \
    --with-daemon-group=%gname \
    --with-daemon-user=%uname \
    --localstatedir=%_var \
    --libdir=%_libdir \
    --docdir=%glue_docdir

%build
%make_build docdir=%glue_docdir

%install
%makeinstall_std docdir=%glue_docdir

install -pD logd/logd.cf %buildroot%_sysconfdir/logd.cf
install -pD hb_report/utillib.sh %buildroot%_datadir/%name/utillib.sh

## tree fix up
# Dont package static libs
find %buildroot -name '*.a' -exec rm {} \;
find %buildroot -name '*.la' -exec rm {} \;

%pre
groupadd -rf %gname
getent passwd %uname >/dev/null || useradd -r -g %gname -d %_var/lib/heartbeat/cores/hacluster -s /sbin/nologin -c "cluster user" %uname
exit 0

%files
%doc doc/stonith/README* logd/logd.cf AUTHORS COPYING ChangeLog
%_sbindir/*
%_datadir/%name

%_libdir/heartbeat

%dir %_var/lib/heartbeat
%dir %_var/lib/heartbeat/cores
%dir %attr (0700, root, root)		%_var/lib/heartbeat/cores/root
%dir %attr (0700, nobody, %nogroup)	%_var/lib/heartbeat/cores/nobody
%dir %attr (0700, %uname, %gname)	%_var/lib/heartbeat/cores/%uname
%_mandir/man1/*
%_man8dir/*


%exclude %_sbindir/stonith
%exclude %_man8dir/stonith*

%exclude %_libdir/heartbeat/ha_logd
%exclude %_man8dir/ha_logd.*

%exclude %_libdir/heartbeat/ipctest
%exclude %_libdir/heartbeat/ipctransientclient
%exclude %_libdir/heartbeat/ipctransientserver
%exclude %_libdir/heartbeat/transient-test.sh
%exclude %_libdir/heartbeat/base64_md5_test
%exclude %_libdir/heartbeat/logtest
%exclude %_libdir/heartbeat/plugins/test*
%exclude %_datadir/%name/lrmtest

%files logd
%config(noreplace) %_sysconfdir/logd.cf
%_sysconfdir/init.d/*
%_libdir/heartbeat/ha_logd

%files stonith
%_sbindir/stonith
%_libdir/stonith
%_man8dir/stonith*

%exclude %_libdir/stonith/plugins/external/ssh
%exclude %_libdir/stonith/plugins/stonith2/null.so
%exclude %_libdir/stonith/plugins/stonith2/ssh.so

%files -n lib%name
%_libdir/lib*.so.*
%doc AUTHORS COPYING.LIB

%files -n lib%name-devel
%_libdir/lib*.so
%_libdir/heartbeat/ipctest
%_libdir/heartbeat/ipctransientclient
%_libdir/heartbeat/ipctransientserver
%_libdir/heartbeat/transient-test.sh
%_libdir/heartbeat/base64_md5_test
%_libdir/heartbeat/logtest
%_libdir/heartbeat/plugins/test/test.so
%_libdir/stonith/plugins/external/ssh
%_libdir/stonith/plugins/stonith2/null.so
%_libdir/stonith/plugins/stonith2/ssh.so
%_includedir/*
%_datadir/%name/lrmtest
%doc AUTHORS COPYING COPYING.LIB

%changelog
* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt1
- Version 1.0.12

* Wed Aug 14 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt2
- Add patched %_datadir/%name/utillib.sh for cibsecret

* Thu Mar 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt1
- Build for ALT

