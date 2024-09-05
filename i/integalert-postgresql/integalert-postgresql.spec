%define _unpackaged_files_terminate_build 1

Name:     integalert-postgresql
Version:  0.1.2
Release:  alt1

Summary:  PostgreSQL checking module for Integalert
License:  GPLv2
Group:    Monitoring
Url:      http://git.altlinux.org/people/manowar/packages/integalert-postgresql.git

Packager: Paul Wolneykien <manowar@altlinux.org>
Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: integalert >= 0.4.14

Requires: integalert >= 0.4.14

%description
Configuration files and services to check PostgreSQL integrity
using Integalert.

%prep
%setup

%build
%make_build

%install
%makeinstall_std sysconfdir=%_sysconfdir unitdir=%_unitdir logrotatedir=%_logrotatedir

# For ghost:
touch %buildroot%_sysconfdir/osec/integalert_postgresql/dirs.conf

%files
%_unitdir/integalert_postgresql.*
%_unitdir/postgresql-integ-failed.target
%config(noreplace) %_sysconfdir/osec/integalert_postgresql/files.list
%config(noreplace) %_logrotatedir/integalert_postgresql.conf
%config(noreplace) %_sysconfdir/osec/integalert_postgresql/pipe.conf
%_sysconfdir/osec/integalert_postgresql/sender
%config(noreplace) %_sysconfdir/osec/integalert_postgresql/sender.conf
%config(noreplace) %_sysconfdir/osec/integalert_postgresql/exclude.conf
%ghost %_sysconfdir/osec/integalert_postgresql/dirs.conf

%changelog
* Thu Sep 05 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- integalert_postgresql.service: Run /usr/sbin/integalert.
- Build with integalert. Package configuration files and scripts.

* Sun Jul 07 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Make integalert_postgresql.service a part of postgresql.service.

* Fri Jun 28 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version for C10F2.
