%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-core

Name:          gem-cucumber-core
Version:       17.0.0
Release:       alt1
Summary:       cucumber-core-17.0.0
License:       MIT
Group:         Development/Ruby
Url:           https://cucumber.io
Vcs:           https://github.com/cucumber/cucumber-ruby-core.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(cucumber-gherkin) > 36
BuildRequires: gem(cucumber-messages) > 31
BuildRequires: gem(cucumber-tag-expressions) > 6
BuildRequires: gem(rake) >= 13.3
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.81.6
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rake) >= 0.7.1
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildConflicts: gem(cucumber-gherkin) >= 42
BuildConflicts: gem(cucumber-messages) >= 35
BuildConflicts: gem(cucumber-tag-expressions) >= 11
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency cucumber-gherkin >= 41.0.0,cucumber-gherkin < 42
%ruby_use_gem_dependency cucumber-messages >= 34.0.1,cucumber-messages < 35
%ruby_use_gem_dependency cucumber-tag-expressions >= 10.0.0,cucumber-tag-expressions < 11
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency rubocop-rake >= 0.7.1,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 3.2
Requires:      rubygems >= 3.2.8
Requires:      gem(cucumber-gherkin) > 36
Requires:      gem(cucumber-messages) > 31
Requires:      gem(cucumber-tag-expressions) > 6
Conflicts:     gem(cucumber-gherkin) >= 42
Conflicts:     gem(cucumber-messages) >= 35
Conflicts:     gem(cucumber-tag-expressions) >= 11
Provides:      gem(cucumber-core) = 17.0.0

%description
Core library for the Cucumber BDD app


%if_enabled    doc
%package       -n gem-cucumber-core-doc
Version:       17.0.0
Release:       alt1
Summary:       cucumber-core-17.0.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-core
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-core) = 17.0.0

%description   -n gem-cucumber-core-doc
cucumber-core-17.0.0 documentation files.

Core library for the Cucumber BDD app

%description   -n gem-cucumber-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-core.
%endif


%if_enabled    devel
%package       -n gem-cucumber-core-devel
Version:       17.0.0
Release:       alt1
Summary:       cucumber-core-17.0.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-core
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-core) = 17.0.0
Requires:      gem(rake) >= 13.3
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.81.6
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-rake) >= 0.7.1
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-core-devel
cucumber-core-17.0.0 development package.

Core library for the Cucumber BDD app

%description   -n gem-cucumber-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-core.
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
%doc CHANGELOG.md LICENSE README.md CHANGELOG.old.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cucumber-core-doc
%doc CHANGELOG.md LICENSE README.md CHANGELOG.old.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-core-devel
%doc CHANGELOG.md LICENSE README.md CHANGELOG.old.md CONTRIBUTING.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 17.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
