%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rubocop-ruby3_2

Name:          gem-rubocop-ruby3-2
Version:       2.0.7
Release:       alt1
Summary:       Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop-lts/rubocop-ruby3_2
Vcs:           https://github.com/rubocop-lts/rubocop-ruby3_2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(simplecov-json) >= 0.2
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(standard-rails) >= 0.1
BuildRequires: gem(betterlint) >= 1.4.7
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-block_is_expected) >= 1.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0
BuildRequires: gem(redcarpet) >= 3.6
BuildRequires: gem(pry-suite) >= 1.2
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rubocop-gradual) >= 0.3.1
BuildRequires: gem(rubocop-md) >= 1.2
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(rubocop-shopify) >= 2.14
BuildRequires: gem(rubocop-thread_safety) >= 0.5.1
BuildRequires: gem(standard-rubocop-lts) >= 1.0.7
BuildRequires: gem(version_gem) >= 1.1.3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-json) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(standard-rails) >= 1
BuildConflicts: gem(betterlint) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(pry-suite) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rubocop-gradual) >= 1
BuildConflicts: gem(rubocop-md) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-shopify) >= 3
BuildConflicts: gem(rubocop-thread_safety) >= 1
BuildConflicts: gem(standard-rubocop-lts) >= 2
BuildConflicts: gem(version_gem) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      gem(rubocop-gradual) >= 0.3.1
Requires:      gem(rubocop-md) >= 1.2
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(rubocop-shopify) >= 2.14
Requires:      gem(rubocop-thread_safety) >= 0.5.1
Requires:      gem(standard-rubocop-lts) >= 1.0.7
Requires:      gem(version_gem) >= 1.1.3
Conflicts:     gem(rubocop-gradual) >= 1
Conflicts:     gem(rubocop-md) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-shopify) >= 3
Conflicts:     gem(rubocop-thread_safety) >= 1
Conflicts:     gem(standard-rubocop-lts) >= 2
Conflicts:     gem(version_gem) >= 3
Provides:      gem(rubocop-ruby3_2) = 2.0.7


%description
Configure RuboCop + a bevy of friends to gradually lint Ruby 3.2 code


%if_enabled    doc
%package       -n gem-rubocop-ruby3-2-doc
Version:       2.0.7
Release:       alt1
Summary:       Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-ruby3_2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-ruby3_2) = 2.0.7

%description   -n gem-rubocop-ruby3-2-doc
Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual
documentation files.

Configure RuboCop + a bevy of friends to gradually lint Ruby 3.2 code

%description   -n gem-rubocop-ruby3-2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-ruby3_2.
%endif


%if_enabled    devel
%package       -n gem-rubocop-ruby3-2-devel
Version:       2.0.7
Release:       alt1
Summary:       Rules for Rubies: Rubocop + Standard + Betterlint + Shopify + Gradual development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-ruby3_2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-ruby3_2) = 2.0.7
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(simplecov-json) >= 0.2
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(standard-rails) >= 0.1
Requires:      gem(betterlint) >= 1.4.7
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-block_is_expected) >= 1.0
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-junk) >= 0.0
Requires:      gem(redcarpet) >= 3.6
Requires:      gem(pry-suite) >= 1.2
Requires:      gem(pry-debugger-jruby) >= 2.1
Requires:      gem(rake) >= 13.0
Requires:      gem(pry) >= 0.13.1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-json) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(standard-rails) >= 1
Conflicts:     gem(betterlint) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-block_is_expected) >= 2
Conflicts:     gem(yard-junk) >= 1
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(pry-suite) >= 2
Conflicts:     gem(pry-debugger-jruby) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(pry) >= 1

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-ruby3-2-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-ruby3-2-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.7-alt1
- + packaged gem with Ruby Policy 2.0
