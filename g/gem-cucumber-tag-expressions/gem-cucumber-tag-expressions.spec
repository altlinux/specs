%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-tag-expressions

Name:          gem-cucumber-tag-expressions
Version:       10.0.0
Release:       alt1
Summary:       cucumber-tag-expressions-10.0.0
License:       MIT
Group:         Development/Ruby
Url:           https://cucumber.io/docs/cucumber/api/#tag-expressions
Vcs:           https://github.com/cucumber/tag-expressions.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.3
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.47.0
BuildRequires: gem(rubocop-performance) >= 1.16.0
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.18.0
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
Requires:      ruby >= 2.6
Requires:      rubygems >= 3.2.3
Provides:      gem(cucumber-tag-expressions) = 10.0.0

%description
Cucumber tag expressions for ruby


%if_enabled    doc
%package       -n gem-cucumber-tag-expressions-doc
Version:       10.0.0
Release:       alt1
Summary:       cucumber-tag-expressions-10.0.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-tag-expressions
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-tag-expressions) = 10.0.0

%description   -n gem-cucumber-tag-expressions-doc
cucumber-tag-expressions-10.0.0 documentation files.

Cucumber tag expressions for ruby

%description   -n gem-cucumber-tag-expressions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-tag-expressions.
%endif


%if_enabled    devel
%package       -n gem-cucumber-tag-expressions-devel
Version:       10.0.0
Release:       alt1
Summary:       cucumber-tag-expressions-10.0.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-tag-expressions
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-tag-expressions) = 10.0.0
Requires:      gem(rake) >= 13.3
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.47.0
Requires:      gem(rubocop-performance) >= 1.16.0
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.18.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-tag-expressions-devel
cucumber-tag-expressions-10.0.0 development package.

Cucumber tag expressions for ruby

%description   -n gem-cucumber-tag-expressions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-tag-expressions.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cucumber-tag-expressions-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-tag-expressions-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 10.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
