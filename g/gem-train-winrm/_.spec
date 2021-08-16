%define        gemname train-winrm

Name:          gem-train-winrm
Version:       0.2.12
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
BuildRequires: gem(winrm) >= 2.3.6 gem(winrm) < 3.0
BuildRequires: gem(winrm-elevated) >= 1.2.2 gem(winrm-elevated) < 1.3
BuildRequires: gem(winrm-fs) >= 1.0 gem(winrm-fs) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(winrm) >= 2.3.6 gem(winrm) < 3.0
Requires:      gem(winrm-elevated) >= 1.2.2 gem(winrm-elevated) < 1.3
Requires:      gem(winrm-fs) >= 1.0 gem(winrm-fs) < 2
Provides:      gem(train-winrm) = 0.2.12


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
Version:       0.2.12
Release:       alt1
Summary:       WinRM transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-winrm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-winrm) = 0.2.12

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
Version:       0.2.12
Release:       alt1
Summary:       WinRM transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-winrm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-winrm) = 0.2.12

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
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.12-alt1
- ^ 0.2.6 -> 0.2.12

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.6-alt1
- + packaged gem with usage Ruby Policy 2.0
