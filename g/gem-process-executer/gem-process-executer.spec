%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname process_executer

Name:          gem-process-executer
Version:       1.2.0
Release:       alt1
Summary:       An API for executing commands in a subprocess
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/main-branch/process_executer
Vcs:           https://github.com/main-branch/process_executer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler-audit) >= 0.9
BuildRequires: gem(create_github_release) >= 2.1
BuildRequires: gem(main_branch_shared_rubocop_config) >= 0.1
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(semverify) >= 0.3
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(simplecov-rspec) >= 0.3
BuildRequires: gem(redcarpet) >= 3.6
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yardstick) >= 0.9
BuildConflicts: gem(bundler-audit) >= 1
BuildConflicts: gem(create_github_release) >= 3
BuildConflicts: gem(main_branch_shared_rubocop_config) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(semverify) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(simplecov-rspec) >= 1
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(yardstick) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Provides:      gem(process_executer) = 1.2.0


%description
An API for executing commands in a subprocess


%if_enabled    doc
%package       -n gem-process-executer-doc
Version:       1.2.0
Release:       alt1
Summary:       An API for executing commands in a subprocess documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета process_executer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(process_executer) = 1.2.0

%description   -n gem-process-executer-doc
An API for executing commands in a subprocess documentation files.

%description   -n gem-process-executer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета process_executer.
%endif


%if_enabled    devel
%package       -n gem-process-executer-devel
Version:       1.2.0
Release:       alt1
Summary:       An API for executing commands in a subprocess development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета process_executer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(process_executer) = 1.2.0
Requires:      gem(bundler-audit) >= 0.9
Requires:      gem(create_github_release) >= 2.1
Requires:      gem(main_branch_shared_rubocop_config) >= 0.1
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(semverify) >= 0.3
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(simplecov-rspec) >= 0.3
Requires:      gem(redcarpet) >= 3.6
Requires:      gem(yard) >= 0.9
Requires:      gem(yardstick) >= 0.9
Conflicts:     gem(bundler-audit) >= 1
Conflicts:     gem(create_github_release) >= 3
Conflicts:     gem(main_branch_shared_rubocop_config) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(semverify) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(simplecov-rspec) >= 1
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yardstick) >= 1

%description   -n gem-process-executer-devel
An API for executing commands in a subprocess development package.

%description   -n gem-process-executer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета process_executer.
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
%files         -n gem-process-executer-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-process-executer-devel
%doc README.md
%endif


%changelog
* Wed Oct 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
