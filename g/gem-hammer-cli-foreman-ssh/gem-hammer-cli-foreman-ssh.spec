%define        gemname hammer_cli_foreman_ssh

Name:          gem-hammer-cli-foreman-ssh
Version:       0.0.3
Release:       alt1.1
Summary:       Adds Remote SSH support to Hammer Foreman CLI
License:       GPLv3+
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-ssh
Vcs:           https://github.com/theforeman/hammer-cli-foreman-ssh.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_ssh.yml
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(hammer_cli) >= 0.0.6
BuildRequires: gem(hammer_cli_foreman) >= 0
BuildRequires: gem(net-ssh-multi) >= 1.2.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(ci_reporter) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_ssh,hammer-cli-foreman-ssh
Requires:      gem(hammer_cli) >= 0.0.6
Requires:      gem(hammer_cli_foreman) >= 0
Requires:      gem(net-ssh-multi) >= 1.2.1
Provides:      gem(hammer_cli_foreman_ssh) = 0.0.3


%description
SSH plugin for hammer. Adds Remote SSH support to Hammer Foreman CLI.


%package       -n gem-hammer-cli-foreman-ssh-doc
Version:       0.0.3
Release:       alt1.1
Summary:       Adds Remote SSH support to Hammer Foreman CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_ssh
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_ssh) = 0.0.3

%description   -n gem-hammer-cli-foreman-ssh-doc
Adds Remote SSH support to Hammer Foreman CLI documentation files.

SSH plugin for hammer. Adds Remote SSH support to Hammer Foreman CLI.

%description   -n gem-hammer-cli-foreman-ssh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_ssh.


%package       -n gem-hammer-cli-foreman-ssh-devel
Version:       0.0.3
Release:       alt1.1
Summary:       Adds Remote SSH support to Hammer Foreman CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_ssh
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_ssh) = 0.0.3
Requires:      gem(rake) >= 10.1.0
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(ci_reporter) >= 3

%description   -n gem-hammer-cli-foreman-ssh-devel
Adds Remote SSH support to Hammer Foreman CLI development package.

SSH plugin for hammer. Adds Remote SSH support to Hammer Foreman CLI.

%description   -n gem-hammer-cli-foreman-ssh-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_ssh.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_ssh.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_ssh.yml

%files         -n gem-hammer-cli-foreman-ssh-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-ssh-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1.1
- ! closes build deps under check condition

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1
- + packaged gem with Ruby Policy 2.0
