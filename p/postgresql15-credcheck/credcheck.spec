%define pg_ver 15
%ifarch loongarch64
# XXX: psql jit uses LLVM, versions <= 15.
# These versions do not support LoongArch targets.
%def_without jit
%else
%def_with jit
%endif

Name: postgresql%pg_ver-credcheck
Version: 2.8
Release: alt1

Summary: The credcheck PostgreSQL extension provides few general credential checks
License: PostgreSQL
Group: Databases
Url: https://github.com/MigOpsRepos/credcheck

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: postgresql%pg_ver-server-devel libssl-devel libkrb5-devel

Requires: postgresql%pg_ver-server

%description
The credcheck PostgreSQL extension provides few general credential checks, which will
be evaluated during the user creation, during the password change and user renaming.
By using this extension, we can define a set of rules:

- allow a specific set of credentials
- reject a certain type of credentials
- deny password that can be easily cracked
- enforce use of an expiration date with a minimum of day for a password
- define a password reuse policy
- define the number of authentication failure allowed before a user is banned


%prep
%setup
%patch0 -p1

%build
%make PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%_libdir/pgsql/*.so
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Wed Aug 28 2024 Alexei Takaseev <taf@altlinux.org> 2.8-alt1
- Initial build for ALT Linux
