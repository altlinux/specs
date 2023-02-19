%define        gemname hammer_cli_foreman_statistics

Name:          gem-hammer-cli-foreman-statistics
Version:       0.0.1
Release:       alt1.1
Summary:       Foreman Statistics plugin for Hammer CLI
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-statistics
Vcs:           https://github.com/theforeman/hammer-cli-foreman-statistics.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(ci_reporter) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_statistics,hammer-cli-foreman-statistics
Provides:      gem(hammer_cli_foreman_statistics) = 0.0.1


%description
This Hammer CLI plugin contains set of commands for foreman_statistics.


%package       -n gem-hammer-cli-foreman-statistics-doc
Version:       0.0.1
Release:       alt1.1
Summary:       Foreman Statistics plugin for Hammer CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_statistics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_statistics) = 0.0.1

%description   -n gem-hammer-cli-foreman-statistics-doc
Foreman Statistics plugin for Hammer CLI documentation files.

This Hammer CLI plugin contains set of commands for foreman_statistics.

%description   -n gem-hammer-cli-foreman-statistics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_statistics.


%package       -n gem-hammer-cli-foreman-statistics-devel
Version:       0.0.1
Release:       alt1.1
Summary:       Foreman Statistics plugin for Hammer CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_statistics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_statistics) = 0.0.1
Requires:      gem(rake) >= 10.1.0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(ci_reporter) >= 3

%description   -n gem-hammer-cli-foreman-statistics-devel
Foreman Statistics plugin for Hammer CLI development package.

This Hammer CLI plugin contains set of commands for foreman_statistics.

%description   -n gem-hammer-cli-foreman-statistics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_statistics.


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

%files         -n gem-hammer-cli-foreman-statistics-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-statistics-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1.1
- ! closes build deps under check condition

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
