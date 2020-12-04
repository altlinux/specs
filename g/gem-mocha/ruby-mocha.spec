%define        pkgname mocha

Name:          gem-%pkgname
Version:       1.11.2
Release:       alt1
Summary:       Library for mocking and stubbing in Ruby
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/freerange/mocha
Vcs:           https://github.com/freerange/mocha.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(metaclass)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Mocha is a library for mocking and stubbing in Ruby using a syntax
like that of JMock. Mocha provides a unified, simple and readable
syntax for both traditional and partial mocking.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Fri Dec 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.11.2-alt1
- ^ 1.9.0 -> 1.11.2
- ! spec tags

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- > Ruby Policy 2.0
- ^ 1.7.0 -> 1.9.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

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

