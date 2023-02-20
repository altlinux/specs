%define pg_ver 14

Name: postgresql%pg_ver-pg_checksums
Version: 1.1
Release: alt1

Summary: pg_checksums_ext can verify, activate or deactivate checksums
License: PostgreSQL
Group: Databases
Url: https://github.com/credativ/pg_checksums

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libecpg6-devel-static postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
`pg_checksums_ext` is based on the `pg_verify_checksums` and `pg_checksums`
programs available in PostgreSQL version 11 and from 12, respectively. It can
verify, activate or deactivate checksums. Activating requires all database
blocks to be read and all page headers to be updated, so can take a long time
on a large database.

The database cluster needs to be shutdown cleanly in the case of checksum
activation or deactivation, while checksum verification can be performed
online, contrary to PostgreSQL's `pg_checksums`

%prep
%setup
%patch0 -p1

%build
%make PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Mon Feb 20 2023 Alexei Takaseev <taf@altlinux.org> 1.1-alt1
- Initial build for ALT Linux
