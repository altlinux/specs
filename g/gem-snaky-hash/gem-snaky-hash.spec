%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname snaky_hash

Name:          gem-snaky-hash
Version:       2.0.1.2
Release:       alt0.1
Summary:       A very snaky hash
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/snaky_hash
Vcs:           https://gitlab.com/oauth-xx/snaky_hash.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec-block_is_expected) >= 0
BuildRequires: gem(rubocop-lts) >= 8.0
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(overcommit) >= 0.58
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-thread_safety) >= 0
BuildRequires: gem(codecov) >= 0.6
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(simplecov-json) >= 0
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(hashie) >= 0
BuildRequires: gem(version_gem) >= 1.1.1
BuildConflicts: gem(rubocop-lts) >= 25
BuildConflicts: gem(overcommit) >= 1
BuildConflicts: gem(codecov) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(version_gem) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-lts < 25
%ruby_alias_names snaky_hash,snaky-hash
Requires:      gem(hashie) >= 0
Requires:      gem(version_gem) >= 1.1.1
Conflicts:     gem(version_gem) >= 2
Provides:      gem(snaky_hash) = 2.0.1.2

%ruby_use_gem_version snaky_hash:2.0.1.2

%description
A Hashie::Mash joint to make #snakelife better


%if_enabled    doc
%package       -n gem-snaky-hash-doc
Version:       2.0.1.2
Release:       alt0.1
Summary:       A very snaky hash documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета snaky_hash
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(snaky_hash) = 2.0.1.2

%description   -n gem-snaky-hash-doc
A very snaky hash documentation files.

A Hashie::Mash joint to make #snakelife better
%description   -n gem-snaky-hash-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета snaky_hash.
%endif


%if_enabled    devel
%package       -n gem-snaky-hash-devel
Version:       2.0.1.2
Release:       alt0.1
Summary:       A very snaky hash development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета snaky_hash
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(snaky_hash) = 2.0.1.2
Requires:      gem(rspec-block_is_expected) >= 0
Requires:      gem(rubocop-lts) >= 8.0
Requires:      gem(rake) >= 12
Requires:      gem(rspec) >= 3
Requires:      gem(overcommit) >= 0.58
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rubocop-thread_safety) >= 0
Requires:      gem(codecov) >= 0.6
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(simplecov-json) >= 0
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(byebug) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rubocop-lts) >= 25
Conflicts:     gem(overcommit) >= 1
Conflicts:     gem(codecov) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1

%description   -n gem-snaky-hash-devel
A very snaky hash development package.

A Hashie::Mash joint to make #snakelife better
%description   -n gem-snaky-hash-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета snaky_hash.
%endif


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

%if_enabled    doc
%files         -n gem-snaky-hash-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-snaky-hash-devel
%doc README.md
%endif


%changelog
* Fri Apr 19 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.1.2-alt0.1
- ^ 2.0.1 -> 2.0.1p2

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
