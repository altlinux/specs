%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rubocop-ruby3_2

Name:          gem-rubocop-ruby3-2
Version:       2.0.7.68
Release:       alt0.1
Summary:       Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop-lts/rubocop-ruby3_2
Vcs:           https://github.com/rubocop-lts/rubocop-ruby3_2.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(kettle-soup-cover) >= 1.0.4
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-block_is_expected) >= 1.0.5
BuildRequires: gem(rspec-stubbed_env) >= 1.0.1
BuildRequires: gem(rspec_junit_formatter) >= 0.5.1
BuildRequires: gem(rubocop-gradual) >= 0.3.4
BuildRequires: gem(rubocop-md) >= 1.2.1
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(rubocop-rspec) >= 2.25
BuildRequires: gem(rubocop-thread_safety) >= 0.5.1
BuildRequires: gem(standard-rubocop-lts) >= 1.0.9
BuildRequires: gem(version_gem) >= 1.1.3
BuildRequires: gem(yard) >= 0.9.34
BuildRequires: gem(yard-junk) >= 0.0.9
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(rspec-stubbed_env) >= 2
BuildConflicts: gem(rspec_junit_formatter) >= 1
BuildConflicts: gem(rubocop-gradual) >= 1
BuildConflicts: gem(rubocop-md) >= 3
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(rubocop-thread_safety) >= 1
BuildConflicts: gem(standard-rubocop-lts) >= 2
BuildConflicts: gem(version_gem) >= 3
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(yard-junk) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rspec_junit_formatter >= 0.5.1,rspec_junit_formatter < 1
%ruby_use_gem_dependency rubocop-md >= 2.0,rubocop-md < 3
%ruby_alias_names rubocop-ruby3_2,rubocop-ruby3-2
Requires:      ruby >= 3.2
Requires:      gem(rubocop-gradual) >= 0.3.4
Requires:      gem(rubocop-md) >= 1.2.1
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(rubocop-thread_safety) >= 0.5.1
Requires:      gem(standard-rubocop-lts) >= 1.0.9
Requires:      gem(version_gem) >= 1.1.3
Conflicts:     gem(rubocop-gradual) >= 1
Conflicts:     gem(rubocop-md) >= 3
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-thread_safety) >= 1
Conflicts:     gem(standard-rubocop-lts) >= 2
Conflicts:     gem(version_gem) >= 3
Provides:      gem(rubocop-ruby3_2) = 2.0.7.68

%ruby_use_gem_version rubocop-ruby3_2:2.0.7.68

%description
Configure RuboCop + a bevy of friends to gradually lint Ruby 3.2 code


%if_enabled    doc
%package       -n gem-rubocop-ruby3-2-doc
Version:       2.0.7.68
Release:       alt0.1
Summary:       Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-ruby3_2
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-ruby3_2) = 2.0.7.68

%description   -n gem-rubocop-ruby3-2-doc
Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual
documentation files.

Configure RuboCop + a bevy of friends to gradually lint Ruby 3.2 code

%description   -n gem-rubocop-ruby3-2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-ruby3_2.
%endif


%if_enabled    devel
%package       -n gem-rubocop-ruby3-2-devel
Version:       2.0.7.68
Release:       alt0.1
Summary:       Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-ruby3_2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-ruby3_2) = 2.0.7.68
Requires:      gem(kettle-soup-cover) >= 1.0.4
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(rake) >= 13.1
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-block_is_expected) >= 1.0.5
Requires:      gem(rspec-stubbed_env) >= 1.0.1
Requires:      gem(rspec_junit_formatter) >= 0.5.1
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-rspec) >= 2.25
Requires:      gem(yard) >= 0.9.34
Requires:      gem(yard-junk) >= 0.0.9
Conflicts:     gem(kettle-soup-cover) >= 2
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-block_is_expected) >= 2
Conflicts:     gem(rspec-stubbed_env) >= 2
Conflicts:     gem(rspec_junit_formatter) >= 1
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(yard-junk) >= 1

%description   -n gem-rubocop-ruby3-2-devel
Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual
development package.

Configure RuboCop + a bevy of friends to gradually lint Ruby 3.2 code

%description   -n gem-rubocop-ruby3-2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-ruby3_2.
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
%files         -n gem-rubocop-ruby3-2-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-ruby3-2-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Tue Dec 09 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.7.68-alt0.1
- ^ 2.0.7 -> 2.0.7p68

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.7-alt1
- + packaged gem with Ruby Policy 2.0
