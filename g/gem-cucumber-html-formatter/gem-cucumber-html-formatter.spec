%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-html-formatter

Name:          gem-cucumber-html-formatter
Version:       24.0.0
Release:       alt1
Summary:       cucumber-html-formatter-24.0.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cucumber/html-formatter
Vcs:           https://github.com/cucumber/html-formatter.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(cucumber-messages) > 23
BuildRequires: gem(rake) >= 13.3
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.81.0
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildConflicts: gem(cucumber-messages) >= 35
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency cucumber-messages >= 34.0.1,cucumber-messages < 35
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-rake >= 0.7.1,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 3.1
Requires:      rubygems >= 3.2.8
Requires:      gem(cucumber-messages) > 23
Conflicts:     gem(cucumber-messages) >= 35
Provides:      gem(cucumber-html-formatter) = 24.0.0

%description
HTML formatter for Cucumber


%package       -n cucumber-html-formatter
Version:       24.0.0
Release:       alt1
Summary:       cucumber-html-formatter-24.0.0 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета cucumber-html-formatter
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-html-formatter) = 24.0.0

%description   -n cucumber-html-formatter
cucumber-html-formatter-24.0.0 executable(s).

HTML formatter for Cucumber

%description   -n cucumber-html-formatter -l ru_RU.UTF-8
Исполнямка для самоцвета cucumber-html-formatter.


%if_enabled    doc
%package       -n gem-cucumber-html-formatter-doc
Version:       24.0.0
Release:       alt1
Summary:       cucumber-html-formatter-24.0.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-html-formatter
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-html-formatter) = 24.0.0

%description   -n gem-cucumber-html-formatter-doc
cucumber-html-formatter-24.0.0 documentation files.

HTML formatter for Cucumber

%description   -n gem-cucumber-html-formatter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-html-formatter.
%endif


%if_enabled    devel
%package       -n gem-cucumber-html-formatter-devel
Version:       24.0.0
Release:       alt1
Summary:       cucumber-html-formatter-24.0.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-html-formatter
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-html-formatter) = 24.0.0
Requires:      gem(rake) >= 13.3
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.81.0
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-html-formatter-devel
cucumber-html-formatter-24.0.0 development package.

HTML formatter for Cucumber

%description   -n gem-cucumber-html-formatter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-html-formatter.
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

%files         -n cucumber-html-formatter
%doc LICENSE README.md
%_bindir/cucumber-html-formatter

%if_enabled    doc
%files         -n gem-cucumber-html-formatter-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-html-formatter-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 24.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
