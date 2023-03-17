BuildArch: noarch

%define PGSQL pgsql

Name: postgresql-common
Summary: create postgresql user and groups
Version: 1.0
Release: alt9
License: GPL
Group: Databases

Url: http://sisyphus.ru/ru/srpm/Sisyphus/postgresql-common

Source1: postgresql.monit

Requires: monit-base

# Need for groupadd/useradd
PreReq: shadow-utils

%description
%summary

%prep
%build
%install
install -D -m 644 %SOURCE1 %buildroot/etc/monitrc.d/postgresql

%pre
exec &>/dev/null
/usr/sbin/groupadd -r psqluser ||:
/usr/sbin/groupadd -r -g 46 postgres \
	|| /usr/sbin/groupadd -r postgres \
	||:
/usr/sbin/useradd -M -o -r -d %_localstatedir/%PGSQL -s /dev/null \
	-c "PostgreSQL Server" -u 46 postgres -g postgres \
	|| /usr/sbin/useradd -M -o -r -d %_localstatedir/%PGSQL -s /dev/null \
	-c "PostgreSQL Server" postgres -g postgres \
	||:

%files
%config(noreplace) %_sysconfdir/monitrc.d/postgresql

%changelog
* Fri Mar 03 2023 Alexei Takaseev <taf@altlinux.org> 1.0-alt9
- Delete dead code for chroot's start
- Move /etc/sysconfig/postgresql to server package

* Wed Nov 03 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt8
- delete symlink to socket when changing control state to "traditional"
  (Closes: #17883)

* Sat Oct 31 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt7
- add Url tag

* Sat Oct 31 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt6
- fix user/group creation (ALT#15268)

* Sun Apr 26 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt5
- make /etc/sysconfig/postgresql as %config (ALT #17844)

* Sat Aug 02 2008 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt4.1
- rebuild

* Thu Jun 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.0-alt4
- Added control facility for postgresql.

* Thu Nov 02 2006 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt3
- add monit support

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt2
- PreReq: shadow-utils

* Wed Sep 22 2006 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build for Sisyphus

