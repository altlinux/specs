%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname em-spec

Name:          gem-em-spec
Version:       0.2.7
Release:       alt1
Summary:       BDD for Ruby/EventMachine
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/joshbuddy/em-spec
Vcs:           https://github.com/joshbuddy/em-spec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) > 2.6.0
BuildRequires: gem(bacon) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(rake) >= 0.8.7
BuildRequires: gem(eventmachine) >= 0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      gem(eventmachine) >= 0
Provides:      gem(em-spec) = 0.2.7


%description
Simple BDD API for testing asynchronous Ruby/EventMachine code


%if_enabled    doc
%package       -n gem-em-spec-doc
Version:       0.2.7
Release:       alt1
Summary:       BDD for Ruby/EventMachine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета em-spec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(em-spec) = 0.2.7

%description   -n gem-em-spec-doc
BDD for Ruby/EventMachine documentation files.

Simple BDD API for testing asynchronous Ruby/EventMachine code

%description   -n gem-em-spec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета em-spec.
%endif


%if_enabled    devel
%package       -n gem-em-spec-devel
Version:       0.2.7
Release:       alt1
Summary:       BDD for Ruby/EventMachine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета em-spec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(em-spec) = 0.2.7
Requires:      gem(rspec) > 2.6.0
Requires:      gem(bacon) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(guard-bundler) >= 0
Requires:      gem(rake) >= 0.8.7
Conflicts:     gem(rake) >= 14

%description   -n gem-em-spec-devel
BDD for Ruby/EventMachine development package.

Simple BDD API for testing asynchronous Ruby/EventMachine code

%description   -n gem-em-spec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета em-spec.
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
%files         -n gem-em-spec-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-em-spec-devel
%doc README.md
%endif


%changelog
* Mon Jul 29 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.7-alt1
- + packaged gem with Ruby Policy 2.0
