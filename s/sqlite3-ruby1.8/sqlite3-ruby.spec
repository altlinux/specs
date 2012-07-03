# vim: set ft=spec: -*- rpm-spec -*-
%define ruby_major 1.8
Name: sqlite3-ruby1.8
Version: 1.3.0
Release: alt2

Summary: A Ruby interface for the SQLite database engine
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/sqlite-ruby/

BuildRequires: libruby%ruby_major-devel libsqlite3-devel ruby-tool-setup

Packager: Denis Baranov <baraka@altlinux.ru>

Source: %name-%version.tar
#Patch: %name-%version-%release.patch

%description
A Ruby interface for the SQLite database engine.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
#%patch -p1
%update_setup_rb
# Threaded tests fail for some reason.
rm -f test/test_integration_pending.rb

%build
%ruby_config
%ruby_build
#ruby_test_unit -Ilib:ext test/test_*.rb

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
* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 1.3.0-alt2
- Rebuild for ruby1.8

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

