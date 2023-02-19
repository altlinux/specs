%define        gemname hammer_cli_foreman_remote_execution

Name:          gem-hammer-cli-foreman-remote-execution
Version:       0.2.2.1
Release:       alt0.1
Summary:       CLI for the Foreman remote execution plugin
License:       GPL-3.0-or-later
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer_cli_foreman_remote_execution
Vcs:           https://github.com/theforeman/hammer_cli_foreman_remote_execution.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source1:       foreman_remote_execution.yml
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(hammer_cli_foreman) >= 0.1.3
BuildRequires: gem(hammer_cli_foreman_tasks) >= 0.0.3
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(hammer_cli_foreman) >= 4.0.0
BuildConflicts: gem(hammer_cli_foreman_tasks) >= 0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_remote_execution,hammer-cli-foreman-remote-execution
Requires:      gem(hammer_cli_foreman) >= 0.1.3
Requires:      gem(hammer_cli_foreman_tasks) >= 0.0.3
Conflicts:     gem(hammer_cli_foreman) >= 4.0.0
Conflicts:     gem(hammer_cli_foreman_tasks) >= 0.1
Provides:      gem(hammer_cli_foreman_remote_execution) = 0.2.2.1

%ruby_use_gem_version hammer_cli_foreman_remote_execution:0.2.2.1

%description
This Hammer CLI plugin contains commands for foreman_remote_execution.


%package       -n gem-hammer-cli-foreman-remote-execution-doc
Version:       0.2.2.1
Release:       alt0.1
Summary:       CLI for the Foreman remote execution plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_remote_execution
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_remote_execution) = 0.2.2.1

%description   -n gem-hammer-cli-foreman-remote-execution-doc
CLI for the Foreman remote execution plugin documentation files.

This Hammer CLI plugin contains commands for foreman_remote_execution.

%description   -n gem-hammer-cli-foreman-remote-execution-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_remote_execution.


%package       -n gem-hammer-cli-foreman-remote-execution-devel
Version:       0.2.2.1
Release:       alt0.1
Summary:       CLI for the Foreman remote execution plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_remote_execution
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_remote_execution) = 0.2.2.1
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(rake) >= 10.1.0
Requires:      gem(thor) >= 0
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(ci_reporter) >= 3

%description   -n gem-hammer-cli-foreman-remote-execution-devel
CLI for the Foreman remote execution plugin development package.

This Hammer CLI plugin contains commands for foreman_remote_execution.

%description   -n gem-hammer-cli-foreman-remote-execution-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_remote_execution.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_remote_execution.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%config(noreplace) %attr(770,_foreman,foreman) %_sysconfdir/hammer/cli.modules.d/foreman_remote_execution.yml

%files         -n gem-hammer-cli-foreman-remote-execution-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-remote-execution-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.2.1-alt0.1
- ^ 0.2.2 -> 0.2.2p1

* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- + packaged gem with Ruby Policy 2.0
