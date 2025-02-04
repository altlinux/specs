%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_ansible

Name:          gem-foreman-ansible
Version:       15.0.1
Release:       alt1
Summary:       Ansible integration in Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_ansible
Vcs:           https://github.com/theforeman/foreman_ansible.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       .public.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildRequires: gem(acts_as_list) >= 1.0.3
BuildRequires: gem(foreman_remote_execution) >= 14.0
BuildRequires: gem(foreman-tasks) >= 10.0
BuildConflicts: gem(theforeman-rubocop) >= 0.2
BuildConflicts: gem(acts_as_list) >= 1.1
BuildConflicts: gem(deface) >= 2.0
BuildConflicts: gem(foreman_remote_execution) >= 15
BuildConflicts: gem(foreman-tasks) >= 11
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_ansible,foreman-ansible
Requires:      gem(acts_as_list) >= 1.0.3
Requires:      gem(foreman_remote_execution) >= 14.0
Requires:      gem(foreman-tasks) >= 10.0
Conflicts:     gem(acts_as_list) >= 1.1
Conflicts:     gem(deface) >= 2.0
Conflicts:     gem(foreman_remote_execution) >= 15
Conflicts:     gem(foreman-tasks) >= 11
Provides:      gem(foreman_ansible) = 15.0.1


%description
Reporting and facts import from Ansible to Foreman.

* Import facts
* Monitor playbook and Ansible runs runtime
* Sends Ansible reports to Foreman that contain what changed on your system
after an ansible run.
* Stores a list of roles applicable to your hosts and 'plays' them
* Looking for an Ansible dynamic inventory for Foreman? Use
foreman_ansible_inventory


%if_enabled    doc
%package       -n gem-foreman-ansible-doc
Version:       15.0.1
Release:       alt1
Summary:       Ansible integration in Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_ansible
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_ansible) = 15.0.1

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
%endif


%if_enabled    devel
%package       -n gem-foreman-ansible-devel
Version:       15.0.1
Release:       alt1
Summary:       Ansible integration in Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_ansible
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_ansible) = 15.0.1
Requires:      gem(theforeman-rubocop) >= 0.1.0
Conflicts:     gem(theforeman-rubocop) >= 0.2

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
%endif


%prep
%setup -a 1

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp .public %buildroot%_datadir/foreman/public

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%if_enabled    doc
%files         -n gem-foreman-ansible-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-ansible-devel
%doc README.md
%endif


%changelog
* Fri Oct 04 2024 Pavel Skrylev <majioa@altlinux.org> 15.0.1-alt1
- ^ 10.0.1 -> 15.0.1

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 10.0.1-alt1.1
- ! public webpack and assets

* Tue Jan 31 2023 Pavel Skrylev <majioa@altlinux.org> 10.0.1-alt1
- ^ 10.0.0 -> 10.0.1

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 10.0.0-alt1
- ^ 6.4.1 -> 10.0.0

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.4.1-alt1
- ^ 6.0.1 -> 6.4.1

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 6.0.1-alt1
- + packaged gem with usage Ruby Policy 2.0
