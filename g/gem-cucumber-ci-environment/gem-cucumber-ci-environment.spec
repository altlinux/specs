%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-ci-environment

Name:          gem-cucumber-ci-environment
Version:       14.0.0
Release:       alt1
Summary:       cucumber-ci-environment-14.0.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cucumber/ci-environment
Vcs:           https://github.com/cucumber/ci-environment.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.3
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.81.0
BuildRequires: gem(rubocop-performance) >= 1.23.0
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.26.0,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.7.1,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 3.2
Requires:      rubygems >= 3.2.8
Provides:      gem(cucumber-ci-environment) = 14.0.0

%description
Detect CI Environment from environment variables


%if_enabled    doc
%package       -n gem-cucumber-ci-environment-doc
Version:       14.0.0
Release:       alt1
Summary:       cucumber-ci-environment-14.0.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-ci-environment
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-ci-environment) = 14.0.0

%description   -n gem-cucumber-ci-environment-doc
cucumber-ci-environment-14.0.0 documentation files.

Detect CI Environment from environment variables

%description   -n gem-cucumber-ci-environment-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-ci-environment.
%endif


%if_enabled    devel
%package       -n gem-cucumber-ci-environment-devel
Version:       14.0.0
Release:       alt1
Summary:       cucumber-ci-environment-14.0.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-ci-environment
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-ci-environment) = 14.0.0
Requires:      gem(rake) >= 13.3
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.81.0
Requires:      gem(rubocop-performance) >= 1.23.0
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-ci-environment-devel
cucumber-ci-environment-14.0.0 development package.

Detect CI Environment from environment variables

%description   -n gem-cucumber-ci-environment-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-ci-environment.
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
%doc LICENSE
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cucumber-ci-environment-doc
%doc LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-ci-environment-devel
%doc LICENSE
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 14.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
