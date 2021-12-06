%define        gemname hammer_cli_foreman_tasks

Name:          gem-hammer-cli-foreman-tasks
Version:       0.0.16
Release:       alt1
Summary:       Foreman CLI plugin for showing tasks information for resoruces and users
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-tasks
Vcs:           https://github.com/theforeman/hammer-cli-foreman-tasks.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_tasks.yml
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(powerbar) >= 1.0.11 gem(powerbar) < 3.0
BuildRequires: gem(hammer_cli_foreman) > 0.1.1 gem(hammer_cli_foreman) < 4.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(powerbar) >= 1.0.11 gem(powerbar) < 3.0
Requires:      gem(hammer_cli_foreman) > 0.1.1 gem(hammer_cli_foreman) < 4.0.0
Provides:      gem(hammer_cli_foreman_tasks) = 0.0.16


%description
Contains the code for showing of the tasks (results and progress) in the Hammer
CLI.


%package       -n gem-hammer-cli-foreman-tasks-doc
Version:       0.0.16
Release:       alt1
Summary:       Foreman CLI plugin for showing tasks information for resoruces and users documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_tasks) = 0.0.16

%description   -n gem-hammer-cli-foreman-tasks-doc
Foreman CLI plugin for showing tasks information for resoruces and users
documentation files.

%description   -n gem-hammer-cli-foreman-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_tasks.


%package       -n gem-hammer-cli-foreman-tasks-devel
Version:       0.0.16
Release:       alt1
Summary:       Foreman CLI plugin for showing tasks information for resoruces and users development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_tasks) = 0.0.16

%description   -n gem-hammer-cli-foreman-tasks-devel
Foreman CLI plugin for showing tasks information for resoruces and users
development package.

%description   -n gem-hammer-cli-foreman-tasks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_tasks.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_tasks.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_tasks.yml

%files         -n gem-hammer-cli-foreman-tasks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-tasks-devel
%doc README.md


%changelog
* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.16-alt1
- + packaged gem with Ruby Policy 2.0
