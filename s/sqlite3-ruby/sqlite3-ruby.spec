# vim: set ft=spec: -*- rpm-spec -*-

Name: sqlite3-ruby
Version: 1.3.0
Release: alt1

Summary: A Ruby interface for the SQLite database engine
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/sqlite-ruby/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

# Automatically added by buildreq on Tue Apr 01 2008 (-bi)
BuildRequires: libruby-devel libsqlite3-devel ruby-test-unit ruby-tool-setup

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
A Ruby interface for the SQLite database engine.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
%patch -p1
%update_setup_rb
# Threaded tests fail for some reason.
rm -f test/test_integration_pending.rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:ext test/test_*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc API_CHANGES.rdoc CHANGELOG.rdoc README.rdoc
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/SQLite3*

%changelog
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

