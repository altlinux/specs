%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname train

Name:          gem-train
Version:       3.16.5
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train/
Vcs:           https://github.com/inspec/train.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activesupport) >= 7.1
BuildRequires: gem(addressable) >= 2.5
BuildRequires: gem(azure_graph_rbac) >= 0.16
BuildRequires: gem(azure_mgmt_key_vault) >= 0.17
BuildRequires: gem(azure_mgmt_resources) >= 0.15
BuildRequires: gem(azure_mgmt_security) >= 0.18
BuildRequires: gem(azure_mgmt_storage) >= 0.18
BuildRequires: gem(bcrypt_pbkdf) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(chefstyle) >= 2.2.2
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(docker-api) >= 1.26
BuildRequires: gem(ed25519) >= 0
BuildRequires: gem(ffi) >= 1.16.0
BuildRequires: gem(google-apis-admin_directory_v1) >= 0.46.0
BuildRequires: gem(google-apis-cloudkms_v1) >= 0.41.0
BuildRequires: gem(google-apis-cloudresourcemanager_v1) >= 0.35.0
BuildRequires: gem(google-apis-compute_v1) >= 0.83.0
BuildRequires: gem(google-apis-iam_v1) >= 0.50.0
BuildRequires: gem(google-apis-monitoring_v3) >= 0.51.0
BuildRequires: gem(google-apis-storage_v1) >= 0.30.0
BuildRequires: gem(googleauth) >= 1.17.2
BuildRequires: gem(inifile) >= 3.0
BuildRequires: gem(json) >= 2.3.0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(mixlib-shellout) >= 2.0
BuildRequires: gem(mocha) >= 2.1
BuildRequires: gem(net-scp) >= 1.2
BuildRequires: gem(net-ssh) >= 2.9
BuildRequires: gem(ostruct) >= 0.6.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov_json_formatter) >= 0
BuildRequires: gem(train-winrm) >= 0.2.13
BuildRequires: gem(x25519) >= 0
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(azure_graph_rbac) >= 1
BuildConflicts: gem(azure_mgmt_key_vault) >= 1
BuildConflicts: gem(azure_mgmt_resources) >= 1
BuildConflicts: gem(azure_mgmt_security) >= 1
BuildConflicts: gem(azure_mgmt_storage) >= 1
BuildConflicts: gem(bigdecimal) >= 4
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(docker-api) >= 3.0
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(google-apis-admin_directory_v1) >= 1
BuildConflicts: gem(google-apis-cloudkms_v1) >= 1
BuildConflicts: gem(google-apis-cloudresourcemanager_v1) >= 1
BuildConflicts: gem(google-apis-compute_v1) >= 1
BuildConflicts: gem(google-apis-iam_v1) >= 1
BuildConflicts: gem(google-apis-monitoring_v3) >= 1
BuildConflicts: gem(google-apis-storage_v1) >= 1
BuildConflicts: gem(googleauth) >= 2
BuildConflicts: gem(inifile) >= 4
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(mixlib-shellout) >= 4.0
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(net-scp) >= 5.0
BuildConflicts: gem(net-ssh) >= 8.0
BuildConflicts: gem(ostruct) >= 0.7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(train-winrm) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_use_gem_dependency train-winrm >= 0.2.13,train-winrm < 1
%ruby_use_gem_dependency google-apis-admin_directory_v1 >= 0.46
%ruby_use_gem_dependency google-apis-cloudkms_v1 >= 0.41
%ruby_use_gem_dependency google-apis-cloudresourcemanager_v1 >= 0.35
%ruby_use_gem_dependency google-apis-compute_v1 >= 0.83
%ruby_use_gem_dependency google-apis-iam_v1 >= 0.50
%ruby_use_gem_dependency google-apis-monitoring_v3 >= 0.51
%ruby_use_gem_dependency google-apis-storage_v1 >= 0.30
%ruby_use_gem_dependency googleauth >= 1.17.3
%ruby_use_gem_dependency minitest >= 6.0
Requires:      ruby >= 3.1.0
Requires:      gem(activesupport) >= 7.1
Requires:      gem(azure_graph_rbac) >= 0.16
Requires:      gem(azure_mgmt_key_vault) >= 0.17
Requires:      gem(azure_mgmt_resources) >= 0.15
Requires:      gem(azure_mgmt_security) >= 0.18
Requires:      gem(azure_mgmt_storage) >= 0.18
Requires:      gem(docker-api) >= 1.26
Requires:      gem(google-apis-admin_directory_v1) >= 0.46.0
Requires:      gem(google-apis-cloudkms_v1) >= 0.41.0
Requires:      gem(google-apis-cloudresourcemanager_v1) >= 0.35.0
Requires:      gem(google-apis-compute_v1) >= 0.83.0
Requires:      gem(google-apis-iam_v1) >= 0.50.0
Requires:      gem(google-apis-monitoring_v3) >= 0.51.0
Requires:      gem(google-apis-storage_v1) >= 0.30.0
Requires:      gem(googleauth) >= 1.17.2
Requires:      gem(inifile) >= 3.0
Requires:      gem(ostruct) >= 0.6.0
Requires:      gem(train-winrm) >= 0.2.13
Conflicts:     gem(azure_graph_rbac) >= 1
Conflicts:     gem(azure_mgmt_key_vault) >= 1
Conflicts:     gem(azure_mgmt_resources) >= 1
Conflicts:     gem(azure_mgmt_security) >= 1
Conflicts:     gem(azure_mgmt_storage) >= 1
Conflicts:     gem(bigdecimal) >= 4
Conflicts:     gem(docker-api) >= 3.0
Conflicts:     gem(google-apis-admin_directory_v1) >= 1
Conflicts:     gem(google-apis-cloudkms_v1) >= 1
Conflicts:     gem(google-apis-cloudresourcemanager_v1) >= 1
Conflicts:     gem(google-apis-compute_v1) >= 1
Conflicts:     gem(google-apis-iam_v1) >= 1
Conflicts:     gem(google-apis-monitoring_v3) >= 1
Conflicts:     gem(google-apis-storage_v1) >= 1
Conflicts:     gem(googleauth) >= 2
Conflicts:     gem(inifile) >= 4
Conflicts:     gem(ostruct) >= 0.7
Conflicts:     gem(train-winrm) >= 1
Provides:      train = %EVR
Provides:      gem(train) = 3.16.5

%ruby_ignore_names train-test-fixture

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
Version:       3.16.5
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 3.1.0
Requires:      gem(addressable) >= 2.5
Requires:      gem(ffi) >= 1.16.0
Requires:      gem(json) >= 2.19.2
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(net-scp) >= 1.2
Requires:      gem(net-ssh) >= 2.9
Requires:      gem(train) >= 0
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(ffi) >= 1.18
Conflicts:     gem(json) >= 3.0
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(net-scp) >= 5.0
Conflicts:     gem(net-ssh) >= 8.0
Provides:      train-core = %EVR
Provides:      gem(train-core) = 3.16.5

%description   -n gem-train-core
Transport Interface to unify communication over SSH, WinRM, and friends.


%if_enabled    doc
%package       -n gem-train-core-doc
Version:       3.16.5
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-core) = 3.16.5

%description   -n gem-train-core-doc
Transport Interface to unify communication over SSH, WinRM, and friends
documentation files.

%description   -n gem-train-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-core.
%endif


%if_enabled    devel
%package       -n gem-train-core-devel
Version:       3.16.5
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-core) = 3.16.5
Requires:      gem(bcrypt_pbkdf) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(chefstyle) >= 2.2.2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(ed25519) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 5.8
Requires:      gem(mocha) >= 2.1
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov_json_formatter) >= 0
Requires:      gem(x25519) >= 0
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

%description   -n gem-train-core-devel
Transport Interface to unify communication over SSH, WinRM, and friends
development package.

%description   -n gem-train-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-core.
%endif


%if_enabled    doc
%package       -n gem-train-doc
Version:       3.16.5
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train) = 3.16.5

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
%endif


%if_enabled    devel
%package       -n gem-train-devel
Version:       3.16.5
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train) = 3.16.5
Requires:      gem(bcrypt_pbkdf) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(chefstyle) >= 2.2.2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(ed25519) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 5.8
Requires:      gem(mocha) >= 2.1
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov_json_formatter) >= 0
Requires:      gem(x25519) >= 0
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

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
%endif


%prep
%setup
sed '/^$/! {/train-test-fixture/{ s/^#*/#/g; }}' -i Gemfile

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md contrib
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-train-core
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md contrib
%ruby_gemspecdir/train-core-3.16.5.gemspec
%ruby_gemslibdir/train-core-3.16.5

%if_enabled    doc
%files         -n gem-train-core-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md contrib
%ruby_gemsdocdir/train-core-3.16.5
%endif

%if_enabled    devel
%files         -n gem-train-core-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md contrib
%endif

%if_enabled    doc
%files         -n gem-train-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md contrib
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-train-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md contrib
%endif


%changelog
* Thu Aug 20 2026 Pavel Skrylev <majioa@altlinux.org> 3.16.5-alt1
- ^ 3.11.5 -> 3.16.5

* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 3.11.5-alt1.2
- ! fixed dep to minitest gem

* Sun Aug 09 2026 Pavel Skrylev <majioa@altlinux.org> 3.11.5-alt1.1
- + dep to train-core gem (closes ALT #60125)

* Wed Nov 19 2025 Pavel Skrylev <majioa@altlinux.org> 3.11.5-alt1
- ^ 3.11.1 -> 3.11.5

* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 3.11.1-alt1
- ^ 3.10.7 -> 3.11.1

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
