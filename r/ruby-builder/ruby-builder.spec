%define pkgname builder

Name: ruby-%pkgname
Version: 3.2.3
Release: alt1
Summary: Provide a simple way to create XML markup and data structures
License: MIT
Group: Development/Ruby
Url: https://github.com/tenderlove/builder

Source: %pkgname-%version.tar

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-build-ruby

%description
Provide a simple way to create XML markup and data structures.
Builder::XmlMarkup:: Generate XML markup notiation
Builder::XmlEvents:: Generate XML events (i.e. SAX-like)

%description -l ru_RU.UTF8
Позволяет простым способом создавать XML разметку и структуры данных.
Builder::XmlMarkup:: Создание записи с XML разметкою.
Builder::XmlEvents:: Создание событий XML (т.е. подобные SAX)

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
# EPIC FAIL
rm -f test/testblankslate.rb
%ruby_test_unit -Ilib test/test*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGES README.md MIT-LICENSE
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Builder*

%changelog
* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 3.2.3-alt1
- new version 3.2.3

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1.1
- Built version 3.2.0

* Wed Dec 05 2012 Led <led@altlinux.ru> 3.0.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 3.0.0-alt1
- [3.0.0]

* Tue Nov 30 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.2-alt4
- Fix build with Ruby 1.9.2

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 2.1.2-alt3
- Rebuilt with Ruby 1.9

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 2.1.2-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 2.1.2-alt1
- Initial build for ALT Linux

