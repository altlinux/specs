%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-lts

Name:          gem-rubocop-lts
Version:       24.0.2
Release:       alt1
Summary:       Rubocop LTS - Semantically Versioned
License:       MIT
Group:         Development/Ruby
Url:           https://rubocop-lts.gitlab.io/
Vcs:           https://github.com/rubocop-lts/rubocop-lts.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rspec-block_is_expected) >= 1.0
BuildRequires: gem(rubocop-gradual) >= 0.3
BuildRequires: gem(rubocop-md) >= 1.2
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(rubocop-rspec) >= 2.22
BuildRequires: gem(rubocop-ruby3_2) >= 2.0.5
BuildRequires: gem(rubocop-thread_safety) >= 0.5
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(simplecov-json) >= 0.2
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(simplecov-rcov) >= 0
BuildRequires: gem(standard-rubocop-lts) >= 1.0.3
BuildRequires: gem(version_gem) >= 1.1.2
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(rubocop-gradual) >= 1
BuildConflicts: gem(rubocop-md) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(rubocop-ruby3_2) >= 3
BuildConflicts: gem(rubocop-thread_safety) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-json) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(standard-rubocop-lts) >= 3
BuildConflicts: gem(version_gem) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      ruby >= 3.2
Requires:      gem(rubocop-ruby3_2) >= 2.0.5
Requires:      gem(standard-rubocop-lts) >= 1.0.3
Requires:      gem(version_gem) >= 1.1.2
Conflicts:     gem(rubocop-ruby3_2) >= 3
Conflicts:     gem(standard-rubocop-lts) >= 3
Conflicts:     gem(version_gem) >= 3
Provides:      gem(rubocop-lts) = 24.0.2

%description
Rubocop LTS - Chaos Reduction In a Bottle.


%if_enabled    doc
%package       -n gem-rubocop-lts-doc
Version:       24.0.2
Release:       alt1
Summary:       Rubocop LTS - Semantically Versioned documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-lts
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-lts) = 24.0.2

%description   -n gem-rubocop-lts-doc
Rubocop LTS - Semantically Versioned documentation files.

Rubocop LTS - Chaos Reduction In a Bottle.

%description   -n gem-rubocop-lts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-lts.
%endif


%if_enabled    devel
%package       -n gem-rubocop-lts-devel
Version:       24.0.2
Release:       alt1
Summary:       Rubocop LTS - Semantically Versioned development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-lts
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(rspec-block_is_expected) >= 1.0
Requires:      gem(rubocop-gradual) >= 0.3
Requires:      gem(rubocop-md) >= 1.2
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(rubocop-rspec) >= 2.22
Requires:      gem(rubocop-ruby3_2) >= 2.0.5
Requires:      gem(rubocop-thread_safety) >= 0.5
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(simplecov-json) >= 0.2
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(simplecov-rcov) >= 0
Requires:      gem(standard-rubocop-lts) >= 1.0.3
Requires:      gem(version_gem) >= 1.1.2
Requires:      gem(yard) >= 0.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-block_is_expected) >= 2
Conflicts:     gem(rubocop-gradual) >= 1
Conflicts:     gem(rubocop-md) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(rubocop-ruby3_2) >= 3
Conflicts:     gem(rubocop-thread_safety) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-json) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(standard-rubocop-lts) >= 3
Conflicts:     gem(version_gem) >= 3

%description   -n gem-rubocop-lts-devel
Rubocop LTS - Semantically Versioned development package.

Rubocop LTS - Chaos Reduction In a Bottle.

%description   -n gem-rubocop-lts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-lts.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-lts-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-lts-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Wed Nov 19 2025 Pavel Skrylev <majioa@altlinux.org> 24.0.2-alt1
- ^ 24.0.1 -> 24.0.2

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 24.0.1-alt1
- ^ 22.0.1 -> 24.0.1

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 22.0.1-alt1
- + packaged gem with Ruby Policy 2.0
