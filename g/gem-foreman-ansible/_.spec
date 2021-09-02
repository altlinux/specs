%define        gemname foreman_ansible

Name:          gem-foreman-ansible
Version:       6.4.1
Release:       alt1
Summary:       Ansible integration in Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_ansible
Vcs:           https://github.com/theforeman/foreman_ansible.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(acts_as_list) >= 1.0.3 gem(acts_as_list) < 1.1
BuildRequires: gem(deface) < 2.0
BuildRequires: gem(foreman_remote_execution) >= 4.4.0
BuildRequires: gem(ipaddress) >= 0.8.0 gem(ipaddress) < 1.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_ansible,foreman-ansible
Requires:      gem(acts_as_list) >= 1.0.3 gem(acts_as_list) < 1.1
Requires:      gem(deface) < 2.0
Requires:      gem(foreman_remote_execution) >= 4.4.0
Requires:      gem(ipaddress) >= 0.8.0 gem(ipaddress) < 1.0
Provides:      gem(foreman_ansible) = 6.4.1


%description
Reporting and facts import from Ansible to Foreman.

* Import facts
* Monitor playbook and Ansible runs runtime
* Sends Ansible reports to Foreman that contain what changed on your system
after an ansible run.
* Stores a list of roles applicable to your hosts and 'plays' them
* Looking for an Ansible dynamic inventory for Foreman? Use
foreman_ansible_inventory


%package       -n gem-foreman-ansible-doc
Version:       6.4.1
Release:       alt1
Summary:       Ansible integration in Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_ansible
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_ansible) = 6.4.1

%description   -n gem-foreman-ansible-doc
Ansible integration in Foreman documentation files.

Reporting and facts import from Ansible to Foreman.

* Import facts
* Monitor playbook and Ansible runs runtime
* Sends Ansible reports to Foreman that contain what changed on your system
after an ansible run.
* Stores a list of roles applicable to your hosts and 'plays' them
* Looking for an Ansible dynamic inventory for Foreman? Use
foreman_ansible_inventory

%description   -n gem-foreman-ansible-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_ansible.


%package       -n gem-foreman-ansible-devel
Version:       6.4.1
Release:       alt1
Summary:       Ansible integration in Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_ansible
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_ansible) = 6.4.1

%description   -n gem-foreman-ansible-devel
Ansible integration in Foreman development package.

Reporting and facts import from Ansible to Foreman.

* Import facts
* Monitor playbook and Ansible runs runtime
* Sends Ansible reports to Foreman that contain what changed on your system
after an ansible run.
* Stores a list of roles applicable to your hosts and 'plays' them
* Looking for an Ansible dynamic inventory for Foreman? Use
foreman_ansible_inventory

%description   -n gem-foreman-ansible-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_ansible.


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

%files         -n gem-foreman-ansible-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-ansible-devel
%doc README.md
#%ruby_includedir/*


%changelog
* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.4.1-alt1
- ^ 6.0.1 -> 6.4.1

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 6.0.1-alt1
- + packaged gem with usage Ruby Policy 2.0
