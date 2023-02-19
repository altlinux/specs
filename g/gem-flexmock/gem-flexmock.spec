%define        gemname flexmock

Name:          gem-flexmock
Version:       2.3.6.1
Release:       alt1.1
Summary:       Simple mock object library for Ruby unit testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/doudou/flexmock
Vcs:           https://github.com/doudou/flexmock.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0.11.0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rspec) >= 2.11
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-flexmock < %EVR
Provides:      ruby-flexmock = %EVR
Provides:      gem(flexmock) = 2.3.6.1

%ruby_use_gem_version flexmock:2.3.6.1

%description
FlexMock is a simple, but flexible, mock object library for Ruby unit testing.


%package       -n gem-flexmock-doc
Version:       2.3.6.1
Release:       alt1.1
Summary:       Simple mock object library for Ruby unit testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета flexmock
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(flexmock) = 2.3.6.1

%description   -n gem-flexmock-doc
Simple mock object library for Ruby unit testing documentation files.

FlexMock is a simple, but flexible, mock object library for Ruby unit testing.

%description   -n gem-flexmock-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета flexmock.


%package       -n gem-flexmock-devel
Version:       2.3.6.1
Release:       alt1.1
Summary:       Simple mock object library for Ruby unit testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета flexmock
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(flexmock) = 2.3.6.1
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0.11.0
Requires:      gem(coveralls) >= 0
Requires:      gem(rspec) >= 2.11

%description   -n gem-flexmock-devel
Simple mock object library for Ruby unit testing development package.

FlexMock is a simple, but flexible, mock object library for Ruby unit testing.

%description   -n gem-flexmock-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета flexmock.


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

%files         -n gem-flexmock-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-flexmock-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 2.3.6.1-alt1.1
- ! closes build req under check condition

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.3.6.1-alt1
- ^ 2.3.6 -> 2.3.6.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.6-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Oct 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1
- New version

* Wed Sep 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version
- Remove experimental mocking by rails

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.0-alt1
- [0.9.0]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.6-alt1
- [0.8.6]

* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 0.8.2-alt1
- Built for Sisyphus
