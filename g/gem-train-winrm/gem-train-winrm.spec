%define        _unpackaged_files_terminate_build 1
%define        gemname train-winrm

Name:          gem-train-winrm
Version:       0.2.13
Release:       alt1
Summary:       WinRM transport for Train
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train-winrm
Vcs:           https://github.com/inspec/train-winrm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(train-core) >= 3.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(winrm-elevated) >= 0
BuildRequires: gem(winrm) >= 2.3.6
BuildRequires: gem(winrm-fs) >= 1.0
BuildConflicts: gem(train-core) >= 4
BuildConflicts: gem(winrm-elevated) > 2
BuildConflicts: gem(winrm) >= 3.0
BuildConflicts: gem(winrm-fs) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency winrm-elevated >= 1.2.3,winrm-elevated < 2
Requires:      gem(winrm-elevated) >= 0
Requires:      gem(winrm) >= 2.3.6
Requires:      gem(winrm-fs) >= 1.0
Conflicts:     gem(winrm-elevated) > 2
Conflicts:     gem(winrm) >= 3.0
Conflicts:     gem(winrm-fs) >= 2
Provides:      gem(train-winrm) = 0.2.13


%description
This plugin allows applications that rely on Train to communicate with the WinRM
API. For example, you could use this to audit Windows Server 2016
machines.

This plugin relies on the winrm and winrm-fs gems for implementation.

Train itself has no CLI, nor a sophisticated test harness. Chef InSpec does have
such facilities, so installing Train plugins will require a Chef InSpec
installation. You do not need to use or understand Chef InSpec.

Train plugins may be developed without a Chef InSpec installation.


%package       -n gem-train-winrm-doc
Version:       0.2.13
Release:       alt1
Summary:       WinRM transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-winrm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-winrm) = 0.2.13

%description   -n gem-train-winrm-doc
WinRM transport for Train documentation files.

This plugin allows applications that rely on Train to communicate with the WinRM
API. For example, you could use this to audit Windows Server 2016
machines.

This plugin relies on the winrm and winrm-fs gems for implementation.

Train itself has no CLI, nor a sophisticated test harness. Chef InSpec does have
such facilities, so installing Train plugins will require a Chef InSpec
installation. You do not need to use or understand Chef InSpec.

Train plugins may be developed without a Chef InSpec installation.

%description   -n gem-train-winrm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-winrm.


%package       -n gem-train-winrm-devel
Version:       0.2.13
Release:       alt1
Summary:       WinRM transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-winrm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-winrm) = 0.2.13
Requires:      gem(train-core) >= 3.0
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(chefstyle) >= 0
Conflicts:     gem(train-core) >= 4

%description   -n gem-train-winrm-devel
WinRM transport for Train development package.

This plugin allows applications that rely on Train to communicate with the WinRM
API. For example, you could use this to audit Windows Server 2016
machines.

This plugin relies on the winrm and winrm-fs gems for implementation.

Train itself has no CLI, nor a sophisticated test harness. Chef InSpec does have
such facilities, so installing Train plugins will require a Chef InSpec
installation. You do not need to use or understand Chef InSpec.

Train plugins may be developed without a Chef InSpec installation.

%description   -n gem-train-winrm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-winrm.


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

%files         -n gem-train-winrm-doc
%ruby_gemdocdir

%files         -n gem-train-winrm-devel


%changelog
* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.13-alt1
- ^ 0.2.12 -> 0.2.13

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.12-alt1
- ^ 0.2.6 -> 0.2.12

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.6-alt1
- + packaged gem with usage Ruby Policy 2.0
