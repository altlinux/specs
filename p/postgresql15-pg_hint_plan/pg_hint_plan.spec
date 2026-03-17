%define pg_ver 15
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_hint_plan
Version: 1.5.3
Release: alt2

Summary: pg_hint_plan makes it possible to tweak PostgreSQL execution plans using so-called "hints" in SQL comments
License: BSD and PostgreSQL
Group: Databases
Url: https://github.com/ossc-db/pg_hint_plan

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: flex
BuildRequires: python3-module-myst-parser
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinxcontrib-applehelp
BuildRequires: python3-module-sphinxcontrib-devhelp
BuildRequires: python3-module-sphinxcontrib-htmlhelp
BuildRequires: python3-module-sphinxcontrib-jquery
BuildRequires: python3-module-sphinxcontrib-qthelp
BuildRequires: python3-module-sphinxcontrib-serializinghtml
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
`pg_hint_plan` makes it possible to tweak PostgreSQL execution plans using
so-called "hints" in SQL comments, like `/*+ SeqScan(a) */`.

PostgreSQL uses a cost-based optimizer, that uses data statistics, not static
rules.  The planner (optimizer) estimates costs of each possible execution
plans for a SQL statement, then executes the plan with the lowest cost.
The planner does its best to select the best execution plan, but it is far
from perfect, since it may not count some data properties, like correlation
between columns.


%prep
%setup
%patch0 -p1

%build
%make_build PG_CONFIG=/usr/bin/pg_server_config
%make_build -C docs/ man

%install
%makeinstall_std

install -pDm0644 docs/_build/man/pg_hint_plan.1 %buildroot%_man1dir/pg_hint_plan.1

%files
%doc COPYRIGHT COPYRIGHT.postgresql README.md
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*
%_man1dir/*

%changelog
* Tue Mar 17 2026 Alexei Takaseev <taf@altlinux.org> 1.5.3-alt2
- Use LLVM if it used in PostgreSQL

* Mon Nov 10 2025 Alexei Takaseev <taf@altlinux.org> 1.5.3-alt1
- Initial build for ALT Linux
