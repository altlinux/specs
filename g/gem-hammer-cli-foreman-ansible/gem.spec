%define        gemname hammer_cli_foreman_ansible

Name:          gem-hammer-cli-foreman-ansible
Version:       0.3.4
Release:       alt1
Summary:       Foreman Ansible plugin for Hammer CLI
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-ansible
Vcs:           https://github.com/theforeman/hammer-cli-foreman-ansible.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_ansible.yml
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hammer_cli_foreman) >= 0.12.0
BuildRequires: gem(rake) >= 12.3.3 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(hammer_cli_foreman) >= 0.12.0
Provides:      gem(hammer_cli_foreman_ansible) = 0.3.4


%description
This Hammer CLI plugin contains set of commands for foreman_ansible, a plugin
to Foreman for Ansible.


%package       -n gem-hammer-cli-foreman-ansible-doc
Version:       0.3.4
Release:       alt1
Summary:       Foreman Ansible plugin for Hammer CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_ansible
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_ansible) = 0.3.4

%description   -n gem-hammer-cli-foreman-ansible-doc
Foreman Ansible plugin for Hammer CLI documentation files.

This Hammer CLI plugin contains set of commands for foreman_ansible, a plugin
to Foreman for Ansible.

%description   -n gem-hammer-cli-foreman-ansible-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_ansible.


%package       -n gem-hammer-cli-foreman-ansible-devel
Version:       0.3.4
Release:       alt1
Summary:       Foreman Ansible plugin for Hammer CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_ansible
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_ansible) = 0.3.4
Requires:      gem(rake) >= 12.3.3 gem(rake) < 14

%description   -n gem-hammer-cli-foreman-ansible-devel
Foreman Ansible plugin for Hammer CLI development package.

This Hammer CLI plugin contains set of commands for foreman_ansible, a plugin
to Foreman for Ansible.

%description   -n gem-hammer-cli-foreman-ansible-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_ansible.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_ansible.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_ansible.yml

%files         -n gem-hammer-cli-foreman-ansible-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-ansible-devel
%doc README.md


%changelog
* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.4-alt1
- + packaged gem with Ruby Policy 2.0
