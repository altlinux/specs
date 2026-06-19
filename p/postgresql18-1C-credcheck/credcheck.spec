%define pg_ver 18-1C
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-credcheck
Version: 5.0
Release: alt1

Summary: The credcheck PostgreSQL extension provides few general credential checks
License: PostgreSQL
Group: Databases
Url: https://github.com/MigOpsRepos/credcheck

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: postgresql%pg_ver-server-devel libssl-devel libkrb5-devel
BuildRequires: cracklib-devel

Requires: postgresql%pg_ver-server
Requires: cracklib-words

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
%doc LICENSE README.md
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Fri Jun 19 2026 Alexei Takaseev <taf@altlinux.org> 5.0-alt1
- 5.0

* Mon Apr 20 2026 Alexei Takaseev <taf@altlinux.org> 4.7-alt1
- 4.7

* Fri Mar 13 2026 Alexei Takaseev <taf@altlinux.org> 4.6-alt2
- Use LLVM if it used in PostgreSQL

* Thu Feb 19 2026 Alexei Takaseev <taf@altlinux.org> 4.6-alt1
- 4.6

* Tue Feb 10 2026 Alexei Takaseev <taf@altlinux.org> 4.5-alt1
- 4.5

* Thu Jan 15 2026 Alexei Takaseev <taf@altlinux.org> 4.4-alt1
- 4.4

* Fri Dec 26 2025 Alexei Takaseev <taf@altlinux.org> 4.3-alt1
- 4.3

* Thu Oct 23 2025 Alexei Takaseev <taf@altlinux.org> 4.2-alt1
- 4.2

* Mon Oct 20 2025 Alexei Takaseev <taf@altlinux.org> 4.1-alt1
- 4.1
- Drop view pg_banned_rolename, fixed on upstream
- Fix build for PostgreSQL 16 and older

* Fri Oct 17 2025 Alexei Takaseev <taf@altlinux.org> 4.0-alt1
- 4.0
- Add view pg_banned_rolename show banned roles as rolenames
- Add to package docs
- Enable JIT for loongarch64

* Tue Jan 14 2025 Alexei Takaseev <taf@altlinux.org> 3.0-alt1
- 3.0

* Mon Oct 07 2024 Alexei Takaseev <taf@altlinux.org> 2.8-alt3
- Fix path to cracklib dictionary

* Thu Oct 03 2024 Alexei Takaseev <taf@altlinux.org> 2.8-alt2
- Build with cracklib support

* Wed Aug 28 2024 Alexei Takaseev <taf@altlinux.org> 2.8-alt1
- Initial build for ALT Linux
