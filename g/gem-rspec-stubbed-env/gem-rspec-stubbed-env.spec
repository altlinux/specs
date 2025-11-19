%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rspec-stubbed_env

Name:          gem-rspec-stubbed-env
Version:       1.0.4
Release:       alt1
Summary:       Unobtrusively stub ENV keys and values during testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pboling/rspec-stubbed_env
Vcs:           https://github.com/pboling/rspec-stubbed_env.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal2) >= 3.0
BuildRequires: gem(benchmark) >= 0.4.1
BuildRequires: gem(bundler-audit) >= 0.9.2
BuildRequires: gem(kettle-soup-cover) >= 1.0.6
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(reek) >= 6.4
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-block_is_expected) >= 1.0
BuildRequires: gem(rspec_junit_formatter) >= 0.5.1
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-lts) >= 0.1.1
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rspec) >= 3.2
BuildRequires: gem(standard) >= 1.50
BuildRequires: gem(stone_checksums) >= 1.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0.10
BuildRequires: gem(yard-relative_markdown_links) >= 0.5.0
BuildConflicts: gem(appraisal2) >= 4
BuildConflicts: gem(benchmark) >= 1
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(rspec_junit_formatter) >= 1
BuildConflicts: gem(rubocop-lts) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-relative_markdown_links) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rspec_junit_formatter >= 0.5.1,rspec_junit_formatter < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_alias_names rspec-stubbed_env,rspec-stubbed-env
Requires:      ruby >= 1.8.7
Provides:      gem(rspec-stubbed_env) = 1.0.4

%description
Stub environment variables in a scoped context for testing stub_env(
'AWS_REGION' => 'us-east-1', 'REDIS_URL' => 'redis://localhost:6379/' )


%if_enabled    doc
%package       -n gem-rspec-stubbed-env-doc
Version:       1.0.4
Release:       alt1
Summary:       Unobtrusively stub ENV keys and values during testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-stubbed_env
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-stubbed_env) = 1.0.4

%description   -n gem-rspec-stubbed-env-doc
Unobtrusively stub ENV keys and values during testing documentation files.

Stub environment variables in a scoped context for testing stub_env(
'AWS_REGION' => 'us-east-1', 'REDIS_URL' => 'redis://localhost:6379/' )

%description   -n gem-rspec-stubbed-env-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-stubbed_env.
%endif


%if_enabled    devel
%package       -n gem-rspec-stubbed-env-devel
Version:       1.0.4
Release:       alt1
Summary:       Unobtrusively stub ENV keys and values during testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-stubbed_env
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(appraisal2) >= 3.0
Requires:      gem(benchmark) >= 0.4.1
Requires:      gem(bundler-audit) >= 0.9.2
Requires:      gem(kettle-soup-cover) >= 1.0.6
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(reek) >= 6.4
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-block_is_expected) >= 1.0
Requires:      gem(rspec_junit_formatter) >= 0.5.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-lts) >= 0.1.1
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-rspec) >= 3.2
Requires:      gem(standard) >= 1.50
Requires:      gem(stone_checksums) >= 1.0
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-junk) >= 0.0.10
Requires:      gem(yard-relative_markdown_links) >= 0.5.0
Conflicts:     gem(appraisal2) >= 4
Conflicts:     gem(benchmark) >= 1
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(kettle-soup-cover) >= 2
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(reek) >= 7
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-block_is_expected) >= 2
Conflicts:     gem(rspec_junit_formatter) >= 1
Conflicts:     gem(rubocop-lts) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(stone_checksums) >= 2
Conflicts:     gem(yard-junk) >= 1
Conflicts:     gem(yard-relative_markdown_links) >= 0.6

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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rspec-stubbed-env-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-stubbed-env-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Wed Nov 19 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- ^ 1.0.1 -> 1.0.4

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
