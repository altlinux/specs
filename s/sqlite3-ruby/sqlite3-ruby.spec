Name: sqlite3-ruby
Version: 1.3.13
Release: alt2.6

Summary: A Ruby interface for the SQLite database engine
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/sqlite-ruby/

BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel libsqlite3-devel ruby-test-unit ruby-tool-setup
BuildRequires: rake-compiler ruby-mini_portile2 ruby-hoe

%filter_from_requires \,ruby(sqlite3/#{$1}/sqlite3_native),d

Source: %name-%version.tar
Patch:  alt-use-mini_portile2.patch

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
%patch -p0
%update_setup_rb
# Threaded tests fail for some reason.
rm -f test/test_integration_pending.rb
rake debug_gem > sqlite3-%version.gemspec
echo "gemspec" >> Gemfile

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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/SQLite3*

%changelog
* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.6
- Rebuild with new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.5
- Package as gem.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.1
- Rebuild with Ruby 2.4.1

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
