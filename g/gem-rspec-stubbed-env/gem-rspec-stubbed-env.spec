%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec-stubbed_env

Name:          gem-rspec-stubbed-env
Version:       1.0.1
Release:       alt1
Summary:       Unobtrusively stub ENV keys and values during testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pboling/rspec-stubbed_env
Vcs:           https://github.com/pboling/rspec-stubbed_env/tree/v1.0.1.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 2.1
BuildRequires: gem(simplecov-json) >= 0.2
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(rubocop-gradual) >= 0.3
BuildRequires: gem(rubocop-lts) >= 18.0
BuildRequires: gem(rubocop-md) >= 1.2
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(rubocop-shopify) >= 2.12
BuildRequires: gem(rubocop-thread_safety) >= 0.5
BuildRequires: gem(standard) >= 1.25
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rspec-block_is_expected) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-cobertura) >= 3
BuildConflicts: gem(simplecov-json) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(rubocop-gradual) >= 1
BuildConflicts: gem(rubocop-lts) >= 25
BuildConflicts: gem(rubocop-md) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(rubocop-shopify) >= 3
BuildConflicts: gem(rubocop-thread_safety) >= 1
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-lts < 25
Provides:      gem(rspec-stubbed_env) = 1.0.1


%description
Stub environment variables in a scoped context for testing stub_env(
'AWS_REGION' => 'us-east-1', 'REDIS_URL' => 'redis://localhost:6379/' )


%if_enabled    doc
%package       -n gem-rspec-stubbed-env-doc
Version:       1.0.1
Release:       alt1
Summary:       Unobtrusively stub ENV keys and values during testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-stubbed_env
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-stubbed_env) = 1.0.1

%description   -n gem-rspec-stubbed-env-doc
Unobtrusively stub ENV keys and values during testing documentation files.

Stub environment variables in a scoped context for testing stub_env(
'AWS_REGION' => 'us-east-1', 'REDIS_URL' => 'redis://localhost:6379/' )

%description   -n gem-rspec-stubbed-env-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-stubbed_env.
%endif


%if_enabled    devel
%package       -n gem-rspec-stubbed-env-devel
Version:       1.0.1
Release:       alt1
Summary:       Unobtrusively stub ENV keys and values during testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-stubbed_env
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-stubbed_env) = 1.0.1
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-cobertura) >= 2.1
Requires:      gem(simplecov-json) >= 0.2
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(rubocop-gradual) >= 0.3
Requires:      gem(rubocop-lts) >= 18.0
Requires:      gem(rubocop-md) >= 1.2
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(rubocop-shopify) >= 2.12
Requires:      gem(rubocop-thread_safety) >= 0.5
Requires:      gem(standard) >= 1.25
Requires:      gem(rspec) >= 3.8
Requires:      gem(rspec-block_is_expected) >= 1.0
Requires:      gem(rake) >= 13.0
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-cobertura) >= 3
Conflicts:     gem(simplecov-json) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(rubocop-gradual) >= 1
Conflicts:     gem(rubocop-lts) >= 25
Conflicts:     gem(rubocop-md) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(rubocop-shopify) >= 3
Conflicts:     gem(rubocop-thread_safety) >= 1
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-block_is_expected) >= 2
Conflicts:     gem(rake) >= 14

%description   -n gem-rspec-stubbed-env-devel
Unobtrusively stub ENV keys and values during testing development package.

Stub environment variables in a scoped context for testing stub_env(
'AWS_REGION' => 'us-east-1', 'REDIS_URL' => 'redis://localhost:6379/' )

%description   -n gem-rspec-stubbed-env-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-stubbed_env.
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
%files         -n gem-rspec-stubbed-env-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-stubbed-env-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
