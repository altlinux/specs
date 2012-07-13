%define antmon_plugindir %_libexecdir/%name

Summary: AntMon monitoring system
Name: antmon
Version: 3.2
Release: alt6
Requires: libstatgrab >= 0214
Packager: Sergey Zhumatiy <zhum@altlinux.org>

License: GPL
Group: System/Servers
Source: %name-%version.tgz

#BuildReq: libstatgrab-devel >= 0.14

# Automatically added by buildreq on Fri Aug 01 2008
BuildRequires: gcc-c++ libnet-snmp-devel libstatgrab-devel

%description
AntMon is a monitoring system for computing clusters And other systems.

%package server
Summary: AntMon monitoring system. Server part
Group: System/Servers

%description server
AntMon is a monitoring system for computing clusters And other systems.

%package agent
Summary: AntMon monitoring system. Agent part
Group: System/Servers

%description agent
AntMon is a monitoring system for computing clusters And other systems.

%package cleo
Summary: AntMon monitoring system. Agent module for Cleo monitoring
Group: System/Servers
Requires: perl
#BuildArch: noarch

%description cleo
AntMon is a monitoring system for computing clusters And other systems.
This package provides additional module for Cleo availability check.

#%package diskfree
#Summary: AntMon monitoring system. Agent module for disk space monitoring
#Group: System/Servers
#BuildArch: noarch

%package snmp
Summary: AntMon monitoring system. Agent module for snmp sources monitoring
Group: System/Servers
BuildRequires: libnet-snmp-devel
Requires: libnet-snmp

#%package fantemp
#Summary: AntMon monitoring system. Agent modules for temperature and fan monitoring (for old kernels)
#Group: System/Servers

%package http
Summary: AntMon monitoring system. Agent module for website availability monitopring
Group: System/Servers
BuildPreReq: perl-libwww
Requires: perl-libwww
#BuildArch: noarch

#%package scali
#Summary: AntMon monitoring system. Agent module for SCI checking
#Group: System/Servers

%package actionxmlrpc
Summary: AntMon monitoring system.  Extra action to send events via XML-RPC
Group: System/Servers
BuildPreReq: perl-Frontier-RPC
BuildPreReq: perl-TimeDate
Requires: perl-TimeDate
Requires: perl-Frontier-RPC
#BuildArch: noarch

%package actionrrd
Summary: AntMon monitoring system. Extra action to log into RRD
Group: System/Servers
BuildPreReq: rrd-perl
Requires: rrd-perl
#BuildArch: noarch

#%description diskfree
#AntMon is a monitoring system for computing clusters And other systems.
#This package provides additional module for diskspace check.

%description snmp
AntMon is a monitoring system for computing clusters And other systems.
This package provides additional module to read snmp sources.

#%description fantemp
#AntMon is a monitoring system for computing clusters And other systems.
#This package provides additional module for temperature and fans speed
#check.

%description http
AntMon is a monitoring system for computing clusters And other systems.
This package provides additional module for website availability check.

#%description scali
#AntMon is a monitoring system for computing clusters And other systems.
#This package provides additional module for SCI check.

%description actionrrd
AntMon is a monitoring system for computing clusters And other systems.
This package provides additional action to write data into RRD.

%description actionxmlrpc
AntMon is a monitoring system for computing clusters And other systems.
This package provides additional action to send data via xmlrpc.

%prep
%setup -q

%build
make DESTDIR=$RPM_BUILD_ROOT

%install

%__install -d $RPM_BUILD_ROOT%_sbindir/
%__install -d $RPM_BUILD_ROOT%_man1dir/
%__install -d $RPM_BUILD_ROOT%_sysconfdir/sysconfig/
%__install -d $RPM_BUILD_ROOT%_initdir/rc.d/

make DESTDIR=$RPM_BUILD_ROOT PLUGDIR=%antmon_plugindir install

#rm -f $RPM_BUILD_ROOT/%_bindir/statgrab*
#rm -f $RPM_BUILD_ROOT/%_prefix/lib/libstatgrab*
#rm -f $RPM_BUILD_ROOT/%_includedir/statgrab*

%__install rpm/antmon-sys $RPM_BUILD_ROOT%_sysconfdir/sysconfig/antmon
%__install rpm/antmon-agent-sys $RPM_BUILD_ROOT%_sysconfdir/sysconfig/antmon-agent
%__install rpm/antmon-alt $RPM_BUILD_ROOT%_initdir/antmon
%__install rpm/antmon-agent-alt $RPM_BUILD_ROOT%_initdir/antmon-agent

%pre server
/usr/sbin/groupadd -r -f _antmon 2>/dev/null >&2 || true;
/usr/sbin/useradd -r -g _antmon -s /dev/null -d /var/empty -n _antmon 2>/dev/null >&2 || true;

%post server
%post_service antmon

%preun server
%preun_service antmon

%pre agent
/usr/sbin/groupadd -r -f _antmon 2>/dev/null >&2 || true;
/usr/sbin/useradd -r -g _antmon -s /dev/null -d /var/empty -n _antmon 2>/dev/null >&2 || true;

%post agent
%post_service antmon-agent

%preun agent
%preun_service antmon-agent

%files server
%doc README COPYING
%config %attr(644, root, root) %_sysconfdir/antmon.conf
%_sysconfdir/sysconfig/antmon
%_initdir/antmon
%_sbindir/ant_mon
%antmon_plugindir/action-cleorestart
%antmon_plugindir/action-dumpplain
%antmon_plugindir/action-dumpstatus
%antmon_plugindir/action-logplain
%antmon_plugindir/action-mailto
%antmon_plugindir/action-restrictmail
%antmon_plugindir/action-smsto
%antmon_plugindir/action-statall
%_man1dir/ant_mon.1.gz
%_man5dir/antmon.conf.5.gz

%files agent
%_sbindir/ant_agent
%antmon_plugindir/system.antmod
%antmon_plugindir/sysstat.antmod
%antmon_plugindir/readfile.antmod
%antmon_plugindir/pop3.antmod
%antmon_plugindir/pinger.antmod
%antmon_plugindir/network1.antmod
%antmon_plugindir/infiniband.antmod
%_sysconfdir/sysconfig/antmon-agent
%_initdir/antmon-agent
%_man1dir/ant_agent.1.gz

%files cleo
%antmon_plugindir/cleo.antmod

%files snmp
%antmon_plugindir/snmp.antmod

#%files diskfree
#%antmon_plugindir/diskfree.antmod

#%files fantemp
#%antmon_plugindir/fantemp.antmod

%files http
%antmon_plugindir/http.antmod

#%files scali
#%antmon_plugindir/scali.antmod

%files actionxmlrpc
%antmon_plugindir/action-xmlrpc

%files actionrrd
%antmon_plugindir/action-logrrd

%changelog
* Fri Jul 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2-alt6
- Rebuild with new libnet-snmp

* Sun Oct 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2-alt5
- Rebuild with new libnet-snmp
- Fix (ALT #18107)

* Fri May 29 2009 Sergey Zhumatiy <zhum@altlinux.org> 3.2-alt3
- fictive version increment for libstatgrab compiling with git.alt

* Mon Sep 22 2008 Sergey Zhumatiy <zhum@altlinux.org> 3.2-alt2
- Startup procedure cleanup

* Fri Aug 01 2008 Sergey Zhumatiy <zhum@altlinux.org> 3.2-alt1
- SNMP module added
- Readfile improved (now you can get value rate)
- Some spec cleanups

* Fri Nov 16 2007 Sergey Zhumatiy <zhum@altlinux.org> 3.1-alt2
- Some dependencies added
- Minor optimizations

* Thu Oct 04 2007 Sergey Zhumatiy <zhum@altlinux.org> 3.1-alt1
- Initial build
