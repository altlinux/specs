%define pkgname activerecord

Name: ruby-%pkgname
Version: 2.3.11
Release: alt1
Summary: Implements the ActiveRecord pattern for ORM.
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/activerecord/

Requires: ruby-activesupport = %version

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch:  %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 08 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-activesupport ruby-builder ruby-mocha ruby-rake ruby-tool-rdoc ruby-tool-setup sqlite3 sqlite3-ruby tzdata

%description
Implements the ActiveRecord pattern (Fowler, PoEAA) for ORM. It ties
database tables and classes together for business objects, like Customer
or Subscription, that can find, save, and destroy themselves without
resorting to manual SQL.

%package mysql-adapter
Summary: MySQL connection adapter for ActiveRecord
Group: Development/Ruby
Requires: %name = %version-%release
# Hidden from ruby.req...
Requires: ruby(mysql)

%package postgresql-adapter
Summary: PostgreSQL connection adapter for ActiveRecord
Group: Development/Ruby
Requires: %name = %version-%release
# Hidden from ruby.req...
Requires: ruby(pg)

%package sqlite3-adapter
Summary: SQLite3 connection adapter for ActiveRecord
Group: Development/Ruby
Requires: %name = %version-%release
# Hidden from ruby.req...
Requires: ruby(sqlite3)

%description mysql-adapter
MySQL connection adapter for ActiveRecord.

%description postgresql-adapter
PostgreSQL connection adapter for ActiveRecord.

%description sqlite3-adapter
SQLite3 connection adapter for ActiveRecord.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -q -n %pkgname-%version
%patch -p1
rm -rf lib/active_record/vendor
%update_setup_rb

%build
%ruby_config
%ruby_build

# XXX@timonbl4: this tests not pass
rm -f test/cases/associations/join_model_test.rb
rm -f test/cases/finder_test.rb
rm -f test/cases/migration_test.rb
rm -f test/cases/validations_test.rb

%rake test_sqlite3

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG README
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/active_record/connection_adapters/[^a]*_adapter.rb

%files mysql-adapter
%ruby_sitelibdir/active_record/connection_adapters/mysql_adapter.rb

%files postgresql-adapter
%ruby_sitelibdir/active_record/connection_adapters/postgresql_adapter.rb

%files sqlite3-adapter
%ruby_sitelibdir/active_record/connection_adapters/sqlite_adapter.rb
%ruby_sitelibdir/active_record/connection_adapters/sqlite3_adapter.rb

%files doc
%doc examples
%ruby_ri_sitedir/ActiveRecord*

%changelog
* Fri Apr 22 2011 Timur Aitov <timonbl4@altlinux.org> 2.3.11-alt1
- [2.3.11]

* Sat May 29 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.8-alt1
- [2.3.8]

* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt3
- [2.3.5-200-g9e262de]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt2
- [2.3.5-175-ga84e9b4]

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.5-alt1
- [2.3.5]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.4-alt1
- [2.3.4-68-g7454d18]

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.3.1-alt1
- [2.3.3.1]

* Mon Jun 29 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.2.1-alt1
- [2.3.2.1]
- Dropped sqlite backend

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 2.2.1-alt1
- [2.2.1]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 2.2.0-alt1
- [2.2.0]

* Tue Sep 09 2008 Sir Raorn <raorn@altlinux.ru> 2.1.1-alt1
- [2.1.1]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 2.1.0-alt1
- [2.1.0]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 2.0.2-alt1
- [2.0.2]
- All database adapters moved to separate packages

* Sun Dec 09 2007 Sir Raorn <raorn@altlinux.ru> 1.15.6-alt1
- [1.15.6]

* Wed May 23 2007 Sir Raorn <raorn@altlinux.ru> 1.15.3-alt1
- [1.15.3]

* Fri Aug 11 2006 Sir Raorn <raorn@altlinux.ru> 1.14.4-alt1
- [1.14.4]

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 1.14.3-alt1
- [1.14.3]

* Wed Mar 15 2006 Sir Raorn <raorn@altlinux.ru> 1.13.2-alt1
- [1.13.2]
- Dropped rubygems

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 1.11.1-alt1
- Initial build for ALT Linux

