Name:    ora2pg
Version: 24.2
Release: alt1

Summary: Ora2Pg is a free tool used to migrate an Oracle database to a PostgreSQL compatible schema
License: GPL-3.0
Group:   Other
Url:     https://github.com/darold/ora2pg

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl-podlators
BuildRequires: perl-DBI

%description
Summary: Ora2Pg is a free tool used to migrate an Oracle database to a
PostgreSQL compatible schema. It connects your Oracle database, scan it
automatically and extracts its structure or data, it then generates SQL scripts
that you can load into PostgreSQL.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install
install -Dpm0644 ora2pg.conf.dist %buildroot%_sysconfdir/ora2pg/ora2pg.conf

%files
%doc README
%config(noreplace) %_sysconfdir/ora2pg/ora2pg.conf
%_bindir/*
%perl_vendor_privlib/Ora2Pg*

%changelog
* Fri Mar 22 2024 Andrey Cherepanov <cas@altlinux.org> 24.2-alt1
- Initial build for Sisyphus
