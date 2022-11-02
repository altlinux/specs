%define        gemname train

Name:          gem-train
Version:       3.10.7
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train/
Vcs:           https://github.com/inspec/train.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(minitest) >= 5.8 gem(minitest) < 6
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(chefstyle) >= 2.1.1 gem(chefstyle) < 3
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(ed25519) >= 0
BuildRequires: gem(bcrypt_pbkdf) >= 0
BuildRequires: gem(mocha) >= 1.1 gem(mocha) < 2
BuildRequires: gem(berkshelf) >= 6.0
BuildRequires: gem(test-kitchen) >= 2
BuildRequires: gem(kitchen-vagrant) >= 0
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(license_finder) >= 0
BuildRequires: gem(train-winrm) >= 0.2 gem(train-winrm) < 1
BuildRequires: gem(activesupport) >= 6.0.3.1
BuildRequires: gem(inifile) >= 3.0 gem(inifile) < 4
BuildRequires: gem(azure_graph_rbac) >= 0.16 gem(azure_graph_rbac) < 1
BuildRequires: gem(azure_mgmt_key_vault) >= 0.17 gem(azure_mgmt_key_vault) < 1
BuildRequires: gem(azure_mgmt_resources) >= 0.15 gem(azure_mgmt_resources) < 1
BuildRequires: gem(azure_mgmt_security) >= 0.18 gem(azure_mgmt_security) < 1
BuildRequires: gem(azure_mgmt_storage) >= 0.18 gem(azure_mgmt_storage) < 1
BuildRequires: gem(docker-api) >= 1.26 gem(docker-api) < 3.0
BuildRequires: gem(google-api-client) >= 0.53.0 gem(google-api-client) < 1
BuildRequires: gem(googleauth) >= 1.2.0 gem(googleauth) < 2
BuildRequires: gem(addressable) >= 2.5 gem(addressable) < 3
BuildRequires: gem(ffi) > 1.13.0
BuildRequires: gem(json) >= 1.8 gem(json) < 3
BuildRequires: gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
BuildRequires: gem(net-scp) >= 1.2 gem(net-scp) < 5.0
BuildRequires: gem(net-ssh) >= 2.9 gem(net-ssh) < 8.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_use_gem_dependency google-api-client >= 2.2.2,google-api-client < 3
%ruby_use_gem_dependency googleauth >= 1.2.0,googleauth < 2
Requires:      gem(train-core) = 3.10.7
Requires:      gem(train-winrm) >= 0.2 gem(train-winrm) < 1
Requires:      gem(activesupport) >= 6.0.3.1
Requires:      gem(inifile) >= 3.0 gem(inifile) < 4
Requires:      gem(azure_graph_rbac) >= 0.16 gem(azure_graph_rbac) < 1
Requires:      gem(azure_mgmt_key_vault) >= 0.17 gem(azure_mgmt_key_vault) < 1
Requires:      gem(azure_mgmt_resources) >= 0.15 gem(azure_mgmt_resources) < 1
Requires:      gem(azure_mgmt_security) >= 0.18 gem(azure_mgmt_security) < 1
Requires:      gem(azure_mgmt_storage) >= 0.18 gem(azure_mgmt_storage) < 1
Requires:      gem(docker-api) >= 1.26 gem(docker-api) < 3.0
Requires:      gem(google-api-client) >= 0.53.0 gem(google-api-client) < 1
Requires:      gem(googleauth) >= 1.2.0 gem(googleauth) < 2
Provides:      gem(train) = 3.10.7


%description
Train lets you talk to your local or remote operating systems and APIs with an
unified interface.

It allows you to:

* execute commands via run_command
* interact with files via file
* identify the target operating system via os
* authenticate to API-based services and treat them like a platform

Train supports:

* Local execution
* SSH
* WinRM
* Docker
* Mock (for testing and debugging)
* AWS as an API
* Azure as an API
* VMware via PowerCLI


%package       -n gem-train-core
Version:       3.10.7
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(addressable) >= 2.5 gem(addressable) < 3
Requires:      gem(ffi) > 1.13.0
Requires:      gem(json) >= 1.8 gem(json) < 3
Requires:      gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
Requires:      gem(net-scp) >= 1.2 gem(net-scp) < 5.0
Requires:      gem(net-ssh) >= 2.9 gem(net-ssh) < 8.0
Provides:      gem(train-core) = 3.10.7

%description   -n gem-train-core
Transport Interface to unify communication over SSH, WinRM, and friends.


%package       -n gem-train-core-doc
Version:       3.10.7
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-core) = 3.10.7

%description   -n gem-train-core-doc
Transport Interface to unify communication over SSH, WinRM, and friends
documentation files.

%description   -n gem-train-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-core.


%package       -n gem-train-doc
Version:       3.10.7
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train) = 3.10.7

%description   -n gem-train-doc
Transport Interface to unify communication over SSH, WinRM, and friends
documentation files.

Train lets you talk to your local or remote operating systems and APIs with an
unified interface.

It allows you to:

* execute commands via run_command
* interact with files via file
* identify the target operating system via os
* authenticate to API-based services and treat them like a platform

Train supports:

* Local execution
* SSH
* WinRM
* Docker
* Mock (for testing and debugging)
* AWS as an API
* Azure as an API
* VMware via PowerCLI

%description   -n gem-train-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-train-core
%ruby_gemspecdir/train-core-3.10.7.gemspec
%ruby_gemslibdir/train-core-3.10.7

%files         -n gem-train-core-doc
%ruby_gemsdocdir/train-core-3.10.7

%files         -n gem-train-doc
%ruby_gemdocdir


%changelog
* Fri Oct 28 2022 Pavel Skrylev <majioa@altlinux.org> 3.10.7-alt1
- ^ 3.7.6 -> 3.10.7

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 3.7.6-alt1
- ^ 3.4.4 -> 3.7.6

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.4-alt1
- ^ 3.3.7 -> 3.4.4
- * relicencing to Apache-2.0

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.3.7-alt1
- ^ 3.2.26 -> 3.3.7

* Thu Mar 26 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.26-alt1
- ^ 3.2.24 -> 3.2.26

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.24-alt1
- ^ 3.1.1 -> 3.2.24
- ! spec minorly

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- ^ 3.0.1 -> 3.1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- + packaged gems with usage Ruby Policy 2.0
