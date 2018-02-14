%define  pkgname sequel

# not in ALTLinux repo
%filter_from_requires /^ruby(amalgalite)/d
%filter_from_requires /^ruby(cubrid)/d
%filter_from_requires /^ruby(data_objects)/d
%filter_from_requires /^ruby(fastercsv)/d
%filter_from_requires /^ruby(ibm_db)/d
%filter_from_requires /^ruby(java)/d
%filter_from_requires /^ruby(mysql)/d
%filter_from_requires /^ruby(mysqlplus)/d
%filter_from_requires /^ruby(oci8)/d
%filter_from_requires /^ruby(postgres-pr\/postgres-compat)/d
%filter_from_requires /^ruby(sequel_pg)/d
%filter_from_requires /^ruby(sqlanywhere)/d
%filter_from_requires /^ruby(swift\/db\/mysql)/d
%filter_from_requires /^ruby(swift\/db\/postgres)/d
%filter_from_requires /^ruby(swift\/db\/sqlite3)/d
%filter_from_requires /^ruby(tiny_tds)/d
%filter_from_requires /^ruby(win32ole)/d

Name: ruby-%pkgname
Version: 5.5.0
Release: alt1

Summary: Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby
License: MIT
Group:   Development/Ruby
Url:     http://sequel.jeremyevans.net
BuildArch: noarch
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: memcached

%description
Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby.

- Sequel provides thread safety, connection pooling
  and a concise DSL for constructing SQL queries and table schemas.
- Sequel includes a comprehensive ORM layer for mapping records
  to Ruby objects and handling associated records.
- Sequel supports advanced database features such as prepared statements,
  bound variables, savepoints, two-phase commit, transaction isolation,
  master/slave configurations, and database sharding.
- Sequel currently has adapters for ADO, Amalgalite, IBM_DB, JDBC, MySQL,
  Mysql2, ODBC, Oracle, PostgreSQL, SQLAnywhere, SQLite3, and TinyTDS.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 5.5.0-alt1
- 5.5.0

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.49.0-alt2.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.49.0-alt2
-  Revert "do not require rubygems"

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.49.0-alt1
- Initial build in Sisyphus
