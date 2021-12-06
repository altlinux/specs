%define        gemname hammer_cli_foreman_remote_execution

Name:          gem-hammer-cli-foreman-remote-execution
Version:       0.2.2
Release:       alt1
Summary:       CLI for the Foreman remote execution plugin
License:       GPL-3.0-or-later
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer_cli_foreman_remote_execution
Vcs:           https://github.com/theforeman/hammer_cli_foreman_remote_execution.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_remote_execution.yml
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hammer_cli_foreman) >= 0.1.3 gem(hammer_cli_foreman) < 4.0.0
BuildRequires: gem(hammer_cli_foreman_tasks) >= 0.0.3 gem(hammer_cli_foreman_tasks) < 0.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli_foreman) >= 0.1.3 gem(hammer_cli_foreman) < 4.0.0
Requires:      gem(hammer_cli_foreman_tasks) >= 0.0.3 gem(hammer_cli_foreman_tasks) < 0.1
Provides:      gem(hammer_cli_foreman_remote_execution) = 0.2.2


%description
This Hammer CLI plugin contains commands for foreman_remote_execution.


%package       -n gem-hammer-cli-foreman-remote-execution-doc
Version:       0.2.2
Release:       alt1
Summary:       CLI for the Foreman remote execution plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_remote_execution
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_remote_execution) = 0.2.2

%description   -n gem-hammer-cli-foreman-remote-execution-doc
CLI for the Foreman remote execution plugin documentation files.

This Hammer CLI plugin contains commands for foreman_remote_execution.

%description   -n gem-hammer-cli-foreman-remote-execution-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_remote_execution.


%package       -n gem-hammer-cli-foreman-remote-execution-devel
Version:       0.2.2
Release:       alt1
Summary:       CLI for the Foreman remote execution plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_remote_execution
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_remote_execution) = 0.2.2

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
* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- + packaged gem with Ruby Policy 2.0
