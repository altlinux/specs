%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-gherkin

Name:          gem-cucumber-gherkin
Version:       41.0.0
Release:       alt1
Summary:       cucumber-gherkin-41.0.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cucumber/gherkin
Vcs:           https://github.com/cucumber/gherkin.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(cucumber-messages) >= 31
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.71.2
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-performance) >= 1.23.1
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.4.0
BuildConflicts: gem(cucumber-messages) >= 35
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency cucumber-messages >= 34.0.1,cucumber-messages < 35
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency rubocop-performance >= 1.26.0,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.7.1,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 3.2
Requires:      rubygems >= 3.2.8
Requires:      gem(cucumber-messages) >= 31
Conflicts:     gem(cucumber-messages) >= 35
Provides:      gem(cucumber-gherkin) = 41.0.0

%description
Gherkin parser


%package       -n gherkin
Version:       41.0.0
Release:       alt1
Summary:       cucumber-gherkin-41.0.0 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета cucumber-gherkin
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-gherkin) = 41.0.0

%description   -n gherkin
cucumber-gherkin-41.0.0 executable(s).

Gherkin parser

%description   -n gherkin -l ru_RU.UTF-8
Исполнямка для самоцвета cucumber-gherkin.


%if_enabled    doc
%package       -n gem-cucumber-gherkin-doc
Version:       41.0.0
Release:       alt1
Summary:       cucumber-gherkin-41.0.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-gherkin
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-gherkin) = 41.0.0

%description   -n gem-cucumber-gherkin-doc
cucumber-gherkin-41.0.0 documentation files.

Gherkin parser

%description   -n gem-cucumber-gherkin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-gherkin.
%endif


%if_enabled    devel
%package       -n gem-cucumber-gherkin-devel
Version:       41.0.0
Release:       alt1
Summary:       cucumber-gherkin-41.0.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-gherkin
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-gherkin) = 41.0.0
Requires:      gem(rake) >= 13.1
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.71.2
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-performance) >= 1.23.1
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.4.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-gherkin-devel
cucumber-gherkin-41.0.0 development package.

Gherkin parser

%description   -n gem-cucumber-gherkin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-gherkin.
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
%doc LICENSE README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gherkin
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/gherkin-ruby
%_bindir/gherkin

%if_enabled    doc
%files         -n gem-cucumber-gherkin-doc
%doc LICENSE README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-gherkin-devel
%doc LICENSE README.md CONTRIBUTING.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 41.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
