%define        gemname mocha

Name:          gem-mocha
Version:       1.15.0
Release:       alt1
Summary:       Library for mocking and stubbing in Ruby
License:       MIT or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/freerange/mocha
Vcs:           https://github.com/freerange/mocha.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(introspection) >= 0.0.1
BuildRequires: gem(psych) < 5
BuildRequires: gem(minitest) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency psych >= 4.0.3,psych < 5
Obsoletes:     ruby-mocha < %EVR
Provides:      ruby-mocha = %EVR
Provides:      gem(mocha) = 1.15.0


%description
Mocha is a library for mocking and stubbing in Ruby using a syntax like that of
JMock. Mocha provides a unified, simple and readable syntax for both traditional
and partial mocking.


%package       -n gem-mocha-doc
Version:       1.15.0
Release:       alt1
Summary:       Library for mocking and stubbing in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mocha
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mocha) = 1.15.0

%description   -n gem-mocha-doc
Library for mocking and stubbing in Ruby documentation files.

Mocha is a library for mocking and stubbing in Ruby using a syntax like that of
JMock. Mocha provides a unified, simple and readable syntax for both traditional
and partial mocking.

%description   -n gem-mocha-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mocha.


%package       -n gem-mocha-devel
Version:       1.15.0
Release:       alt1
Summary:       Library for mocking and stubbing in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mocha
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mocha) = 1.15.0
Requires:      gem(rake) >= 0
Requires:      gem(introspection) >= 0.0.1 gem(introspection) < 0.1
Requires:      gem(psych) < 5
Requires:      gem(minitest) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-mocha-devel
Library for mocking and stubbing in Ruby development package.

Mocha is a library for mocking and stubbing in Ruby using a syntax like that of
JMock. Mocha provides a unified, simple and readable syntax for both traditional
and partial mocking.

%description   -n gem-mocha-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mocha.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-mocha-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mocha-devel
%doc README.md


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.15.0-alt1
- ^ 1.11.2 -> 1.15.0

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
