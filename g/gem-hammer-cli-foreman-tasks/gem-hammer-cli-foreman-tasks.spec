%define        gemname hammer_cli_foreman_tasks

Name:          gem-hammer-cli-foreman-tasks
Version:       0.0.18
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
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(psych) >= 0
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(powerbar) >= 1.0.11
BuildRequires: gem(hammer_cli_foreman) > 0.1.1
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(powerbar) >= 3.0
BuildConflicts: gem(hammer_cli_foreman) >= 4.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_tasks,hammer-cli-foreman-tasks
Requires:      gem(powerbar) >= 1.0.11
Requires:      gem(hammer_cli_foreman) > 0.1.1
Conflicts:     gem(powerbar) >= 3.0
Conflicts:     gem(hammer_cli_foreman) >= 4.0.0
Provides:      gem(hammer_cli_foreman_tasks) = 0.0.18


%description
Contains the code for showing of the tasks (results and progress) in the Hammer
CLI.


%package       -n gem-hammer-cli-foreman-tasks-doc
Version:       0.0.18
Release:       alt1
Summary:       Foreman CLI plugin for showing tasks information for resoruces and users documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_tasks) = 0.0.18

%description   -n gem-hammer-cli-foreman-tasks-doc
Foreman CLI plugin for showing tasks information for resoruces and users
documentation files.

%description   -n gem-hammer-cli-foreman-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_tasks.


%package       -n gem-hammer-cli-foreman-tasks-devel
Version:       0.0.18
Release:       alt1
Summary:       Foreman CLI plugin for showing tasks information for resoruces and users development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_tasks) = 0.0.18
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(psych) >= 0
Requires:      gem(rake) >= 10.1.0
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(ci_reporter) >= 3

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
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.18-alt1
- ^ 0.0.16 -> 0.0.18

* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.16-alt1
- + packaged gem with Ruby Policy 2.0
