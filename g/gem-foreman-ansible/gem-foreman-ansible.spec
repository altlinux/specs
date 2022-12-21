%define        gemname foreman_ansible

Name:          gem-foreman-ansible
Version:       10.0.0
Release:       alt1
Summary:       Ansible integration in Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_ansible
Vcs:           https://github.com/theforeman/foreman_ansible.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       public.tar
Patch:         graphql.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(acts_as_list) >= 1.0.3 gem(acts_as_list) < 1.1
BuildRequires: gem(deface) < 2.0
BuildRequires: gem(foreman_remote_execution) >= 8.0.0
BuildRequires: gem(foreman-tasks) >= 7.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_ansible,foreman-ansible
Requires:      gem(acts_as_list) >= 1.0.3 gem(acts_as_list) < 1.1
Requires:      gem(deface) < 2.0
Requires:      gem(foreman_remote_execution) >= 8.0.0
Requires:      gem(foreman-tasks) >= 7.0.0
Provides:      gem(foreman_ansible) = 10.0.0


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
Version:       10.0.0
Release:       alt1
Summary:       Ansible integration in Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_ansible
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_ansible) = 10.0.0

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
Version:       10.0.0
Release:       alt1
Summary:       Ansible integration in Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_ansible
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_ansible) = 10.0.0

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
%setup -a 1
%autopatch

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp public %buildroot%_datadir/foreman

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%files         -n gem-foreman-ansible-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-ansible-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 10.0.0-alt1
- ^ 6.4.1 -> 10.0.0

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.4.1-alt1
- ^ 6.0.1 -> 6.4.1

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 6.0.1-alt1
- + packaged gem with usage Ruby Policy 2.0
