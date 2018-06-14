%define pkgname mocha

Name: ruby-%pkgname
Version: 1.5.0
Release: alt1

Summary: Library for mocking and stubbing in Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/mocha/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby 
BuildRequires: ruby-tool-rdoc ruby-tool-setup ruby-test-unit
BuildRequires: ruby-metaclass

%description
Mocha is a library for mocking and stubbing in Ruby using a syntax
like that of JMock. Mocha provides a unified, simple and readable
syntax for both traditional and partial mocking.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%ruby_test_unit -Ilib:test test/unit/*_test.rb test/unit/*/*_test.rb

%files
%doc *.md
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Mocha*

%changelog
* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.12-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.12-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.12-alt1
- [0.9.12]

* Tue May 12 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.5-alt1
- [0.9.5]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.9.2-alt1
- Built for Sisyphus

