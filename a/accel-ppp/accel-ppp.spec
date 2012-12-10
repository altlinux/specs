Name: accel-ppp
Version: 1.7.3
Release: alt1
Summary: High performance PPTP/L2TP/PPPoE server
Group: System/Servers

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: http://sourceforge.net/projects/accel-ppp/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Requires: snmp-mibs-std
AutoProv: yes

BuildRequires: cmake libnet-snmp-devel libpcre-devel libnl-devel libssl-devel

%description
The ACCEL-PPP is completly new implementation of PPTP/PPPoE/L2TP
which was written from scratch. Userspace daemon has its own PPP
implementation, so it does not uses pppd and one process (multi-threaded)
manages all connections. ACCEL-PPP uses only kernel-mode implementations
of pptp/l2tp/pppoe.

Features:
- PPTP server
- PPPoE server
- L2TPv2 server
- Radius CoA/DM (PoD)
- Built-in shaper (htb)
- Command line interface (telnet)
- SNMP
- IPv6 (including builtin Neighbor Discovery and DHCPv6)

%prep
%setup
%patch0 -p1

for i in `find . -type f -name CMakeLists.txt -print`
do
    sed -i 's/lib\/accel-ppp/${LIB_DIR}/' $i
done

%build
%cmake \
      -DCMAKE_SKIP_RPATH=FALSE \
      -DLIB_DIR=%_libdir/%name \
      -DBUILD_DRIVER=FALSE \
      -DCMAKE_INSTALL_PREFIX=%prefix \
      -DRADIUS=TRUE \
      -DNETSNMP=TRUE \
      -DLOG_PGSQL=FALSE \
      -DBUILD_INSTALL_PREFIX=%buildroot \
      ..

%make_build -C BUILD

%install
make install/fast DESTDIR=%buildroot -C BUILD

mkdir -p %buildroot%_sysconfdir/ld.so.conf.d

install -Dpm 644 alt-linux/%name.tmpfiles %buildroot%_sysconfdir/tmpfiles.d/%name.conf
install -d %buildroot%_sysconfdir/{rc.d/init.d,sysconfig,logrotate.d}
install -pDm0644 alt-linux/%name.sysconfig	%buildroot%_sysconfdir/sysconfig/%name
install -pDm0755 alt-linux/%name.init		%buildroot%_initdir/%name
install -pDm0644 alt-linux/%name.logrotate	%buildroot%_sysconfdir/logrotate.d/%name
echo "0" > %buildroot%_runtimedir/accel-ppp/seq

%files
%doc COPYING README accel-pppd/extra/net-snmp/ACCEL-PPP-MIB.txt
%config(noreplace) %_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%config %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/tmpfiles.d/*
%_sysconfdir/accel-ppp.conf.dist
%_sbindir/accel-pppd
%_libdir/%name
%_datadir/accel-ppp/
%_mandir/man5/accel-ppp.conf.5*
%_runtimedir/accel-ppp/
%_runtimedir/accel-ppp/*
%_logdir/accel-ppp/

%post
%post_service %name

%preun
%preun_service %name

%changelog
* Tue Dec 11 2012 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt1
- 1.7.3

* Sat Nov 03 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt4
- ppp: force to send dns

* Thu Oct 18 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt3
- remove unresolved=relaxed

* Thu Oct 04 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt2
- Add log messages for terminate sessions

* Thu Sep 06 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Aug 28 2012 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt2
- fix build with glibc-2.16

* Mon Jul 30 2012 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sat Jun 30 2012 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt2
- Build git 20120630

* Mon Jun 18 2012 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt1
- 1.7.0

* Mon Jun 11 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt7
- update upstream to git:fa315a7a7584f6f4954888c010e3cc84c2b33330

* Sun May 27 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt6
- Fix underlinked libraries for libnet-snmp.so

* Fri May 18 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt5
- update upstream to git:cf358fcdc57dd52d30ca490b1164d832cf11fe8b
- add config for systemd-tmpfiles

* Mon Apr 30 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt4
- fix deadlock interface when restart service

* Sat Apr 21 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt3
- quoted username in log messages
- Add username to disconnect log messages

* Wed Apr 04 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt2
- add MIB file

* Sun Mar 25 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- Initial RPM release
