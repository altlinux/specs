%define        gemname coveralls_reborn

Name:          gem-coveralls-reborn
Version:       0.26.0
Release:       alt1
Summary:       A Ruby implementation of the Coveralls API
License:       MIT
Group:         Development/Ruby
Url:           https://coveralls.io
Vcs:           https://github.com/tagliala/coveralls-ruby-reborn.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(simplecov-lcov) >= 0.8.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(truthy) >= 1.0
BuildRequires: gem(vcr) >= 6.1
BuildRequires: gem(webmock) >= 3.13.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(term-ansicolor) >= 1.7
BuildRequires: gem(thor) >= 1.2
BuildRequires: gem(tins) >= 1.32
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(simplecov-lcov) >= 0.9
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(truthy) >= 2
BuildConflicts: gem(vcr) >= 7
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(term-ansicolor) >= 2
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(tins) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      gem(simplecov) >= 0.17
Requires:      gem(term-ansicolor) >= 1.7
Requires:      gem(thor) >= 1.2
Requires:      gem(tins) >= 1.32
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(term-ansicolor) >= 2
Conflicts:     gem(thor) >= 2
Conflicts:     gem(tins) >= 2
Provides:      gem(coveralls_reborn) = 0.26.0


%description
A Ruby implementation of the Coveralls API.


%package       -n coveralls-reborn
Version:       0.26.0
Release:       alt1
Summary:       A Ruby implementation of the Coveralls API executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета coveralls_reborn
Group:         Other
BuildArch:     noarch

Requires:      gem(coveralls_reborn) = 0.26.0
Conflicts:     coveralls

%description   -n coveralls-reborn
A Ruby implementation of the Coveralls API executable(s).

%description   -n coveralls-reborn -l ru_RU.UTF-8
Исполнямка для самоцвета coveralls_reborn.


%package       -n gem-coveralls-reborn-doc
Version:       0.26.0
Release:       alt1
Summary:       A Ruby implementation of the Coveralls API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coveralls_reborn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coveralls_reborn) = 0.26.0

%description   -n gem-coveralls-reborn-doc
A Ruby implementation of the Coveralls API documentation files.

%description   -n gem-coveralls-reborn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coveralls_reborn.


%package       -n gem-coveralls-reborn-devel
Version:       0.26.0
Release:       alt1
Summary:       A Ruby implementation of the Coveralls API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета coveralls_reborn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coveralls_reborn) = 0.26.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(simplecov-lcov) >= 0.8.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(truthy) >= 1.0
Requires:      gem(vcr) >= 6.1
Requires:      gem(webmock) >= 3.13.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(simplecov-lcov) >= 0.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(truthy) >= 2
Conflicts:     gem(vcr) >= 7
Conflicts:     gem(webmock) >= 4

%description   -n gem-coveralls-reborn-devel
A Ruby implementation of the Coveralls API development package.

%description   -n gem-coveralls-reborn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета coveralls_reborn.


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

%files         -n coveralls-reborn
%doc README.md
%_bindir/coveralls

%files         -n gem-coveralls-reborn-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-coveralls-reborn-devel
%doc README.md


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.26.0-alt1
- + packaged gem with Ruby Policy 2.0
