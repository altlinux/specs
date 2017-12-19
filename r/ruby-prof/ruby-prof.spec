# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ruby-prof

Name: %pkgname
Version: 0.17.0
Release: alt1

Summary: Fast code profiler for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: https://github.com/ruby-prof/ruby-prof

Source: %pkgname-%version.tar

BuildRequires: libruby-devel ruby-tool-setup ruby-test-unit

%description
ruby-prof is a fast code profiler for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
# Results unreliable
#ruby -e '$LOAD_PATH.unshift(*%%w(lib ext test)); require "test_suite"'

%install
%ruby_install
%rdoc lib/ ext/*.c

%files
%doc README.rdoc
%_bindir/*
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/RubyProf*

%changelog
* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt1
- new version 0.16.2

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.9.2-alt1.3
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.2-alt1.2
- fix ruby 2.0 compile error

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.9.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.2-alt1
- [0.9.2]

* Mon Jun 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.7.3-alt1
- [0.7.3]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- Built for Sisyphus
