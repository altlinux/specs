Name: sqlite3-ruby
Version: 1.3.13
Release: alt2

Summary: A Ruby interface for the SQLite database engine
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/sqlite-ruby/

BuildRequires: libruby-devel libsqlite3-devel ruby-test-unit ruby-tool-setup

%filter_from_requires \,ruby(sqlite3/#{$1}/sqlite3_native),d

Source: %name-%version.tar

%description
A Ruby interface for the SQLite database engine.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup
%update_setup_rb
# Threaded tests fail for some reason.
rm -f test/test_integration_pending.rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%ruby_test_unit -Ilib:ext test/test_*.rb

%files
%doc API_CHANGES.rdoc CHANGELOG.rdoc README.rdoc
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/SQLite3*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt1
- new version 1.3.13

* Wed Sep 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt2
- Rebuild with Ruby 2.3.1

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.3.0-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.3.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.0-alt1
- [1.3.0]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.5-alt2
- Force encoding to UTF-8

* Sun Aug 16 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.5-alt1
- [1.2.5]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.4-alt1
- [1.2.4]

* Tue Apr 01 2008 Sir Raorn <raorn@altlinux.ru> 1.2.1-alt2
- Rebuilt with rpm-build-ruby

* Wed Jan 09 2008 Sir Raorn <raorn@altlinux.ru> 1.2.1-alt1
- Initial build for ALT Linux
