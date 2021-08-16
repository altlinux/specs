%define        gemname train

Name:          gem-train
Version:       3.7.6
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
BuildRequires: gem(addressable) >= 2.5 gem(addressable) < 3
BuildRequires: gem(ffi) > 1.13.0
BuildRequires: gem(json) >= 1.8 gem(json) < 3.0
BuildRequires: gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
BuildRequires: gem(net-scp) >= 1.2 gem(net-scp) < 4.0
BuildRequires: gem(net-ssh) >= 2.9 gem(net-ssh) < 7.0
BuildRequires: gem(train-winrm) >= 0.2 gem(train-winrm) < 1
BuildRequires: gem(activesupport) >= 6.0 gem(activesupport) <= 7
BuildRequires: gem(inifile) >= 3.0 gem(inifile) < 4
BuildRequires: gem(azure_graph_rbac) >= 0.16 gem(azure_graph_rbac) < 1
BuildRequires: gem(azure_mgmt_key_vault) >= 0.17 gem(azure_mgmt_key_vault) < 1
BuildRequires: gem(azure_mgmt_resources) >= 0.15 gem(azure_mgmt_resources) < 1
BuildRequires: gem(azure_mgmt_security) >= 0.18 gem(azure_mgmt_security) < 1
BuildRequires: gem(azure_mgmt_storage) >= 0.18 gem(azure_mgmt_storage) < 1
BuildRequires: gem(docker-api) >= 1.26 gem(docker-api) < 3.0
BuildRequires: gem(google-api-client) >= 0.53.0 gem(google-api-client) < 1
BuildRequires: gem(googleauth) >= 0.16 gem(googleauth) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency google-api-client >= 0.53.0,google-api-client < 1
%ruby_use_gem_dependency net-ssh >= 6.1.0,net-ssh < 7
%ruby_use_gem_dependency activesupport >= 6.0,activesupport < 7
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency googleauth >= 0.16,googleauth < 1
%ruby_ignore_names train-test-fixture,train-local-rot13
Requires:      gem(train-core) = 3.7.6
Requires:      gem(train-winrm) >= 0.2 gem(train-winrm) < 1
Requires:      gem(activesupport) >= 6.0 gem(activesupport) <= 7
Requires:      gem(inifile) >= 3.0 gem(inifile) < 4
Requires:      gem(azure_graph_rbac) >= 0.16 gem(azure_graph_rbac) < 1
Requires:      gem(azure_mgmt_key_vault) >= 0.17 gem(azure_mgmt_key_vault) < 1
Requires:      gem(azure_mgmt_resources) >= 0.15 gem(azure_mgmt_resources) < 1
Requires:      gem(azure_mgmt_security) >= 0.18 gem(azure_mgmt_security) < 1
Requires:      gem(azure_mgmt_storage) >= 0.18 gem(azure_mgmt_storage) < 1
Requires:      gem(docker-api) >= 1.26 gem(docker-api) < 3.0
Requires:      gem(google-api-client) >= 0.23.9 gem(google-api-client) < 1
Requires:      gem(googleauth) >= 0.16 gem(googleauth) < 1
Provides:      gem(train) = 3.7.6


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
Version:       3.7.6
Release:       alt1
Summary:       Core for transport Interface to unify communication over SSH, WinRM, and friends
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(addressable) >= 2.5 gem(addressable) < 3
Requires:      gem(ffi) > 1.13.0
Requires:      gem(json) >= 1.8 gem(json) < 3.0
Requires:      gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
Requires:      gem(net-scp) >= 1.2 gem(net-scp) < 4.0
Requires:      gem(net-ssh) >= 2.9 gem(net-ssh) < 7.0
Provides:      gem(train-core) = 3.7.6

%description   -n gem-train-core
Core for transport Interface to unify communication over SSH, WinRM, and
friends.


%package       -n gem-train-core-doc
Version:       3.7.6
Release:       alt1
Summary:       Core for transport Interface to unify communication over SSH, WinRM, and friends documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-core) = 3.7.6

%description   -n gem-train-core-doc
Core for transport Interface to unify communication over SSH, WinRM, and friends
documentation files.

%description   -n gem-train-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-core.


%package       -n gem-train-core-devel
Version:       3.7.6
Release:       alt1
Summary:       Core for transport Interface to unify communication over SSH, WinRM, and friends development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-core) = 3.7.6
Requires:      gem(google-api-client) >= 0.44 gem(google-api-client) < 1
Requires:      gem(activesupport) >= 6.0 gem(activesupport) < 7
Requires:      gem(googleauth) >= 0.16 gem(googleauth) < 1

%description   -n gem-train-core-devel
Core for transport Interface to unify communication over SSH, WinRM, and friends
development package.

%description   -n gem-train-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-core.


%package       -n gem-train-doc
Version:       3.7.6
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train) = 3.7.6

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


%package       -n gem-train-devel
Version:       3.7.6
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train) = 3.7.6
Requires:      gem(google-api-client) >= 0.44 gem(google-api-client) < 1
Requires:      gem(activesupport) >= 6.0 gem(activesupport) < 7
Requires:      gem(googleauth) >= 0.16 gem(googleauth) < 1

%description   -n gem-train-devel
Transport Interface to unify communication over SSH, WinRM, and friends
development package.

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

%description   -n gem-train-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train.


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

%files         -n gem-train-core
%doc README.md
%ruby_gemspecdir/train-core-3.7.6.gemspec
%ruby_gemslibdir/train-core-3.7.6

%files         -n gem-train-core-doc
%doc README.md
%ruby_gemsdocdir/train-core-3.7.6

%files         -n gem-train-core-devel
%doc README.md

%files         -n gem-train-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-train-devel
%doc README.md


%changelog
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
