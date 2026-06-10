# Build ftpd, mavisd, spawnd, tac_plus, tcprelay
%def_with extra
%def_without tac_plus

Name: event-driven-servers
Version: 2026.06.08.2
Release: alt1

Summary: This is a collection of high-performance and scalable event-driven servers
License: BSD-3-Clause
Group: Other
Url: https://github.com/MarcJHuber/event-driven-servers/
Vcs: https://github.com/MarcJHuber/event-driven-servers.git

Source: %name-%version.tar

ExcludeArch: %ix86 ppc64le armh

BuildRequires(pre): rpm-build-python3
BuildRequires: python3
BuildRequires: libcares-devel
BuildRequires: libpcre2-devel
BuildRequires: libradcli-devel
BuildRequires: libpam-devel
BuildRequires: libcurl-devel
BuildRequires: libcrypt-devel
BuildRequires: libssl-devel
# BuildRequires: libtls-devel
BuildRequires: liblksctp-devel
BuildRequires: zlib-devel
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(Net/LDAP.pm)
BuildRequires: perl(Net/TacacsPlus/Packet.pm)

Requires: libmavis = %EVR

%add_findreq_skiplist %perl_vendor_privlib/mavis/mavis_tacplus_opie.pl
%add_findreq_skiplist %_bindir/mavis_tacplus*.py

%description
%summary.

%package -n tac_plus-ng
Summary: TACACS+ daemon
Group: System/Servers
Requires: %name = %EVR
Requires: python3(mavis) = %EVR

%description -n tac_plus-ng
TACACS+ daemon. It provides networking components like routers
and switches with authentication, authorisation and accounting services.

%package -n libmavis
Summary: Library for event-driven servers
Group: System/Libraries

%description -n libmavis
Library for event-driven servers.

%package -n libmavis-devel
Summary: Library for event-driven servers
Group: System/Libraries
Requires: libmavis = %EVR

%description -n libmavis-devel
Library for event-driven servers.
This package contains development files for libmavis.

%package -n python3-module-mavis
Summary: Python module for mavis library
Group: Development/Python3
Provides: python3(mavis) = %EVR
BuildArch: noarch

%description -n python3-module-mavis
Python module for mavis library.

%package -n ftpd
Summary: FTP Daemon
Group: Networking/File transfer

%description -n ftpd
FTP Daemon.

%package -n mavisd
Summary: MAVIS daemon
Group: Networking/Other

%description -n mavisd
In conjunction with the remote module, this daemon allows
extending MAVIS (modular attribute-value interchange system)
functionality over the network, using UDP packets for
communication with clients and/or other MAVIS daemons.

# tcprelay
%package -n spawnd
Summary: spawnd is a broker with load-balancing functionality
Group: Networking/Other

%description -n spawnd
spawnd is a broker with load-balancing functionality that
listens for incoming TCP (or SCTP) connections on IP, UNIX or
possibly IPv6 sockets, accepts them and finally forwards them
(using ancillary messages over UNIX domain sockets) to the
spawned worker processes.

%package -n tac_plus
Summary: TACACS+ daemon
Group: Networking/Other

%description -n tac_plus
tac_plus is a TACACS+ daemon. It provides Cisco Systems routers
and access servers with authentication, authorisation and
accounting services.

%package -n tcprelay
Summary: TCP-Relay
Group: Networking/Other

%description -n tcprelay
tcprelay is a TCP connection forwarder with load balancing
capabilities. If compiled with TLS support, it may be used as
SSL encryption wrapper.


%prep
%setup

%build
./configure --installroot=%buildroot --prefix=%_prefix \
    --bindir=%_bindir --etcdir=%_sysconfdir --sbindir=%_sbindir \
    --libdir=%_libdir --libarchdir=%_libdir --libexecdir=%_prefix/libexec \
    mavis spawnd mavisd ftpd tac_plus tac_plus-ng tcprelay
#   --without-ssl --with-ares --with-sctp --with-zlib --without-crypto mavis spawnd mavisd ftpd tac_plus tac_plus-ng tcprelay
#   --without-ssl --without-ares --without-sctp --without-zlib --without-crypto mavis spawnd mavisd ftpd tac_plus tac_plus-ng tcprelay

export NPROCS=1
%make_build

# https://github.com/MarcJHuber/event-driven-servers/issues/20#issuecomment-1310656856
find ./build/ -name packet.o -delete
sed -i -e 's/-O2/-O0/g' ./build/Makefile.inc.linux-*
%make_build

%install
%makeinstall_std -j1
pushd spawnd/perl
perl Makefile.PL
sed -i 's!/usr/local!%_prefix!' Makefile
sed -i -e 's!/usr/lib !%_libdir !' -e 's!/usr/lib$!%_libdir!' Makefile
sed -i '/^SITELIBEXP/s!.*!SITELIBEXP = %perl_vendorlib!' Makefile
sed -i '/^INSTALLSITELIB/s!.*!INSTALLSITELIB = %perl_vendorlib!' Makefile
sed -i '/^INSTALLSITEARCH/s!.*!INSTALLSITEARCH = %perl_vendor_archlib!' Makefile
%makeinstall_std -j1
popd

# Python3
mkdir -p %buildroot%python3_sitelibdir_noarch/mavis
mv %buildroot%_libdir/mavis/{mavis.py,__pycache__} %buildroot%python3_sitelibdir_noarch/mavis/
mv %buildroot%_libdir/mavis/*.py %buildroot%_bindir/

# Perl5
mkdir -p %buildroot%perl_vendor_privlib/mavis
sed -i 's!/usr/lib64/mavis!%perl_vendor_privlib/mavis!' %buildroot%_libdir/mavis/*.pl
sed -i 's!/usr/local/lib/mavis!%perl_vendor_privlib/mavis!' %buildroot%_libdir/mavis/*.pl
mv %buildroot%_libdir/mavis/Mavis.pm %buildroot%perl_vendor_privlib/
mv %buildroot%_libdir/mavis/*.pl %buildroot%perl_vendor_privlib/mavis/

install -Dm 0644 spawnd/perl/Scm.pm %buildroot%perl_vendor_privlib/Scm.pm

install -Dm 0755 tac_plus-ng/perl/tactrace.pl %buildroot%_bindir/tactrace.pl
sed -i 's!/usr/local/etc!%_sysconfdir!' %buildroot%_bindir/tactrace.pl
sed -i 's!/usr/local/sbin!%_sbindir!' %buildroot%_bindir/tactrace.pl

# MIBs
mkdir -p %buildroot%_datadir/snmp/mibs
mv %buildroot%_libdir/mavis/extra/* %buildroot%_datadir/snmp/mibs/
rmdir %buildroot%_libdir/mavis/extra/

# Systemd units
mkdir -p %buildroot%systemd_unitdir
cat > %buildroot%systemd_unitdir/tac_plus-ng.service << __EOF__
[Unit]
Description=TACACS+ NG Service
After=syslog.target network.target network-online.target

[Service]
ExecStart=/usr/sbin/tac_plus-ng -f /etc/tac_plus-ng.cfg
KillMode=process
Restart=always
ExecReload=/bin/kill -HUP \$MAINPID

[Install]
WantedBy=multi-user.target
__EOF__

cat > %buildroot%systemd_unitdir/tac_plus.service << __EOF__
[Unit]
Description=TACACS+ Service
After=syslog.target network.target network-online.target

[Service]
ExecStart=/usr/sbin/tac_plus -f /etc/tac_plus.cfg
KillMode=process
Restart=always
ExecReload=/bin/kill -HUP \$MAINPID

[Install]
WantedBy=multi-user.target
__EOF__

# Config files
install -Dm 0644 tac_plus-ng/sample/tac_plus-ng-simple.cfg %buildroot%_sysconfdir/tac_plus-ng.cfg
sed -i 's!/usr/local/bin!%_bindir!' %buildroot%_sysconfdir/tac_plus-ng.cfg %buildroot%_sysconfdir/mavis/sample/tac_plus-ng-simple.cfg
sed -i 's!/usr/bin/env -S !!' %buildroot%_sysconfdir/tac_plus-ng.cfg %buildroot%_sysconfdir/mavis/sample/tac_plus-ng-simple.cfg

install -Dm 0644 tac_plus/sample/tac_plus.cfg %buildroot%_sysconfdir/tac_plus.cfg
sed -i 's|^#!.*|#!%_sbindir/tac_plus|' %buildroot%_sysconfdir/tac_plus.cfg

install -Dm 0644 ftpd/sample/ftpd.cfg %buildroot%_sysconfdir/ftpd.cfg
sed -i 's|^#!.*|#!%_sbindir/ftpd|' %buildroot%_sysconfdir/ftpd.cfg

install -Dm 0644 tcprelay/sample/tcprelay.cfg %buildroot%_sysconfdir/tcprelay.cfg
sed -i 's|^#!.*|#!%_sbindir/tcprelay|' %buildroot%_sysconfdir/tcprelay.cfg

# Remove extra files
%if_without extra
rm %buildroot%_sbindir/{ftpd,mavisd,spawnd,tcprelay}
%endif
%if_without tac_plus
rm %buildroot%_sbindir/tac_plus
rm %buildroot%_sysconfdir/tac_plus.cfg
rm %buildroot%_unitdir/tac_plus.service
%endif

%post -n tac_plus-ng
%post_service tac_plus-ng

%preun -n tac_plus-ng
%preun_service tac_plus-ng

%files
%doc *.md LICENSE
%_bindir/mavistest
%_sbindir/radmavis
%_datadir/mavis
%_sysconfdir/mavis
%perl_vendor_privlib/Mavis.pm
%perl_vendor_privlib/mavis
%perl_vendor_privlib/Scm.pm
%perl_vendor_archlib/Scm.pm
%perl_vendor_archlib/auto/Scm
%perl_vendor_archlib/receiver.pl

%files -n tac_plus-ng
%doc doc/tac_plus-ng.txt
%_bindir/mavis_tacplus*
%_bindir/tactrace.pl
%_sbindir/tac_plus-ng
%_datadir/snmp/mibs/*
%config(noreplace) %_sysconfdir/tac_plus-ng.cfg
%systemd_unitdir/tac_plus-ng.service

%files -n libmavis
%doc doc/mavis.txt
%_libdir/*.so.*
%_libdir/mavis

%files -n libmavis-devel
%_libdir/*.so

%files -n python3-module-mavis
%python3_sitelibdir_noarch/mavis

%if_with extra
%files -n ftpd
%doc doc/ftpd.txt
%_sbindir/ftpd
%config(noreplace) %_sysconfdir/ftpd.cfg

%files -n mavisd
%doc doc/mavisd.txt
%_sbindir/mavisd

%files -n spawnd
%doc doc/spawnd.txt
%_sbindir/spawnd

%files -n tcprelay
%doc doc/tcprelay.txt
%_sbindir/tcprelay
%config(noreplace) %_sysconfdir/tcprelay.cfg
%endif

%if_with tac_plus
%files -n tac_plus
%doc doc/tac_plus.txt
%_sbindir/tac_plus
%config(noreplace) %_sysconfdir/tac_plus.cfg
%systemd_unitdir/tac_plus.service
%endif


%changelog
* Tue Jun 09 2026 Andrew A. Vasilyev <andy@altlinux.org> 2026.06.08.2-alt1
- update to upstream/master
- switch off optimization for packet.o (ALT #58317)

* Mon Mar 31 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt7
- add extra packages (ftpd, mavisd, spawnd, tac_plus, tcprelay)

* Mon Mar 31 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt6
- update to upstream/master

* Mon Mar 17 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt5
- update to upstream/master and reduce NPROCS

* Sun Mar 16 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt4
- add debug and O2 flags and lost dependencies

* Fri Mar 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt3
- update to upstream/master

* Fri Feb 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt2
- get rid of /usr/bin/env in config (no -S option in old version)

* Mon Oct 07 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- Initial build for ALT.

