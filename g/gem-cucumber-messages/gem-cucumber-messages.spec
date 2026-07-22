%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber-messages

Name:          gem-cucumber-messages
Version:       34.0.1
Release:       alt1
Summary:       cucumber-messages-34.0.1
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cucumber/messages#readme
Vcs:           https://github.com/cucumber/messages.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.3.1
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.81.6
BuildRequires: gem(rubocop-performance) >= 1.26.0
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
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.26.0,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.7.1,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 3.3
Requires:      rubygems >= 3.2.8
Provides:      gem(cucumber-messages) = 34.0.1

%description
JSON schema-based messages for Cucumber's inter-process communication


%if_enabled    doc
%package       -n gem-cucumber-messages-doc
Version:       34.0.1
Release:       alt1
Summary:       cucumber-messages-34.0.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber-messages
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-messages) = 34.0.1

%description   -n gem-cucumber-messages-doc
cucumber-messages-34.0.1 documentation files.

JSON schema-based messages for Cucumber's inter-process communication

%description   -n gem-cucumber-messages-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber-messages.
%endif


%if_enabled    devel
%package       -n gem-cucumber-messages-devel
Version:       34.0.1
Release:       alt1
Summary:       cucumber-messages-34.0.1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber-messages
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber-messages) = 34.0.1
Requires:      gem(rake) >= 13.3.1
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.81.6
Requires:      gem(rubocop-performance) >= 1.26.0
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-cucumber-messages-devel
cucumber-messages-34.0.1 development package.

JSON schema-based messages for Cucumber's inter-process communication

%description   -n gem-cucumber-messages-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber-messages.
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
%files         -n gem-cucumber-messages-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-messages-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 34.0.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
