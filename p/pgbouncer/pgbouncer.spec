%define _unpackaged_files_terminate_build 1

Name:       pgbouncer
Version:    1.23.0
Release:    alt1
Summary:    Lightweight connection pooler for PostgreSQL
License:    ISC
Group:      Databases
Url:        https://github.com/pgbouncer/pgbouncer
Source:     %name-%version.tar
Source100:  libusual.tar
Source101:  uthash.tar
Source1:    pgbouncer.init
Source2:    pgbouncer.ini
Source3:    users.txt
Source4:    pgbouncer.tmpfiles
Source5:    pgbouncer.service
Source6:    pgbouncer.logrotate
Source7:    pgbouncer.pam
Source8:    pgbouncer.sysconfig

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(libcares) >= 1.9.0
BuildRequires: libpam-devel
BuildRequires: libsystemd-devel
BuildRequires: pandoc
# That was a pkg with an ugly temporary name:
Obsoletes: pgbouncer17 < %EVR

%description
Several levels of brutality when rotating connections:

Session pooling - Most polite method. When client connects, a server
connection will be assigned to it for the whole duration it stays
connected. When client disconnects, the server connection will be put
back into pool.

Transaction pooling - Server connection is assigned to client only
during a transaction. When PgBouncer notices that transaction is over,
the server will be put back into pool. This is a hack as it breaks
application expectations of backend connection. You can use it only
when application cooperates with such usage by not using features that
can break. See the table below for breaking features.

Statement pooling - Most aggressive method. This is transaction
pooling with a twist - multi-statement transactions are disallowed.
This is meant to enforce "autocommit" mode on client, mostly targeted
for PL/Proxy.

%prep
%setup -q
tar -xf %SOURCE100 -C lib
tar -xf %SOURCE101 -C uthash

%build
export PYTHON=%__python3
touch lib/mk/install-sh
./autogen.sh
%configure \
    --with-systemd \
    --with-pam \
    --with-root-ca-file=/etc/pki/tls/certs/ca-bundle.crt

%make_build

%install
%makeinstall_std

mkdir -p %buildroot{%_sysconfdir,%_logdir}/%name
mkdir -p %buildroot{%_logrotatedir,%_unitdir,%_initdir,%_tmpfilesdir}

install -p -m755 %SOURCE1 %buildroot%_initdir/%name
install -p -m640 %SOURCE2 %buildroot%_sysconfdir/%name/%name.ini
install -p -m640 %SOURCE3 %buildroot%_sysconfdir/%name/users.txt
install -p -m644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
install -p -m644 %SOURCE5 %buildroot%_unitdir/%name.service
install -p -m644 %SOURCE6 %buildroot%_logrotatedir/%name
install -p -m644 -D %SOURCE7 %buildroot%_sysconfdir/pam.d/%name
install -p -m644 -D %SOURCE8 %buildroot%_sysconfdir/sysconfig/%name

# Let RPM pick up docs in the files section
rm -fr %buildroot%_defaultdocdir

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd  -r -g %name -s /sbin/nologin -c "PgBouncer Server" -M -d /run/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc NEWS.md README.md doc/*.md
%_bindir/%name
%_man1dir/*
%_man5dir/*
%attr(750,root,%name) %dir %_sysconfdir/%name
%config(noreplace) %attr(640,root,%name) %_sysconfdir/%name/%name.ini
%config(noreplace) %attr(640,root,%name) %_sysconfdir/%name/users.txt
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_tmpfilesdir/%name.conf
%_initdir/%name
%_unitdir/%name.service
%attr(1770,root,%name) %dir %_logdir/%name

%changelog
* Thu Jul 04 2024 Alexey Shabalin <shaba@altlinux.org> 1.23.0-alt1
- 1.23.0.

* Thu Feb 10 2022 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- 1.16.1 (Fixes: CVE-2021-3935).

* Thu Feb 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt3
- Use python3 for build.

* Sun Feb 07 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt2
- add /etc/sysconfig/pgbouncer

* Fri Feb 05 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- Build new version.
- Build with libcares, pam, systemd support.
- Define root ca file.
- Add %%pre, %%post, %%preun.
- Add systemd unit.
- Update sysv init script.
- Add logrotate config.
- Update pgbouncer config.
- Add pam config.
- Execute service as pgbouncer system user.

* Wed Apr 29 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.0-alt1
- Build new version.

* Thu Mar 26 2020 Grigory Ustinov <grenka@altlinux.org> 1.12.0-alt1
- Build new version.

* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 1.11.0-alt1
- Build new version.

* Tue Jul 16 2019 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- Build new version.

* Thu Jan 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Build new version.

* Wed May 10 2017 Ivan Zakharyaschev <imz@altlinux.org> 1.7.2-alt8
- %%config(noreplace) modifiers used where needed

* Fri Apr 21 2017 Ivan Zakharyaschev <imz@altlinux.org> 1.7.2-alt7
- Our own dir (/etc/pgbouncer/) is used to hold the additional conf
  (like in other distros). Less mess in /etc/

* Wed Apr 19 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt6
- NMU merged pgbouncer17 updates

* Mon Apr 17 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt5
- fix perms for pid file and its location

* Mon Apr 17 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt4
- fix typo

* Mon Apr 17 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt3
- fix tmpfiles place

* Fri Apr 14 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt2
- conflicts with open's pgbouncer

* Thu Apr 13 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt1
- bumped to 1.7.2

* Thu Jul 28 2011 Alexander V Openkin <open@altlinux.ru> 1.4.2-alt1
- 1.4.2 

* Fri Apr 30 2010 Alexander V Openkin <open@altlinux.ru> 1.3.2-alt0.M50p.1
- 1.3.2 

* Thu Oct 15 2009 Alexander V Openkin <open@altlinux.ru> 1.3.1-alt1
- 1.3.1 release 

* Wed Apr 15 2009 Alexander V Openkin <open@altlinux.ru> 1.3-alt1
- 1.3 release 

* Tue Apr 14 2009 Alexander V Openkin <open@altlinux.ru> 1.2.3-alt2
- init script fixed

* Tue Sep 23 2008 Alexander V Openkin <open@altlinux.ru> 1.2.3-alt1
-  1.2.3 release. 

* Sat Feb 16 2008 Alexander V Openkin <open@altlinux.ru> 1.1.2-alt1
-  1.1.2 release.
