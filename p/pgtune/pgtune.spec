Name: pgtune
Version: 0.9.2
Release: alt1.1

Summary: PostgreSQL Config Tuner
License: BSD
Group: Databases

Url: http://pgfoundry.org/projects/pgtune
Source0: %name-%version.tar
Buildarch: noarch

Requires: postgresql-server

%description
pgtune takes the wimpy default postgresql.conf and expands the database
server to be as powerful as the hardware it's being deployed on.

%prep
%setup

%build
%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name

install -m 755 pgtune %buildroot%_bindir
install -m 644 -p pg_settings* %buildroot%_datadir/%name

%files
%dir %_datadir/%name
%_datadir/%name/*
%_bindir/pgtune
%doc TODO README

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.1
- Rebuild with Python-2.7

* Sat Nov 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus

* Wed Oct 28 2009 Devrim Gunduz <devrim@commandprompt.com> 0.9.1-1
- Initial packaging for PostgreSQL RPM Repository

* Wed Oct 28 2009 Greg Smith <gsmith@gregsmith.com> 0.9.2-1
- Added copyright file, doesn't install sample postgresql.conf file.
