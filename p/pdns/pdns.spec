%global backends %{nil}
%define _pkgdocdir %_docdir/%name

Name: pdns
Version: 4.0.3
Release: alt2
Summary: A modern, advanced and high performance authoritative-only nameserver
Group: System/Servers
License: GPLv2
URL: http://powerdns.com
Source0: %{name}-%{version}.tar
Source1: pdns.service
Patch0: pdns-disable-secpoll.patch
Patch1: fix-unit-tests-32bit.patch
Patch2: fix-negative-ipv6-32bit.patch

Requires(pre): shadow-utils
Requires(post): systemd-units

BuildRequires: gcc-c++ boost-program_options-devel curl libsqlite3-devel
BuildRequires: systemd-devel
BuildRequires: boost-devel
BuildRequires: liblua5-devel
BuildRequires: bison
BuildRequires: libzeromq-devel
BuildRequires: openssl-devel
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
Provides: powerdns = %{version}-%{release}
%global backends %{backends} bind

%description
The PowerDNS Nameserver is a modern, advanced and high performance
authoritative-only nameserver. It is written from scratch and conforms
to all relevant DNS standards documents.
Furthermore, PowerDNS interfaces with almost any database.

%package tools
Summary: Extra tools for %{name}
Group: System/Servers

%description tools
This package contains the extra tools for %{name}

%package backend-mysql
Summary: MySQL backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmysqlclient-devel
%global backends %{backends} gmysql

%description backend-mysql
This package contains the gmysql backend for %{name}

%package backend-postgresql
Summary: PostgreSQL backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: postgresql-devel
%global backends %{backends} gpgsql

%description backend-postgresql
This package contains the gpgsql backend for %{name}

%package backend-pipe
Summary: Pipe backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} pipe

%description backend-pipe
This package contains the pipe backend for %{name}

%package backend-remote
Summary: Remote backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} remote

%description backend-remote
This package contains the remote backend for %{name}

%package backend-ldap
Summary: LDAP backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: openldap-devel
%global backends %{backends} ldap

%description backend-ldap
This package contains the ldap backend for %{name}

%package backend-lua
Summary: LUA backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} lua

%description backend-lua
This package contains the lua backend for %{name}

%package backend-sqlite
Summary: SQLite backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel
%global backends %{backends} gsqlite3

%description backend-sqlite
This package contains the SQLite backend for %{name}

%package backend-opendbx
Summary: OpenDBX backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: opendbx-devel
%global backends %{backends} opendbx

%description backend-opendbx
This package contains the opendbx backend for %{name}

%package backend-geoip
Summary: GeoIP backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libGeoIP-devel
BuildRequires: libyaml-cpp-devel
%global backends %{backends} geoip

%description backend-geoip
This package contains the GeoIP backend for %{name}

%package backend-mydns
Summary: MyDNS backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} mydns

%description backend-mydns
This package contains the MyDNS backend for %{name}

%package backend-tinydns
Summary: TinyDNS backend for %{name}
Group: System/Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: tinycdb-devel
%global backends %{backends} tinydns

%description backend-tinydns
This package contains the TinyDNS backend for %{name}

%prep
%setup -q
%patch0 -p1 -b .disable-secpoll
%patch1 -p1 -b .fix-unit-tests-32bit
%patch2 -p1 -b .fix-negative-ipv6-32bit

%build
export CPPFLAGS="-DLDAP_DEPRECATED"

%configure \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--disable-static \
	--disable-dependency-tracking \
	--disable-silent-rules \
	--with-modules='' \
	--with-lua \
	--with-dynmodules='%{backends}' \
	--enable-tools \
	--enable-remotebackend-zeromq \
	--enable-unit-tests \
	--enable-reproducible

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%{__rm} -f %{buildroot}%{_libdir}/%{name}/*.la
%{__mv} %{buildroot}%{_sysconfdir}/%{name}/pdns.conf{-dist,}

chmod 600 %{buildroot}%{_sysconfdir}/%{name}/pdns.conf

# rename zone2ldap to pdns-zone2ldap (#1193116)
%{__mv} %{buildroot}/%{_bindir}/zone2ldap %{buildroot}/%{_bindir}/pdns_zone2ldap
%{__mv} %{buildroot}/%{_mandir}/man1/zone2ldap.1 %{buildroot}/%{_mandir}/man1/pdns_zone2ldap.1

# Copy systemd service file
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/pdns.service

# change user/group to pdns
# change default backend to bind
sed -i \
    -e 's/# setuid=/setuid=pdns/' \
    -e 's/# setgid=/setgid=pdns/' \
    -e 's/# launch=/launch=bind/' \
    %{buildroot}%{_sysconfdir}/%{name}/pdns.conf

%{__rm} %{buildroot}/%{_bindir}/stubquery

%check
make %{?_smp_mflags} -C pdns check || cat pdns/test-suite.log

%pre
getent group pdns >/dev/null || groupadd -r pdns
getent passwd pdns >/dev/null || \
	useradd -r -g pdns -d / -s /sbin/nologin \
	-c "PowerDNS user" pdns
exit 0

%post
%post_service pdns

%preun
%preun_service pdns

%files
%doc COPYING README
%{_bindir}/pdns_control
%{_bindir}/pdnsutil
%{_bindir}/pdns_zone2ldap
%{_bindir}/zone2sql
%{_bindir}/zone2json
%{_sbindir}/pdns_server
%{_mandir}/man1/pdns_control.1.*
%{_mandir}/man1/pdns_server.1.*
%{_mandir}/man1/zone2sql.1.*
%{_mandir}/man1/zone2json.1.*
%{_mandir}/man1/pdns_zone2ldap.1.*
%{_mandir}/man1/pdnsutil.1.*
%{_unitdir}/pdns.service
%{_libdir}/%{name}/libbindbackend.so
%dir %{_libdir}/%{name}/
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/pdns.conf

%files tools
%{_bindir}/calidns
%{_bindir}/dnsbulktest
%{_bindir}/dnsgram
%{_bindir}/dnspcap2protobuf
%{_bindir}/dnsreplay
%{_bindir}/dnsscan
%{_bindir}/dnsscope
%{_bindir}/dnstcpbench
%{_bindir}/dnswasher
%{_bindir}/dumresp
%{_bindir}/ixplore
%{_bindir}/pdns_notify
%{_bindir}/nproxy
%{_bindir}/nsec3dig
%{_bindir}/saxfr
%{_bindir}/sdig
%{_mandir}/man1/calidns.1.*
%{_mandir}/man1/dnsbulktest.1.*
%{_mandir}/man1/dnsgram.1.*
%{_mandir}/man1/dnspcap2protobuf.1.*
%{_mandir}/man1/dnsreplay.1.*
%{_mandir}/man1/dnsscan.1.*
%{_mandir}/man1/dnsscope.1.*
%{_mandir}/man1/dnstcpbench.1.*
%{_mandir}/man1/dnswasher.1.*
%{_mandir}/man1/dumresp.1.*
%{_mandir}/man1/ixplore.1.*
%{_mandir}/man1/pdns_notify.1.*
%{_mandir}/man1/nproxy.1.*
%{_mandir}/man1/nsec3dig.1.*
%{_mandir}/man1/saxfr.1.*
%{_mandir}/man1/sdig.1.*

%files backend-mysql
%{_pkgdocdir}/schema.mysql.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.mysql.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.mysql.sql
%{_libdir}/%{name}/libgmysqlbackend.so

%files backend-postgresql
%{_pkgdocdir}/schema.pgsql.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.pgsql.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.pgsql.sql
%{_libdir}/%{name}/libgpgsqlbackend.so

%files backend-pipe
%{_libdir}/%{name}/libpipebackend.so

%files backend-remote
%{_libdir}/%{name}/libremotebackend.so

%files backend-ldap
%{_libdir}/%{name}/libldapbackend.so

%files backend-lua
%{_libdir}/%{name}/libluabackend.so

%files backend-sqlite
%{_pkgdocdir}/schema.sqlite3.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.sqlite3.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.sqlite3.sql
%{_libdir}/%{name}/libgsqlite3backend.so

%files backend-opendbx
%{_libdir}/%{name}/libopendbxbackend.so

%files backend-geoip
%{_libdir}/%{name}/libgeoipbackend.so

%files backend-mydns
%{_pkgdocdir}/schema.mydns.sql
%{_libdir}/%{name}/libmydnsbackend.so

%files backend-tinydns
%{_libdir}/%{name}/libtinydnsbackend.so

%changelog
* Tue Mar 28 2017 Lenar Shakirov <snejok@altlinux.ru> 4.0.3-alt2
- Fake release up for make test

* Wed Feb 15 2017 Lenar Shakirov <snejok@altlinux.ru> 4.0.3-alt1
- New version (based on 4.0.3-3.fc26.src)

* Mon Apr 01 2013 Michael Shigorin <mike@altlinux.org> 2.9.22-alt1.2
- NMU: fixed MySQL client library dependencies

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.9.22-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Thu Mar 25 2010 Pavel Shilovsky <piastry@altlinux.org> 2.9.22-alt1
- Import 2.9.22 sources
- Patch work
  + Rewrite patch #6
  + Delete patches #1, #3, #4
  + Change patch numbers (#2, #5, #6) to (#1, #2, #3)
- Change .gear-rules according to deleted patches

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 2.9.21.2-alt5.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon May 25 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt5
- fixed build errors on gcc 4.4

* Wed Mar  4 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt4
- fixed some bugs in patch #5

* Tue Mar  3 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt3
- bugfix #18871: added patch #5

* Sat Jan 24 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt2
- fixed missing backend-mysql package requires

* Sun Dec 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.9.21.2-alt1
- updated to new version 2.9.21.2

* Sun Dec 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.9.21.1-alt3
- fixed instaltions problems with devel package requires
- built pgsql backend

* Wed Oct 29 2008 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.1-alt2
- fixed problems with g++ 4.3
   + add patch to support g++ 4.3

* Sun Oct 19 2008 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.1-alt1
- updated to new version 2.9.21.1
   + add patch to support boost 1.36
   + add backend sqlite3

* Sun Apr 29 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.21-alt1
- updated to new version 2.9.21
   + remove patch #3
   + boost 1.33 or later is required now

* Fri Jan 12 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt3
- bugfix #10650: added patch #3

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt2
- bugfix #10138

* Wed Sep 13 2006 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt1
- initial build for ALTLinux, based on 2.9.20-2mdk

## EOF ##

